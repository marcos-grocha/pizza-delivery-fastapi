# --- Inicia o Framework ---
from fastapi import FastAPI

app = FastAPI()

# --- Define e chama as rotas ---
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
