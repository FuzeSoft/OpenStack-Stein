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
from oslo_utils.fixture import uuidsentinel as uuids

from placement import exception
from placement.objects import user as user_obj
from placement.tests.functional.db import test_base as tb


class UserTestCase(tb.PlacementDbBaseTestCase):
    def test_non_existing_user(self):
        self.assertRaises(
            exception.UserNotFound, user_obj.User.get_by_external_id,
            self.ctx, uuids.non_existing_user)

    def test_create_and_get(self):
        u = user_obj.User(self.ctx, external_id='another-user')
        u.create()
        u = user_obj.User.get_by_external_id(self.ctx, 'another-user')
        # User ID == 1 is fake-user created in setup
        self.assertEqual(2, u.id)
        self.assertRaises(exception.UserExists, u.create)
