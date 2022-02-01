#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: wireless_enterprise_ssid
short_description: Resource module for Wireless Enterprise Ssid
description:
- Manage operations create, update and delete of the resource Wireless Enterprise Ssid.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  basicServiceSetClientIdleTimeout:
    description: Basic Service Set Client Idle Timeout.
    type: int
  clientExclusionTimeout:
    description: Client Exclusion Timeout.
    type: int
  enableBasicServiceSetMaxIdle:
    description: Enable Basic Service Set Max Idle.
    type: bool
  enableBroadcastSSID:
    description: Enable Broadcast SSID.
    type: bool
  enableClientExclusion:
    description: Enable Client Exclusion.
    type: bool
  enableDirectedMulticastService:
    description: Enable Directed Multicast Service.
    type: bool
  enableFastLane:
    description: Enable Fast Lane.
    type: bool
  enableMACFiltering:
    description: Enable MAC Filtering.
    type: bool
  enableNeighborList:
    description: Enable Neighbor List.
    type: bool
  enableSessionTimeOut:
    description: Enable Session Timeout.
    type: bool
  fastTransition:
    description: Fast Transition.
    type: str
  mfpClientProtection:
    description: Management Frame Protection Client.
    type: str
  name:
    description: Enter SSID Name.
    type: str
  passphrase:
    description: Pass Phrase (Only applicable for SSID with PERSONAL security level).
    type: str
  radioPolicy:
    description: Radio Policy. Allowed values are 'Dual band operation (2.4GHz and 5GHz)',
      'Dual band operation with band select', '5GHz only', '2.4GHz only'.
    type: str
  securityLevel:
    description: Security Level.
    type: str
  sessionTimeOut:
    description: Session Time Out.
    type: int
  ssidName:
    description: SsidName path parameter. Enter the SSID name to be deleted.
    type: str
  trafficType:
    description: Traffic Type.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Wireless Enterprise Ssid reference
  description: Complete reference of the Wireless Enterprise Ssid object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    basicServiceSetClientIdleTimeout: 0
    clientExclusionTimeout: 0
    enableBasicServiceSetMaxIdle: true
    enableBroadcastSSID: true
    enableClientExclusion: true
    enableDirectedMulticastService: true
    enableFastLane: true
    enableMACFiltering: true
    enableNeighborList: true
    enableSessionTimeOut: true
    fastTransition: string
    mfpClientProtection: string
    name: string
    passphrase: string
    radioPolicy: string
    securityLevel: string
    sessionTimeOut: 0
    trafficType: string

- name: Update all
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    basicServiceSetClientIdleTimeout: 0
    clientExclusionTimeout: 0
    enableBasicServiceSetMaxIdle: true
    enableBroadcastSSID: true
    enableClientExclusion: true
    enableDirectedMulticastService: true
    enableFastLane: true
    enableMACFiltering: true
    enableNeighborList: true
    enableSessionTimeOut: true
    fastTransition: string
    mfpClientProtection: string
    name: string
    passphrase: string
    radioPolicy: string
    securityLevel: string
    sessionTimeOut: 0
    trafficType: string

- name: Delete by name
  cisco.dnac.wireless_enterprise_ssid:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    ssidName: string

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
