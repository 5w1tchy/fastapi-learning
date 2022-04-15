"""add content column to posts table

Revision ID: fd3300c9c905
Revises: 348e0b65fed8
Create Date: 2022-04-14 19:11:38.993999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd3300c9c905'
down_revision = '348e0b65fed8'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
