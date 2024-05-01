from fastapi import FastAPI, Depends
from src.routers import rotas_auth


app = FastAPI()

#ROTAS AUTH
app.include_router(rotas_auth.router)
