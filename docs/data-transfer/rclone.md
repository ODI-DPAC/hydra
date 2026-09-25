# rclone and cloud storage

[rclone](https://rclone.org/) copies between Hydra and cloud storage: Dropbox, OneDrive, Google Drive, Amazon S3 and the [other services rclone supports](https://rclone.org/#providers). It is the way to reach a cloud account from Hydra, and the way to move data to Hydra from a computer that cannot connect to the login nodes, such as one on telework.si.edu.

## Authorise a cloud account

Authorising rclone needs a browser, and the login nodes have none, so the configuration runs in two places: `rclone config` on Hydra, and `rclone authorize` on a computer with a browser, whose output you paste back into the Hydra session.

1. On a login node, load the module and start the configuration:

    ```console
    $ module load tools/rclone
    $ rclone config
    ```

    Choose `n` for a new remote, give it a short name (`db` for Dropbox, say), and pick the storage type. Accept the defaults for the client ID and secret, and answer `n` to "Use auto config?" because Hydra has no browser. rclone then prints an `rclone authorize` command.

2. On your own computer, install rclone and run that command. A browser window opens for the cloud service's sign-in; when it completes, rclone prints a token.

3. Paste the token into the waiting `rclone config` session on Hydra and finish the dialogue. The remote is saved in `~/.config/rclone/rclone.conf`.

rclone's pages for [Dropbox](https://rclone.org/dropbox/), [OneDrive](https://rclone.org/onedrive/) and [Google Drive](https://rclone.org/drive/) show the dialogue for each service. rclone's shared app ID works for most people. The pages say how to register your own if the shared one is throttled. To withdraw access later, remove rclone from the service's connected-apps settings.

## Copy and sync

```console
$ rclone copy results.tar db:hydra_backup/                       # one file to the cloud
$ rclone copy /scratch/genomics/USERNAME/project db:project/      # a directory to the cloud
$ rclone copy db:raw/ /scratch/genomics/USERNAME/raw/             # from the cloud to Hydra
$ rclone sync -i /scratch/genomics/USERNAME/project db:project/   # make the cloud copy match; -i asks before each change
```

`rclone ls db:` lists the remote, and `--dry-run` on any command shows what it would do. rclone runs on the login nodes, which are the nodes with a route to the internet. A large copy can trip the login-node limits, so cap the rate with `--bwlimit 20M` and run the copy in `screen` or `tmux` so it survives a dropped connection.
