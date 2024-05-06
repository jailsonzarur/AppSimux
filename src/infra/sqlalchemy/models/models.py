from src.infra.sqlalchemy.config.database import Base
from sqlalchemy import String, Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(String, primary_key=True)
    username = Column(String)
    senha = Column(String)

    simulados = relationship('Simulado', back_populates='usuario')

class Simulado(Base):
    __tablename__ = 'simulados'

    id = Column(String, primary_key=True)
    tipo = Column(String)
    data = Column(Date)
    usuario_id = Column(String, ForeignKey('usuarios.id', name = 'fk_usuario'))

    usuario = relationship('Usuario', back_populates='simulados')
    erros = relationship('Erro', back_populates='simulado')


class Erro(Base):
    __tablename__ = 'erros'

    id = Column(String, primary_key=True)
    materia = Column(String)
    assunto = Column(String)
    bloco = Column(String)
    simulado_id = Column(String, ForeignKey('simulados.id', name='fk_simulado'))

    simulado = relationship('Simulado', back_populates='erros')