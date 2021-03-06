"""Added Seen table for resolutions

Revision ID: a6d5c000cdba
Revises: e290d528e4be
Create Date: 2020-06-28 19:30:01.324069

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a6d5c000cdba'
down_revision = '1066445071d6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seen',
    sa.Column('resolution_id', sa.Integer(), nullable=False),
    sa.Column('association', sa.String(length=32), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['resolution_id'], ['resolution.id'], ),
    sa.PrimaryKeyConstraint('resolution_id', 'association')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('seen')
    # ### end Alembic commands ###
