"""add default to document chunk created at

Revision ID: 7f1861fc0097
Revises: d39a50782788
Create Date: 2026-09-14 17:27:56.238054

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "7f1861fc0097"
down_revision: Union[str, Sequence[str], None] = "d39a50782788"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.alter_column(
        "document_chunks",
        "created_at",
        server_default=sa.text("now()"),
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column(
        "document_chunks",
        "created_at",
        server_default=None,
    )