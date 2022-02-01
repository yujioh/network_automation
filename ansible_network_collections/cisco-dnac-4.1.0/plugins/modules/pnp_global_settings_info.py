#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: pnp_global_settings_info
short_description: Information module for Pnp Global Settings
description:
- Get all Pnp Global Settings.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Pnp Global Settings reference
  description: Complete reference of the Pnp Global Settings object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all Pnp Global Settings
  cisco.dnac.pnp_global_settings_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "savaMappingList": [
        {
          "syncStatus": "string",
          "syncStartTime": 0,
          "syncResult": {
            "syncList": [
              {
                "syncType": "string",
                "deviceSnList": [
                  "string"
                ]
              }
            ],
            "syncMsg": "string"
          },
          "lastSync": 0,
          "tenantId": "string",
          "profile": {
            "port": 0,
            "addressIpV4": "string",
            "addressFqdn": "string",
            "profileId": "string",
            "proxy": true,
            "makeDefault": true,
            "cert": "string",
            "name": "string"
          },
          "token": "string",
          "expiry": 0,
          "ccoUser": "string",
          "smartAccountId": "string",
          "virtualAccountId": "string",
          "autoSyncPeriod": 0,
          "syncResultStr": "string"
        }
      ],
      "taskTimeOuts": {
        "imageDownloadTimeOut": 0,
        "configTimeOut": 0,
        "generalTimeOut": 0
      },
      "tenantId": "string",
      "aaaCredentials": {
        "password": "string",
        "username": "string"
      },
      "defaultProfile": {
        "fqdnAddresses": [
          "string"
        ],
        "proxy": true,
        "cert": "string",
        "ipAddresses": [
          "string"
        ],
        "port": 0
      },
      "acceptEula": true,
      "id": "string",
      "_id": "string",
      "version": 0
    }
"""
