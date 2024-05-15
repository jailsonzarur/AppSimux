from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.routers.auth_utils import obter_usuario_logado
from src.infra.sqlalchemy.repositories.erro import Erro
from src.schemas.simulado import Simulado
from src.schemas.erro import Erro
from src.schemas.usuario import Usuario
from src.infra.sqlalchemy.config.database import get_bd
from src.infra.sqlalchemy.repositories.erro import RepositorioErro

router = APIRouter()

@router.post('/simulados/erros/{simulado_id}')
def cadastrar_erros(simulado_id: str, erro: Erro, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    erro = RepositorioErro(db).criar(erro, simulado_id)
    return erro

@router.put('/simulados/erros/{erro_id}')
def editar_erro(erro_id: str, erro: Erro, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    RepositorioErro(db).editar(erro_id, erro)
    return {"Message": "Alterado com sucesso!"}

@router.get('/simulados/erros/{simulado_id}')
def listar_erros(simulado_id: str, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    erros = RepositorioErro(db).listar(simulado_id)
    return erros

@router.get('/simulados/erros/{bloco}')
def listar_erros_por_bloco(bloco: str, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    erros = RepositorioErro(db).listar_por_bloco(bloco)
    return erros

@router.get('/simulados/erros/{bloco}/{materia}')
def listar_erros_por_materia(bloco: str, materia:str, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    erros = RepositorioErro(db).listar_por_materia(bloco, materia)
    return erros

@router.delete('/simulados/erros/{erro_id}')
def deletar_erro(erro_id: str, usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    RepositorioErro(db).deletar(erro_id)
    return {'Message': "Deletado com sucesso!"}