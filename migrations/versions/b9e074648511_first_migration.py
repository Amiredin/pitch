"""First migration

Revision ID: b9e074648511
Revises: 05c6c349c47a
Create Date: 2019-04-24 18:02:18.282646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b9e074648511'
down_revision = '05c6c349c47a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('profile_photos')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('profile_photos',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='profile_photos_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='profile_photos_pkey')
    )
    # ### end Alembic commands ###
