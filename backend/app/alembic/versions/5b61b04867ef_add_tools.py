"""add tools

Revision ID: 5b61b04867ef
Revises: 52e822035335
Create Date: 2021-02-04 13:48:26.421148

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b61b04867ef'
down_revision = '52e822035335'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_tool_id'), 'tool', ['id'], unique=False)
    op.create_table('user_tool',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('tool_id', sa.Integer(), nullable=False),
    sa.Column('details', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['tool_id'], ['tool.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id', 'tool_id', name='uix_user_tool_user_id_tool_id')
    )
    op.create_index(op.f('ix_user_tool_id'), 'user_tool', ['id'], unique=False)
    op.create_unique_constraint('uix_project_worker_active_user_project_worker', 'project_worker_active', ['project_worker_id', 'user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uix_project_worker_active_user_project_worker', 'project_worker_active', type_='unique')
    op.drop_index(op.f('ix_user_tool_id'), table_name='user_tool')
    op.drop_table('user_tool')
    op.drop_index(op.f('ix_tool_id'), table_name='tool')
    op.drop_table('tool')
    # ### end Alembic commands ###
