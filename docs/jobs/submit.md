# Write and submit a job

The simplest job runs a program on one CPU. It takes a job file, `qsub`, and an output file. Every other kind of job starts from the same file with more options. If you need more memory, CPUs or time, see [Request a queue, memory and CPUs](request-resources.md). If you have many similar runs, see [Submit a job array](arrays.md). If your program is threaded or uses MPI, see [Submit a parallel job](parallel.md).

## Submit a job

1. Change to the directory the job runs in, under `/scratch` or `/data`. The group directory under `/scratch` (`genomics` in the examples) is the one your welcome email names:

    ```bash
    cd /scratch/genomics/USERNAME/demo
    ```

2. Create the job file. The `#$` lines are options for `qsub`; the rest is a shell script.

    ```sh title="crunch.job"
    #$ -S /bin/sh
    #$ -N crunch -cwd -j y -o crunch.log
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    ./crunch
    echo = `date` job $JOB_NAME done
    ```

3. Submit it:

    ```console
    $ qsub crunch.job
    Your job 8736123 ("crunch") has been submitted
    ```

4. Check that it is queued or running:

    ```console
    $ qstat
    job-ID   prior   name   user      state submit/start at     queue          slots
    ------------------------------------------------------------------------------------
    8736123  0.50000 crunch USERNAME  r     09/23/2026 10:04:11 sThC.q@compute-64-11    1
    ```

5. When the job is gone from `qstat`, read its log:

    ```console
    $ cat crunch.log
    + Wed Sep 23 10:04:11 EDT 2026 job crunch started in sThC.q with jobID=8736123 on compute-64-11
    = Wed Sep 23 10:09:52 EDT 2026 job crunch done
    ```

The two `echo` lines record which node and queue the job ran in and when it started and finished. Keep them in every job file. Without `-cwd`, the job runs in your home directory. Without `-o` and `-j y`, its output goes to `~/crunch.oJOBID` and `~/crunch.eJOBID`. [Job script reference](job-scripts.md) lists every option.

With no queue or resource options the job runs in `sThC.q`, which allows 7 hours of CPU time and 8 GB of memory. Anything larger needs a [queue, memory or CPU request](request-resources.md).

## Pass arguments to the job

One job file serves many runs when the script reads its parameters from the command line. Anything after the file name on the `qsub` line reaches the script as `$1`, `$2`, and so on.

1. Use the arguments in the script:

    ```sh title="crunch.job"
    #$ -S /bin/sh
    #$ -N crunch -cwd -j y -o crunch.log
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    OPTIONS="-from $1 -to $2"
    echo starting crunch $OPTIONS
    ./crunch $OPTIONS
    echo = `date` job $JOB_NAME done
    ```

2. Submit each run with its own name and log file, so the runs do not overwrite each other:

    ```console
    $ qsub -N crunch-20-50 -o crunch-20-50.log crunch.job 20 50
    Your job 8736124 ("crunch-20-50") has been submitted
    $ qsub -N crunch-100-150 -o crunch-100-150.log crunch.job 100 150
    Your job 8736125 ("crunch-100-150") has been submitted
    ```

Options on the command line override the `#$` lines. For more than a handful of runs, use a [job array](arrays.md).

## Get email when the job ends

1. Add to the job file:

    ```sh
    #$ -m abe
    ```

    `b` mails when the job begins, `e` when it ends, `a` when it aborts; use any subset.

2. Mail goes to the address in your `~/.forward` file on Hydra. To send it elsewhere, add:

    ```sh
    #$ -M you@example.org
    ```

Do not request mail for every task of a large job array.

## Catch the time limit

Each queue has a soft and a hard time limit 15 minutes apart. At the soft limit the scheduler sends the job a signal. At the hard limit it kills the job. A Bourne-shell script can catch the signal and save its state.

1. Put a `trap` before the command that does the work:

    ```sh title="trap.job"
    #$ -S /bin/sh
    #$ -cwd -j y -N trap -o trap.log
    #
    warn()
    {
      echo @ `date` warning, received $1 signal.
    }
    trap "warn xcpu" SIGXCPU
    trap "warn usr1" SIGUSR1
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    ./crunch
    echo = `date` job $JOB_NAME done
    ```

2. Replace the `echo` in `warn` with whatever saves the state of the run.

The trap runs when the signal arrives, but the command already running continues until it exits. Put checkpointing inside the program where possible. `csh` scripts cannot catch signals; use `-S /bin/sh`. [Job script reference](job-scripts.md#signals-at-the-time-limits) lists the signals.

## Run jobs in sequence

`-hold_jid JOBID` holds a job until the named job has finished. Use it to chain steps that need different resources, so each step requests only what it uses.

1. Submit the first step:

    ```console
    $ qsub -N pre pre-process.job
    Your job 12345678 ("pre") has been submitted
    ```

2. Submit the next step held on the first:

    ```console
    $ qsub -hold_jid 12345678 -N main process.job
    Your job 12345679 ("main") has been submitted
    ```

3. `qstat` shows the held job in state `hqw` until the first finishes.

In a script, capture each job ID with `-terse`, which prints only the ID:

```sh title="chain.sh"
#!/bin/sh
parameter=$1
name=$2
jid1=`qsub -terse -N "pre-$name" pre-process.job $parameter`
jid2=`qsub -terse -hold_jid $jid1 -N "process-$name" process.job $parameter`
jid3=`qsub -terse -hold_jid $jid2 -N "post-$name" post-process.job $parameter`
echo submitted $jid1 $jid2 $jid3
```

`qchain`, in the `tools/local` module, adds the `-hold_jid` options for you. `qchain *.job` submits the matching job files in alphabetical order, each waiting for the previous one. Quote each argument to pass options to `qsub` and arguments to the scripts:

```bash
module load tools/local
qchain '-N start first.job 123' '-N crunch second.job 123' '-N post finish.job 123'
```

## Submit many jobs without exceeding the limit

One user may have 2,500 jobs queued at once (see [Resource limits](limits.md)). A script that submits more has to wait for its own jobs to finish.

1. Load the local tools and use `q-wait`, which pauses until jobs whose name contains a string have left the queue, or until fewer than a given number remain:

    ```console
    $ module load tools/local
    $ q-wait crunch                       # until no job named *crunch* is queued or running
    $ q-wait -N 125 -wait 3600 crunch     # until at most 125 remain, checking hourly
    ```

2. Or count with `qstat` in the submission script:

    ```sh
    NMAX=250
    while [ `qstat -u $USER | tail --lines=+3 | wc -l` -ge $NMAX ]
    do
      sleep 180
    done
    ```

    Add `-s p` to `qstat` to count only pending jobs.

A [job array](arrays.md) counts as one job, so an array of 10,000 tasks needs neither.

## Further reading

- [Job script reference](job-scripts.md) for every `#$` option, the variables the scheduler sets, and the signals at the time limits
- [Request a queue, memory and CPUs](request-resources.md) when the default queue is not enough
- [Monitor and manage jobs](monitoring.md) for what to do once the job is running
- [Examples](examples.md) for complete, tested job files under `~hpc/examples`
