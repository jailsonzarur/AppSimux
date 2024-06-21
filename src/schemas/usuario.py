from pydantic import BaseModel
from typing import List
from src.schemas.simulado import Simulado

class Usuario(BaseModel):
    id: str = None
    username: str
    senha: str
    simulados: List[Simulado] = []

    class Config:
        from_attributes = True

class UsuarioInfo(BaseModel):
    id: str = None
    username: str
    simulados: List[Simulado] = []

    class Config:
        from_attributes = True

class SimuladoData(BaseModel):
    simulados: List[Simulado] = []

    class Config:
        from_attributes = True

class LoginData(BaseModel):
    username: str
    senha: str

class LoginSucesso(BaseModel):
    username: str
    acess_token: str

