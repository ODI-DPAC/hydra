# Data transfer

| Method | Best for |
|---|---|
| [scp, sftp, rsync](scp-rsync.md) | anything from your laptop or another Unix host |
| [Globus](globus.md) | large transfers, transfers between institutions, unattended transfers |
| [rclone](rclone.md) | Dropbox, OneDrive, Google Drive, S3 and other cloud storage |

Transfers to `/store` must run from the I/O queue; see [Use /store and the I/O queue](../storage/store.md).
