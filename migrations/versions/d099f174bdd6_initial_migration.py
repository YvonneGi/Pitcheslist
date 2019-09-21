"""Initial Migration

Revision ID: d099f174bdd6
Revises: 4de94f670f78
Create Date: 2019-09-21 13:57:44.959403

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd099f174bdd6'
down_revision = '4de94f670f78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch', sa.String(length=255), nullable=True))
    op.drop_column('pitches', 'pitch_title')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pitches', sa.Column('pitch_title', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('pitches', 'pitch')
    # ### end Alembic commands ###