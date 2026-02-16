from fastapi import APIRouter, Depends
from models import Pedido
from schemas import PedidoSchema
from dependencies import pegar_sessao
from sqlalchemy.orm import Session

# Determina a rota à uma variável + pré caminho do endpoint + marcador para o /docs
order_router = APIRouter(prefix="/order", tags=["order"])

# Determina a próxima combinação do endpoint
@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/criar_pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(
        usuario=pedido_schema.usuario,
        status=pedido_schema.status,
        preco=pedido_schema.preco
    )
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": "Você criou um pedido"}