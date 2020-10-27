"""empty message

Revision ID: d52896e4df80
Revises: 
Create Date: 2020-10-27 20:21:28.693208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd52896e4df80'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('info',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('otziv',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=1024), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('name_pdf', sa.String(length=64), nullable=True),
    sa.Column('name_img', sa.String(length=64), nullable=True),
    sa.Column('type_otz', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quest',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('text', sa.String(length=1024), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quest')
    op.drop_table('otziv')
    op.drop_table('info')
    # ### end Alembic commands ###
