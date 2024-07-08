from sqlalchemy.orm import Session
import app.models as models
import app.schemas as schemas

# Categoria CRUD
def get_categoria(db: Session, categoria_id: int):
    return db.query(models.Categoria).filter(models.Categoria.pk_id == categoria_id).first()

def get_categorias(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Categoria).offset(skip).limit(limit).all()

def create_categoria(db: Session, categoria: schemas.CategoriaCreate):
    db_categoria = models.Categoria(nome=categoria.nome)
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_categoria(db: Session, categoria_id: int, categoria: schemas.CategoriaCreate):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.pk_id == categoria_id).first()
    if db_categoria:
        db_categoria.nome = categoria.nome
        db.commit()
        db.refresh(db_categoria)
    return db_categoria

def delete_categoria(db: Session, categoria_id: int):
    db_categoria = db.query(models.Categoria).filter(models.Categoria.pk_id == categoria_id).first()
    if db_categoria:
        db.delete(db_categoria)
        db.commit()
    return db_categoria

# CentroTreinamento CRUD
def get_centro_treinamento(db: Session, centro_treinamento_id: int):
    return db.query(models.CentroTreinamento).filter(models.CentroTreinamento.pk_id == centro_treinamento_id).first()

def get_centros_treinamento(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.CentroTreinamento).offset(skip).limit(limit).all()

def create_centro_treinamento(db: Session, centro_treinamento: schemas.CentroTreinamentoCreate):
    db_centro_treinamento = models.CentroTreinamento(
        nome=centro_treinamento.nome,
        endereco=centro_treinamento.endereco,
        proprietario=centro_treinamento.proprietario
    )
    db.add(db_centro_treinamento)
    db.commit()
    db.refresh(db_centro_treinamento)
    return db_centro_treinamento

def update_centro_treinamento(db: Session, centro_treinamento_id: int, centro_treinamento: schemas.CentroTreinamentoCreate):
    db_centro_treinamento = db.query(models.CentroTreinamento).filter(models.CentroTreinamento.pk_id == centro_treinamento_id).first()
    if db_centro_treinamento:
        db_centro_treinamento.nome = centro_treinamento.nome
        db_centro_treinamento.endereco = centro_treinamento.endereco
        db_centro_treinamento.proprietario = centro_treinamento.proprietario
        db.commit()
        db.refresh(db_centro_treinamento)
    return db_centro_treinamento

def delete_centro_treinamento(db: Session, centro_treinamento_id: int):
    db_centro_treinamento = db.query(models.CentroTreinamento).filter(models.CentroTreinamento.pk_id == centro_treinamento_id).first()
    if db_centro_treinamento:
        # Atualizar atletas associados a esse centro de treinamento
        db.query(models.Atleta).filter(models.Atleta.centro_treinamento_id == centro_treinamento_id).update({models.Atleta.centro_treinamento_id: None})
        db.commit()
        
        # Excluir o centro de treinamento
        db.delete(db_centro_treinamento)
        db.commit()
    return db_centro_treinamento

# Atleta CRUD
def get_atleta(db: Session, atleta_id: int):
    return db.query(models.Atleta).filter(models.Atleta.pk_id == atleta_id).first()

def get_atletas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Atleta).offset(skip).limit(limit).all()

def get_atleta_by_nome(db: Session, nome: str):
    return db.query(models.Atleta).filter(models.Atleta.nome == nome).all()

def get_atleta_by_cpf(db: Session, cpf: str):
    return db.query(models.Atleta).filter(models.Atleta.cpf == cpf).first()

def create_atleta(db: Session, atleta: schemas.AtletaCreate):
    if db.query(models.Atleta).filter(models.Atleta.cpf == atleta.cpf).first():
        return None

    # Verificar se centro_treinamento_id existe
    if not db.query(models.CentroTreinamento).filter(models.CentroTreinamento.pk_id == atleta.centro_treinamento_id).first():
        raise ValueError(f"Centro de treinamento com ID {atleta.centro_treinamento_id} não existe.")

    # Verificar se categoria_id existe
    if not db.query(models.Categoria).filter(models.Categoria.pk_id == atleta.categoria_id).first():
        raise ValueError(f"Categoria com ID {atleta.categoria_id} não existe.")

    db_atleta = models.Atleta(
        nome=atleta.nome,
        cpf=atleta.cpf,
        idade=atleta.idade,
        peso=atleta.peso,
        altura=atleta.altura,
        sexo=atleta.sexo,
        centro_treinamento_id=atleta.centro_treinamento_id,
        categoria_id=atleta.categoria_id
    )
    db.add(db_atleta)
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

def update_atleta(db: Session, atleta_id: int, atleta: schemas.AtletaCreate):
    db_atleta = db.query(models.Atleta).filter(models.Atleta.pk_id == atleta_id).first()
    if not db_atleta:
        return None

    # Verificar se centro_treinamento_id existe
    if not db.query(models.CentroTreinamento).filter(models.CentroTreinamento.pk_id == atleta.centro_treinamento_id).first():
        raise ValueError(f"Centro de treinamento com ID {atleta.centro_treinamento_id} não existe.")

    # Verificar se categoria_id existe
    if not db.query(models.Categoria).filter(models.Categoria.pk_id == atleta.categoria_id).first():
        raise ValueError(f"Categoria com ID {atleta.categoria_id} não existe.")

    db_atleta.nome = atleta.nome
    db_atleta.cpf = atleta.cpf
    db_atleta.idade = atleta.idade
    db_atleta.peso = atleta.peso
    db_atleta.altura = atleta.altura
    db_atleta.sexo = atleta.sexo
    db_atleta.centro_treinamento_id = atleta.centro_treinamento_id
    db_atleta.categoria_id = atleta.categoria_id
    db.commit()
    db.refresh(db_atleta)
    return db_atleta

def delete_atleta(db: Session, atleta_id: int):
    db_atleta = db.query(models.Atleta).filter(models.Atleta.pk_id == atleta_id).first()
    if db_atleta:
        db.delete(db_atleta)
        db.commit()
    return db_atleta

def get_atleta_with_details(db: Session, atleta_id: int):
    return db.query(
        models.Atleta.pk_id,
        models.Atleta.id,
        models.Atleta.nome,
        models.Atleta.cpf,
        models.Atleta.idade,
        models.Atleta.peso,
        models.Atleta.altura,
        models.Atleta.sexo,
        models.Atleta.centro_treinamento_id,
        models.Atleta.categoria_id,
        models.CentroTreinamento.nome.label("centro_treinamento_nome"),
        models.Categoria.nome.label("categoria_nome")
    ).join(
        models.CentroTreinamento, models.Atleta.centro_treinamento_id == models.CentroTreinamento.pk_id, isouter=True
    ).join(
        models.Categoria, models.Atleta.categoria_id == models.Categoria.pk_id, isouter=True
    ).filter(
        models.Atleta.pk_id == atleta_id
    ).first()

def get_all_data(db: Session, skip: int = 0, limit: int = 10):
    atletas = db.query(models.Atleta).offset(skip).limit(limit).all()
    categorias = db.query(models.Categoria).offset(skip).limit(limit).all()
    centros_treinamento = db.query(models.CentroTreinamento).offset(skip).limit(limit).all()
    return atletas, categorias, centros_treinamento