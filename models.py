from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# --- Cria a conexão com banco de dados ---
db = create_engine("sqlite:///banco.db")

# --- Cria a base do banco de dados ---
Base = declarative_base()

# --- Cria as classes/tabelas do banco ---
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String) # Definindo de maneira explícita
    email = Column(String, nullable=False)
    senha = Column(String)
    ativo = Column(Boolean)
    admin = Column(Boolean, default=False)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin

class Pedido(Base):
    __tablename__ = "pedidos"

    # STATUS_PEDIDOS = (
    #     ("PENDENTE", "Pendente"),
    #     ("CANCELADO", "Cancelado"),
    #     ("FINALIZADO", "Finalizado")
    # )

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario = Column(Integer, ForeignKey("usuarios.id"))
    status = Column(String) # from sqlalchemy_utils.types import ChoiceType
    preco = Column(Float)
    itens = relationship("ItemPedido", cascade="all, delete")

    def __init__(self, usuario, status="PENDENTE", preco=0):
        self.usuario = usuario
        self.status = status
        self.preco = preco

    def calcular_preco(self):
        preco_total = 0
        for item in self.itens:
            preco_total += item.quantidade * item.preco_unitario
        self.preco = preco_total

class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, autoincrement=True)
    quantidade = Column(Integer)
    sabor = Column(String)
    tamanho = Column(String)
    preco_unitario = Column(Float)
    pedido = Column(Integer, ForeignKey("pedidos.id"))

    def __init__(self, quantidade, sabor, tamanho, preco_unitario, pedido):
        self.quantidade = quantidade
        self.sabor = sabor
        self.tamanho = tamanho
        self.preco_unitario = preco_unitario
        self.pedido = pedido