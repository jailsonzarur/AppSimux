from sqlalchemy import select
from sqlalchemy.orm import Session
from src.schemas import usuario
from src.infra.sqlalchemy.models import models
from src.infra.providers import hash_provider

class RepositorioUsuario:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: usuario.Usuario):
        db_usuario = models.Usuario(username= usuario.username, senha= hash_provider.gerar_hash(usuario.senha))

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario
    
    def obter_por_username(self, username: str):
        stmt = select(models.Usuario).where(models.Usuario.username == username)
        usuario = self.db.execute(stmt)
        return usuario.scalars().first()
    