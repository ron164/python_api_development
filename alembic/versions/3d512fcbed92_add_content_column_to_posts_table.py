"""add content column to posts table

Revision ID: 3d512fcbed92
Revises: 39423704ab69
Create Date: 2022-09-03 20:01:01.416309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d512fcbed92'
down_revision = '39423704ab69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
