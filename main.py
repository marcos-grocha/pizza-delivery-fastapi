from fastapi import FastAPI

# --- Configurações ---
ALGORITHM = "HS256"
SECRET_KEY = "secret"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Inicia o Framework ---
app = FastAPI()

# --- Define e chama as rotas ---
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
