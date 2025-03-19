# SPDX-FileCopyrightText: 2023 Marlon W (Mawoka)
#
# SPDX-License-Identifier: MPL-2.0

"""Added totp

Revision ID: 694cb11c6886
Revises: 901dfcdf8d38
Create Date: 2022-12-18 13:20:48.091675

"""
from alembic import op
import sqlalchemy as sa
import ormar


# revision identifiers, used by Alembic.
revision = "694cb11c6886"
down_revision = "901dfcdf8d38"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("users", sa.Column("totp_secret", sa.String(length=32), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("users", "totp_secret")
    # ### end Alembic commands ###
