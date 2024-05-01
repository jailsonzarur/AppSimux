from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.schemas.simulado import Simulado
from src.infra.sqlalchemy.config.database import get_bd

router = APIRouter()

@router.post('/simulados')
def cadastrar_simulados(simulado: Simulado, db: Session = Depends(get_bd)):
    