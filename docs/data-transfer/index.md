# Data transfer

Data goes to and from Hydra through the login nodes with `scp`, `sftp` or `rsync` from your own computer, through [Globus](globus.md) for large or unattended transfers and for anything between institutions, or through [rclone](rclone.md) for cloud storage such as Dropbox, OneDrive and Google Drive. Transfers to Hydra start from a computer on the Smithsonian network or the SI VPN; transfers from Hydra can go anywhere the login nodes can reach.

!!! warning "Copy data to `/scratch` or `/data`, not to `/home`"

    The home directory has a quota of 350 GB and 9 million files, and it is where `scp` puts files when no destination is given. Give every transfer a destination under `/scratch/genomics/USERNAME` or `/data`. Do not use `/tmp`.

[scp, sftp and rsync](scp-rsync.md) covers the command-line tools and the graphical ones (WinSCP, FileZilla) that use the same protocol. [Globus](globus.md) covers the Hydra collections and Globus Connect Personal. [rclone](rclone.md) covers authorising a cloud account from a machine with no browser. Transfers to and from `/store` run as [I/O jobs](../storage/store.md), not from the login nodes.
