from pydantic import BaseModel
from typing import List
from src.schemas.simulado import Simulado

class Usuario(BaseModel):
    username: str
    senha: str
    simulados: List[Simulado] = []
    