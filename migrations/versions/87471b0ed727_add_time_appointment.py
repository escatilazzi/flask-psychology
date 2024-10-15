"""add time appointment

Revision ID: 87471b0ed727
Revises: a64a0e2e6852
Create Date: 2024-10-08 23:26:14.449036

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '87471b0ed727'
down_revision = 'a64a0e2e6852'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.Time(), nullable=False))
        batch_op.alter_column('date',
               existing_type=postgresql.TIMESTAMP(),
               type_=sa.Date(),
               existing_nullable=False)

    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.add_column(sa.Column('appointment_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'appointments', ['appointment_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('sessions', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('appointment_id')

    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.Date(),
               type_=postgresql.TIMESTAMP(),
               existing_nullable=False)
        batch_op.drop_column('time')

    # ### end Alembic commands ###
