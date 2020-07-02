"""Add flag 'is_client'

Revision ID: a80664069f26
Revises: 5a1abcc1f037
Create Date: 2020-06-04 19:42:48.270572

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a80664069f26'
down_revision = '5a1abcc1f037'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('is_client', sa.Boolean(), nullable=False, server_default='0'))


def downgrade():
    op.drop_column('user', 'is_client')
