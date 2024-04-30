from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app_simux.db"
#SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:pangare@localhost[3306]/app_blx.db"
#SQLALCHEMY_DATABASE_URL = "postgresql://postgres:pangare@localhost:5432/appblx"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def criar_bd():
    Base.metadata.create_all(bind=engine)

def get_bd():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()