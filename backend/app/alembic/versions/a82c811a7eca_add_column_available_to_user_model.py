"""Add column 'available' to User model

Revision ID: a82c811a7eca
Revises: 0110018d511c
Create Date: 2020-11-19 23:55:38.421280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a82c811a7eca'
down_revision = '0110018d511c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('available', sa.Boolean(), server_default='1', nullable=False))
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'role',
               existing_type=sa.VARCHAR(),
               nullable=True,
               existing_server_default=sa.text("'worker'::character varying"))
    op.create_index(op.f('ix_user_first_name'), 'user', ['first_name'], unique=False)
    op.create_index(op.f('ix_user_last_name'), 'user', ['last_name'], unique=False)
    op.drop_index('ix_user_full_name', table_name='user')
    op.drop_column('user', 'full_name')
    op.alter_column('user_role', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_role', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('user', sa.Column('full_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.create_index('ix_user_full_name', 'user', ['full_name'], unique=False)
    op.drop_index(op.f('ix_user_last_name'), table_name='user')
    op.drop_index(op.f('ix_user_first_name'), table_name='user')
    op.alter_column('user', 'role',
               existing_type=sa.VARCHAR(),
               nullable=False,
               existing_server_default=sa.text("'worker'::character varying"))
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_column('user', 'available')
    # ### end Alembic commands ###
