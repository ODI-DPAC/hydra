# Storage

Hydra has several filesystems with different purposes, speeds, quotas and retention rules.

## Which filesystem

| Path | Purpose | Backed up | Snapshots | Scrubbed |
|---|---|---|---|---|
| `/home` | dotfiles, scripts, small files | see [Backups](backups.md) | hourly and weekly, two weeks | no |
| `/data` | project data | see [Backups](backups.md) | hourly and weekly, two weeks | no |
| `/scratch` | working space for jobs (GPFS over InfiniBand) | no | no | files older than 180 days |
| `/store` | near-line storage, I/O queue only | no | ZFS snapshots | no |

## In this section

- [Filesystems in detail](filesystems.md)
- [Quotas and checking your usage](quotas.md)
- [Snapshots and recovering deleted files](snapshots.md)
- [The scrubber and requesting restores](scrubber.md)
- [Local SSD, NAS and bigtmp](special.md)
- [Backups and disaster recovery](backups.md)

Moving data on and off Hydra is covered under [Data transfer](../../data-transfer/index.md).
