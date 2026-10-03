# Filesystems

Hydra has public partitions and a number of project partitions, each with its own quotas and retention rules. We adjust sizes and quotas as needed. `disk-usage -d all+ -quotas` on a login node prints the current values ([Check your disk usage and quotas](quotas.md)).

## Public partitions

| Partition | System | Size | Space quota, soft / hard | File quota, soft / hard |
|---|---|---|---|---|
| `/home` | NetApp | 22 TB | 350 GB / 384 GB | 9 M / 10 M |
| `/data/public` | NetApp | 330 TB | 4.3 TB / 4.5 TB | 9.5 M / 10 M |
| `/scratch/public` | GPFS | 800 TB | 14 TB / 15 TB | 37 M / 39 M |

| Partition | Snapshots | Scrubbed | Use for |
|---|---|---|---|
| `/home` | 4 weeks | no | configuration files, scripts, job files, source code |
| `/data/public` | 2 weeks | no | final results, small important files; space from deleted files is not freed until the snapshots age out |
| `/scratch/public` | none | files older than 180 days, weekly | input data and working files for jobs; the fastest partition, over InfiniBand |

!!! note "`/store/public` is being phased out"

    `/store/public` is no longer available. Use `/data/public`. A cloud-based cold-storage service is being evaluated as the replacement. Project `/store` partitions are not affected.

A soft limit can be exceeded for a grace period. At the hard limit writes fail. The file quota counts inodes, so many small files reach it before the space quota does. `/scratch/dbs` (10 TB) holds the shared bioinformatics databases. See [Local databases](../software/guides/databases.md).

`/scratch/public` is divided by unit or discipline into `biology`, `genomics`, `humanities`, `nasm`, `odi` and `sao`. Your directory is under one of them, `/scratch/public/genomics/USERNAME` for example. The shorter form `/scratch/genomics` is a link to `/scratch/public/genomics`, and either works.

## Project partitions

Groups with their own funding have dedicated partitions under `/scratch` and `/store`, with quotas set per project. `quota+` shows the ones you have access to. Dedicated space is bought with project funds when the disk farm is expanded. Email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).

## Storage systems

| System | Partitions | Access | Properties |
|---|---|---|---|
| NetApp | `/home`, `/data` | every node | snapshots; disaster-recovery copy to AWS Glacier (see [Backups](backups.md)) |
| GPFS over InfiniBand | `/scratch` | every node | fastest; no snapshots; scrubbed |
| NAS | `/store` (project partitions) | login, head, interactive and RStudio server nodes only | snapshots, 8 weeks; fault tolerant but not highly available (see [Use /store and the I/O queue](store.md)) |
| local SSD | `$SSD_DIR` | the node the job runs on, while it runs | see [Use a node's local SSD](ssd.md) |

## Scrubbing

!!! danger "Files on `/scratch/public` older than 180 days are deleted every week"

    `/scratch` has no snapshots and no backup. Move anything you need to keep to `/data` or off Hydra before it is 180 days old.

A scrubber runs weekly and removes files on `/scratch/public` older than 180 days, and old empty directories. It holds the removed files in a staging area for about ten days before deleting them. During that time they still count against your quota, and we can restore them on request. See [Find scrubbed files and request a restore](scrubber.md). A restored file's change time (`ctime`) is reset, so it is safe for another 180 days.

None of the storage systems on Hydra are meant for [archival storage](backups.md#long-term-storage). Delete what you no longer need. Compress or archive sets of small files. `tar -czf archive.tgz dir/` packs a directory into one file, and `tar -xf archive.tgz` unpacks it.
