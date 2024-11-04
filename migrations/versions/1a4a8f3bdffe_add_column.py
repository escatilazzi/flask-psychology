"""add column

Revision ID: 1a4a8f3bdffe
Revises: 04ff4f75da52
Create Date: 2024-10-28 00:43:21.843868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a4a8f3bdffe'
down_revision = '04ff4f75da52'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('recurrence_days', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.drop_column('recurrence_days')

    # ### end Alembic commands ###