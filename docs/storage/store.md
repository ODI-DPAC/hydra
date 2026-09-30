# Use /store and the I/O queue

`/store` holds the project partitions on the NAS, a large and inexpensive near-line system that is not mounted on the compute nodes, so data moves between it and the partitions jobs can read. It holds data waiting to be processed or already processed, and it is not backed up. [SI-HPC@si.edu](mailto:SI-HPC@si.edu) sets up the groups that have a `/store` partition.

!!! note "`/store/public` is being phased out"

    `/store/public` is no longer available. Use `/data/public`. A cloud-based cold-storage service is being evaluated as the replacement.

`/store` is mounted on the login nodes, the head node and the interactive nodes. A job on any other node cannot see it, so you copy data from `/store` to `/scratch` or `/data` before a job uses it, and copy it back afterwards.

!!! warning "`/store` is not mounted on the compute nodes"

    A job that opens a path under `/store` fails. Copy the data to `/scratch` or `/data` first, on a login node or with an I/O job.

## Copy data on a login node or in a qrsh session

For a small copy, run `cp` or `rsync` on a login node, or under `qrsh` for anything that takes more than a few minutes:

```console
$ rsync -a /store/PROJECT/USERNAME/run-12/ /scratch/genomics/USERNAME/run-12/
```

The login-node limits apply (see [Warning emails](../jobs/efficiency.md#high-cpu-use-on-a-login-node)), and a `qrsh` session ends after 24 hours.

## Copy data as an I/O job

Large or repeated copies run as jobs in the I/O queue, `lTIO.sq`, which runs on the interactive nodes. An I/O job can run for 72 hours but use only 12 hours of CPU and 8 GB per slot. One user may run eight I/O jobs at once, with up to 8 slots in total.

1. Write a job file that requests the queue with `-q lTIO.sq -l ioq`:

    ```sh title="getData.job"
    #$ -S /bin/sh
    #$ -N getData -o getData.log -cwd -j y
    #$ -q lTIO.sq -l ioq
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    rsync -a /store/PROJECT/USERNAME/run-12/ /scratch/genomics/USERNAME/run-12/
    echo = `date` job $JOB_NAME done
    ```

2. Submit it:

    ```console
    $ qsub getData.job
    Your job 7437744 ("getData") has been submitted
    ```

3. Chain the analysis and the copy back so they start when the previous step finishes:

    ```console
    $ qsub -hold_jid 7437744 analyze.job
    Your job 7437745 ("analyze") has been submitted
    $ qsub -hold_jid 7437745 saveNClean.job
    Your job 7437746 ("saveNClean") has been submitted
    $ qstat+ +a%
    Total running (PEs/jobs) = 1/1, 2 queued (jobs) for user 'USERNAME'.
       jobID name                     stat     age nPEs      cpu% queue     node taskID
     7437744 getData                     r   00:01    1           lTIO.sq  8-31
     7437745 analyze                   hqw   00:00    1           sThC.q
     7437746 saveNClean                hqw   00:00    1           lTIO.sq
    ```

    `hqw` is a job waiting on a hold. `qchain getData.job analyze.job saveNClean.job` submits the three with the holds set; see [Run jobs in sequence](../jobs/submit.md#run-jobs-in-sequence).

`/store` snapshots and quotas are on the [Filesystems](filesystems.md) page. `quota+` shows your `/store` usage, which the Linux `quota` command does not. Recovering a file from a `/store` snapshot is under [Recover a file from a snapshot](snapshots.md#recover-a-file-on-store).

## Further reading

- [Filesystems](filesystems.md) for the `/store` partitions, their quotas and snapshots
- [Queues](../jobs/queues.md) for the I/O queue's limits
- [Globus](../data-transfer/globus.md) for moving data between `/store` and other institutions
