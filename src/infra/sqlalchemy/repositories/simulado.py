from sqlalchemy import delete 
from sqlalchemy.orm import Session
from src.schemas.simulado import Simulado
from src.infra.sqlalchemy.models import models

class RepositorioSimulado:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, simulado: Simulado, usuario_id: int):
        db_simulado = models.Simulado(tipo = simulado.tipo, data = simulado.data, usuario_id = usuario_id)
        self.db.add(db_simulado)
        self.db.commit()
        self.db.refresh(db_simulado)
        return db_simulado

    def listar(self, usuario_id: int):
        simulados = self.db.query(models.Simulado).filter(models.Simulado.usuario_id == usuario_id).all()
        return simulados
    
    def deletar(self, simulado_id: int):
        stmt = delete(models.Simulado).where(models.Simulado.id == simulado_id)
        self.db.execute(stmt)
        self.db.commit()