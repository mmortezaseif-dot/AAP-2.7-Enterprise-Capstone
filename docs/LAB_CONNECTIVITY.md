# Lab Connectivity and Constraints

## Purpose

This document records how the temporary Red Hat AAP 2.7 sandbox reaches the local Cisco GNS3 lab, what limitations exist, which workarounds are used, and what the production-equivalent design would be.

## Environments

### Automation Platform

- Red Hat Ansible Automation Platform 2.7
- Red Hat Developer Sandbox
- Disposable / temporary environment

### Network Lab

- GNS3
- Cisco IOS routers
- Exact device and IOS capability matrix will be documented after capability discovery.

## Connectivity Constraint

The cloud-hosted Developer Sandbox cannot be treated as if it were on the same routed management network as a local GNS3 environment.

Therefore, direct production-style management connectivity cannot be assumed.

## Lab Workaround

The lab may require a temporary transport/tunneling workaround between the cloud sandbox and the local GNS3 environment.

The exact path for this fresh environment will be revalidated before use and documented here with:

- ingress/egress direction
- protocol and port mapping
- encryption/TLS boundary
- local forwarding/proxy components
- AAP Execution Environment dependencies
- security limitations
- failure modes

## Important Boundary

Any tunneling, forwarding, console transport, or public-ingress workaround used here is a **lab-only solution**.

It must not be presented as the recommended production architecture.

## Production Equivalent

A production design should place execution capability close to the managed network, typically using:

- Automation Mesh
- Execution Nodes in or near the network management zone
- SSH / HTTPS / NETCONF as supported by the target platform
- enterprise routing/firewall controls
- enterprise PKI and secret management
- no unnecessary exposure of device-management interfaces to the public Internet

## Validation Checklist

Before starting routing automation on the fresh sandbox, validate:

- AAP can start an execution environment.
- The execution environment can reach the chosen lab transport endpoint.
- Cisco authentication succeeds.
- `ansible_network_os` and connection method are correct.
- `cisco.ios.ios_facts` succeeds.
- basic show commands succeed.
- configuration changes can be independently verified.
- persistence behavior is known for each IOS image.

## Documentation Rule

Every workaround discovered during the Capstone must be documented with:

1. Problem
2. Root cause
3. Lab workaround
4. Security impact
5. Production alternative
6. Validation evidence
