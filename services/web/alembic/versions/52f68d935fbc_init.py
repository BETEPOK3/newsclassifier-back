"""init

Revision ID: 52f68d935fbc
Revises: 8e0792a7d844
Create Date: 2023-12-18 09:37:08.124606

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52f68d935fbc'
down_revision = '8e0792a7d844'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'article_author',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('article', 'article_author',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
