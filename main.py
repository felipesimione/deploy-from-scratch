from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

produtos: List[Dict[str, str]] = [
    {"id": 1, "nome": "Smartphone", "preco": 1000.00},
    {"id": 2, "nome": "Notebook", "preco": 3000.00},
    {"id": 3, "nome": "Fone de ouvido", "preco": 30.00},
]

@app.get("/")
def ola_mundo():
    return {"message": "Olá, pessoal!"}

@app.get("/produtos")
def listar_produtos():
    return produtos