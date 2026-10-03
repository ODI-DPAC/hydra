# Submit a job array

A job array runs one job file many times, each run with a different task ID. For more than a handful of similar runs it replaces a loop of `qsub` commands. You submit one job file once, get one job ID, and the scheduler starts the tasks as slots become free.

## Submit an array

1. Write a job file that reads its task ID from `$SGE_TASK_ID`. `$TASK_ID` in a `#$` line gives each task its own log file:

    ```sh title="model.job"
    #$ -S /bin/sh
    #$ -N model-1k -cwd -j y -o model.$TASK_ID.log
    #$ -t 1-1000 -tc 100
    #
    echo + `date` $JOB_NAME started on $HOSTNAME in $QUEUE with jobID=$JOB_ID and taskID=$SGE_TASK_ID
    #
    ./model -id model.$SGE_TASK_ID
    #
    echo = `date` $JOB_NAME for taskID=$SGE_TASK_ID done.
    ```

    `-t 1-1000` runs tasks 1 to 1000. `-tc 100` runs at most 100 of them at once.

2. Submit it:

    ```console
    $ qsub model.job
    Your job-array 8736123.1-1000:1 ("model-1k") has been submitted
    ```

3. Watch the tasks:

    ```console
    $ qstat -g d
    job-ID   prior   name      user      state submit/start at     queue                 slots ja-task-ID
    -----------------------------------------------------------------------------------------------------
    8736123  0.50000 model-1k  USERNAME  r     09/23/2026 10:04:11 sThC.q@compute-64-11      1 1
    8736123  0.50000 model-1k  USERNAME  r     09/23/2026 10:04:11 sThC.q@compute-64-12      1 2
    ...
    8736123  0.00000 model-1k  USERNAME  qw    09/23/2026 10:04:01                           1 101-1000:1
    ```

4. Read a task's log, `model.123.log`, once it is done. `qacct -j 8736123 -t 123` reports on one task.

| `-t` value | Tasks |
|---|---|
| `-t 1-20` | 20 tasks, IDs 1 to 20 |
| `-t 10-30` | 21 tasks, IDs 10 to 30 |
| `-t 50-140:10` | 10 tasks, IDs 50, 60, ..., 140 |
| `-t 20` | one task, ID 20 |

An array has at most 10,000 tasks and counts as one job against the 2,500-job limit (see [Resource limits](limits.md)). `-t` combines with `-pe`, and each task then starts as a [parallel job](parallel.md) with the requested slots. Do not add `-m abe` to a large array.

## Turn the task ID into parameters

Most programs need more than an integer. Three ways to map the task ID to a run, each one line in the job file:

1. One input file per task, `input.1` to `input.1000`:

    ```sh
    ./domodel < input.$SGE_TASK_ID
    ```

    For zero-padded names such as `input.001`, format the ID first:

    ```sh
    I=`echo $SGE_TASK_ID | awk '{printf "%3.3d", $1}'`
    ./domodel < input.$I
    ```

2. One line per task in a parameter file, `parameters-list.txt`:

    ```sh
    P=`awk "NR==$SGE_TASK_ID" parameters-list.txt`
    ./compute $P
    ```

3. A script of your own, `mytool`, that prints the parameters for a given ID:

    ```sh
    P=`./mytool $SGE_TASK_ID`
    ./compute $P
    ```

## Group short tasks into fewer jobs

Starting a task costs the scheduler time. An array of 5,000 three-minute tasks spends a quarter to a half of its time starting and tracking tasks. A step size gives each task a block of IDs to loop over.

1. Set `-t` with a step, and compute the block in the job file:

    ```sh title="domodel.job"
    #$ -S /bin/sh
    #$ -N model-1k20 -cwd -j y -o model-$TASK_ID-by-20.log
    #$ -t 1-1000:20
    #
    echo + `date` $JOB_NAME started on $HOSTNAME in $QUEUE with jobID=$JOB_ID
    #
    iFr=$SGE_TASK_ID
    iTo=$(( iFr + SGE_TASK_STEPSIZE - 1 ))
    if [ $iTo -gt $SGE_TASK_LAST ]; then iTo=$SGE_TASK_LAST; fi
    #
    echo running model.sh for taskIDs $iFr to $iTo
    i=$iFr
    while [ $i -le $iTo ]
    do
      ./model.sh $i > model-$i.log 2>&1
      i=$(( i + 1 ))
    done
    #
    echo = `date` $JOB_NAME for taskIDs $iFr to $iTo done.
    ```

2. Put one run in a script the loop calls:

    ```sh title="model.sh"
    #!/bin/sh
    TID=$1
    echo + `date` model.sh started for taskID=$TID
    ./model -id $TID
    echo = `date` model.sh for taskID=$TID done.
    ```

    ```bash
    chmod +x model.sh
    ```

3. Submit `domodel.job`. `-t 1-1000:20` starts 50 tasks with IDs 1, 21, 41, ..., 981, each running 20 models. The array finishes 1,000 models as 50 one-hour tasks instead of 1,000 three-minute ones.

Choose the step to match the run time of one model. A step of 1 is right when each model runs for hours.

## Further reading

- [Job script reference](job-scripts.md) for `-t`, `-tc` and `$SGE_TASK_ID`
- [Resource limits](limits.md) for how many tasks may run at once
- [Monitor and manage jobs](monitoring.md) for watching and deleting tasks
