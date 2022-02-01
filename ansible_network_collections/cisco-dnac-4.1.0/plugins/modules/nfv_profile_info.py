#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: nfv_profile_info
short_description: Information module for Nfv Profile
description:
- Get Nfv Profile by id.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. ID of network profile to retrieve.
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row.
    type: str
  limit:
    description:
    - Limit query parameter. Number of profile to be retrieved.
    type: str
  name:
    description:
    - Name query parameter. Name of network profile to be retrieved.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Nfv Profile reference
  description: Complete reference of the Nfv Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get Nfv Profile by id
  cisco.dnac.nfv_profile_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    offset: string
    limit: string
    name: string
    id: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "profileName": "string",
          "id": "string",
          "device": [
            {
              "deviceType": "string",
              "deviceTag": "string",
              "serviceProviderProfile": [
                {
                  "linkType": "string",
                  "connect": true,
                  "connectDefaultGatewayOnWan": true,
                  "serviceProvider": "string"
                }
              ],
              "directInternetAccessForFirewall": true,
              "services": [
                {
                  "serviceType": "string",
                  "profileType": "string",
                  "serviceName": "string",
                  "imageName": "string",
                  "vNicMapping": [
                    {
                      "networkType": "string",
                      "assignIpAddressToNetwork": true
                    }
                  ],
                  "firewallMode": "string"
                }
              ],
              "customNetworks": [
                {
                  "networkName": "string",
                  "servicesToConnect": [
                    {
                      "serviceName": "string"
                    }
                  ],
                  "connectionType": "string",
                  "vlanMode": "string",
                  "vlanId": "string"
                }
              ],
              "vlanForL2": [
                {
                  "vlanType": "string",
                  "vlanId": "string",
                  "vlanDescription": "string"
                }
              ],
              "customTemplate": [
                {
                  "deviceType": "string",
                  "template": "string",
                  "templateType": "string"
                }
              ]
            }
          ]
        }
      ]
    }
"""
