# Copyright 2017 Huawei Technologies Co.,LTD.
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


CONDUCTOR_TOPIC = 'cyborg-conductor'
AGENT_TOPIC = 'cyborg-agent'
DEVICE_GPU = 'GPU'
DEVICE_FPGA = 'FPGA'


ARQ_STATES = (ARQINITIAL, ARQBOUND, ARQUNBOUND, ARQBINDFAILED) = \
    ('Initial', 'Bound', 'Unbound', 'BindFailed')

# Device type
DEVICE_TYPE = (DEVICE_GPU, DEVICE_FPGA)
