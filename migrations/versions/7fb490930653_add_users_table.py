"""Add users table
Revision ID: 7fb490930653
Revises: 0d29d33a28ab
Create Date: 2026-05-06 19:47:50.775304
"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa

revision: str = '7fb490930653'
down_revision: Union[str, None] = '0d29d33a28ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('password', sa.String(), nullable=False),
    )

def downgrade() -> None:
    op.drop_table('users')