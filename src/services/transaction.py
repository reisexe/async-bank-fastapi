from fastapi import HTTPException
from src.database import database
from src.models.user import users as usuarios  
from src.models.transaction import transacoes
import sqlalchemy as sa

class TransactionService:
    """
    Serviço responsável pela lógica de negócio das operações bancárias.
    Lida com depósitos, saques e consulta de extrato.
    """

    async def depositar(self, user_id: int, valor: float):
        """
        Registra um depósito na tabela de transações e atualiza o saldo do usuário.
        """
        query_transacao = transacoes.insert().values(
            tipo="deposito",
            valor=valor,
            user_id=user_id
        )
        await database.execute(query_transacao)

        query_saldo = (
            usuarios.update()
            .where(usuarios.c.id == user_id)
            .values(saldo=usuarios.c.saldo + valor)
        )
        await database.execute(query_saldo)
        return {"message": "Depósito realizado com sucesso!"}

    async def sacar(self, user_id: int, valor: float):
        """
        Realiza o saque após validar se o usuário possui saldo suficiente em tempo real.
        """
        query_depositos = sa.select(sa.func.sum(transacoes.c.valor)).where(
            transacoes.c.user_id == user_id, 
            transacoes.c.tipo == "deposito"
        )
        query_saques = sa.select(sa.func.sum(transacoes.c.valor)).where(
            transacoes.c.user_id == user_id, 
            transacoes.c.tipo == "saque"
        )

        dep_val = await database.fetch_val(query_depositos)
        saq_val = await database.fetch_val(query_saques)

        total_dep = float(dep_val) if dep_val is not None else 0.0
        total_saq = float(saq_val) if saq_val is not None else 0.0
        user_saldo = total_dep - total_saq

        if user_saldo < valor:
            raise HTTPException(
                status_code=400, 
                detail=f"Saldo insuficiente! Saldo disponível: R$ {user_saldo:.2f}"
            )

        query_saque = transacoes.insert().values(
            user_id=user_id,
            valor=valor,
            tipo="saque"
        )
        await database.execute(query_saque)

        query_update_saldo = (
            usuarios.update()
            .where(usuarios.c.id == user_id)
            .values(saldo=usuarios.c.saldo - valor)
        )
        await database.execute(query_update_saldo)

        return {
            "message": "Saque realizado com sucesso!", 
            "valor_sacado": valor,
            "saldo_restante": user_saldo - valor
        }

    async def visualizar_extrato(self, user_id: int):
        """
        Retorna o histórico completo com data e hora.
        """
        query = transacoes.select().where(
            transacoes.c.user_id == user_id
        ).order_by(transacoes.c.data_de_registro.desc()) 
        
        resultado = await database.fetch_all(query)
        
        if not resultado:
            return {"message": "Você ainda não possui transações registradas."}
            
        return resultado