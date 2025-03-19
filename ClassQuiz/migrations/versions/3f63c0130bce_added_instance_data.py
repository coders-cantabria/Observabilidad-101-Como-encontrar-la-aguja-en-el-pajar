# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

"""added instance_data

Revision ID: 3f63c0130bce
Revises: ff573859eb32
Create Date: 2022-08-28 20:20:28.932854

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = "3f63c0130bce"
down_revision = "ff573859eb32"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "instance_data",
        sa.Column("instance_id", ormar.fields.sqlalchemy_uuid.CHAR(32), nullable=False),
        sa.PrimaryKeyConstraint("instance_id"),
        sa.UniqueConstraint("instance_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("instance_data")
    # ### end Alembic commands ###
