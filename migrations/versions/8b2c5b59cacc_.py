"""empty message

Revision ID: 8b2c5b59cacc
Revises: d12b70d81f7f
Create Date: 2023-05-08 16:30:50.293157

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8b2c5b59cacc'
down_revision = 'd12b70d81f7f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('planet', 'moon_of_planet')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('planet', sa.Column('moon_of_planet', sa.VARCHAR(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###