from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.usuario import Usuario
from src.schemas.simulado import Simulado
from src.routers.auth_utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_bd
from src.infra.sqlalchemy.repositories.simulado import RepositorioSimulado


router = APIRouter()

@router.post('/simulados')
def cadastrar_simulados(simulado: Simulado, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    simulado = RepositorioSimulado(db).criar(simulado, usuario.id)
    return simulado