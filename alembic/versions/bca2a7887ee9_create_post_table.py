"""create post table

Revision ID: bca2a7887ee9
Revises: 
Create Date: 2025-09-24 21:47:39.710619

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bca2a7887ee9'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts',
    sa.Column('id',sa.Integer(),nullable=False,primary_key=True),
    sa.Column('title',sa.String(),nullable=False)
    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
