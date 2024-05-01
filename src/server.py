from fastapi import FastAPI, Depends
from src.routers import rotas_auth, rotas_simulados


app = FastAPI()

#ROTAS AUTH
app.include_router(rotas_auth.router, prefix='/auth')

#ROTAS SIMULADOS
app.include_router(rotas_simulados.router)