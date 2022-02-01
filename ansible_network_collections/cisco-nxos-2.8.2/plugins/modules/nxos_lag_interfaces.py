#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2019 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

#############################################
#                WARNING                    #
#############################################
#
# This file is auto generated by the resource
#   module builder playbook.
#
# Do not edit this file manually.
#
# Changes to this file will be over written
#   by the resource module builder.
#
# Changes should be made in the model used to
#   generate this file or in the resource module
#   builder template.
#
#############################################

"""
The module file for nxos_lag_interfaces
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = """
module: nxos_lag_interfaces
short_description: LAG interfaces resource module
description: This module manages attributes of link aggregation groups of NX-OS Interfaces.
version_added: 1.0.0
author:
- Trishna Guha (@trishnaguha)
- Nilashish Chakraborty (@NilashishC)
options:
  running_config:
    description:
    - This option is used only with state I(parsed).
    - The value of this option should be the output received from the NX-OS device
      by executing the command B(show running-config | section ^interface).
    - The state I(parsed) reads the configuration from C(running_config) option and
      transforms it into Ansible structured data as per the resource module's argspec
      and the value is then returned in the I(parsed) key within the result.
    type: str
  config:
    description: A list of link aggregation group configurations.
    type: list
    elements: dict
    suboptions:
      name:
        description:
        - Name of the link aggregation group (LAG).
        type: str
        required: true
      members:
        description:
        - The list of interfaces that are part of the group.
        type: list
        elements: dict
        suboptions:
          member:
            description:
            - The interface name.
            type: str
          mode:
            description:
            - Link aggregation group (LAG).
            type: str
            choices:
            - 'active'
            - 'on'
            - 'passive'
          force:
            description:
            - When true it forces link aggregation group members to match what is
              declared in the members param. This can be used to remove members.
            type: bool
  state:
    description:
    - The state of the configuration after module completion.
    type: str
    choices:
    - merged
    - replaced
    - overridden
    - deleted
    - gathered
    - rendered
    - parsed
    default: merged
notes:
- Tested against NXOS 7.3.(0)D1(1) on VIRL.
- Unsupported for Cisco MDS
- This module works with connection C(network_cli).

"""
EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# interface Ethernet1/4

- name: Merge provided configuration with device configuration.
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel99
      members:
      - member: Ethernet1/4
    state: merged

# After state:
# ------------
#
# interface Ethernet1/4
#   channel-group 99


# Using replaced

# Before state:
# -------------
#
# interface Ethernet1/4
#   channel-group 99 mode active

- name: Replace device configuration of specified LAG attributes of given interfaces
    with provided configuration.
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel10
      members:
      - member: Ethernet1/4
    state: replaced

# After state:
# ------------
#
# interface Ethernet1/4
#   channel-group 10


# Using overridden

# Before state:
# -------------
#
# interface Ethernet1/4
#   channel-group 10
# interface Ethernet1/2
#   channel-group 99 mode passive

- name: Override device configuration of all LAG attributes of given interfaces on
    device with provided configuration.
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel20
      members:
      - member: Ethernet1/6
        force: true
    state: overridden

# After state:
# ------------
# interface Ethernet1/2
# interface Ethernet1/4
# interface Ethernet1/6
#   channel-group 20 force


# Using deleted

# Before state:
# -------------
#
# interface Ethernet1/4
#   channel-group 99 mode active

- name: Delete LAG attributes of given interface (This won't delete the port-channel
    itself).
  cisco.nxos.nxos_lag_interfaces:
    config:
    - port-channel: port-channel99
    state: deleted

- name: Delete LAG attributes of all the interfaces
  cisco.nxos.nxos_lag_interfaces:
    state: deleted

# After state:
# ------------
#
# interface Ethernet1/4
#   no channel-group 99

# Using rendered

- name: Use rendered state to convert task input to device specific commands
  cisco.nxos.nxos_lag_interfaces:
    config:
    - name: port-channel10
      members:
      - member: Ethernet1/800
        mode: active
      - member: Ethernet1/801
    - name: port-channel11
      members:
      - member: Ethernet1/802
        mode: passive
    state: rendered

# Task Output (redacted)
# -----------------------

# rendered:
#  - "interface Ethernet1/800"
#  - "channel-group 10 mode active"
#  - "interface Ethernet1/801"
#  - "channel-group 10"
#  - "interface Ethernet1/802"
#  - "channel-group 11 mode passive"

# Using parsed

# parsed.cfg
# ------------

# interface port-channel10
# interface port-channel11
# interface port-channel12
# interface Ethernet1/800
#   channel-group 10 mode active
# interface Ethernet1/801
#   channel-group 10 mode active
# interface Ethernet1/802
#   channel-group 11 mode passive
# interface Ethernet1/803
#   channel-group 11 mode passive

- name: Use parsed state to convert externally supplied config to structured format
  cisco.nxos.nxos_lag_interfaces:
    running_config: "{{ lookup('file', 'parsed.cfg') }}"
    state: parsed

# Task output (redacted)
# -----------------------

# parsed:
#  - members:
#      - member: Ethernet1/800
#        mode: active
#      - member: Ethernet1/801
#        mode: active
#    name: port-channel10
#
#  - members:
#      - member: Ethernet1/802
#        mode: passive
#      - member: Ethernet1/803
#        mode: passive
#    name: port-channel11
#
#  - name: port-channel12

# Using gathered

# Existing device config state
# -------------------------------
# interface port-channel10
# interface port-channel11
# interface Ethernet1/1
#   channel-group 10 mode active
# interface Ethernet1/2
#   channel-group 11 mode passive
#

- name: Gather lag_interfaces facts from the device using nxos_lag_interfaces
  cisco.nxos.nxos_lag_interfaces:
    state: gathered

# Task output (redacted)
# -----------------------
# gathered:
#  - name: port-channel10
#    members:
#      - member: Ethernet1/1
#        mode: active
#  - name: port-channel11
#    members:
#      - member: Ethernet1/2
#        mode: passive
"""
RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample:
    - "interface Ethernet1/800"
    - "channel-group 10 mode active"
    - "interface Ethernet1/801"
    - "channel-group 10"
    - "interface Ethernet1/802"
    - "channel-group 11 mode passive"
"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.argspec.lag_interfaces.lag_interfaces import (
    Lag_interfacesArgs,
)
from ansible_collections.cisco.nxos.plugins.module_utils.network.nxos.config.lag_interfaces.lag_interfaces import (
    Lag_interfaces,
)


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=Lag_interfacesArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Lag_interfaces(module).execute_module()
    module.exit_json(**result)


if __name__ == "__main__":
    main()
