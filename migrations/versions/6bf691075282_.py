"""empty message

Revision ID: 6bf691075282
Revises: 
Create Date: 2022-08-18 22:58:26.053527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6bf691075282'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('homeworld', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('homeworld'),
    sa.UniqueConstraint('homeworld')
    )
    op.create_table('planetas',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('email')
    )
    op.create_table('fav_people',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=120), nullable=True),
    sa.Column('people', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['people'], ['people.uid'], ),
    sa.ForeignKeyConstraint(['user'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('fav_planetas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user', sa.String(length=120), nullable=True),
    sa.Column('planetas', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['planetas'], ['planetas.name'], ),
    sa.ForeignKeyConstraint(['user'], ['user.email'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('fav_planetas')
    op.drop_table('fav_people')
    op.drop_table('user')
    op.drop_table('planetas')
    op.drop_table('people')
    # ### end Alembic commands ###