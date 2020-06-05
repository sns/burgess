"""create Items table

Revision ID: 0391bf76d153
Revises: 
Create Date: 2020-06-04 23:01:23.677309

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0391bf76d153'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    items_table = op.create_table(
        'Items',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String(50), nullable=False, unique=True, index=True),
        sa.Column('quantity', sa.Integer, nullable=False, default=0),
    )

    # initialize 
    op.bulk_insert(items_table,
        [
            { 'id': 1, 'name': 'Apples', 'quantity': 3 },
            { 'id': 2, 'name': 'Oranges', 'quantity': 7 },
            { 'id': 3, 'name': 'Pomegranates', 'quantity': 55 }
        ]
    )    

def downgrade():
    op.drop_table('Items')
