# Network Management Path

## Goal

The Capstone will prefer official Cisco IOS resource modules from the `cisco.ios` collection for routing automation such as OSPF and BGP.

These modules require a real network management connection such as `ansible.netcommon.network_cli` over SSH.

## Why the Existing Console Workaround Is Not Enough

The original lab path used:

```text
AAP EE
  -> socat TLS relay
  -> Tailscale Funnel
  -> GNS3 console TCP port
  -> Cisco console
```

This is useful for lab-only console automation, but it is not equivalent to an SSH management plane and is not the preferred transport for Cisco IOS resource modules.

## Target Lab Path

The target for this Capstone is:

```text
AAP 2.7 Sandbox
  -> Custom Network EE
  -> ansible.netcommon.network_cli
  -> local socat TLS relay
  -> Tailscale Funnel
  -> local SSH relay / management path
  -> Cisco IOS SSH service
```

This keeps AAP as the execution platform while allowing the network automation content to use the same SSH-based connection model expected in production.

## Production Equivalent

```text
AAP Controller
  -> Automation Mesh
  -> Execution Node near the management network
  -> SSH / network_cli
  -> Cisco IOS devices
```

The Tailscale/Funnel/relay elements are strictly lab-only and must not be presented as the recommended production design.

## Validation Requirements

The SSH management path is considered proven only after:

1. TCP transport succeeds.
2. SSH authentication succeeds.
3. `ansible.netcommon.network_cli` establishes a persistent connection.
4. `cisco.ios.ios_facts` succeeds.
5. A second independent command validates the device identity.
6. The same path works for both R1 and R2.

## Fallback

If the local GNS3 host cannot provide an SSH management path to the cloud sandbox, the limitation will be documented explicitly. Console automation may still be used for transport experiments, but routing resource-module validation must be performed on a transport that supports `network_cli`.
