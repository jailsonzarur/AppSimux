from sqlalchemy import delete, update
from sqlalchemy.orm import Session
from src.schemas.simulado import Simulado
from src.infra.sqlalchemy.models import models
from uuid import uuid4

class RepositorioSimulado:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, simulado: Simulado, usuario_id: str):
        db_simulado = models.Simulado(id = str(uuid4()), tipo = simulado.tipo, data = simulado.data, usuario_id = usuario_id)
        self.db.add(db_simulado)
        self.db.commit()
        self.db.refresh(db_simulado)
        return db_simulado

    def listar(self, usuario_id: str):
        simulados = self.db.query(models.Simulado).filter(models.Simulado.usuario_id == usuario_id).all()
        return simulados
    
    def deletar(self, simulado_id: str):
        stmt = delete(models.Simulado).where(models.Simulado.id == simulado_id)
        self.db.execute(stmt)
        self.db.commit()

    def editar(self, simulado_id: str, simulado: Simulado):
        stmt = update(models.Simulado).where(models.Simulado.id == simulado_id).values(tipo=simulado.tipo, data=simulado.data)
        self.db.execute(stmt)
        self.db.commit()