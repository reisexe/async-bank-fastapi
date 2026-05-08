from src.database import metadata
import sqlalchemy as sa

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("username", sa.String, unique=True, nullable=False),
    sa.Column("password", sa.String, nullable=False),
    sa.Column("saldo", sa.Float, default=0.0)
)