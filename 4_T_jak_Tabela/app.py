import string
import random
import secrets
import uuid
from contextlib import contextmanager
from datetime import datetime
from hashlib import sha512
from typing import List, Optional, Union

from fastapi import APIRouter


from fastapi import Cookie, Depends, FastAPI, HTTPException, Request, Response, status, Query
from fastapi.responses import (
    HTMLResponse,
    JSONResponse,
    PlainTextResponse,
    RedirectResponse,
)
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

import aiosqlite
from fastapi import FastAPI

app = FastAPI()




class Customer(BaseModel):
    company_name: str


@app.on_event("startup")
async def startup():
    app.db_connection = await aiosqlite.connect("northwind.db")
    app.db_connection.text_factory = lambda b: b.decode(errors="ignore")  # northwind specific
    app.db_connection.row_factory = aiosqlite.Row


@app.on_event("shutdown")
async def shutdown():
    await app.db_connection.close()


@app.get("/data")
async def root():
    cursor = await app.db_connection.execute("SELECT * FROM Customers")
    data = await cursor.fetchall()
    return {"data": data}

@app.get("/suppliers/{supplier_id}")
async def single_supplier(supplier_id: int):
    data = await app.db_connection.execute(
        f"SELECT CompanyName, Address FROM Suppliers WHERE SupplierID = {supplier_id}")
    data = await data.fetchone()

    return data

@app.get("/products")
async def products():
    products_query = await app.db_connection.execute("SELECT ProductName FROM Products")
    products = await products_query.fetchall()
    return {
        "products_counter": len(products),
        "products": products
    }

@app.get("/customers")
async def customers():
    app.db_connection.row_factory = lambda cursor, x: x[0]
    artists_cursor = await app.db_connection.execute("SELECT CompanyName FROM Customers")
    data = await artists_cursor.fetchall()
    return data

@app.post("/customers/add")
async def customer_add(customer: Customer):
    new_customer_id = "".join(random.choice(string.ascii_letters) for _ in range(5))

    cursor = await app.db_connection.execute(
        "INSERT INTO Customers (CustomerID, CompanyName) VALUES (?,?)", (new_customer_id, customer.company_name),
    )
    await app.db_connection.commit()
    app.db_connection.row_factory = aiosqlite.Row
    customer_cursor = await app.db_connection.execute(
        """SELECT CustomerID AS customer_id, CompanyName AS company_name
         FROM Customers WHERE CustomerID = ?""",
        (new_customer_id, ))
    customer = await customer_cursor.fetchone()
    
    return customer