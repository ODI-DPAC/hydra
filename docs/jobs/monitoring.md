# Monitor and manage jobs

This page covers watching a job, changing or deleting it, reading what it used after it finished, and looking at the nodes and the cluster. The commands and their output fields are listed under [Monitoring tools](tools.md).

## Check on a job

1. List your jobs:

    ```console
    $ qstat
    job-ID   prior   name   user      state submit/start at     queue                 slots
    ------------------------------------------------------------------------------------------
    8736123  0.50000 crunch USERNAME  r     09/23/2026 10:04:11 sThC.q@compute-64-11      1
    8736124  0.00000 model  USERNAME  qw    09/23/2026 10:05:32                           4
    ```

    `r` is running, `qw` is waiting, `Eqw` is waiting in error and will not run; the [state table](tools.md#job-states) has the rest. `qstat -s r` shows only running jobs, `-s p` only pending, `-g d` one line per array task.

2. For a running job, see its age and how much of its requested CPU it uses:

    ```console
    $ qstat+ +r%
    ```

    A `cpu%` near 100 means the job uses every slot it requested; near `100/NSLOTS`, it runs on one CPU and ignores the rest. `qstat+ +rr%` adds memory and I/O.

3. For a waiting job, ask why:

    ```console
    $ qstat -j JOBID
    ```

    The `scheduling info` lines at the end name the resource or quota it is waiting for. `qquota -u $USER` shows your usage against the [resource limits](limits.md).

4. For a job in `Eqw`, get the error, delete the job, fix the cause and resubmit:

    ```console
    $ qstat -explain E -j JOBID
    $ qdel JOBID
    ```

    The usual cause is a directory or file named in the job that does not exist.

## Delete a job

1. Delete one job, or all of yours:

    ```console
    $ qdel JOBID
    $ qdel -u $USER
    ```

2. To delete some of them, generate the commands from `qstat`, edit the list, run it:

    ```console
    $ qstat -u $USER | grep $USER | grep rax | awk '{print "qdel", $1}' > qdel.sh
    $ nano qdel.sh
    $ sh qdel.sh
    ```

    `grep rax` keeps the jobs whose name contains `rax`; `-s r` or `-s p` on `qstat` limits the list to running or pending jobs.

## Change a waiting job

`qalter` changes most properties of a job in `qw`, and a few of a running job.

```console
$ qalter -q mThC.q JOBID          # move to another queue
$ qalter -o run-3.log JOBID       # rename the output file
$ qalter -m abe JOBID             # change email notification
$ qalter -l s_cpu=240:: JOBID     # change the requested CPU time
```

## Check a finished job

Read the accounting record after every new kind of job and set the memory and CPU requests of the next jobs from it.

1. Print the record:

    ```console
    $ qacct -j JOBID
    ==============================================================
    qname        mThM.q
    hostname     compute-65-03
    ...
    granted_pe   mthread
    slots        8
    failed       0
    exit_status  0
    ru_wallclock 5187
    cpu          40912.512
    mem          61.207
    maxvmem      6.318G
    ```

    `qacct -j JOBID -t TASKID` reports one task of an array. `qacct+ -j JOBID` reads the same data from a database, faster for old jobs, with selectable fields.

2. Read `maxvmem` against the memory you reserved, `cpu` against `ru_wallclock × slots`, and `failed` and `exit_status` (both `0` when the job completed). The fields are listed under [qacct fields](tools.md#qacct-fields).

3. Adjust the request. A job that used 6.3 GB with 32 GB reserved held 25 GB back from everyone else; a job whose `cpu` is a quarter of `ru_wallclock × slots` ran on one CPU of the four requested.

`qacct -d 3 -o $USER -j > qacct.log` saves every job of the past three days for filtering with `egrep`.

## Watch a high-memory job over time

Jobs in the high-memory queues are sampled every five minutes.

1. Plot the memory and CPU of a job as a PNG:

    ```console
    $ module load gnuplot
    $ plot-qmemuse JOBID
    ```

    `plot-qmemuse JOBID.TASKID` plots one array task; `-o FILE` names the output, `-x` plots on screen over X11 instead.

2. View the PNG with `display FILE` over an X11 connection, or copy it to your computer.

`show-qmemuse JOBID` prints the same as text. `plot-qssduse` and `show-qssduse` do the same for local SSD use.

## Look at a job's processes on its node

1. Find the node:

    ```console
    $ qstat+ -nlist JOBID
    ```

2. Run `top` there:

    ```console
    $ rtop+ -u $USER 64-05
    ```

    `rtop+ -50 64-05` shows 50 lines; `rpstree+ 64-05` shows the process tree.

## Check the state of the cluster

1. Slots in use, reserved and free in every queue:

    ```console
    $ qstat -g c
    CLUSTER QUEUE                   CQLOAD   USED    RES  AVAIL  TOTAL aoACDS  cdsuE
    --------------------------------------------------------------------------------
    lTIO.sq                           0.00      0      0      8      8      0      0
    lThC.q                            0.38    634      0   4374   5008      0      0
    lThM.q                            0.37    390      0   4162   4552      0      0
    ...
    ```

    `qstat+ -gc` adds node counts and the percentage in use; `show-qslots` prints only the free slots; `qstat+ -es` lists empty slots and `qstat+ -down` nodes that are down; `check-gpu-use` shows the GPUs.

2. One node, or a set of nodes:

    ```console
    $ qhost -h compute-64-02 compute-64-03      # CPUs, load, memory
    $ qhost -q -h compute-64-02                 # the queues on the node
    $ qhost -j -h compute-64-02                 # the jobs on the node
    $ qhost | egrep 'LOAD|e-6[45]'              # header plus the compute-64 and compute-65 nodes
    ```

    `qhost` takes no patterns; filter with `egrep`.

The [status page](../policies/status.md) shows the same as graphs, with past usage and disk space.
