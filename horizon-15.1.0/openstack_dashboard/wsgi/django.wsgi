# Copyright (c) 2017 OpenStack Foundation.
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

"""
WSGI config for openstack_dashboard project.
"""

import logging
import os
import sys

from django.core.wsgi import get_wsgi_application

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.normpath(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), '../..')))
os.environ['DJANGO_SETTINGS_MODULE'] = 'openstack_dashboard.settings'
sys.stdout = sys.stderr

logging.warning(
    "Use of this 'djano.wsgi' file has been deprecated since the Rocky "
    "release in favor of 'wsgi.py' in the 'openstack_dashboard' module. This "
    "file is a legacy naming from before Django 1.4 and an importable "
    "'wsgi.py' is now the default. This file will be removed in the T release "
    "cycle."
)

application = get_wsgi_application()
