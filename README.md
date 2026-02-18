# 🍕 Marcão Pizzaria
Sistema *backend* que expõe a **API** para [Pizza Delivery React](https://github.com/marcos-grocha/pizza-delivery-react).

## Instalação
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
pip install -r requirements.txt
```
<!--
```pip install ...```
- fastapi
- uvicorn
- sqlalchemy
- sqlalchemy_utils
- alembic
- passlib[bcrypt]
- python-jose[cryptography]
- python-dotenv
- python-multipart
- pipreqs
-->

### Execute o framework com reload automático
```
uvicorn main:app --reload
```

### Consulte a documentação da API gerado pelo FastAPI em:
```http://localhost:8000/docs```

--- 

## Banco de Dados
### Inicia o alembic
```alembic init alembic```

### Gera migração
```alembic revision --autogenerate -m "Mensagem da migração"```

### Roda migração
```alembic upgrade head```

--- 

## Endpoints
<img width="1867" height="451" alt="image" src="https://github.com/user-attachments/assets/58c67f58-ea94-4e4e-95d9-28f3e472ea70" />
<img width="1858" height="715" alt="image" src="https://github.com/user-attachments/assets/fa1cf4ac-bfb0-4271-b25a-ef725e96d4a0" />

---
## Autor
Desenvolvido por [Marcos Rocha](https://www.linkedin.com/in/marcos-grocha/).