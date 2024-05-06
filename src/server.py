from fastapi import FastAPI, Depends
from src.routers import rotas_auth, rotas_simulados, rotas_erros
from src.infra.sqlalchemy.config.database import criar_bd

app = FastAPI()

#ROTAS AUTH
app.include_router(rotas_auth.router, prefix='/auth')

#ROTAS SIMULADOS
app.include_router(rotas_simulados.router)

#ROTAS ERROS
app.include_router(rotas_erros.router)