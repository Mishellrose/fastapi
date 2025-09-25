"""add content coloumn to post table

Revision ID: 4f64d644acaf
Revises: bca2a7887ee9
Create Date: 2025-09-24 21:51:50.616051

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4f64d644acaf'
down_revision: Union[str, Sequence[str], None] = 'bca2a7887ee9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts',sa.Column('content',sa.String(),nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
