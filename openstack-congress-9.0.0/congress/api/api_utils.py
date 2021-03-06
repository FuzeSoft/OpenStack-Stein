# Copyright (c) 2015 NTT All rights reserved.
#
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

from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from oslo_log import log as logging

from congress.api import base
from congress.api import webservice
from congress.db import datasources as db_datasources

LOG = logging.getLogger(__name__)


def create_table_dict(tablename, schema):
    cols = [{'name': x['name'], 'description': x['desc']}
            if isinstance(x, dict)
            else {'name': x, 'description': 'None'}
            for x in schema[tablename]]
    return {'table_id': tablename,
            'columns': cols}


# Note(thread-safety): blocking function
def get_id_from_context(context):
    if 'ds_id' in context:
        # Note(thread-safety): blocking call
        ds_name = db_datasources.get_datasource_name(context.get('ds_id'))
        return ds_name, context.get('ds_id')
    elif 'policy_id' in context:
        return base.ENGINE_SERVICE_ID, context.get('policy_id')
    else:
        msg = "Internal error: context %s should have included " % str(context)
        "either ds_id or policy_id"
        try:  # Py3: ensure LOG.exception is inside except
            raise webservice.DataModelException('404', msg)
        except webservice.DataModelException:
            LOG.exception(msg)
            raise
