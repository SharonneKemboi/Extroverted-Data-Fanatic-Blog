"""Initial Migration

Revision ID: 7f15cf0502e6
Revises: e015560cf52d
Create Date: 2022-05-15 19:31:15.684501

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f15cf0502e6'
down_revision = 'e015560cf52d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('comments', sa.Column('content', sa.String(), nullable=True))
    op.drop_index('ix_comments_post_comment', table_name='comments')
    op.drop_column('comments', 'post_comment')
    op.drop_index('ix_posts_content', table_name='posts')
    op.drop_index('ix_posts_title', table_name='posts')
    op.add_column('users', sa.Column('name', sa.String(), nullable=True))
    op.add_column('users', sa.Column('profile_pic', sa.String(), nullable=True))
    op.drop_index('ix_users_email', table_name='users')
    op.drop_index('ix_users_username', table_name='users')
    op.drop_column('users', 'username')
    op.drop_column('users', 'profile_pic_path')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('profile_pic_path', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('users', sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_index('ix_users_username', 'users', ['username'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.drop_column('users', 'profile_pic')
    op.drop_column('users', 'name')
    op.create_index('ix_posts_title', 'posts', ['title'], unique=False)
    op.create_index('ix_posts_content', 'posts', ['content'], unique=False)
    op.add_column('comments', sa.Column('post_comment', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.create_index('ix_comments_post_comment', 'comments', ['post_comment'], unique=False)
    op.drop_column('comments', 'content')
    # ### end Alembic commands ###
