"""Added Users and Movies models

Revision ID: 94f4d967e0a8
Revises: ad9fd754e63b
Create Date: 2023-10-13 19:20:48.516450

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '94f4d967e0a8'
down_revision: Union[str, None] = 'ad9fd754e63b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('admins', 'updated_at')
    op.drop_column('movies', 'updated_at')
    op.drop_column('users', 'updated_at')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('movies', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('admins', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
