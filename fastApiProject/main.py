from fastapi import FastAPI
from contactos import Contacto

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/teste")
async def teste(ct: Contacto):
    return ct