from fastapi import FastAPI, Depends
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from src.routers import rotas_auth, rotas_simulados, rotas_erros
from src.infra.sqlalchemy.config.database import criar_bd

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

criar_bd()
app = FastAPI(middleware=middleware)

@app.get('/', tags=['Home'])
def home():
    return {"Message": "APPSimux!"}


#ROTAS AUTH
app.include_router(rotas_auth.router, prefix='/auth', tags=["Auth"])

#ROTAS SIMULADOS
app.include_router(rotas_simulados.router, tags=["Simulados"])

#ROTAS ERROS
app.include_router(rotas_erros.router, tags=["Erros"])



