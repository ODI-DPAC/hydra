# Storage

Hydra has four kinds of disk space. Keep scripts and configuration in `/home`, results in `/data`, the working files of jobs in `/scratch`, and project data waiting for analysis in `/store`. Each has its own quota and retention rules. See [Filesystems](filesystems.md).

To see how much space you are using, [check your usage and quotas](quotas.md). If you deleted or overwrote a file on `/home`, `/data` or `/store`, you can [recover it from a snapshot](snapshots.md). If the scrubber removed a file from `/scratch`, you can [request a restore](scrubber.md) for about ten days. If your job reads and writes intensively, it can [use the node's local SSD](ssd.md). If your data is on `/store`, you [copy it with the I/O queue](store.md) before a job uses it.

!!! danger "Files on `/scratch/public` older than 180 days are deleted every week"

    `/scratch` has no snapshots and no backup. Keep results on `/data` or off Hydra. We can restore a scrubbed file for about ten days after the [scrubber](scrubber.md) removes it.

None of the storage systems on Hydra are meant for archival storage. [Backups](backups.md) explains what is protected against what, so that you can decide where else to keep a copy. To move data on and off the cluster, see [Data transfer](../data-transfer/index.md).
