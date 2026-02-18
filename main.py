from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- Configurações ---
ALGORITHM = "HS256"
SECRET_KEY = "secret"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# --- Inicia o Framework ---
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, o endereço do front
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Define e chama as rotas ---
from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)
