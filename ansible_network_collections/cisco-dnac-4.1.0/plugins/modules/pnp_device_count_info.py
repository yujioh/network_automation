#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_device_count_info
short_description: Information module for Pnp Device Count
description:
- Get all Pnp Device Count.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  serialNumber:
    description:
    - SerialNumber query parameter. Device Serial Number.
    type: list
  state_:
    description:
    - State query parameter. Device State.
    type: list
  onbState:
    description:
    - OnbState query parameter. Device Onboarding State.
    type: list
  cmState:
    description:
    - CmState query parameter. Device Connection Manager State.
    type: list
  name:
    description:
    - Name query parameter. Device Name.
    type: list
  pid:
    description:
    - Pid query parameter. Device ProductId.
    type: list
  source:
    description:
    - Source query parameter. Device Source.
    type: list
  projectId:
    description:
    - ProjectId query parameter. Device Project Id.
    type: list
  workflowId:
    description:
    - WorkflowId query parameter. Device Workflow Id.
    type: list
  projectName:
    description:
    - ProjectName query parameter. Device Project Name.
    type: list
  workflowName:
    description:
    - WorkflowName query parameter. Device Workflow Name.
    type: list
  smartAccountId:
    description:
    - SmartAccountId query parameter. Device Smart Account.
    type: list
  virtualAccountId:
    description:
    - VirtualAccountId query parameter. Device Virtual Account.
    type: list
  lastContact:
    description:
    - LastContact query parameter. Device Has Contacted lastContact > 0.
    type: bool
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Pnp Device Count reference
  description: Complete reference of the Pnp Device Count object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Pnp Device Count
  cisco.dnac.pnp_device_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    serialNumber: []
    state_: []
    onbState: []
    cmState: []
    name: []
    pid: []
    source: []
    projectId: []
    workflowId: []
    projectName: []
    workflowName: []
    smartAccountId: []
    virtualAccountId: []
    lastContact: True
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": 0
    }
"""
