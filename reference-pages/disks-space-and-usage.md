---
title: "Disks Space and Usage"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152303/Disks+Space+and+Usage"
date-modified: "2025-10-06"
author: "SGK/PBF"
categories: ["hydra7"]
---

1. [Introduction: What Disks to Use](disks-space-and-usage.md)
2. [Disks Space Configuration](disks-space-and-usage/disks-space-configuration.md)
3. [How to Check Disk & Quota Usage](disks-space-and-usage/how-to-check-disk-quota-usage.md)
4. [How to Copy Files to/from Hydra](disks-space-and-usage/how-to-copy-files-to-from-hydra.md)
5. [How to Recover Old or Deleted Files using Snapshots](disks-space-and-usage/how-to-recover-old-or-deleted-files-using-snapshots.md)
6. [Public Disks Scrubber and How to Request Scrubbed Files to be Restored](disks-space-and-usage/scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)
7. [How to Use Local SSD Space](disks-space-and-usage/how-to-use-local-ssd-space.md)
8. [How to Use NAS Storage and the I/O Queue](disks-space-and-usage/how-to-use-nas-storage-and-the-i-o-queue.md)
9. [How to Use "bigtmp" - Access to Large Temporary Disk Space](disks-space-and-usage/how-to-use-bigtmp-access-to-large-temporary-disk-space.md)


As of 06 Oct 2025


## 1. Introduction: What Disks to Use


The disk space available on the cluster is mounted off a set of dedicated devices:


1. A NetApp filer, via NFS,
2. Two GPFS units, via the Infiniband fabric,
3. Two low cost NAS, via NFS, accessible on only a subset of nodes.


The available disk space is divided in several area (aka volumes, filesets or partitions):


- a small partition for basic configuration files and minimal storage, the `/home` partition`,`
- a set of medium size partitions, the `/data` partitions,
- a set of very large partitions for temporary storage, the `/scratch` partitions,
- a set of medium, size low-cost, partitions, the `/store` partitions.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The `/scratch/public` partition is scrubbed every Sunday, i.e.: files older that 180 days are automatically removed ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg)


- Consult the [Scrubber and How to Request Scrubbed Files to be Restored](disks-space-and-usage/scrubber-and-how-to-request-scrubbed-files-to-be-restored.md) page for more information.


### SSD


A subset of nodes have local SSDs (solid state disks) that can be used for applications that require very high I/O rates, and will complete faster when using SSDs.


- Jobs that do not perform intensive I/O should not use the SSDs - this is a scarce shared resource.


These disks are local to the compute nodes, hence:


- you cannot see the SSDs from either login nodes,
- your job will be able to use the SSD *only while the job is running*, hence your job need to be adjusted accordingly and request SSD space.
- If your job exceeds the amount of SSD space requested, your job won't be able to write any longer to the SSD,
- consult the [How to Use Local SSD Space](disks-space-and-usage/how-to-use-local-ssd-space.md) page for more information.


## Remember


- We impose quotas:
    - limits on how much can be stored on each disk (partition/volume/fileset) by each user, and
    - we monitor disk usage;
- `/home` should not be used to keep large files, use `/scratch,`or,`/data` instead;
- `/scratch/public` is for active temporary storage (i.e., while analyzing data), not for long term storage.
- `/scratch/public` has been moved to a faster GPFS unit
    - public space on `/scratch` is regularly scrubbed: old stuff is deleted to make sure there is space for active users.
- None of the disks on the cluster are for long term storage:
    - please copy your results back to your *home* computer and
    - delete what you don't need any longer.
- While the disk systems on `Hydra` are highly reliable, most of the disks on the cluster are *not* backed up, although:
    - some partitions have snapshots enabled: this allows you to 'undelete' files that were recently deleted (see [How to Recover Old or Deleted Files using Snapshots](disks-space-and-usage/how-to-recover-old-or-deleted-files-using-snapshots.md))
    - `/home` and `/data` are backed up to AWS Glacier for disaster recovery (DR).
- Once you reach your quota you won't be able to write anything on that partition until you delete stuff.
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Do not keep a very large number of files in the same directory:
    - ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)best practice is to keep less then 5,000 - 50,000 files in the same directory.
- If you keep too many of them in the same directory:
    - you may not be able to write more files,
    - listing the content of such directory will be exceedingly slow.
- What to do instead?
    - Use subdirectories to better organize your files (and your work).
