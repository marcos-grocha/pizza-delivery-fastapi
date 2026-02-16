from fastapi import APIRouter

# Determina a rota à uma variável + pré caminho do endpoint + marcador para o /docs
order_router = APIRouter(prefix="/order", tags=["order"])

# Determina a próxima combinação do endpoint
@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}