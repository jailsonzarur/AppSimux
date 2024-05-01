from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.usuario import Usuario
from src.infra.sqlalchemy.config.database import get_bd
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario

router = APIRouter()

@router.post('/signup')
def signin(usuario: Usuario, db: Session = Depends(get_bd)):
    