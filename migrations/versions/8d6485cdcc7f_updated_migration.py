"""updated migration

Revision ID: 8d6485cdcc7f
Revises: cc1df4b7dbdd
Create Date: 2022-05-17 13:05:46.849856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d6485cdcc7f'
down_revision = 'cc1df4b7dbdd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('downvote')
    op.drop_table('upvote')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upvote',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('upvotes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='upvote_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='upvote_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='upvote_pkey')
    )
    op.create_table('downvote',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('downvotes', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('post_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['post_id'], ['posts.id'], name='downvote_post_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='downvote_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='downvote_pkey')
    )
    # ### end Alembic commands ###