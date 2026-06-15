"""create test_runs table

Revision ID: a47117405db6
Revises: 
Create Date: 2026-06-15 09:28:18.686455

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a47117405db6'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'test_runs',
        sa.Column('id', sa.String(length=50), nullable=False),
        sa.Column('name', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=50), nullable=False),
        sa.Column('duration_ms', sa.Integer(), nullable=True),
        sa.Column('started_at', sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    # We added an index to the 'id' column in our model, so we create it here
    op.create_index(op.f('ix_test_runs_id'), 'test_runs', ['id'], unique=False)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_test_runs_id'), table_name='test_runs')
    op.drop_table('test_runs')
