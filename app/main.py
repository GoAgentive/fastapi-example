from typing import Union
import logging
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    logging.info("Hello World")
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    logging.info("Hello World")
    return {"item_id": item_id, "q": q}