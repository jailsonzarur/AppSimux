from pydantic import BaseModel

class Erro(BaseModel):
    materia: str
    assunto: str
    bloco: str = None


    class Config:
        from_attributes = True