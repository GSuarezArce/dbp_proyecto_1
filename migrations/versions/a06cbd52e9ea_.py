"""empty message

Revision ID: a06cbd52e9ea
Revises: 177877f315d3
Create Date: 2021-06-16 16:52:07.532351

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a06cbd52e9ea'
down_revision = '177877f315d3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('equipos', sa.Column('n_empates', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('equipos', 'n_empates')
    # ### end Alembic commands ###
