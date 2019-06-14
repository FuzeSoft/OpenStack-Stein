# Copyright 2011 OpenStack Foundation
# All Rights Reserved.
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

"""
A filter middleware that inspects the requested URI for a version string
and/or Accept headers and attempts to negotiate an API controller to
return
"""

from oslo_config import cfg
from oslo_log import log as logging

from searchlight.api import versions
from searchlight.common import wsgi
from searchlight.i18n import _

CONF = cfg.CONF

LOG = logging.getLogger(__name__)


class VersionNegotiationFilter(wsgi.Middleware):

    def __init__(self, app):
        self.versions_app = versions.Controller()
        super(VersionNegotiationFilter, self).__init__(app)

    def process_request(self, req):
        """Try to find a version first in the accept header, then the URL"""
        msg = _("Determining version of request: %(method)s %(path)s"
                " Accept: %(accept)s")
        args = {'method': req.method, 'path': req.path, 'accept': req.accept}
        LOG.debug(msg % args)

        LOG.debug("Using url versioning")
        # Remove version in url so it doesn't conflict later
        req_version = self._pop_path_info(req)

        try:
            version = self._match_version_string(req_version)
        except ValueError:
            LOG.warning("Unknown version. Returning version choices.")
            return self.versions_app

        req.environ['api.version'] = version
        req.path_info = ''.join(('/v', str(version), req.path_info))
        LOG.debug("Matched version: v%d", version)
        LOG.debug('new path %s', req.path_info)
        return None

    def _match_version_string(self, subject):
        """
        Given a string, tries to match a major and/or
        minor version number.

        :param subject: The string to check
        :returns version found in the subject
        :raises ValueError if no acceptable version could be found
        """
        # TODO(lakshmis): Add newer versions whenever they are introduced
        if subject in ('v1', 'v1.0'):
            major_version = 1
        else:
            raise ValueError()

        return major_version

    def _pop_path_info(self, req):
        """
        'Pops' off the next segment of PATH_INFO, returns the popped
        segment. Do NOT push it onto SCRIPT_NAME.
        """
        path = req.path_info
        if not path:
            return None
        while path.startswith('/'):
            path = path[1:]
        idx = path.find('/')
        if idx == -1:
            idx = len(path)
        r = path[:idx]
        req.path_info = path[idx:]
        return r
