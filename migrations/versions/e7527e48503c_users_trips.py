"""users + trips

Revision ID: e7527e48503c
Revises: 
Create Date: 2018-03-17 10:21:52.406592

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7527e48503c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('trip',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tripname', sa.String(length=64), nullable=True),
    sa.Column('destination', sa.String(length=64), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_trip_destination'), 'trip', ['destination'], unique=True)
    op.create_index(op.f('ix_trip_tripname'), 'trip', ['tripname'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_trip_tripname'), table_name='trip')
    op.drop_index(op.f('ix_trip_destination'), table_name='trip')
    op.drop_table('trip')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###