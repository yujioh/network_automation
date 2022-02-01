#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: cli_credential
short_description: Resource module for Cli Credential
description:
- Manage operations create and update of the resource Cli Credential.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  comments:
    description: Cli Credential's comments.
    type: str
  credentialType:
    description: Cli Credential's credentialType.
    type: str
  description:
    description: Cli Credential's description.
    type: str
  enablePassword:
    description: Cli Credential's enablePassword.
    type: str
  id:
    description: Cli Credential's id.
    type: str
  instanceTenantId:
    description: Cli Credential's instanceTenantId.
    type: str
  instanceUuid:
    description: Cli Credential's instanceUuid.
    type: str
  password:
    description: Cli Credential's password.
    type: str
  username:
    description: Cli Credential's username.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Cli Credential reference
  description: Complete reference of the Cli Credential object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.cli_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    enablePassword: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    password: string
    username: string

- name: Create
  cisco.dnac.cli_credential:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    comments: string
    credentialType: string
    description: string
    enablePassword: string
    id: string
    instanceTenantId: string
    instanceUuid: string
    password: string
    username: string
"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""
