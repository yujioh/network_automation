#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_profile
short_description: Resource module for Wireless Profile
description:
- Manage operations create, update and delete of the resource Wireless Profile.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  profileDetails:
    description: Wireless Profile's profileDetails.
    suboptions:
      name:
        description: Profile Name.
        type: str
      sites:
        description: Array of site name hierarchies(eg "Global/aaa/zzz", "Global/aaa/zzz").
        elements: str
        type: list
      ssidDetails:
        description: Wireless Profile's ssidDetails.
        suboptions:
          enableFabric:
            description: True is ssid is fabric else false.
            type: bool
          flexConnect:
            description: Wireless Profile's flexConnect.
            suboptions:
              enableFlexConnect:
                description: True if flex connect is enabled else false.
                type: bool
              localToVlan:
                description: Local To Vlan.
                type: int
            type: dict
          interfaceName:
            description: Interface Name.
            type: str
          name:
            description: Ssid Name.
            type: str
          type:
            description: Ssid Type(enum Enterprise/Guest).
            type: str
        type: list
    type: dict
  wirelessProfileName:
    description: WirelessProfileName path parameter. Wireless Profile Name.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Wireless Profile reference
  description: Complete reference of the Wireless Profile object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Delete by name
  cisco.dnac.wireless_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    wirelessProfileName: string

- name: Update all
  cisco.dnac.wireless_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    profileDetails:
      name: string
      sites:
      - string
      ssidDetails:
      - enableFabric: true
        flexConnect:
          enableFlexConnect: true
          localToVlan: 0
        interfaceName: string
        name: string
        type: string

- name: Create
  cisco.dnac.wireless_profile:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    profileDetails:
      name: string
      sites:
      - string
      ssidDetails:
      - enableFabric: true
        flexConnect:
          enableFlexConnect: true
          localToVlan: 0
        interfaceName: string
        name: string
        type: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""
