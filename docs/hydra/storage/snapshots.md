# Snapshots and recovering files

Some of the disks on the NetApp filer and the NAS have the so called "snapshot mechanism" enabled:


- This allow users to recover deleted files or access an older version of a file.
- Indeed, the NetApp filer makes a "snapshot" copy of the file system (the content of the disk) every so often and keeps these snapshots up to a given age.
- So if we enable hourly snapshot and set a two weeks retention, you can recover a file as it was hours ago, days ago or weeks ago, but only up to two weeks ago.
- The drawback of the snapshot is that when files are deleted, the disk space is not freed until the deleted files age-out, like 2 or 4 weeks later.


## How to Use the NetApp Snapshots:


To recover an old version or a deleted file, foo.dat, that was (for example) in`/data/genomics/frandsen/important/results/`:


- If the file was deleted:


```
   % cd /data/genomics/.snapshot/XXXX/frandsen/important/results
   % cp -pi foo.dat /data/genomics/frandsen/important/results/foo.dat
```


- If you want to recover an old version:


```
   % cd /data/genomics/.snapshot/XXXX/frandsen/important/results
   % cp -pi foo.dat /data/genomics/frandsen/important/results/old-foo.dat
```


- The "`-p"` will preserve the file creation date and the`"-i"`will prevent overwriting an existing file.
- The `"XXXX`" is to be replaced by either:
    - `hourly.YYYY-MM-DD_HHMM`
    - `daily.YYYY-MM-DD_0010`
    - `weekly.YYYY-MM-DD_0015` 
where `YYY-MM-DD` is a date specification (i.e., `2015-11-01`)
- The files under `.snapshot` are read-only:
    - they be recovered using `cp`, `tar` or `rsync`; but
    - they cannot be moved (`mv`) or deleted (`rm`).


## How to Use the NAS/ZFS Snapshots:


- The snapshots on the `/store` disks are:
    - located under `/store/XXX/.zfs/snapshot` (where XXX is, for example, `public`) and
    - in sub-directories named `auto-YYMMDD.0230-8w` where YYYYMMDD represent the date of the snapshot.
- Content of NAS/ZFS snapshots can be recovered as described above.
