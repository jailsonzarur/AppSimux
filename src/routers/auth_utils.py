from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from src.infra.providers import token_provider
from src.infra.sqlalchemy.repositories.usuario import RepositorioUsuario
from src.infra.sqlalchemy.config.database import get_bd
from sqlalchemy.orm import Session

oauth2_schema = OAuth2PasswordBearer(tokenUrl='token')

def obter_usuario_logado(token: str = Depends(oauth2_schema), db: Session = Depends(get_bd)):
    
    try:
        username = token_provider.verificar_acess_token(token)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido.')
    
    if not username:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido.')
    
    usuario = RepositorioUsuario(db).obter_por_username(username)

    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token inválido')
    
    return usuario