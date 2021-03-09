"""Fix columns

Revision ID: 1829e668f7b0
Revises: 6357364d6380
Create Date: 2020-12-10 06:53:54.533856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1829e668f7b0'
down_revision = '6357364d6380'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('project', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.add_column('project_worker', sa.Column('removed_dt', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_worker', 'removed_dt')
    op.alter_column('project', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###
