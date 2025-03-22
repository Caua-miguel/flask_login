"""refact: table User to Users.

Revision ID: 080841afd158
Revises: 41bf425d7ae3
Create Date: 2025-03-20 13:34:31.255195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '080841afd158'
down_revision = '41bf425d7ae3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('user', 'users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('users', 'user')
    # ### end Alembic commands ###
