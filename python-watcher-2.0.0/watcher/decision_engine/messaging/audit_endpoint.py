# -*- encoding: utf-8 -*-
# Copyright (c) 2015 b<>com
#
# Authors: Jean-Emile DARTOIS <jean-emile.dartois@b-com.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from concurrent import futures

from oslo_config import cfg
from oslo_log import log

from watcher.decision_engine.audit import continuous as c_handler
from watcher.decision_engine.audit import oneshot as o_handler

from watcher import objects

CONF = cfg.CONF
LOG = log.getLogger(__name__)


class AuditEndpoint(object):

    def __init__(self, messaging):
        self._messaging = messaging
        self._executor = futures.ThreadPoolExecutor(
            max_workers=CONF.watcher_decision_engine.max_workers)
        self._oneshot_handler = o_handler.OneShotAuditHandler()
        self._continuous_handler = c_handler.ContinuousAuditHandler().start()

    @property
    def executor(self):
        return self._executor

    def do_trigger_audit(self, context, audit_uuid):
        audit = objects.Audit.get_by_uuid(context, audit_uuid, eager=True)
        self._oneshot_handler.execute(audit, context)

    def trigger_audit(self, context, audit_uuid):
        LOG.debug("Trigger audit %s", audit_uuid)
        self.executor.submit(self.do_trigger_audit,
                             context,
                             audit_uuid)
        return audit_uuid
