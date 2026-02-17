from fastapi import APIRouter, Depends, HTTPException
from models import Pedido, Usuario
from schemas import PedidoSchema
from dependencies import pegar_sessao, verificar_token
from sqlalchemy.orm import Session

# Determina a rota e bloqueia todos os endpoints seguintes
order_router = APIRouter(prefix="/order", tags=["order"], dependencies=[Depends(verificar_token)])

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você acessou a rota de pedidos"}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(
        usuario=pedido_schema.usuario,
        status=pedido_schema.status,
        preco=pedido_schema.preco
    )
    session.add(novo_pedido)
    session.commit()
    return {"mensagem": "Você criou um pedido"}

@order_router.get("/pedido/cancelar/{id_pedido}")
async def cancelar_pedido(id_pedido: int, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
    pedido = session.query(Pedido).filter(Pedido.id==id_pedido).first()
    if not pedido:
        raise HTTPException(status_code=404, detail="Pedido não encontrado")
    if not usuario.admin and pedido.usuario != usuario.id:
        raise HTTPException(status_code=403, detail="Você não tem permissão para cancelar este pedido")

    pedido.status = "CANCELADO"
    session.commit()
    return {"mensagem": f"Você cancelou o pedido número {pedido.id}", "pedido": pedido}