from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
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

oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-oauth")
def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
    try:
        dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        id_usuario = dic_info.get("sub")
    except JWSError:
        raise HTTPException(status_code=401, detail="Token inválido, verifique a validade.")
    
    usuario = session.query(Usuario).filter(Usuario.id==id_usuario).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")
    
    return usuario