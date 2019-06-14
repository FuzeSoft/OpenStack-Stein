#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


import sqlalchemy as sql

from keystone.common import sql as ks_sql


def upgrade(migrate_engine):
    meta = sql.MetaData()
    meta.bind = migrate_engine

    # NOTE(morgan): column is nullable here for migration purposes
    # it is set to not-nullable in the contract phase to ensure we can handle
    # rolling upgrades in a sane way. This differs from the model in
    # keystone.identity.backends.sql_model by design.
    created_at = sql.Column('created_at_int', ks_sql.DateTimeInt(),
                            nullable=True)
    expires_at = sql.Column('expires_at_int', ks_sql.DateTimeInt(),
                            nullable=True)
    password_table = sql.Table('password', meta, autoload=True)
    password_table.create_column(created_at)
    password_table.create_column(expires_at)
