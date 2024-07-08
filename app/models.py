from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categoria'
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    nome = Column(String(10), unique=True, nullable=False)

class CentroTreinamento(Base):
    __tablename__ = 'centro_treinamento'
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    nome = Column(String(20), unique=True, nullable=False)
    endereco = Column(String(60), nullable=False)
    proprietario = Column(String(30), nullable=False)

class Atleta(Base):
    __tablename__ = 'atleta'
    pk_id = Column(Integer, primary_key=True, index=True)
    id = Column(String(36), default=lambda: str(uuid.uuid4()), unique=True, nullable=False)
    nome = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    idade = Column(Integer, nullable=False)
    peso = Column(Float(10, 2), nullable=False)
    altura = Column(Float(10, 2), nullable=False)
    sexo = Column(String(1), nullable=False)
    centro_treinamento_id = Column(Integer, ForeignKey('centro_treinamento.pk_id'), nullable=True)  # Permitir valores NULL
    categoria_id = Column(Integer, ForeignKey('categoria.pk_id'), nullable=False)
