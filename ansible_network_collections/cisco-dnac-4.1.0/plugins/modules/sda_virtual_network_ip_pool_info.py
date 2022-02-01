#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_virtual_network_ip_pool_info
short_description: Information module for Sda Virtual Network Ip Pool
description:
- Get all Sda Virtual Network Ip Pool.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  ipPoolName:
    description:
    - IpPoolName query parameter.
    type: str
  virtualNetworkName:
    description:
    - VirtualNetworkName query parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Sda Virtual Network Ip Pool reference
  description: Complete reference of the Sda Virtual Network Ip Pool object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Sda Virtual Network Ip Pool
  cisco.dnac.sda_virtual_network_ip_pool_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    ipPoolName: string
    virtualNetworkName: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "virtualNetworkName": "string",
      "ipPoolName": "string",
      "authenticationPolicyName": "string",
      "trafficType": "string",
      "scalableGroupName": "string",
      "isL2FloodingEnabled": true,
      "isThisCriticalPool": true
    }
"""
