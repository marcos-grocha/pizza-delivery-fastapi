from fastapi import APIRouter

# Determina a rota à uma variável + pré caminho do endpoint + marcador para o /docs
auth_router = APIRouter(prefix="/auth", tags=["auth"])

# Determina a próxima combinação do endpoint
@auth_router.get("/")
async def autenticar():
    """
    Docstring para autenticar
    Essa é a rota padrão para autenticar
    """
    return {"mensagem": "Você acessou a rota de autenticação", "autenticação": False}