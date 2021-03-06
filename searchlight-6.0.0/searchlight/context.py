# Copyright 2011-2014 OpenStack Foundation
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

from oslo_context import context

from searchlight.api import policy

ADMIN_ROLE_FILTER = "admin"
USER_ROLE_FILTER = "user"


class RequestContext(context.RequestContext):
    """Stores information about the security context.

    Stores how the user accesses the system, as well as additional request
    information.

    """

    def __init__(self, roles=None,
                 owner_is_tenant=True, service_catalog=None,
                 policy_enforcer=None, **kwargs):
        super(RequestContext, self).__init__(**kwargs)
        self.roles = roles or []
        self.owner_is_tenant = owner_is_tenant
        self.service_catalog = service_catalog
        self.policy_enforcer = policy_enforcer or policy.Enforcer()
        if not self.is_admin:
            self.is_admin = self.policy_enforcer.check_is_admin(self)
        self.user_role_filter = (ADMIN_ROLE_FILTER if self.is_admin
                                 else USER_ROLE_FILTER)

    def to_dict(self):
        d = super(RequestContext, self).to_dict()
        d.update({
            'roles': self.roles,
            'service_catalog': self.service_catalog,
            'is_admin': self.is_admin,
            'user_id': self.user,
            'project_id': self.tenant,
            'tenant_id': self.tenant
        })
        return d

    @classmethod
    def from_dict(cls, values):
        return cls(**values)

    @property
    def owner(self):
        """Return the owner to correlate with an image."""
        return self.tenant if self.owner_is_tenant else self.user

    @property
    def can_see_deleted(self):
        """Admins can see deleted by default"""
        return self.show_deleted or self.is_admin

    @property
    def policy_target(self):
        """For use when there's no actual target defined for policy; this
        allows 'admin_or_owner' type rules to use the context as a target.
        """
        return {
            'project_id': self.tenant,
            'tenant_id': self.tenant,
            'user_id': self.user
        }
