# Cisco Capability Matrix

This matrix records which automation features are actually validated against the GNS3 IOS images used by this Capstone.

| Device | Model | IOS Version | Transport | ios_facts | L3 Interfaces | Static Routes | OSPFv2 | BGP Global | BGP AF | Prefix Lists | Route Maps | Save/Persist |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| R2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Validation Rules

- A feature is marked supported only after a successful AAP job and independent device-side verification.
- Collection documentation does not automatically prove compatibility with the specific IOS image in this lab.
- Unsupported or partially supported features must be documented with the exact error/behavior observed.
- If a resource module is not usable on the lab image, a fallback such as `cisco.ios.ios_config` may be evaluated, but the reason must be documented.
- Lab workarounds must not be represented as production recommendations.

## Evidence to Record

For each tested capability, record:

- AAP Job Template / playbook
- module used
- device and IOS version
- before state
- intended change
- after state
- independent verification command
- idempotency result
- persistence result
- known limitation/workaround
