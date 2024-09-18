"""Renaming students to scholars

Revision ID: 897842462eb6
Revises: 791279dd0760
Create Date: 2024-09-18 16:11:30.229525

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '897842462eb6'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')
    pass


def downgrade() -> None:
    op.rename_table('scholars', 'students')
    pass
