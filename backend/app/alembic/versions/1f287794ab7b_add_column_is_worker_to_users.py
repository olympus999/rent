"""Add column is_worker to users

Revision ID: 1f287794ab7b
Revises: a80664069f26
Create Date: 2020-07-02 11:27:20.763570

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f287794ab7b'
down_revision = 'a80664069f26'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('is_worker', sa.Boolean(), nullable=False, server_default='0'))


def downgrade():
    op.drop_column('user', 'is_worker')
