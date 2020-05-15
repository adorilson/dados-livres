"""add tag e catogorie software

Revision ID: caaf1f9ec27e
Revises: 6909a29c2b38
Create Date: 2020-03-24 02:05:08.316565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caaf1f9ec27e'
down_revision = '6909a29c2b38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('softwares', sa.Column('categorie', sa.String(length=800), nullable=True))
    op.add_column('softwares', sa.Column('tag', sa.String(length=800), nullable=True))
    op.create_index(op.f('ix_softwares_categorie'), 'softwares', ['categorie'], unique=False)
    op.create_index(op.f('ix_softwares_tag'), 'softwares', ['tag'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_softwares_tag'), table_name='softwares')
    op.drop_index(op.f('ix_softwares_categorie'), table_name='softwares')
    op.drop_column('softwares', 'tag')
    op.drop_column('softwares', 'categorie')
    # ### end Alembic commands ###