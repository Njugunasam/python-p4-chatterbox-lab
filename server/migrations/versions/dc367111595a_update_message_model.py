"""Update Message model

Revision ID: dc367111595a
Revises: 33d0e00628b0
Create Date: 2024-01-25 15:49:42.797930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dc367111595a'
down_revision = '33d0e00628b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.VARCHAR(),
               type_=sa.DateTime(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('messages', schema=None) as batch_op:
        batch_op.alter_column('created_at',
               existing_type=sa.DateTime(),
               type_=sa.VARCHAR(),
               existing_nullable=True)

    # ### end Alembic commands ###
