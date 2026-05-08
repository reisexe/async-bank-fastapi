from pydantic import BaseModel, Field

# Esquema para ENTRADA de dados (o que o usuário envia no Insomnia)
class TransactionCreate(BaseModel):
    # 'gt=0' mata a regra do desafio de não aceitar valores negativos
    valor: float = Field(..., gt=0, description="Valor da transação (deve ser maior que zero)")

# Esquema para SAÍDA de dados (o que a API responde para o usuário)
class TransactionOut(BaseModel):
    id: int
    tipo: str
    valor: float
    user_id: int

    class Config:
        from_attributes = True # Isso permite que o Pydantic leia dados do SQLAlchemy