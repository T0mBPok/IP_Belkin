"""user datetime2

Revision ID: 54bdb9820ea0
Revises: 243e0791edfe
Create Date: 2025-05-29 22:04:09.751049

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '54bdb9820ea0'
down_revision: Union[str, None] = '243e0791edfe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=sa.DATE(),
               type_=sa.DateTime(),
               existing_nullable=False,
               existing_server_default=sa.text('CURRENT_DATE'))
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'created_at',
               existing_type=sa.DateTime(),
               type_=sa.DATE(),
               existing_nullable=False,
               existing_server_default=sa.text('CURRENT_DATE'))
    # ### end Alembic commands ###
