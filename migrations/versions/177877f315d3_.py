"""empty message

Revision ID: 177877f315d3
Revises: fc1393e717d9
Create Date: 2021-06-13 12:07:34.675743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '177877f315d3'
down_revision = 'fc1393e717d9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('solicitudes',
    sa.Column('id_solicitud', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=10000), nullable=False),
    sa.Column('monto_solicitado', sa.Float(), nullable=False),
    sa.Column('id_persona', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_persona'], ['usuario.id_persona'], ),
    sa.PrimaryKeyConstraint('id_solicitud')
    )
    op.create_table('tarjeta_de_credito',
    sa.Column('id_tarjeta', sa.Integer(), nullable=False),
    sa.Column('n_tarjeta', sa.Integer(), nullable=False),
    sa.Column('id_usuario', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id_persona'], ),
    sa.PrimaryKeyConstraint('id_tarjeta')
    )
    op.drop_table('tarjeta')
    op.add_column('usuario', sa.Column('dinero_en_cuenta', sa.Float(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usuario', 'dinero_en_cuenta')
    op.create_table('tarjeta',
    sa.Column('id_tarjeta', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('n_tarjeta', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_usuario', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_usuario'], ['usuario.id_persona'], name='tarjeta_id_usuario_fkey'),
    sa.PrimaryKeyConstraint('id_tarjeta', name='tarjeta_pkey')
    )
    op.drop_table('tarjeta_de_credito')
    op.drop_table('solicitudes')
    # ### end Alembic commands ###