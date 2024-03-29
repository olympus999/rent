"""Improve accounting

Revision ID: e83d032b559b
Revises: c24e28685659
Create Date: 2021-02-22 19:01:23.276021

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e83d032b559b'
down_revision = 'c24e28685659'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('accounting_balance', 'comment')
    op.add_column('accounting_hour', sa.Column('modified_dt', sa.DateTime(), nullable=True))
    op.add_column('accounting_hour', sa.Column('project_id', sa.Integer(), nullable=False))
    op.create_index(op.f('ix_accounting_hour_project_id'), 'accounting_hour', ['project_id'], unique=False)
    op.drop_constraint('uix_accounting_hour_user_id_day', 'accounting_hour', type_='unique')
    op.create_unique_constraint('uix_accounting_hour_user_id_day', 'accounting_hour', ['project_id', 'user_id', 'day'])
    op.create_foreign_key(None, 'accounting_hour', 'project', ['project_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'accounting_hour', type_='foreignkey')
    op.drop_constraint('uix_accounting_hour_user_id_day', 'accounting_hour', type_='unique')
    op.create_unique_constraint('uix_accounting_hour_user_id_day', 'accounting_hour', ['user_id', 'day'])
    op.drop_index(op.f('ix_accounting_hour_project_id'), table_name='accounting_hour')
    op.drop_column('accounting_hour', 'project_id')
    op.drop_column('accounting_hour', 'modified_dt')
    op.add_column('accounting_balance', sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
