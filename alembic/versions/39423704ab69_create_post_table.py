"""create post table

Revision ID: 39423704ab69
Revises: 04c8a1b9c02f
Create Date: 2022-09-03 19:47:34.327823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39423704ab69'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('post')
    pass
