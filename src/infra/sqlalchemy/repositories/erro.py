from sqlalchemy import delete
from sqlalchemy.orm import Session
from src.schemas.erro import Erro
from src.infra.sqlalchemy.models import models

class RepositorioErro:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, erro: Erro, simulado_id: int):
        db_erro = models.Erro(materia=erro.materia, assunto=erro.assunto, bloco=erro.bloco, simulado_id=simulado_id)
        self.db.add(db_erro)
        self.db.commit()
        self.db.refresh(db_erro)
        return db_erro
    
    def listar(self, simulado_id: int):
        erros = self.db.query(models.Erro).filter(models.Erro.simulado_id == simulado_id).all()
        return erros
    
    def listar_por_bloco(self, request: str):
        erros = self.db.query(models.Erro).filter(models.Erro.bloco == request).all()
        return erros
    
    def deletar(self, erro: Erro, simulado_id: int):
        stmt = delete(models.Erro).where(simulado_id == simulado_id)
        self.db.execute(stmt)
