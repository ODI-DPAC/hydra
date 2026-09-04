---
title: "Storage Systems (Disks)"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152287/Storage+Systems+Disks"
date-modified: "2025-10-06"
author: "SGK"
categories: ["hydra7"]
---

The disk space available on the cluster is mounted off two dedicated devices (NetApp and GPFS); a third one (NAS) is not accessible from all the compute nodes.


The NAS is only accessible from the login, interactive and I/O nodes (hence it is a near-line storage system).


The available public disk space is divided in several area (aka partitions):


- a small partition for basic configuration files and small storage, the `/home` partition`,`
- a set of medium size partitions, the `/data` partitions,
- a set of very large partitions, the `/scratch` partitions,
- a set of medium size, low-cost, partitions, the `/store` partitions.


It should be used as follows:**


| Name | Typical Use | System | Size(*) |
| --- | --- | --- | --- |
| `/home` | For your basic configuration files, scripts and job files:


- low quota limit but you can easily recover old stuff,
- backup to AWS Glacier for disaster recovery (DR) | NetApp | `20TB` |
| `/data/public` | For important but small files like final results, config files, etc


- medium quota limit, you can easily recover old stuff,
- but when deleting files disk space is not released right away.
- backup to AWS Glacier for DR | NetApp | `330TB` |
| `/scratch/public` | For the bulk of your large storage


- faster storage,
- high quota limit, and disk space is released right away when deleting files. | GPFS | `800TB` |
| `/store/public` | For near-line storage. | NAS | 175TB |


(*): These sizes are only indicative, as we adjust them as needed.


## Note


- We impose quotas (limit on how much can be stored on each partition by each user) and we monitor disk usage;
    - `/home` should not be used for storage of large files, use `/scratch` instead;
    - `/data` is best to store things like final results, code, etc.. (important but not too large);
- We implement an automatic scrubber: old stuff get deleted to make space,
    - files older than 180 days and empty directories on /scratch/public will scrubbed.


- None of the disks on the cluster are for long term storage:
    - please copy your results back to your "home" computer and
    - delete what you don't need any longer.
- Once you reach your quota you won't be able to write anything on that partition until you delete stuff.
- Some compute nodes also have local SSDs (solid state disks, see [How to Use Local SSD Space](../disks-space-and-usage/how-to-use-local-ssd-space.md)).


![(info)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/information.svg) A complete description is available at the [Disk Space Configuration](../disks-space-and-usage/disks-space-configuration.md) page.
