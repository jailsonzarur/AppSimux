from fastapi import FastAPI, Depends
from src.schemas.erro import Erro
from src.schemas.simulado import Simulado
from src.schemas.usuario import Usuario
from typing import List
from src.infra.sqlalchemy.config.database import criar_bd, get_bd
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario

criar_bd()

app = FastAPI()

@app.post('/usuarios')
def cadastrar_simulado(usuarios: Usuario, db: Session = Depends(get_bd)):
    usuario = RepositorioUsuario(db).criar(usuarios)
    return usuario

