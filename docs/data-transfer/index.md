# Data transfer

There are three ways to move files to and from Hydra. Which one to use depends on how much data you are moving and where it is.

| Method | Use it for | Page |
|---|---|---|
| `scp`, `sftp`, `rsync` and graphical clients (WinSCP, FileZilla) | files between your computer and Hydra, up to a few tens of gigabytes | [scp, sftp and rsync](scp-rsync.md) |
| Globus | large transfers, transfers between institutions, and transfers that should keep going after you close your laptop | [Globus](globus.md) |
| rclone | cloud storage: Dropbox, OneDrive, Google Drive, S3 | [rclone and cloud storage](rclone.md) |

A transfer to Hydra starts from a computer on the Smithsonian network or the SI VPN. The login nodes do not accept connections from elsewhere. A transfer from Hydra can go to any host the login nodes can reach.

!!! warning "Copy data to `/scratch` or `/data`, not to `/home`"

    The home directory has a quota of 350 GB and 9 million files, and it is where `scp` puts files when you give no destination. We ask that every transfer name a destination under `/scratch/genomics/USERNAME` or `/data`. Do not use `/tmp`; it is small and shared.

Transfers to and from `/store` are different, because `/store` is not mounted on the compute nodes. They run as I/O jobs; see [Use /store and the I/O queue](../storage/store.md).

## Further reading

- [Filesystems](../storage/filesystems.md), for which partition to put data on
- [Check your disk usage and quotas](../storage/quotas.md)
- [Logging in and passwords](../getting-started/login.md), for the login-node names and the VPN
