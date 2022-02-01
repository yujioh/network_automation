#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: system_performance_historical_info
short_description: Information module for System Performance Historical
description:
- Get all System Performance Historical.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  kpi:
    description:
    - Kpi query parameter. Fetch historical data for this kpi. Valid values cpu,memory,network.
    type: str
  startTime:
    description:
    - >
      StartTime query parameter. This is the epoch start time in milliseconds from which performance indicator
      need to be fetched.
    type: int
  endTime:
    description:
    - >
      EndTime query parameter. This is the epoch end time in milliseconds upto which performance indicator need to
      be fetched.
    type: int
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: System Performance Historical reference
  description: Complete reference of the System Performance Historical object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Get all System Performance Historical
  cisco.dnac.system_performance_historical_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    kpi: string
    startTime: 0
    endTime: 0
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "hostName": "string",
      "version": "string",
      "kpis": {
        "legends": {
          "cpu": {
            "units": "string"
          },
          "memory": {
            "units": "string"
          },
          "network tx_rate": {
            "units": "string"
          },
          "network rx_rate": {
            "units": "string"
          }
        },
        "data": {
          "t1": [
            "string"
          ]
        }
      }
    }
"""
