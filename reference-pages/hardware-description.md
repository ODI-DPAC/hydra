---
title: "Hardware Description"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152283/Hardware+Description"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](hardware-description.md)
2. [Login and Head Nodes](hardware-description/login-and-head-nodes.md)
3. [Compute Nodes](hardware-description/compute-nodes.md)
4. [Network: Ethernet and InfiniBand](hardware-description/network-ethernet-and-infiniband.md)
5. [Storage Systems (Disks)](hardware-description/storage-systems-disks.md)


# 1. Introduction


As of May 2024, `Hydra-7` consists of:


- one head node and two login nodes;
- ~70 compute nodes that adds up to ~6,000 CPUs & 8 GPUs, ~45 TB memory;
- a set of 10Gbps network switches, all the nodes are on 10GbE;
- an InfiniBand (IB) director switch (144 ports, expandable to 256, at 100Gbps)
- a 3 tiers storage (disks) configuration:
    - a two nodes NetApp controller (FAS8300) with 8 shelves (total ~900TB):
        - a dedicated device that provides disk space to the cluster, i.e. to all the nodes using NFS (10GbE).
    - a GPFS system with two dedicated NSDs (total ~2PB):
        - a high performance general parallel file system (GPFS, aka IBM Spectrum Scale), using the InfiniBand for I/O.
    - Two NAS systems for near-line storage (total ~1.7PB):
        - a slower, more cost-effective storage available only on some nodes.
- all the nodes (head, login and compute nodes) are connected to the IB switch (except two).
