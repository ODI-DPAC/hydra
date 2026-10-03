# Submit a parallel job

A **parallel job** uses more than one CPU, as threads on one node, as MPI processes across nodes, or both. The program has to be written for one of those, and its documentation says which. A program that runs on one CPU is parallelized by running many copies as a [job array](arrays.md).

A parallel job requests a parallel environment (PE) and a number of slots with `-pe PE N` (`N-M` accepts a range) and reads the number it was given from `$NSLOTS`. Memory limits are per slot, so a job with N slots may use N times the queue's per-slot limit. Reserve it as described under [Reserve memory](request-resources.md#reserve-memory). Only the high-CPU queues run MPI and hybrid jobs. [Job script reference](job-scripts.md#parallel-environments) lists the PEs and MPI modules.

!!! warning "Tell the program how many CPUs it was given"

    `-pe` reserves slots. It does not make the program use them. Pass `$NSLOTS` to the program's thread option, set `OMP_NUM_THREADS=$NSLOTS`, or run `mpirun -np $NSLOTS`. A job that uses fewer or more CPUs than it requested triggers a [warning email](efficiency.md) and can be killed.

## Submit a multi-threaded job

1. Request `mthread` slots and pass `$NSLOTS` to the program. For a program with a thread option:

    ```sh title="demo.job"
    #$ -S /bin/sh
    #$ -cwd -j y -N demo -o demo.log
    #$ -pe mthread 32
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    echo + NSLOTS = $NSLOTS
    #
    module load tools/demo
    demo -threads $NSLOTS
    #
    echo = `date` job $JOB_NAME done
    ```

    For an OpenMP program, set the variable instead:

    ```sh title="hellomp.job"
    #$ -S /bin/sh
    #$ -cwd -j y -N hellomp -o hellomp.log
    #$ -pe mthread 32
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    echo + NSLOTS = $NSLOTS
    #
    module load nvidia
    export OMP_NUM_THREADS=$NSLOTS
    ./hellomp
    #
    echo = `date` job $JOB_NAME done
    ```

    For a program that reads the thread count from a parameter file, write it in with `sed`: `sed "s/MTHREADS/$NSLOTS/" gen-params > all-params`.

2. Submit, then check the log for the `NSLOTS` line and, once the job has run for a while, its CPU use:

    ```console
    $ qsub hellomp.job
    $ qstat+ +r%
    ```

    A `cpu%` near 100 means every slot is busy. A value near `100/NSLOTS` means the program is running on one CPU.

`~hpc/examples/openmp` has this example built with the GNU, Intel and NVIDIA compilers.

## Submit an MPI job

1. Load the MPI module the program was built with (see [MPI modules](job-scripts.md#mpi-modules)) and request the matching PE. That is `orte` for OpenMPI and for Intel MPI, `ompi` for NVIDIA's bundled OpenMPI, and `mpich` for MVAPICH.

2. Start the program with the `mpirun` the module defines and `-np $NSLOTS`. With OpenMPI:

    ```sh title="hello-orte.job"
    #$ -S /bin/sh
    #$ -cwd -j y -N hello -o hello.log
    #$ -pe orte 72
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    echo + NSLOTS = $NSLOTS distributed over:
    cat $PE_HOSTFILE
    #
    module load gcc/13.2/openmpi
    mpirun -np $NSLOTS ./hello
    #
    echo = `date` job $JOB_NAME done
    ```

    With MVAPICH, pass the machine file the scheduler writes to `$TMPDIR/machines`:

    ```sh title="hello-mpich.job"
    #$ -S /bin/sh
    #$ -cwd -j y -N hello -o hello.log
    #$ -pe mpich 72
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    echo using $NSLOTS slots on:
    sort $TMPDIR/machines | uniq -c
    #
    module load nvidia/24/mvapich
    mpirun -np $NSLOTS -machinefile $TMPDIR/machines ./hello
    #
    echo = `date` job $JOB_NAME done
    ```

    With NVIDIA's bundled OpenMPI (`nvidia/24/mpi` and `-pe ompi`), pass the host file the scheduler writes to `$TMPDIR/hostfile`:

    ```sh
    mpirun -np $NSLOTS -hostfile $TMPDIR/hostfile ./hello
    ```

3. Submit and read the log. The `cat $PE_HOSTFILE` or `uniq -c` line lists the nodes and the slots on each:

    ```text
    + Sat Oct 3 13:46:40 EDT 2026 job hello started in sThC.q with jobID=15503711 on compute-65-23
    + NSLOTS = 72 distributed over:
    compute-65-23.cm.cluster 55 sThC.q@compute-65-23.cm.cluster <NULL>
    compute-65-21.cm.cluster 17 sThC.q@compute-65-21.cm.cluster <NULL>
    Loading gcc/13.2/openmpi
      Loading requirement: gcc/13.2.0
    Hello world from process 19 of 72
    ...
    = Sat Oct 3 13:46:42 EDT 2026 job hello done
    ```

Do not call `mpirun` by a full path. The module defines `mpirun` for its own version. A mismatched `mpirun` gives unpredictable results. `~hpc/examples/mpi` holds a hello-world job for every compiler and implementation, described in its `README`.

If the log shows

```text
[proxy:0:0@compute-N-M.local] HYDU_create_process (./utils/launch/launch.c:75): execvp error on file CODE (No such file or directory)
```

`mpirun` could not find the executable `CODE`. Check the path, and that the file is on a filesystem the compute nodes mount.

## Submit a hybrid job

A hybrid job runs K MPI processes on K nodes, each with M threads, for N = K × M slots. The program must be written for it, usually MPI between processes and OpenMP within each.

1. Request the hybrid PE for M threads per node, `hM`, with N a multiple of M. `-pe h8 64` is 8 nodes with 8 slots each, and `-pe h12 48` is 4 nodes with 12 each.

2. Source the configuration file the scheduler writes before `mpirun`. It resets `NSLOTS` to K, sets `OMP_NUM_THREADS` to M, and rewrites the host file (`$HOSTFILE`, OpenMPI) and machine file (`$MACHINEFILE`, MVAPICH) to one entry per node. The `if` lets the same file run as an ordinary MPI job when no hybrid PE was requested:

    ```sh title="hybrid.job"
    #$ -S /bin/sh
    #$ -q mThC.q -pe h8 64
    #$ -N hybrid -o hybrid.log -cwd -j y
    #
    echo $JOB_NAME started `date` on $HOSTNAME in $QUEUE jobID=$JOB_ID
    #
    if [ -e $TMPDIR/set-hybrid-config ]
    then
      . $TMPDIR/set-hybrid-config
    fi
    #
    module load gcc/13.2/openmpi
    mpirun -np $NSLOTS -hostfile $HOSTFILE ./hybrid
    #
    echo `date` $JOB_NAME done.
    ```

3. Submit and read the log. It begins with:

    ```text
    --------------- hybrid_start 1.0/1 ---------------
    hybrid_start: remember to 'source $TMPDIR/set-hybrid-config' to properly setup your env
    --------------------------------------------------
    ...
    PE=h8 NSLOTS=8 OMP_NUM_THREADS=8
    ```

    The last line appears only after the configuration file has been sourced.

`~hpc/examples/hybrid` builds and runs a hello-world hybrid program with the GNU, Intel and NVIDIA compilers, with OpenMPI and MVAPICH.

## Further reading

- [Compilers, libraries and MPI](../software/compilers.md) for building a program against the cluster's MPI
- [Job script reference](job-scripts.md#parallel-environments) for the full list of parallel environments
- [GPUs](../software/gpus.md) for jobs that use a GPU
- [Examples](examples.md) for tested OpenMP, MPI and hybrid jobs under `~hpc/examples`
