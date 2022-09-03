"""add foreign-key to post table

Revision ID: 4f5a5fdebb9d
Revises: cdfb961f00ed
Create Date: 2022-09-03 20:55:05.202986

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f5a5fdebb9d'
down_revision = 'cdfb961f00ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', 'posts')
    op.drop_column('posts', 'owner_id')
    pass
