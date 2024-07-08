from pydantic import BaseModel
from typing import Optional

class CategoriaBase(BaseModel):
    nome: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    pk_id: int
    id: str

    class Config:
        orm_mode = True
        from_attributes = True  

class CentroTreinamentoBase(BaseModel):
    nome: str
    endereco: str
    proprietario: str

class CentroTreinamentoCreate(CentroTreinamentoBase):
    pass

class CentroTreinamento(CentroTreinamentoBase):
    pk_id: int
    id: str

    class Config:
        orm_mode = True
        from_attributes = True

class AtletaBase(BaseModel):
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: int
    categoria_id: int

class AtletaCreate(AtletaBase):
    pass

class Atleta(AtletaBase):
    pk_id: int
    id: str

    class Config:
        orm_mode = True
        from_attributes = True

class AtletaWithDetails(BaseModel):
    pk_id: int
    id: str
    nome: str
    cpf: str
    idade: int
    peso: float
    altura: float
    sexo: str
    centro_treinamento_id: Optional[int]
    categoria_id: Optional[int]
    centro_treinamento_nome: Optional[str]
    categoria_nome: Optional[str]

    class Config:
        orm_mode = True
        from_attributes = True
