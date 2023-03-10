"""user update lendth-5

Revision ID: 78e0297c7901
Revises: 
Create Date: 2023-02-03 12:59:37.923597

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '78e0297c7901'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('name', sa.String(length=16), nullable=False),
    sa.Column('email', sa.String(length=20), nullable=False),
    sa.Column('phone', sa.String(length=10), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('role', sa.Enum('SUPER_ADMIN', 'ADMIN', 'TENANT', name='roleenum'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('building',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('createdBy', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('location', sa.String(length=50), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('single_bed', sa.Integer(), nullable=True),
    sa.Column('double_bed', sa.Integer(), nullable=True),
    sa.Column('three_bed', sa.Integer(), nullable=True),
    sa.Column('four_bed', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tenant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('building', sa.Integer(), nullable=False),
    sa.Column('room_type', sa.String(length=50), nullable=False),
    sa.Column('current_status', sa.String(length=50), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('food_routine',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('building', sa.Integer(), nullable=False),
    sa.Column('lunch_time', sa.DateTime(), nullable=True),
    sa.Column('break_fast_time', sa.DateTime(), nullable=True),
    sa.Column('snack_time', sa.DateTime(), nullable=True),
    sa.Column('dinner_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('user', sa.Integer(), nullable=False),
    sa.Column('building', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=50), nullable=False),
    sa.Column('amount', sa.String(length=50), nullable=False),
    sa.Column('image', sa.String(length=50), nullable=False),
    sa.Column('remark', sa.String(length=50), nullable=False),
    sa.Column('month', sa.String(length=50), nullable=False),
    sa.Column('payment_method', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('token',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('name', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('token', sa.String(length=500), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('token')
    op.drop_table('transaction')
    op.drop_table('food_routine')
    op.drop_table('tenant')
    op.drop_table('building')
    op.drop_table('users')
    # ### end Alembic commands ###
