# Storage

Hydra has four kinds of disk space: `/home` for scripts and configuration, `/data` for results, `/scratch` for the working files of jobs, and `/store` for project near-line storage. Each has its own quota and retention rules, listed under [Filesystems](filesystems.md).

To see where you stand, [check your usage and quotas](quotas.md). To get a file back, [recover it from a snapshot](snapshots.md) on `/home`, `/data` or `/store`, or [request a restore](scrubber.md) if the scrubber removed it from `/scratch`. Jobs that read and write intensively can [use a node's local SSD](ssd.md); data on `/store` is [copied with the I/O queue](store.md) before a job uses it.

!!! danger "Files on `/scratch` older than 180 days are deleted every week"

    `/scratch` has no snapshots and no backup. Keep results on `/data` or off Hydra; the [scrubber](scrubber.md) can restore a file for about ten days after removing it, and not after.

None of the storage systems on Hydra are meant for archival storage; [Backups](backups.md) lists the snapshot and disaster-recovery coverage of each partition. Moving data on and off the cluster is under [Data transfer](../data-transfer/index.md).
