# Monitor and manage jobs

Once a job is submitted, you watch it with `qstat`, change it with `qalter`, delete it with `qdel`, and read what it used with `qacct` after it finishes. You can also look at one node or at the whole cluster. If you need the full list of options and output fields, see [Monitoring tools](tools.md).

## Check on a job

1. List your jobs:

    ```console
    $ qstat
    job-ID     prior   name       user         state submit/start at     queue                          jclass                         slots ja-task-ID
    ------------------------------------------------------------------------------------------------------------------------------------------------
      15503722 0.50500 model      USERNAME     r     10/03/2026 16:14:03 sThC.q@compute-93-04.cm.cluste                                    1 1
      15503722 0.50500 model      USERNAME     r     10/03/2026 16:14:03 sThC.q@compute-65-03.cm.cluste                                    1 2
      15503722 0.00000 model      USERNAME     qw    10/03/2026 16:14:02                                                                   1 3-40:1
    ```

    This is a job array with two tasks running and tasks 3 to 40 waiting. `r` is running, `qw` is waiting, `Eqw` is waiting in error and will not run. The [state table](tools.md#job-states) has the rest. `qstat -s r` shows only running jobs, `-s p` only pending, `-g d` one line per array task.

2. For a running job, see its age and how much of its requested CPU it uses:

    ```console
    $ qstat+ +r%
    ```

    A `cpu%` near 100 means the job uses every slot it requested. A value near `100/NSLOTS` means it runs on one CPU and ignores the rest. `qstat+ +rr%` adds memory and I/O.

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

    `grep rax` keeps the jobs whose name contains `rax`. `-s r` or `-s p` on `qstat` limits the list to running or pending jobs.

## Change a waiting job

`qalter` changes most properties of a job in `qw`, and a few of a running job.

```console
$ qalter -q mThC.q JOBID          # move to another queue
$ qalter -o run-3.log JOBID       # rename the output file
$ qalter -m abe JOBID             # change email notification
$ qalter -l s_cpu=240::,mres=2G,h_data=2G,h_vmem=2G JOBID   # change the CPU time, repeating the memory request
```

!!! warning "`qalter -l` replaces the whole resource request"

    A job submitted with `-l mres=2G,h_data=2G,h_vmem=2G` and altered with `qalter -l s_cpu=1::` is left with `s_cpu` alone. Its memory request is gone. Give `qalter -l` every resource the job needs, and check the result under `hard_resource_list` in `qstat -j JOBID`. `-mods` and `-clears` change or remove a single entry, as `man qalter` describes.

## Check a finished job

Read the accounting record after every new kind of job and set the memory and CPU requests of the next jobs from it.

1. Print the record:

    ```console
    $ qacct -j JOBID
    ==============================================================
    qname                    sThC.q
    hostname                 compute-76-11.cm.cluster
    ...
    granted_pe               mthread
    slots                    4
    ...
    failed                   0
    exit_status              0
    ru_wallclock             9.219
    ...
    cpu                      36.362
    mem                      0.552
    ...
    maxvmem                  145.473M
    ```

    `qacct -j JOBID -t TASKID` reports one task of an array. `qacct+ -j JOBID` reads the same data from a database, faster for old jobs, with selectable fields.

2. Read `maxvmem` against the memory you reserved, `cpu` against `ru_wallclock × slots`, and `failed` and `exit_status` (both `0` when the job completed). [qacct fields](tools.md#qacct-fields) lists them.

3. Adjust the request. A job that used 6.3 GB with 32 GB reserved held more than 25 GB back from everyone else. A job whose `cpu` is a quarter of `ru_wallclock × slots` ran on one CPU of the four requested. In the record above, `cpu` is 36.4 s against 9.2 s × 4 slots, so all four slots were busy.

`qacct -d 3 -o $USER -j > qacct.log` saves every job of the past three days for filtering with `egrep`.

## Watch a high-memory job over time

A sampler records every job in the high-memory queues every five minutes.

1. Plot the memory and CPU of a job as a PNG:

    ```console
    $ module load gnuplot
    $ plot-qmemuse JOBID
    ```

    `plot-qmemuse JOBID.TASKID` plots one array task. `-o FILE` names the output, `-x` plots on screen over X11 instead.

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

    `rtop+ -50 64-05` shows 50 lines. `rpstree+ 64-05` shows the process tree.

## Check the state of the cluster

1. Slots in use, reserved and free in every queue:

    ```console
    $ qstat -g c
    CLUSTER QUEUE                   CQLOAD   USED    RES  AVAIL  TOTAL aoACDS  cdsuE
    --------------------------------------------------------------------------------
    all.q                             -nan      0      0      0      0      0      0
    lTIO.sq                           0.00      0      0     34     34      0      0
    lTWFM.sq                          0.00      0      0     18     18      0      0
    lTb2g.q                           0.23      0      0      2      2      0      0
    lTgpu.q                           0.00      0      0    104    104      0      0
    lThC.q                            0.16    308      0   4308   4616      0      0
    lThM.q                            0.16     77      0   4539   4616      0      0
    ...
    ```

    `qstat+ -gc` adds node counts and the percentage in use. `show-qslots` prints only the free slots, `qstat+ -es` lists empty slots, `qstat+ -down` lists nodes that are down, and `check-gpu-use` shows the GPUs.

2. One node, or a set of nodes:

    ```console
    $ qhost -h compute-64-02 compute-64-03      # CPUs, load, memory
    $ qhost -q -h compute-64-02                 # the queues on the node
    $ qhost -j -h compute-64-02                 # the jobs on the node
    $ qhost | egrep 'LOAD|e-6[45]'              # header plus the compute-64 and compute-65 nodes
    ```

    `qhost` takes no patterns. Filter with `egrep`.

The [status page](../policies/status.md) shows the same as graphs, with past usage and disk space.

## Further reading

- [Monitoring tools](tools.md) for every option and output field of `qstat`, `qstat+`, `qacct` and `qacct+`
- [Warning emails](efficiency.md) for the checks that run on your jobs and what the emails mean
- [Cluster status](../policies/status.md) for the live view of the queues and nodes
