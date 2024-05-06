from pydantic import BaseModel

class Erro(BaseModel):
    materia: str
    assunto: str
    bloco: str = None
    id: str = None

    class Config:
        from_attributes = True