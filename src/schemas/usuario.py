from pydantic import BaseModel
from typing import List
from src.schemas.simulado import Simulado

class Usuario(BaseModel):
    id: int = None
    username: str
    senha: str
    simulados: List[Simulado] = []

    class Config:
        from_attributes = True

class LoginData(BaseModel):
    username: str
    senha: str

class LoginSucesso(BaseModel):
    username: str
    acess_token: str