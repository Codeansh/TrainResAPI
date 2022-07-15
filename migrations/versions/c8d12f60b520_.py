"""empty message

Revision ID: c8d12f60b520
Revises: 
Create Date: 2022-02-27 23:34:30.441363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8d12f60b520'
down_revision = None
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