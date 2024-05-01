from pydantic import BaseModel
from src.schemas.erro import Erro
from typing import List
from datetime import date

class Simulado(BaseModel):
    tipo: str
    erros: List[Erro] = []
    data: date
    id: int = None


    class Config:
        from_attributes = True