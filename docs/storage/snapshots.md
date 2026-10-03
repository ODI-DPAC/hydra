# Recover a file from a snapshot

`/home`, `/data` and the project `/store` partitions keep read-only snapshots of their contents, for 4 weeks on `/home` and 2 weeks on `/data`. On `/store` the period depends on the partition. You copy a file you deleted or overwrote within that time back from the snapshot.

!!! danger "`/scratch` has no snapshots"

    A file you delete from `/scratch` cannot be recovered. We can restore only files the [scrubber](scrubber.md) removed, and only for about ten days.

## Recover a file on /home or /data

1. List the snapshots of the partition. They are in a hidden `.snapshot` directory at its top, named by frequency and time:

    ```console
    $ ls /data/genomics/.snapshot
    daily.2026-10-02_0010   hourly.2026-10-03_1005  hourly.2026-10-03_1305  weekly.2026-09-27_0015
    daily.2026-10-03_0010   hourly.2026-10-03_1105  hourly.2026-10-03_1405
    hourly.2026-10-03_0905  hourly.2026-10-03_1205  weekly.2026-09-20_0015
    ```

2. Change into the snapshot from before the loss, at the path the file had:

    ```bash
    cd /data/genomics/.snapshot/daily.2026-10-02_0010/USERNAME/analysis/results
    ```

3. Copy the file back. `-p` keeps its dates. `-i` asks before overwriting an existing file:

    ```bash
    cp -pi results.csv /data/genomics/USERNAME/analysis/results/results.csv
    ```

    To keep the current version as well, copy the old one under another name:

    ```bash
    cp -pi results.csv /data/genomics/USERNAME/analysis/results/results-old.csv
    ```

Files under `.snapshot` can be read and copied (with `cp`, `tar` or `rsync`) but not moved or deleted. `/home` works the same way, under `/home/.snapshot/`.

## Recover a file on /store

`/store` snapshots are under `.zfs/snapshot` at the top of each `/store` partition, named `auto-YYYY-MM-DD_HH-MM`:

```console
$ ls /store/PROJECT/.zfs/snapshot
auto-2026-09-20_03-00  ...  auto-2026-10-03_03-00
$ cp -pi /store/PROJECT/.zfs/snapshot/auto-2026-10-03_03-00/USERNAME/data.tar /store/PROJECT/USERNAME/
```

!!! warning "How far back `/store` snapshots go depends on the partition"

    Some partitions keep 8 weeks of snapshots, some keep 2 or 4 weeks, and some list none. List the directory on your own partition to see what it has before you rely on it.

`/store` is mounted only on the login nodes, the head node, the interactive nodes and the RStudio server node.

A snapshot lives on the same storage system as the partition, so it does not protect against a failure of that system. [Backups](backups.md) describes what does.

## Further reading

- [Backups](backups.md) for the disaster-recovery copy and what it is for
- [Filesystems](filesystems.md) for the snapshot schedule of each partition
