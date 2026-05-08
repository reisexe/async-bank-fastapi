# Async Bank API - FastAPI
Este projeto é uma API de sistema bancário assíncrono desenvolvida como parte do desafio do curso de Backend com Python da DIO. 

## Tecnologias Utilizadas
- **Python 3.13**
- **FastAPI** (Framework web de alta performance)
- **PostgreSQL** (Banco de dados relacional)
- **SQLAlchemy Core** (Consultas SQL eficientes)
- **Databases** (Suporte assíncrono para o banco de dados)

## Funcionalidades
- **Cadastro e Login**: Autenticação via JWT.
- **Depósitos**: Registro de entrada com atualização automática de saldo.
- **Saques**: Validação de saldo em tempo real (não permite saques sem saldo suficiente).
- **Extrato**: Histórico detalhado de transações ordenado por data de registro.

## Como rodar o projeto
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Configure seu banco de dados no arquivo `.env`.
5. Inicie o servidor: `uvicorn src.main:app --reload`.
