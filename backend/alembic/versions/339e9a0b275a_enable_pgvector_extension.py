"""enable pgvector extension

Revision ID: 339e9a0b275a
Revises: 7f1861fc0097
Create Date: 2026-09-14 18:07:01.183348

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '339e9a0b275a'
down_revision: Union[str, Sequence[str], None] = '7f1861fc0097'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        "CREATE EXTENSION IF NOT EXISTS vector"
    )


def downgrade() -> None:
    op.execute(
        "DROP EXTENSION IF EXISTS vector"
    )
