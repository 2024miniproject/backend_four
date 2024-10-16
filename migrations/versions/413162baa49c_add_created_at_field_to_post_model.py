"""Add created_at field to Post model

Revision ID: 413162baa49c
Revises: 098f05788178
Create Date: 2024-10-14 22:00:19.424396

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '413162baa49c'
down_revision = '098f05788178'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.drop_column('created_at')

    # ### end Alembic commands ###
