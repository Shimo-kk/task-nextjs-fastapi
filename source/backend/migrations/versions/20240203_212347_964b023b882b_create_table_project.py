"""create table project

Revision ID: 964b023b882b
Revises: ee13c632e58d
Create Date: 2024-02-03 21:23:47.753945+09:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '964b023b882b'
down_revision = 'ee13c632e58d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False, comment='登録日時'),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False, comment='更新日時'),
    sa.Column('work_space_id', sa.INTEGER(), nullable=False, comment='ワークスペースID'),
    sa.Column('name', sa.VARCHAR(length=50), nullable=False, comment='名称'),
    sa.Column('summary', sa.TEXT(), nullable=True, comment='概要'),
    sa.Column('start_date', sa.TIMESTAMP(timezone=True), nullable=True, comment='開始日'),
    sa.Column('end_date', sa.TIMESTAMP(timezone=True), nullable=True, comment='終了日'),
    sa.ForeignKeyConstraint(['work_space_id'], ['work_space.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project')
    # ### end Alembic commands ###