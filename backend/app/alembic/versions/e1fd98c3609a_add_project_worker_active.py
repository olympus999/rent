"""Add project_worker_active

Revision ID: e1fd98c3609a
Revises: 9e2e4ac5a27f
Create Date: 2020-12-16 20:40:15.905243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1fd98c3609a'
down_revision = '9e2e4ac5a27f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_worker_active',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('project_worker_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('created_dt', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['project_worker_id'], ['project_worker.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('user_id')
    )
    op.create_index(op.f('ix_project_worker_active_id'), 'project_worker_active', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_project_worker_active_id'), table_name='project_worker_active')
    op.drop_table('project_worker_active')
    # ### end Alembic commands ###
