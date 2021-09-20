"""init

Revision ID: 1feb1a280bb1
Revises: 
Create Date: 2021-09-20 11:01:16.270257

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1feb1a280bb1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'customers',
        sa.Column('Number', sa.Integer,nullable=False),
        sa.Column('customer_id', sa.Integer, primary_key=True),
        sa.Column('first_name', sa.String, nullable=False),
        sa.Column('last_name', sa.String, nullable=False),
        sa.Column('ssn', sa.Integer,nullable=False),
        sa.Column('credit_card', sa.Integer, nullable=False),
        sa.Column('credit_card_provider', sa.String, nullable=False),
        sa.Column('birth_date', sa.Date, nullable=False),
        sa.Column('start_date', sa.Date, nullable=False),
        sa.Column('title', sa.String, nullable=False),
        sa.Column('office', sa.String,nullable=False),
        sa.Column('organization', sa.String, nullable=False),
        sa.Column('salary', sa.Float, nullable=False),
        sa.Column('bonus', sa.Float, nullable=False),
        sa.Column('accured_holidays', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('customers')