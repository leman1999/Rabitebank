"""empty message

Revision ID: 30205ac8a09c
Revises: f931c56548de
Create Date: 2023-07-20 16:22:41.710388

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '30205ac8a09c'
down_revision = 'f931c56548de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emanets', schema=None) as batch_op:
        batch_op.alter_column('phone',
               existing_type=mysql.INTEGER(),
               type_=sa.String(length=255),
               existing_nullable=False)
        batch_op.alter_column('deposit',
               existing_type=mysql.VARCHAR(length=255),
               type_=sa.Text(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('emanets', schema=None) as batch_op:
        batch_op.alter_column('deposit',
               existing_type=sa.Text(),
               type_=mysql.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.String(length=255),
               type_=mysql.INTEGER(),
               existing_nullable=False)

    # ### end Alembic commands ###