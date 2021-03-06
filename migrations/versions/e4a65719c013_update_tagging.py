"""update tagging

Revision ID: e4a65719c013
Revises: b92f8dc500b2
Create Date: 2020-10-19 18:40:21.105020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4a65719c013'
down_revision = 'b92f8dc500b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('keyword', sa.String(length=200), nullable=True))
        batch_op.create_index(batch_op.f('ix_tag_keyword'), ['keyword'], unique=False)
        batch_op.drop_index('ix_tag_tag')
        batch_op.drop_column('tag')

    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('software_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('source_id', sa.Integer(), nullable=True))
        batch_op.alter_column('tag_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.drop_constraint('fk_tags_source_tag_source', type_='foreignkey')
        batch_op.drop_constraint('fk_tags_software_tag_software', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_tags_source_id_source'), 'source', ['source_id'], ['id'])
        batch_op.create_foreign_key(batch_op.f('fk_tags_software_id_software'), 'software', ['software_id'], ['id'])
        batch_op.drop_column('software_tag')
        batch_op.drop_column('source_tag')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tags', schema=None) as batch_op:
        batch_op.add_column(sa.Column('source_tag', sa.INTEGER(), nullable=False))
        batch_op.add_column(sa.Column('software_tag', sa.INTEGER(), nullable=False))
        batch_op.drop_constraint(batch_op.f('fk_tags_software_id_software'), type_='foreignkey')
        batch_op.drop_constraint(batch_op.f('fk_tags_source_id_source'), type_='foreignkey')
        batch_op.create_foreign_key('fk_tags_software_tag_software', 'software', ['software_tag'], ['id'])
        batch_op.create_foreign_key('fk_tags_source_tag_source', 'source', ['source_tag'], ['id'])
        batch_op.alter_column('tag_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('source_id')
        batch_op.drop_column('software_id')

    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('tag', sa.VARCHAR(length=200), nullable=True))
        batch_op.create_index('ix_tag_tag', ['tag'], unique=False)
        batch_op.drop_index(batch_op.f('ix_tag_keyword'))
        batch_op.drop_column('keyword')

    # ### end Alembic commands ###
