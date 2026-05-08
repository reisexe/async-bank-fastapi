from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from src.controllers import auth, post, transaction
from src.database import database, metadata, engine # Importamos o metadata e engine aqui
from src.exceptions import NotFoundPostError

@asynccontextmanager
async def lifespan(app: FastAPI):
    import src.models.user 
    import src.models.post

    metadata.create_all(engine)
    
    await database.connect()
    yield
    await database.disconnect()

tags_metadata = [
    {
        "name": "auth",
        "description": "Operações para autenticação e geração de tokens JWT.",
    },
    {
        "name": "banking",
        "description": "Operações bancárias essenciais: depósitos, saques e extratos.",
    },
    {
        "name": "post",
        "description": "Gerenciamento de posts do blog pessoal.",
    },
]

description = """
DIO Bank & Blog API 🚀

Esta API combina um sistema de blog pessoal com funcionalidades bancárias assíncronas.

## Funcionalidades Bancárias 💰
* **Depósitos**: Adicione saldo à sua conta de forma segura.
* **Saques**: Retire valores (o sistema valida se você possui saldo suficiente).
* **Extrato**: Consulte todo o seu histórico de transações.

---
*Desenvolvido como desafio prático para a DIO.*
"""

app = FastAPI(
    title="DIO Async Bank API",
    version="1.2.0",
    summary="API Bancária e Blog Pessoal Assíncrona.",
    description=description,
    openapi_tags=tags_metadata,
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, tags=["auth"])
app.include_router(post.router, tags=["post"])
app.include_router(transaction.router, tags=["banking"])

@app.exception_handler(NotFoundPostError)
async def not_found_post_exception_handler(request: Request, exc: NotFoundPostError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )