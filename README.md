# Instalação
### Crie ambiente virtual:
```
python -m venv .venv
```

### Inicie o ambiente virtual:
```
.\.venv\Scripts\activate
```

### Instale as dependências dentro do ambiente:
```
pip install ...
```
- fastapi
- uvicorn
- sqlalchemy
- sqlalchemy_utils
- alembic
- passlib[bcrypt]
- python-jose[cryptography]
- python-dotenv
- python-multipart

### Execute o framework com reload automático
```
uvicorn main:app --reload
```

### Consulte a documentação da API gerado pelo FastAPI em:
```
http://localhost:8000/docs
```

--- 

# Banco de Dados
### Inicia o alembic
```alembic init alembic```

### Gera migração
```alembic revision --autogenerate -m "Mensagem da migração"```

### Roda migração
```alembic upgrade head```