"""city table

Revision ID: c6f02e4b5b63
Revises: 8bc488de7bbc
Create Date: 2021-03-10 17:19:11.078125

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6f02e4b5b63'
down_revision = '8bc488de7bbc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('city', sa.Column('date_posted', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('city', 'date_posted')
    # ### end Alembic commands ###
