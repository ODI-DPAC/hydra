# Storage

Hydra has several filesystems with different purposes, speeds, quotas and retention rules. Choosing the right one matters.

| Path | Purpose | Backed up | Snapshots | Scrubbed |
|---|---|---|---|---|
| `/home` | dotfiles, scripts, small files | DR copy to cloud | yes | no |
| `/data` | project data | see [backups](backups.md) | yes | no |
| `/scratch` | working space for jobs (GPFS over InfiniBand) | no | no | yes, files older than 180 days |
| `/store` | near-line storage, reachable from the I/O queue only | no | no | no |
| `/pool` | shared project space | see [backups](backups.md) | yes | no |

<!-- TODO: verify every cell above against the current configuration before launch. -->

- [Filesystems in detail](filesystems.md)
- [Quotas and checking your usage](quotas.md)
- [Snapshots and recovering deleted files](snapshots.md)
- [The scrubber and requesting restores](scrubber.md)
- [Local SSD, NAS and bigtmp](special.md)
- [Backups and disaster recovery](backups.md)
- Moving data on and off Hydra: [Data transfer](../../data-transfer/index.md)
