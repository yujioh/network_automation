#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: device_credential_update
short_description: Resource module for Device Credential Update
description:
- Manage operation update of the resource Device Credential Update.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  settings:
    description: Device Credential Update's settings.
    suboptions:
      cliCredential:
        description: Device Credential Update's cliCredential.
        suboptions:
          description:
            description: Name or description for CLI credential.
            type: str
          enablePassword:
            description: Enable password for CLI credential.
            type: str
          password:
            description: Password for CLI credential.
            type: str
          username:
            description: User name for CLI credential.
            type: str
        type: list
      httpsRead:
        description: Device Credential Update's httpsRead.
        suboptions:
          name:
            description: Name or description of http read credential.
            type: str
          password:
            description: Password for http read credential.
            type: str
          port:
            description: Port for http read credential.
            type: int
          username:
            description: User name of the http read credential.
            type: str
        type: list
      httpsWrite:
        description: Device Credential Update's httpsWrite.
        suboptions:
          name:
            description: Name or description of http write credential.
            type: str
          password:
            description: Password for http write credential.
            type: str
          port:
            description: Port for http write credential.
            type: int
          username:
            description: User name of the http write credential.
            type: str
        type: list
      snmpV2cRead:
        description: Device Credential Update's snmpV2cRead.
        suboptions:
          description:
            description: Description for snmp v2 read.
            type: str
          readCommunity:
            description: Ready community for snmp v2 read credential.
            type: str
        type: list
      snmpV2cWrite:
        description: Device Credential Update's snmpV2cWrite.
        suboptions:
          description:
            description: Description for snmp v2 write.
            type: str
          writeCommunity:
            description: Write community for snmp v2 write credential.
            type: str
        type: list
      snmpV3:
        description: Device Credential Update's snmpV3.
        suboptions:
          authPassword:
            description: Authentication password for snmpv3 credential.
            type: str
          authType:
            description: Authentication type for snmpv3 credential.
            type: str
          description:
            description: Name or description for SNMPV3 credential.
            type: str
          privacyPassword:
            description: Privacy password for snmpv3 credential.
            type: str
          privacyType:
            description: Privacy type for snmpv3 credential.
            type: str
          snmpMode:
            description: Mode for snmpv3 credential.
            type: str
          username:
            description: User name for SNMPv3 credential.
            type: str
        type: list
    type: dict
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Device Credential Update reference
  description: Complete reference of the Device Credential Update object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.device_credential_update:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      cliCredential:
        description: string
        enablePassword: string
        id: string
        password: string
        username: string
      httpsRead:
        id: string
        name: string
        password: string
        port: string
        username: string
      httpsWrite:
        id: string
        name: string
        password: string
        port: string
        username: string
      snmpV2cRead:
        description: string
        id: string
        readCommunity: string
      snmpV2cWrite:
        description: string
        id: string
        writeCommunity: string
      snmpV3:
        authPassword: string
        authType: string
        description: string
        id: string
        privacyPassword: string
        privacyType: string
        snmpMode: string
        username: string

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
