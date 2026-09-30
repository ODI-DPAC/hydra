# Warning emails

Automated checks watch the login nodes, running jobs and the disks, and email you when something you own is outside the limits. The mail goes to the address in your `~/.forward` file on Hydra. The [usage policies](../policies/usage.md) state the thresholds and require you to act on the warnings. We kill jobs that are not corrected.

| Subject | Trigger | Check |
|---|---|---|
| `Process N priority was lowered on hydra-login0X.si.edu` | a process on a login node above 45% CPU for 20 min | continuous |
| `Process N was killed on hydra-login0X.si.edu` | a login-node process above 85% CPU or 55% memory | continuous |
| `Your inefficient job(s) on Hydra` | jobs using under 33% of their requested CPUs | weekly |
| `You have N running job(s) that use almost no CPU cycles: "hosed"` | jobs under 10% efficiency after 36 h | daily |
| `Your oversubscribed job(s) on Hydra` | jobs using over 133% of their requested CPUs | weekly |
| `Memory Over-Reservation Warning` | high-memory jobs older than 12 h that reserved over 2.5× what they use | Tuesday and Friday |
| `Warning: your disk usage is above 95% of your quota` | your usage over 95% of a quota | daily |
| `Warning: disk usage check found N disk(s) with %Use or %IUse >= 95%` | a disk you have files on is over 95% full | daily |



## High CPU use on a login node

The login nodes are for editing, compiling, short tests, transfers and submitting jobs. A process that runs on one for more than 20 minutes at more than 45% CPU has its priority lowered (`renice +5`), and this happens twice. A process that reaches 85% CPU or 55% of the node's memory gets `kill -9`.

```text
Subject: Process 1259315 priority was lowered on hydra-login01.si.edu

Your command '/process/causing/high-CPU' (PID=1259315 on hydra-login01.si.edu) priority was lowered (renice +5) because:
    used TIME = 26.6 > 20 min
    used %CPU = 98.4 > 45 %
Remember: jobs/long computations should be submitted to a queue, or run in the interactive queue, not on a login node.
```

Stop the process and run it as a [job](submit.md) or in an [interactive session](../interactive/qrsh.md). These programs commonly trigger it:

- Analyses: submit them as jobs or run them under `qrsh`.
- `conda`: the "solving environment" step uses a full CPU. Run `conda` under `qrsh`, use `mamba`, and install into a new environment rather than modifying an existing one. See [Python and conda](../software/python.md).
- `gzip`, `zip`, `tar`: run them under `qrsh` or as a job.
- File transfers: some transfer programs use a full CPU. Email [SI-HPC@si.edu](mailto:SI-HPC@si.edu) (SAO users: [hpc@cfa.harvard.edu](mailto:hpc@cfa.harvard.edu)) for alternatives.

After a kill, check the process's output. A transfer may have left partial files; a `tar` archive being written is incomplete and corrupt.

## Inefficient jobs

A job is inefficient when its CPU use, divided by its age and by the number of slots requested, is under 33%. The weekly mail lists your inefficient jobs of the past seven days, running or finished, with the CPU-days each wasted, and shows the command that produced the report:

```console
$ module load tools/local
$ check-qlogs ineff -from -7d -user $USER
```

| Column | Meaning |
|---|---|
| `age` | how long the job has run, as `HH:MM` or `+DD:HH` |
| `nPEs` | slots requested |
| `cpu%` | the share of those slots in use; 50% means half the requested CPUs were busy on average |
| `unused CPUs` | CPU-days requested and not used |

A `cpu%` near `100/nPEs` means the program ran on one CPU because the thread or process count was not passed to it. Check the program's option for the number of threads and set it from `$NSLOTS`, as shown under [Submit a parallel job](parallel.md). Programs whose CPU use varies by stage, as in pipelines where only some steps are parallel, also show low efficiency. Split such pipelines into [jobs run in sequence](submit.md#run-jobs-in-sequence) that each request what they use.

Correct the request in the next jobs you submit. A running job does not need to be deleted for this warning alone. When the cluster load is over 70%, users with many inefficient jobs have jobs killed automatically down to 100 unused slots per user.

## Hosed jobs

A daily check flags jobs that have run for more than 36 hours at under 10% efficiency:

```text
The following job is running but using almost no CPU cycles i.e.: efficiency (CPU/age) < 10% and age > 36hr
   jobID     name   user     age  nPEs   cpu%   queue   node   taskID
 1234570     job4   USER   +3:13    10   9.9%  lThM.q  64-17
```

Either the program has stalled after doing some work, in which case kill it with `qdel`, or it is running on one CPU of the ten requested. In the example above, `cpu%` is 9.9 against a `100/nPEs` of 10. Reply to [SI-HPC-Admin@si.edu](mailto:SI-HPC-Admin@si.edu) within 24 hours to say whether the job should be killed.

## Oversubscribed jobs

A job is oversubscribed when it uses more than 133% of the CPUs it requested. It slows every other job on the node. The weekly mail lists such jobs with the excess CPU-days each used, from `check-qlogs osub -from -7d -user $USER`.

The usual cause is a program that uses every CPU on the node unless told otherwise. Pass `$NSLOTS` to its thread option, or request the slots it uses with `-pe mthread N`. Kill an oversubscribed job that will run for more than another 24 hours and resubmit it with the correct request. Reply to [SI-HPC-Admin@si.edu](mailto:SI-HPC-Admin@si.edu) within 24 hours. Administrators kill oversubscribed jobs when the cluster is busy.

## Memory over-reservation

Twice a week a check compares each job in the high-memory queues with the memory it reserved with `mres`. A job older than 12 hours that has reserved more than 2.5 times its peak use (`maxvmem`) triggers the warning. The mail shows the `check-memres -details -u USERNAME` report with the ratio for each job.

Reserved memory that is not used is unavailable to every other high-memory job. Read `maxvmem` from `qacct -j JOBID` or `qacct+` when the job finishes, since memory use varies during a run, and set the next reservation from it. See [Reserve memory](request-resources.md#reserve-memory).

## Disk quota over 95%

The mail lists each filesystem where your space or file count is above 95% of your quota, marked `***` where it is at or above 100%. Writes fail once you reach a quota. Delete or move files, and consolidate large numbers of small files into an archive. See [Quotas](../storage/quotas.md).

## A disk over 95% full

The mail lists a filesystem that is over 95% full, or over 95% of its inodes, and the top users on it. You receive it because you have files there. Delete or move what you no longer need. See [Storage](../storage/index.md).
