from fastapi import APIRouter, Depends, HTTPException
from src.schemas.transaction import TransactionCreate, TransactionOut
from src.services.transaction import TransactionService
from src.security import get_current_user 
from fastapi.responses import JSONResponse

router = APIRouter()
service = TransactionService()

@router.post("/deposito")
async def deposito(dados: TransactionCreate, user = Depends(get_current_user)):
    return await service.depositar(user["user_id"], dados.valor)

@router.post("/saque")
async def saque(dados: TransactionCreate, user = Depends(get_current_user)):
    return await service.sacar(user["user_id"], dados.valor)

@router.get("/extrato")
async def extrato(user = Depends(get_current_user)):
    return await service.visualizar_extrato(user["user_id"])