"""add user table

Revision ID: 44c5b594a019
Revises: 4f64d644acaf
Create Date: 2025-09-24 21:53:53.157837

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '44c5b594a019'
down_revision: Union[str, Sequence[str], None] = '4f64d644acaf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('users',
    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('email',sa.String(),nullable=False,unique=True),
    sa.Column('password',sa.String(),nullable=False),
    sa.Column('created_at',sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text('now()')),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
