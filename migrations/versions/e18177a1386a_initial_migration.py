"""Initial Migration

Revision ID: e18177a1386a
Revises: 13c138b41b6f
Create Date: 2022-05-16 19:47:49.785929

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e18177a1386a'
down_revision = '13c138b41b6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('upvotes', sa.Integer(), nullable=True))
    op.add_column('posts', sa.Column('downvotes', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'downvotes')
    op.drop_column('posts', 'upvotes')
    # ### end Alembic commands ###
