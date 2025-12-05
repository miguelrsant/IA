"""create_user_session_table

Revision ID: 486dbb0ee419
Revises: dfd970676c3c
Create Date: 2025-12-04 19:28:49.554134
"""
from alembic import op
import sqlalchemy as sa


revision = '486dbb0ee419'
down_revision = 'dfd970676c3c'
branch_labels = None
depends_on = None


def upgrade():

    # ---- SESSIONS TABLE ----
    op.create_table(
        'sessions',
        sa.Column('id', sa.String(length=7), nullable=False),
        sa.Column('user_id', sa.String(length=7), nullable=False),
        sa.Column('token_hash', sa.String(length=255), nullable=False),
        sa.Column('created_at', sa.DateTime(), nullable=True),
        sa.Column('expires_at', sa.DateTime(), nullable=False),
        sa.Column('revoked', sa.Boolean(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )

    # ---- USER: ADD provider ----
    with op.batch_alter_table('user') as batch_op:
        batch_op.add_column(
            sa.Column("provider", sa.String(length=120), nullable=True))

    # Preencher valores para usuários existentes
    op.execute("UPDATE \"user\" SET provider = 'none' WHERE provider IS NULL")

    # Tornar NOT NULL após preencher
    with op.batch_alter_table('user') as batch_op:
        batch_op.alter_column("provider", nullable=False)


def downgrade():

    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column("provider")

    op.drop_table('sessions')
