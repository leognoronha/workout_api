from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import app.crud as crud
import app.models as models
import app.schemas as schemas
from app.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Categoria Endpoints
@app.post("/categorias/", response_model=schemas.Categoria)
def create_categoria(categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    if not categoria.nome:
        raise HTTPException(status_code=400, detail="Preencha todos os campos")
    return crud.create_categoria(db=db, categoria=categoria)

@app.get("/categorias/{categoria_id}", response_model=schemas.Categoria)
def read_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = crud.get_categoria(db, categoria_id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria

@app.get("/categorias/", response_model=list[schemas.Categoria])
def read_categorias(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    categorias = crud.get_categorias(db, skip=skip, limit=limit)
    return categorias

@app.patch("/categorias/{categoria_id}", response_model=schemas.Categoria)
def update_categoria(categoria_id: int, categoria: schemas.CategoriaCreate, db: Session = Depends(get_db)):
    db_categoria = crud.update_categoria(db, categoria_id=categoria_id, categoria=categoria)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria

@app.delete("/categorias/{categoria_id}", response_model=schemas.Categoria)
def delete_categoria(categoria_id: int, db: Session = Depends(get_db)):
    db_categoria = crud.delete_categoria(db, categoria_id=categoria_id)
    if db_categoria is None:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return db_categoria

# CentroTreinamento Endpoints
@app.post("/centros_treinamento/", response_model=schemas.CentroTreinamento)
def create_centro_treinamento(centro_treinamento: schemas.CentroTreinamentoCreate, db: Session = Depends(get_db)):
    if not centro_treinamento.nome or not centro_treinamento.endereco or not centro_treinamento.proprietario:
        raise HTTPException(status_code=400, detail="Preencha todos os campos")
    return crud.create_centro_treinamento(db=db, centro_treinamento=centro_treinamento)

@app.get("/centros_treinamento/{centro_treinamento_id}", response_model=schemas.CentroTreinamento)
def read_centro_treinamento(centro_treinamento_id: int, db: Session = Depends(get_db)):
    db_centro_treinamento = crud.get_centro_treinamento(db, centro_treinamento_id=centro_treinamento_id)
    if db_centro_treinamento is None:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    return db_centro_treinamento

@app.get("/centros_treinamento/", response_model=list[schemas.CentroTreinamento])
def read_centros_treinamento(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    centros_treinamento = crud.get_centros_treinamento(db, skip=skip, limit=limit)
    return centros_treinamento

@app.patch("/centros_treinamento/{centro_treinamento_id}", response_model=schemas.CentroTreinamento)
def update_centro_treinamento(centro_treinamento_id: int, centro_treinamento: schemas.CentroTreinamentoCreate, db: Session = Depends(get_db)):
    db_centro_treinamento = crud.update_centro_treinamento(db, centro_treinamento_id=centro_treinamento_id, centro_treinamento=centro_treinamento)
    if db_centro_treinamento is None:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    return db_centro_treinamento

@app.delete("/centros_treinamento/{centro_treinamento_id}", response_model=schemas.CentroTreinamento)
def delete_centro_treinamento(centro_treinamento_id: int, db: Session = Depends(get_db)):
    db_centro_treinamento = crud.delete_centro_treinamento(db, centro_treinamento_id=centro_treinamento_id)
    if db_centro_treinamento is None:
        raise HTTPException(status_code=404, detail="Centro de treinamento não encontrado")
    return db_centro_treinamento

# Atleta Endpoints
@app.post("/atletas/", response_model=schemas.Atleta)
def create_atleta(atleta: schemas.AtletaCreate, db: Session = Depends(get_db)):
    if not atleta.nome or not atleta.cpf or not atleta.idade or not atleta.peso or not atleta.altura or not atleta.sexo or not atleta.centro_treinamento_id or not atleta.categoria_id:
        raise HTTPException(status_code=400, detail="Preencha todos os campos")
    
    existing_atleta = crud.get_atleta_by_cpf(db, atleta.cpf)
    if existing_atleta:
        raise HTTPException(status_code=303, detail=f"Já existe um atleta cadastrado com o cpf: {atleta.cpf}")
    
    try:
        return crud.create_atleta(db=db, atleta=atleta)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/atletas/{atleta_id}", response_model=schemas.Atleta)
def read_atleta(atleta_id: int, db: Session = Depends(get_db)):
    db_atleta = crud.get_atleta(db, atleta_id=atleta_id)
    if db_atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return db_atleta

@app.get("/atletas/", response_model=list[schemas.Atleta])
def read_atletas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    atletas = crud.get_atletas(db, skip=skip, limit=limit)
    return atletas

@app.patch("/atletas/{atleta_id}", response_model=schemas.Atleta)
def update_atleta(atleta_id: int, atleta: schemas.AtletaCreate, db: Session = Depends(get_db)):
    try:
        db_atleta = crud.update_atleta(db, atleta_id=atleta_id, atleta=atleta)
        if db_atleta is None:
            raise HTTPException(status_code=404, detail="Atleta não encontrado")
        return db_atleta
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/atletas/{atleta_id}", response_model=schemas.Atleta)
def delete_atleta(atleta_id: int, db: Session = Depends(get_db)):
    db_atleta = crud.delete_atleta(db, atleta_id=atleta_id)
    if db_atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return db_atleta

@app.get("/atletas/nome/{nome}", response_model=list[schemas.Atleta])
def read_atleta_by_nome(nome: str, db: Session = Depends(get_db)):
    db_atletas = crud.get_atleta_by_nome(db, nome=nome)
    if not db_atletas:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return db_atletas

@app.get("/atletas/cpf/{cpf}", response_model=schemas.Atleta)
def read_atleta_by_cpf(cpf: str, db: Session = Depends(get_db)):
    db_atleta = crud.get_atleta_by_cpf(db, cpf=cpf)
    if db_atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return db_atleta

@app.get("/atletas/{atleta_id}/detalhes", response_model=schemas.AtletaWithDetails)
def read_atleta_with_details(atleta_id: int, db: Session = Depends(get_db)):
    db_atleta = crud.get_atleta_with_details(db, atleta_id=atleta_id)
    if db_atleta is None:
        raise HTTPException(status_code=404, detail="Atleta não encontrado")
    return schemas.AtletaWithDetails(**db_atleta._asdict())

# Endpoint para obter todos os atletas, categorias e centros de treinamento
@app.get("/todos", response_model=dict)
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    atletas, categorias, centros_treinamento = crud.get_all_data(db, skip=skip, limit=limit)
    return {
        "atletas": [schemas.Atleta.from_orm(atleta) for atleta in atletas],
        "categorias": [schemas.Categoria.from_orm(categoria) for categoria in categorias],
        "centros_treinamento": [schemas.CentroTreinamento.from_orm(centro) for centro in centros_treinamento]
    }
