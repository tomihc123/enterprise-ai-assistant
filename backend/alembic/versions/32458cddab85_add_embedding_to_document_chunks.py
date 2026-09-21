"""add embedding to document chunks

Revision ID: 32458cddab85
Revises: 339e9a0b275a
Create Date: 2026-09-15 06:35:03.037751

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from pgvector.sqlalchemy import Vector


# revision identifiers, used by Alembic.
revision: str = "32458cddab85"
down_revision: Union[str, Sequence[str], None] = "339e9a0b275a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.add_column(
        "document_chunks",
        sa.Column(
            "embedding",
            Vector(384),
            nullable=True,
        ),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column(
        "document_chunks",
        "embedding",
    )