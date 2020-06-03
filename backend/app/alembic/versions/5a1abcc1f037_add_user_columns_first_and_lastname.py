"""Add user columns first- and lastname

Revision ID: 5a1abcc1f037
Revises: d4867f3a4c0a
Create Date: 2020-05-27 22:34:33.940272

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a1abcc1f037'
down_revision = 'd4867f3a4c0a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column("first_name", sa.String()))
    op.add_column('user', sa.Column("last_name", sa.String()))


def downgrade():
    op.drop_column('user', "first_name")
    op.drop_column('user', "last_name")
