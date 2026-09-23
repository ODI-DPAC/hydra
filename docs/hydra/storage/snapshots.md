# Recover a file from a snapshot

This page covers getting back a file you deleted or overwrote on `/home`, `/data` or a project `/store` partition. Those partitions keep read-only snapshots of their contents: `/home` for 4 weeks, `/data` for 2 weeks, `/store` for 8 weeks. 
!!! danger "`/scratch` has no snapshots"

    A file you delete from `/scratch` cannot be recovered. Only files removed by the [scrubber](scrubber.md) can be restored, and only for about ten days.

## Recover a file on /home or /data

1. List the snapshots of the partition. They are in a hidden `.snapshot` directory at its top, named by frequency and time:

    ```console
    $ ls /data/genomics/.snapshot
    hourly.2026-09-23_1005  hourly.2026-09-23_1105  daily.2026-09-23_0010  weekly.2026-09-21_0015
    ```

2. Change into the snapshot from before the loss, at the path the file had:

    ```bash
    cd /data/genomics/.snapshot/daily.2026-09-23_0010/USERNAME/analysis/results
    ```

3. Copy the file back. `-p` keeps its dates; `-i` refuses to overwrite an existing file:

    ```bash
    cp -pi results.csv /data/genomics/USERNAME/analysis/results/results.csv
    ```

    To keep the current version as well, copy the old one under another name:

    ```bash
    cp -pi results.csv /data/genomics/USERNAME/analysis/results/results-old.csv
    ```

Files under `.snapshot` can be read and copied (with `cp`, `tar` or `rsync`) but not moved or deleted. `/home` works the same way: `/home/.snapshot/`.

## Recover a file on /store

`/store` snapshots are under `.zfs/snapshot` at the top of each `/store` partition, one directory per day, named `auto-YYMMDD.0230-8w`:

```console
$ ls /store/PROJECT/.zfs/snapshot
auto-260916.0230-8w  auto-260917.0230-8w  auto-260918.0230-8w  ...
$ cp -pi /store/PROJECT/.zfs/snapshot/auto-260917.0230-8w/USERNAME/data.tar /store/PROJECT/USERNAME/
```

`/store` is mounted on the login and interactive nodes only.

A snapshot lives on the same storage system as the partition, so it does not protect against a failure of that system; what does is described under [Backups](backups.md).
