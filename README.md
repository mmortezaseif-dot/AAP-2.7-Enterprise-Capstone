# AAP 2.7 Enterprise Capstone

Enterprise-style Red Hat Ansible Automation Platform 2.7 capstone focused on Cisco network automation.

## Project Goals

- Build the AAP 2.7 environment from a fresh platform.
- Use GitHub as the Source of Truth for automation content and configuration artifacts.
- Use official Ansible network collections, primarily `cisco.ios` and `ansible.netcommon`.
- Automate real routing scenarios supported by the lab, including OSPF, BGP, route policy, validation, rollback, and persistence where the device images allow it.
- Implement AAP resources such as organizations, RBAC, credentials, projects, inventories, execution environments, job templates, workflows, EDA, notifications, analytics, and Configuration as Code.
- Validate business/network state independently instead of treating a green job as proof of success.
- Document lab constraints, connectivity design, workarounds, troubleshooting, and production alternatives.

## Engineering Principles

- GitHub is the Source of Truth.
- Prefer official resource modules over raw CLI configuration when platform support allows it.
- Safety -> Validation -> Controlled rollout -> Scale.
- Apply != Persist.
- Job success != Desired network state proven.
- Build once -> Test -> Promote the same artifact.
- Secrets must never be committed to Git.

## Planned Cisco Automation Scope

The exact scope is capability-driven and will be validated against the available GNS3 IOS images.

Planned areas include:

- Device facts and capability discovery
- Interface and Layer 3 configuration
- Static routing
- OSPFv2
- BGP
- Prefix lists and route maps
- Routing-policy validation
- Pre-check / change / post-check workflows
- Configuration backup and rollback
- Running-config persistence
- Drift detection
- Event-driven diagnostics/remediation where practical

## AAP 2.7 Capstone Scope

- Platform assessment
- Organization / Teams / RBAC
- Credentials
- GitHub Project
- Inventory and Constructed Inventory
- Custom Execution Environment
- Job Templates
- Workflow Job Templates
- Schedules and Notifications
- Private Automation Hub concepts/artifacts
- Event-Driven Ansible with a real external event path
- Configuration as Code
- Analytics / operational validation
- Troubleshooting and recovery drills

## Repository Documentation

Detailed engineering documentation will be maintained under `docs/`, including:

- lab architecture and connectivity
- AAP-to-GNS3 connectivity constraints and workarounds
- Cisco image/capability matrix
- execution environment design
- routing automation design
- validation and rollback strategy
- EDA architecture
- troubleshooting notes
- production-equivalent architecture

> This repository is public. No passwords, tokens, private keys, or sensitive endpoints should ever be committed.
