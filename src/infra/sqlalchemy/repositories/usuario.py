from sqlalchemy.orm import Session
from src.schemas import usuario
from src.infra.sqlalchemy.models import models

class RepositorioUsuario:

    def __init__(self, db: Session):
        self.db = db

    def criar(self, usuario: usuario.Usuario):
        db_usuario = models.Usuario(username= usuario.username, senha= usuario.senha)

        self.db.add(db_usuario)
        self.db.commit()
        self.db.refresh(db_usuario)
        return db_usuario