from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from src.schemas.usuario import Usuario
from src.schemas.simulado import Simulado
from src.routers.auth_utils import obter_usuario_logado
from src.infra.sqlalchemy.config.database import get_bd
from src.infra.sqlalchemy.repositories.simulado import RepositorioSimulado
from src.infra.sqlalchemy.repositories.erro import RepositorioErro


router = APIRouter()

@router.post('/simulados')
def cadastrar_simulados(simulado: Simulado, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    simulado = RepositorioSimulado(db).criar(simulado, usuario.id)
    return simulado

@router.get('/simulados')
def listar_simulados(usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    simulados = RepositorioSimulado(db).listar(usuario.id)
    return simulados

@router.delete('/simulados/{id}')
def deletar_simulados(id: int, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    RepositorioSimulado(db).deletar(id)  
    RepositorioErro(db).deletar(id)
    return {'Message': "Deletado com sucesso!"}