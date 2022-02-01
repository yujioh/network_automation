#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_create
short_description: Resource module for Network Create
description:
- Manage operation create of the resource Network Create.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  settings:
    description: Network Create's settings.
    suboptions:
      clientAndEndpoint_aaa:
        description: Network Create's clientAndEndpoint_aaa.
        suboptions:
          additionalIp:
            description: Additional IP for ISE server which is not supported by AAA
              server.
            elements: str
            type: list
          ipAddress:
            description: IP address for ISE serve (eg 1.1.1.4). Mandatory for ISE servers.
            type: str
          network:
            description: IP address for AAA or ISE server (eg 2.2.2.1).
            type: str
          protocol:
            description: Protocol for AAA or ISE serve (eg RADIUS).
            type: str
          servers:
            description: Server type AAA or ISE server (eg AAA).
            type: str
          sharedSecret:
            description: Shared secret for ISE server. Supported only by ISE servers.
            type: str
        type: dict
      dhcpServer:
        description: Dhcp serve Ip (eg 1.1.1.1).
        elements: str
        type: list
      dnsServer:
        description: Network Create's dnsServer.
        suboptions:
          domainName:
            description: Domain name of DHCP (eg; cisco). Can only contain alphanumeric
              characters or hyphen.
            type: str
          primaryIpAddress:
            description: Primary ip address for DHCP (eg 2.2.2.2). Valid range 1.0.0.0
              - 223.255.255.255.
            type: str
          secondaryIpAddress:
            description: Secondary ip address for DHCP (eg 3.3.3.3). Valid range 1.0.0.0
              - 223.255.255.255.
            type: str
        type: dict
      messageOfTheday:
        description: Network Create's messageOfTheday.
        suboptions:
          bannerMessage:
            description: Massage for banner message (eg; Good day).
            type: str
          retainExistingBanner:
            description: Retain existing banner message (eg true).
            type: bool
        type: dict
      netflowcollector:
        description: Network Create's netflowcollector.
        suboptions:
          ipAddress:
            description: IP address for netflow collector (eg 3.3.3.1).
            type: str
          port:
            description: Port for netflow collector (eg; 443).
            type: int
        type: dict
      network_aaa:
        description: Network Create's network_aaa.
        suboptions:
          additionalIp:
            description: Additional IP for ISE server which is not supported by AAA
              server.
            elements: str
            type: list
          ipAddress:
            description: IP address for AAA and ISE server (eg 1.1.1.1). Mandatory for
              ISE servers and for AAA consider this as additional Ip.
            type: str
          network:
            description: IP address for AAA or ISE server (eg 2.2.2.2). For AAA server
              consider it as primary IP and For ISE consider as Network.
            type: str
          protocol:
            description: Protocol for AAA or ISE serve (eg RADIUS).
            type: str
          servers:
            description: Server type for AAA network (eg AAA). Server type supported
              by ISE and AAA.
            type: str
          sharedSecret:
            description: Shared secret for ISE server. Supported only by ISE servers.
            type: str
        type: dict
      ntpServer:
        description: IP address for NTP server (eg 1.1.1.2).
        elements: str
        type: list
      snmpServer:
        description: Network Create's snmpServer.
        suboptions:
          configureDnacIP:
            description: Configuration dnac ip for snmp server (eg true).
            type: bool
          ipAddresses:
            description: IP address for snmp server (eg 4.4.4.1).
            elements: str
            type: list
        type: dict
      syslogServer:
        description: Network Create's syslogServer.
        suboptions:
          configureDnacIP:
            description: Configuration dnac ip for syslog server (eg true).
            type: bool
          ipAddresses:
            description: IP address for syslog server (eg 4.4.4.4).
            elements: str
            type: list
        type: dict
      timezone:
        description: Input for time zone (eg Africa/Abidjan (GMT)).
        type: str
    type: dict
  siteId:
    description: SiteId path parameter. Site id to which site details to associate with
      the network settings.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference by Internet resource
- name: Network Create reference
  description: Complete reference of the Network Create object model.
  link: https://dnacentersdk.readthedocs.io/en/latest/api/api.html#v3-0-0-summary
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.network_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    settings:
      clientAndEndpoint_aaa:
        additionalIp:
        - string
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      dhcpServer:
      - string
      dnsServer:
        domainName: string
        primaryIpAddress: string
        secondaryIpAddress: string
      messageOfTheday:
        bannerMessage: string
        retainExistingBanner: true
      netflowcollector:
        ipAddress: string
        port: 0
      network_aaa:
        additionalIp:
        - string
        ipAddress: string
        network: string
        protocol: string
        servers: string
        sharedSecret: string
      ntpServer:
      - string
      snmpServer:
        configureDnacIP: true
        ipAddresses:
        - string
      syslogServer:
        configureDnacIP: true
        ipAddresses:
        - string
      timezone: string
    siteId: string

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
