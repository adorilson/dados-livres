"""table similar timestamp

Revision ID: 410b133dbfb2
Revises: 0bb69d222ea2
Create Date: 2020-07-09 23:01:55.924011

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '410b133dbfb2'
down_revision = '0bb69d222ea2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_similar_timestamp'), ['timestamp'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_similar_timestamp'))
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###