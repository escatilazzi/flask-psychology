"""delete column

Revision ID: 8a7ce05a5849
Revises: 88df872d22a2
Create Date: 2024-10-17 03:16:01.074095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a7ce05a5849'
down_revision = '88df872d22a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('appointments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(length=50), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
