# Backups

No partition on Hydra is backed up in a way you can restore from yourself. Two mechanisms exist, with different purposes: snapshots, which you use to get back a recently deleted or overwritten file, and a disaster-recovery copy of `/home` and `/data`, which exists to rebuild those partitions if the storage system fails.

| Partition | Snapshots | Disaster-recovery copy | Scrubbed |
|---|---|---|---|
| `/home` | yes, 4 weeks | AWS Glacier | no |
| `/data` | yes, 2 weeks | AWS Glacier | no |
| `/scratch` | no | no | files older than 180 days |
| `/store` (project partitions) | yes, 8 weeks | no | no |
| local SSD | no | no | deleted when the job ends |

## Snapshots

Use snapshots to recover a file you deleted or overwrote within the retention period. [Recover a file from a snapshot](snapshots.md) has the procedure for `/home`, `/data` and `/store`.

## Disaster recovery

The Glacier copy of `/home` and `/data` is for rebuilding a partition after a storage failure. It is not for restoring individual files: a restore from Glacier takes staff time and is billed by Amazon, so a request needs a justification, and the requester may be asked to contribute to the cost. The HPC team keeps the copies for up to a year.

## Long-term storage

!!! note "None of the storage systems on Hydra are meant for archival storage"

    Some projects keep data on Hydra for years, because of the volume they collect or because the data were here before other options existed, and their allocations reflect that. Identify a long-term destination off Hydra for every dataset that outlives its analysis, and move data there when the analysis ends. Moving data off the cluster is under [Data transfer](../data-transfer/index.md).
