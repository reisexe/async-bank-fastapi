import sqlalchemy as sa
from src.database import metadata

transacoes = sa.Table(
    "transacoes",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("tipo", sa.String), 
    sa.Column("valor", sa.Float, nullable=False),
    sa.Column("user_id", sa.ForeignKey("users.id"), nullable=False),
    sa.Column("data_de_registro", sa.DateTime(timezone=True), server_default=sa.func.now()))