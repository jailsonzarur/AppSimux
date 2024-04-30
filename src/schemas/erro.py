from pydantic import BaseModel

class Erro(BaseModel):
    materia: str
    assunto: str
    bloco: str = None
    idsimulado: int

    class Config:
        from_attributes = True