"""Add userRole logic instead of isSuperuser, isClient and isWorker

Revision ID: 0110018d511c
Revises: 1f287794ab7b
Create Date: 2020-08-18 18:54:39.420375

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '0110018d511c'
down_revision = '1f287794ab7b'
branch_labels = None
depends_on = None


def upgrade():
    # Create user_role and add column to user
    user_role = op.create_table(
        "user_role",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(), nullable=False, unique=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.bulk_insert(user_role,
                   [
                       {'id': 1, 'name': 'worker'},
                       {'id': 2, 'name': 'client'},
                       {'id': 3, 'name': 'superuser'}
                   ]
                   )

    op.add_column('user', sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=False, server_default='worker'))
    op.create_foreign_key('user_role_fkey', 'user', 'user_role', ['role'], ['name'])

    # Remove unnecessary columns
    op.drop_column('user', 'is_worker')
    op.drop_column('user', 'is_client')
    op.drop_column('user', 'is_superuser')


def downgrade():
    op.add_column('user', sa.Column('is_worker', sa.Boolean(), nullable=False, server_default='1'))
    op.add_column('user', sa.Column('is_client', sa.Boolean(), nullable=False, server_default='0'))
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=False, server_default='0'))

    op.drop_constraint('user_role_fkey', 'user')

    op.drop_column('user', 'role')

    op.drop_table('user_role')
