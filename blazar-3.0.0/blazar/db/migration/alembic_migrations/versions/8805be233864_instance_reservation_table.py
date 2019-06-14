# Copyright 2017 OpenStack Foundation.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""instance-reservation-table

Revision ID: 8805be233864
Revises: 7f1a7bbb2cd2
Create Date: 2017-06-20 07:31:17.379252

"""

# revision identifiers, used by Alembic.
revision = '8805be233864'
down_revision = '7f1a7bbb2cd2'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instance_reservations',
                    sa.Column('created_at', sa.DateTime(), nullable=True),
                    sa.Column('updated_at', sa.DateTime(), nullable=True),
                    sa.Column('id', sa.String(length=36), nullable=False),
                    sa.Column('reservation_id',
                              sa.String(length=36), nullable=True),
                    sa.Column('vcpus', sa.Integer(), nullable=False),
                    sa.Column('memory_mb', sa.Integer(), nullable=False),
                    sa.Column('disk_gb', sa.Integer(), nullable=False),
                    sa.Column('amount', sa.Integer(), nullable=False),
                    sa.Column('affinity', sa.Boolean(), nullable=False),
                    sa.Column('flavor_id',
                              sa.String(length=36), nullable=True),
                    sa.Column('aggregate_id', sa.Integer(), nullable=True),
                    sa.Column('server_group_id',
                              sa.String(length=36), nullable=True),
                    sa.ForeignKeyConstraint(['reservation_id'],
                                            ['reservations.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instance_reservations')
    # ### end Alembic commands ###
