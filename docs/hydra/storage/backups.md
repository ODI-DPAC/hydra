# Backups

No partition on Hydra is backed up in a way you can restore from yourself. Two mechanisms exist, with different purposes: snapshots, which you use to get back a recently deleted or overwritten file, and a disaster-recovery copy of `/home` and `/data`, which exists to rebuild those partitions if the storage system fails.

| Partition | Snapshots | Disaster-recovery copy | Scrubbed |
|---|---|---|---|
| `/home` | yes, 4 weeks | AWS Glacier | no |
| `/data` | yes, 2 weeks | AWS Glacier | no |
| `/scratch` | no | no | files older than 180 days |
| `/store` | yes, daily, 14 days | no | no |
| local SSD | no | no | deleted when the job ends |

## Snapshots

Use snapshots to recover a file you deleted or overwrote within the retention period. [Snapshots](snapshots.md) has the procedure for the NetApp partitions (`/home`, `/data`) and for `/store`.

## Disaster recovery

The Glacier copy of `/home` and `/data` is for rebuilding a partition after a storage failure. It is not for restoring individual files: a restore from Glacier takes staff time and is billed by Amazon, so a request needs a justification, and the requester may be asked to contribute to the cost. Copies are kept for up to a year.

!!! warning "The disaster-recovery copy has been paused since December 2025"

    Backups to Glacier are suspended pending an accounting issue. The NetApp filer holding `/home` and `/data` is unaffected and snapshots still work. See [News](../../news/index.md#2025-12-05).

## Results

!!! warning "Hydra is not long-term storage"

    Copy results to your own systems when an analysis is complete, and delete what you no longer need. `/scratch` is scrubbed after 180 days; see [Scrubber](scrubber.md). Which partition to use for what is on [Filesystems](filesystems.md); moving data off the cluster is under [Data transfer](../../data-transfer/index.md).
