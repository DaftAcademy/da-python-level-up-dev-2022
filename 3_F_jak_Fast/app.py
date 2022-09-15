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

app = FastAPI()
templates = Jinja2Templates(directory="templates")

r1 = APIRouter()

@app.get("/request_query_string_discovery")
def read_items(u: str = "default", q: List[int] = Query(None)):
    query_items = {"q": q, "u": u}

    return askdjhsajdkhaskjd()

    return query_items


@app.get("/askdjhsajdkhaskjd")
def askdjhsajdkhaskjd():
    return {"yeye": "asjkdhaskd"}



@app.get("/static", response_class=HTMLResponse)
@app.get("/jinja",response_class=HTMLResponse)
def read_item(request: Request, my_string: str = Query("Wheeeee!"), my_list: List[str]= Query(None)):
    my_list = my_list or [1,2,3,4]
    return templates.TemplateResponse("index.html.j2", {
        "request": request,
        "my_string": my_string,
        "my_list": my_list
    })

@app.get("/simple_path_tmpl/{sample_variable}/{a}/orders")
def simple_path_tmpl(sample_variable: str, a: int):
    print(f"{sample_variable=}")
    print(type(sample_variable))
    return {"sample_variable": sample_variable,
            "a": a}

@app.get("/muza/{artist}/{album}/{track_no}")
def simple_path_tmpl(artist: str,album: str, track_no: int):
    return {"artist": artist,
            "album": album,
            "track_no": track_no}


objects = {
    1: {"field_a": "1a", "field_b": "1b"},
    2: {"field_a": "2a", "field_b": "2b"},
    3: {"field_a": "3a", "field_b": "3b"},
    # .... #
}

@app.get("/db/{obj_id}/{field}")
def db(obj_id: int, field: str):
    print(f"{obj_id=}")
    print(f"{field=}")
    return {"field": objects.get(obj_id,{}).get(f"field_{field}")}


@app.delete("/db/{obj_id}/{field}")
def db2(obj_id: int, field: str):
    print(f"{obj_id=}")
    print(f"{field=}")
    return {"field": objects.get(obj_id,{}).get(f"field_{field}")}




@r1.get("/files/{file_path:path}/edit")
def edit_file(file_path: str):
    return {"edit_stuff": file_path}

@r1.get("/files/{file_path:path}")
def read_file(file_path: str):
    return {"file_path": file_path}


app.include_router(r1)
app.include_router(
    r1,
    prefix="/v1",
    tags=["v1"],
)
