from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.infra.providers import token_provider, hash_provider
from src.schemas.usuario import Usuario, LoginData, LoginSucesso
from src.infra.sqlalchemy.config.database import get_bd
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.routers.auth_utils import obter_usuario_logado

router = APIRouter()

@router.post('/signup', status_code=status.HTTP_201_CREATED)
def signup(usuario: Usuario, db: Session = Depends(get_bd)):
    
    usuario_localizado = RepositorioUsuario(db).obter_por_username(usuario.username)

    if usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username já existente.')
    
    usuario = RepositorioUsuario(db).criar(usuario)
    return {'Message': 'Usuário cadastrado com sucesso!'}

@router.post('/signin')
def signin(login_data: LoginData, db: Session = Depends(get_bd)):

    usuario_localizado = RepositorioUsuario(db).obter_por_username(login_data.username)

    if not usuario_localizado:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username ou senha estão incorretos.')
    
    senha_valida = hash_provider.verificar_hash(login_data.senha, usuario_localizado.senha)

    if not senha_valida:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Username ou senha estão incorretos.')
    
    #Gerar JWT Token

    token_jwt = token_provider.criar_acess_token({'sub': usuario_localizado.username})
    return LoginSucesso(username=usuario_localizado.username, acess_token=token_jwt)

@router.get('/me', response_model=Usuario)
def my_simulados(usuario: Usuario = Depends(obter_usuario_logado), db: Session = Depends(get_bd)):
    return usuario

