"""add last few columns to posts table

Revision ID: 613d350d0545
Revises: bfe7ea98219e
Create Date: 2022-04-14 19:42:08.820697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '613d350d0545'
down_revision = 'bfe7ea98219e'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
