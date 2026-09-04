---
title: "2024 Cluster Upgrade to Hydra-7"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/242647293/2024+Cluster+Upgrade+to+Hydra-7"
date-modified: "2024-05-03"
author: "SGK"
---

This page lists the upgrades that will take place during the April 22 - May 2, 2024 upgrade.


While we are making every effort to set up the new configuration as backward compatible as possible, there will be changes, see below. 
We will adjust the Wiki once the changes are in place.


## What Is Being Upgraded


1. The OS version (& *flavor*) of the cluster (i.e., Rocky 8.9)
2. The version of the Grid Engine (i.e., v8.8.1 aka 2023.1.1)
3. The cluster management tool, i.e, Base Command Management (aka BCM v10.0)
4. The version of most tools (compilers, etc.)
5. new Hardware: fifteen new compute nodes will be added:
    1. two nodes with 2x96c or 192 cores (CPUs) and 1.5TB of memory
    2. twelve nodes with 2x64c or 128 cores (CPUs) and 1.0TB of memory
    3. One quad GPU servers, with 4x L50S NVIDIA GPUs
6. We have/will decommission our oldest compute nodes, namely
    1. the `compute-43-xx`series, and
    2. the `compute-00-xx` series.
7. This will:
    1. increase the number of CPUs from about 4900 to about 5900,
    2. increase the total memory from about 40 to 50TB,
    3. decrease the number of compute nodes from about 87 to 78.
    4. The new compute nodes have the latest generation architecture.
8. As a result of the hardware upgrades, we will adjust system configuration (queues, disk quota, modules, etc.)
9. We will use the downtime to upgrade any needed firmware and make other adjustments as needed.


## Details on Changes


Click on the links for details


1. [New list of modules](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-New-list-of-modules)
    1. Some modules have moved
    2. New set of compilers versions
    3. MPI
2. [Bio packages](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-Bio-packages)
    1. The list of packages has been pruned
    2. The list of modules has been trimmed
    3. Some generic tools have been moved
3. [Queues](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-Queues): changes and new ones
    1. Changes in limits
    2. New GPU queues
    3. New `ompi` PE for NVIDIA MPI
    4. I/O queues changes, use `-l ioq`
4. [GPUs](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-GPU)
5. [New version of the command `module`](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-Command-module)
    1. version 5.3.1 allows use of shortcut `ml`
    2. customization
6. [Disk space changes](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-Disk-space-changes)
    1. Consolidation
    2. New quotas
7. [Misc](https://confluence.si.edu/display/HPC/2024+Upgrade+Details#id-2024UpgradeDetails-Misc)
