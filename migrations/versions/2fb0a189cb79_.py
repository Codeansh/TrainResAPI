"""empty message

Revision ID: 2fb0a189cb79
Revises: c8d12f60b520
Create Date: 2022-02-27 23:43:39.495276

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2fb0a189cb79'
down_revision = 'c8d12f60b520'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('booking', 'booking_slot',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('booking', 'booking_slot',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###