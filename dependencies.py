from fastapi import Depends, HTTPException
from jose import jwt, JWSError
from main import SECRET_KEY, ALGORITHM
from models import db, Usuario
from sqlalchemy.orm import sessionmaker, Session

def pegar_sessao():
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def verificar_token(token, session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = dic_info.get("sub")
    except JWSError:
        raise HTTPException(status_code=401, detail="Token inválido, verifique a validade.")
    
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    
    return usuario