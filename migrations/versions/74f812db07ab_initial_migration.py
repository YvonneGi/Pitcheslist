"""Initial Migration

Revision ID: 74f812db07ab
Revises: 8635d65efd76
Create Date: 2019-09-24 17:38:08.235056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74f812db07ab'
down_revision = '8635d65efd76'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('comments_category_id_fkey', 'comments', type_='foreignkey')
    op.drop_column('comments', 'category_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('category_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('comments_category_id_fkey', 'comments', 'category', ['category_id'], ['id'])
    # ### end Alembic commands ###
