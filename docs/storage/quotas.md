# Check your disk usage and quotas

This page covers finding out how much space and how many files you are using on each partition, how close you are to a quota, and which directories hold the most. Every partition has a per-user quota (see [Filesystems](filesystems.md)); once you reach the hard limit, writes to that partition fail until you delete something.

## Check your quotas

1. Print your usage and quotas on every partition:

    ```console
    $ quota+
    Disk quotas for user USERNAME (uid 12345):
    Mounted on                             Used   Quota   Limit   Grace   Files   Quota   Limit   Grace
    ----------                          ------- ------- ------- ------- ------- ------- ------- -------
    /data/public                          4.89T  22.50T  23.00T       0  118.0M  280.0M  290.0M       0
    /home                                14.41G  350.0G  384.0G       0  136.6k   9.00M  10.00M       0
    /scratch/public                       2.10T  14.00T  15.00T       0    1.2M  37.00M  39.00M       0
    /store/PROJECT                        1.00G    none    none
    ```

    `Quota` is the soft limit and `Limit` the hard limit, for space and for the number of files. `quota+ +%` adds the percentage used; `quota+ -f /scratch/public` shows one partition. The Linux `quota` command works only on `/home` and `/data`.

2. Delete or archive files on any partition where `Used` is close to `Limit` or `Files` is close to its `Limit`.

!!! warning "Jobs fail when a partition reaches its hard limit"

    Every write to that partition fails, including the log file of a running job. Free space before submitting more jobs.

A warning email goes out when your usage passes 95% of a quota; see [Warning emails](../jobs/efficiency.md#disk-quota-over-95). Above the hard limit, jobs that write to the partition fail.

## See how full a partition is

```console
$ module load tools/local
$ disk-usage -d all+
Filesystem                                Size     Used    Avail Capacity  Mounted on
netapp-fas83:/vol_home                  22.36T   14.45T    7.91T  65%/11%  /home
netapp-fas83-n02:/vol_data_public      332.50T   40.32T  292.18T  13%/2%   /data/public
gpfs02:public                          800.00T  349.32T  450.68T  44%/26%  /scratch/public
nas1:/mnt/pool/PROJECT                 175.00T   94.03T   80.97T  54%/1%   /store/PROJECT
```

`Capacity` is space used / files used. `disk-usage -d all+ -quotas` adds the default quotas of each partition. `df -h /scratch/public` gives the same for one partition without the tool. The [status page](../policies/status.md) plots the same figures over time under Disk Usage & Quota.

## Find what takes the space

1. Load `tools/local+` and run `dus-report` on the directory. It runs `du`, which takes minutes on a large tree, and lists the biggest subdirectories:

    ```console
    $ module load tools/local+
    $ dus-report /scratch/genomics/USERNAME
     612.372 GB            /scratch/genomics/USERNAME
                           capac.   14.000 TB (4% full), avail.   13.388 TB
     447.026 GB  73.00 %   /scratch/genomics/USERNAME/project-a
     308.076 GB  50.31 %   /scratch/genomics/USERNAME/project-a/v4
     138.950 GB  22.69 %   /scratch/genomics/USERNAME/project-a/vX
    report in /tmp/dus.scratch.genomics.USERNAME.USERNAME
    ```

2. Rerun on the saved report to see smaller directories without running `du` again:

    ```console
    $ dus-report -n 999 -pc 1 /tmp/dus.scratch.genomics.USERNAME.USERNAME
    ```

    `-pc 1` lists everything down to 1% of the total; `-n` caps the number of lines.

`du -sh dir/` gives the size of one directory. `quota+` is available in every session; `disk-usage` needs `module load tools/local` and `dus-report` needs `module load tools/local+`. `man quota+`, `disk-usage -help` and `dus-report -help` list their options.

## Reduce your usage

1. Delete input and intermediate files from finished jobs.
2. Compress large files that are not being read: `gzip FILE`.
3. Archive a directory of small files into one file, then delete the directory:

    ```bash
    tar -czf project-a.tgz project-a/
    rm -rf project-a/
    ```

    This frees inodes as well as space. `tar -xf project-a.tgz` unpacks it.

4. Move data that is finished with off Hydra; see [Data transfer](../data-transfer/index.md).

On `/data` and `/home`, space from deleted files is not freed until the snapshots holding them age out (2 and 4 weeks); see [Recover a file from a snapshot](snapshots.md). On `/scratch` it is freed at once.
