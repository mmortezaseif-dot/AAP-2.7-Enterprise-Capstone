# GNS3 Routing Topology

## Initial observed state

At the start of the routing phase:

- R1 FastEthernet0/0 had no IP address and was administratively down.
- R2 FastEthernet0/0 had no IP address and was administratively down.
- CDP showed no neighbor on either router.

This proved that no usable Layer-3 adjacency existed initially.

## Bootstrapped topology

The lab was then bootstrapped to the following design:

```text
                  10.0.12.0/30

        Fa0/0                     Fa0/0
R1  10.0.12.1 ---------------- 10.0.12.2  R2
     Lo0 1.1.1.1/32           Lo0 2.2.2.2/32
```

The Layer-3 link and loopbacks are the foundation for the OSPF and BGP automation exercises.

## Automation plan

```text
L3 baseline
  -> OSPF process 10 / area 0
  -> OSPF adjacency validation
  -> loopback route learning
  -> eBGP AS65001 <-> AS65002
  -> prefix advertisement
  -> routing policy
```

## Lab bootstrap boundary

Physical GNS3 cabling and the minimum initial interface bootstrap were performed manually because the cloud AAP sandbox does not have a native management path to the local GNS3 interfaces.

This manual bootstrap is not the final automation model.

Repeatable routing intent is stored in Git and will be generated using official `cisco.ios` resource modules.

## Lab transport vs production

Lab:

```text
Git desired state
 -> cisco.ios resource modules
 -> rendered Cisco CLI
 -> controlled console transport adapter
 -> IOS
 -> independent verification
```

Production target:

```text
Git desired state
 -> AAP
 -> Automation Mesh / Execution Node near the network
 -> SSH + ansible.netcommon.network_cli
 -> cisco.ios resource modules
 -> IOS / IOS-XE
```

The console/Tailscale/socat path is a lab workaround and must not be treated as the recommended production architecture.
