import sqlite3
from contextlib import contextmanager

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class Category(BaseModel):
    name: str


@contextmanager
def fetch_single_product(product_id: int):
    app.db_connection.row_factory = sqlite3.Row
    product = app.db_connection.execute(
        "SELECT ProductID as id, ProductName as name FROM products WHERE ProductID = :product_id",
        {"product_id": product_id},
    ).fetchone()
    yield product


@contextmanager
def fetch_single_category(category_id: int):
    app.db_connection.row_factory = sqlite3.Row
    category = app.db_connection.execute(
        "SELECT CategoryID, CategoryName FROM categories WHERE CategoryID = :category_id",
        {"category_id": category_id},
    ).fetchone()
    yield category


@app.on_event("startup")
async def startup():
    app.db_connection = sqlite3.connect("northwind.db")
    app.db_connection.text_factory = lambda b: b.decode(errors="ignore")


@app.on_event("shutdown")
async def shutdown():
    app.db_connection.close()


@app.get("/categories")
async def categories(limit: int = None, offset: int = None):
    app.db_connection.row_factory = sqlite3.Row
    categories = app.db_connection.execute(
        "SELECT CategoryID, CategoryName FROM categories"
    ).fetchall()
    return {
        "categories": [
            {"id": c["CategoryID"], "name": c["CategoryName"]} for c in categories
        ]
    }


@app.get("/categories/{category_id}")
async def single_category(category_id: int):
    with fetch_single_category(category_id) as category:
        if not category:
            raise HTTPException(status_code=404, detail="Not found")
        return {"id": category["CategoryID"], "name": category["CategoryName"]}


@app.post("/categories", status_code=201)
async def add_category(category: Category):
    cursor = app.db_connection.execute(
        "INSERT INTO categories (CategoryName) VALUES (?)", (category.name,)
    )
    app.db_connection.commit()
    new_category_id = cursor.lastrowid

    with fetch_single_category(new_category_id) as fetched_category:
        return {
            "id": fetched_category["CategoryID"],
            "name": fetched_category["CategoryName"],
        }


@app.put("/categories/{category_id}")
async def edit_category(category_id: int, category: Category):
    with fetch_single_category(category_id) as fetched_category:
        if not fetched_category:
            raise HTTPException(status_code=404, detail="Not found")

    cursor = app.db_connection.execute(
        "UPDATE categories SET CategoryName = ? WHERE CategoryID = ?",
        (category.name, category_id),
    )
    app.db_connection.commit()

    with fetch_single_category(category_id) as fetched_category:
        return {
            "id": fetched_category["CategoryID"],
            "name": fetched_category["CategoryName"],
        }


@app.delete("/categories/{category_id}")
async def delete_category(category_id: int):
    with fetch_single_category(category_id) as fetched_category:
        if not fetched_category:
            raise HTTPException(status_code=404, detail="Not found")

    cursor = app.db_connection.execute(
        "DELETE FROM categories WHERE CategoryID = ?", (category_id,)
    )
    app.db_connection.commit()
    return {"deleted": cursor.rowcount}


@app.get("/employees")
async def employees(limit: int = None, offset: int = None, order: str = None):
    if order and order not in ["last_name", "first_name", "city"]:
        raise HTTPException(status_code=400, detail="Invalid order")

    sql_query = "SELECT EmployeeID as id, LastName as last_name, FirstName as first_name, City as city FROM Employees"
    if order:
        sql_query = f"{sql_query} ORDER BY {order} ASC"
    if limit and offset:
        sql_query = f"{sql_query} LIMIT :limit OFFSET :offset"
    elif limit:
        sql_query = f"{sql_query} LIMIT :limit"

    app.db_connection.row_factory = sqlite3.Row
    employees = app.db_connection.execute(
        sql_query, {"order": order, "limit": limit, "offset": offset}
    ).fetchall()
    return {"employees": employees}


@app.get("/products")
async def products(limit: int = None, offset: int = None):
    app.db_connection.row_factory = sqlite3.Row
    products = app.db_connection.execute(
        "SELECT ProductID as id, ProductName as name FROM products"
    ).fetchall()
    return {"products": products}


@app.get("/products/{product_id}")
async def single_product(product_id: int):
    with fetch_single_product(product_id) as product:
        if not product:
            raise HTTPException(status_code=404, detail="Not found")
        return product


@app.get("/products/{product_id}/orders")
async def single_product_orders(product_id: int):
    with fetch_single_product(product_id) as product:
        if not product:
            raise HTTPException(status_code=404, detail="Not found")

        orders = app.db_connection.execute(
            """
            Select 
                orders.OrderID as id, 
                customers.CompanyName as customer, 
                orddet.Quantity as quantity ,
                ROUND(((orddet.Quantity * orddet.UnitPrice) - (orddet.Quantity * orddet.UnitPrice * orddet.Discount)), 2) as total_price 
            from Orders
            join customers on orders.CustomerID = customers.CustomerID
            join 'Order Details' as orddet on orders.OrderID = orddet.OrderID and orddet.ProductID = :product_id        
            """,
            {"product_id": product_id},
        ).fetchall()
        return {"orders": orders}


@app.get("/products_extended")
async def products_categories():
    app.db_connection.row_factory = sqlite3.Row
    data = app.db_connection.execute(
        """
        SELECT ProductID as id, ProductName as name, categories.CategoryName as category, suppliers.CompanyName as supplier FROM products
        JOIN categories ON products.CategoryID = categories.CategoryID
        JOIN suppliers on products.SupplierID = suppliers.SupplierID
        """
    ).fetchall()
    return {"products_extended": data}


@app.get("/customers")
async def customers(limit: int = None, offset: int = None):
    sql_query = "SELECT CustomerID as id, CompanyName as name, (Address || ' ' || PostalCode || ' ' || City || ' ' || Country) as full_address FROM customers"
    if limit and offset:
        sql_query = f"{sql_query} LIMIT :limit OFFSET :offset"
    elif limit:
        sql_query = f"{sql_query} LIMIT :limit"

    app.db_connection.row_factory = sqlite3.Row
    customers = app.db_connection.execute(
        sql_query, {"limit": limit, "offset": offset}
    ).fetchall()
    return {"customers": customers}


@app.get("/customers/{customer_id}")
async def single_customer(customer_id: str):
    app.db_connection.row_factory = sqlite3.Row
    customer = app.db_connection.execute(
        """
        SELECT CustomerID as id, CompanyName as name, (City || ' ' || PostalCode || ' ' || Country) as address FROM customers
        WHERE CustomerID = :customer_id
        """,
        {"customer_id": customer_id},
    ).fetchone()
    if not customer:
        raise HTTPException(status_code=404, detail="Not found")
    return customer
