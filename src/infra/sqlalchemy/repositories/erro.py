from sqlalchemy import delete
from sqlalchemy.orm import Session
from src.schemas.erro import Erro
from src.infra.sqlalchemy.models import models
from uuid import uuid4

class RepositorioErro:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, erro: Erro, simulado_id: int):
        db_erro = models.Erro(id = str(uuid4()), materia=erro.materia, assunto=erro.assunto, bloco=erro.bloco, simulado_id=simulado_id)
        self.db.add(db_erro)
        self.db.commit()
        self.db.refresh(db_erro)
        return db_erro
    
    def listar(self, simulado_id: str):
        erros = self.db.query(models.Erro).filter(models.Erro.simulado_id == simulado_id).all()
        return erros
    
    def listar_por_bloco(self, request: str):
        erros = self.db.query(models.Erro).filter(models.Erro.bloco == request).all()
        return erros
    
    def listar_por_materia(self, bloco: str, materia: str):
        erros = self.db.query(models.Erro).filter(models.Erro.materia == materia and models.Erro.bloco == bloco).all()
        return erros
    
    def deletar_todo_simulado(self, simulado_id: str):
        stmt = delete(models.Erro).where(models.Erro.simulado_id == simulado_id)
        self.db.execute(stmt)
        self.db.commit()

    def deletar(self, erro_id: str):
        stmt = delete(models.Erro).where(models.Erro.id == erro_id)
        self.db.execute(stmt)
        self.db.commit()