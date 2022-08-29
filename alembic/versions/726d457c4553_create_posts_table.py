"""create posts table

Revision ID: 726d457c4553
Revises: 
Create Date: 2022-08-29 23:40:47.900995

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '726d457c4553'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title',sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_index('posts')
    pass
