from fastapi import APIRouter, Depends, HTTPException
from dependencies import pegar_sessao
from models import Usuario
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

# Determina a rota à uma variável + pré caminho do endpoint + marcador para o /docs
auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Determina a próxima combinação do endpoint
@auth_router.get("/")
async def autenticar():
    """
    Docstring: Essa é a rota padrão para autenticar
    """
    return {"mensagem": "Você acessou a rota de autenticação", "autenticação": False}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    else:
        novo_usuario = Usuario(
            nome=usuario_schema.nome,
            email=usuario_schema.email,
            senha=usuario_schema.senha,
            ativo=usuario_schema.ativo,
            admin=usuario_schema.admin
            )
        session.add(novo_usuario)
        session.commit()
        return {"mensagem": f"Usuário criado com sucesso! {usuario_schema.email}"}
