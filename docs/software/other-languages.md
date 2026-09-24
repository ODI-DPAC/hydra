# Julia, MATLAB, IDL and Java

This page covers the four languages that need something Hydra-specific to run in a job: a module, a runtime license, or a start-up option that keeps the program to the memory and CPUs the job requested.

## Julia

```console
$ module load tools/julia
$ module load tools/julia/1.6.3
```

`module -t avail 2>&1 | grep julia` lists the versions, 1.2.0 to 1.12.1; the default is 1.10.2. `module help tools/julia` describes the build. In a job that requested `-pe mthread N`, start Julia with `julia --threads $NSLOTS`.

## MATLAB

MATLAB itself is not installed: there is no MATLAB license on Hydra. The MATLAB Runtime is, so a MATLAB program compiled elsewhere with the MATLAB Compiler runs here.

1. Compile the program with MATLAB Compiler on a machine that has it, for the runtime version you will load.
2. In the job file, load the matching runtime (`module load matlab/R2025b`) and start the compiled program through the launcher script the compiler produced. The module sets the runtime location the launcher needs; `~hpc/examples/matlab/README` shows a complete job.

`module -t avail 2>&1 | grep matlab` lists the runtimes, R2014a to R2025b; `matlab/rt` is the default.

## IDL

Hydra has 5 interactive IDL licenses and 128 runtime licenses, for IDL 8.7 to 9.2. The interactive licenses are for preparing and checking code on a login node; jobs use the runtime licenses, which the scheduler counts (see [Resource limits](../jobs/limits.md)).

1. Compile the procedure and everything it calls into a save file, on a login node:

    ```console
    $ module load idl/rt
    $ idl
    IDL> .run reduce
    IDL> resolve_all
    IDL> save, /routine, file='reduce.sav'
    ```

    The save file is a snapshot: recompile after every change to the code. Its name must match the top-level procedure.

2. Submit a job that requests a runtime license with `-l idlrt=1` and runs the save file with `-rt`:

    ```sh title="reduce.job"
    #$ -S /bin/sh
    #$ -N reduce -cwd -j y -o reduce.log
    #$ -l idlrt=1
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    module load idl/rt
    idl -rt=reduce.sav
    echo = `date` job $JOB_NAME done
    ```

A procedure started with `-rt` takes no arguments. Pass parameters on standard input instead, and read them in the procedure when `n_params()` is zero:

```sh
idl -rt=make_my_model.sav << EOF
5943.
124.
sun
EOF
```

```idl title="make_my_model.pro"
pro make_my_model, temperature, density, name
  if n_params() eq 0 then begin
    temperature = 0.D0
    density = 0.D0
    name = ''
    read, temperature
    read, density
    read, name
  endif
  ; the computation goes here
end
```

!!! warning "Limit IDL to the CPUs the job requested"

    IDL starts as many threads as the node has CPUs. Put `CPU, TPOOL_NTHREADS = 1` at the top of the procedure for a serial job, or set it to the slot count in a job that requested `-pe mthread N`.

`idl -rt=src/model` changes to `src` before running. Some IDL commands are refused in runtime mode; the IDL manual lists them. `qhost -F idlrt -h global` shows how many runtime licenses are free. `module -t avail 2>&1 | grep idl` lists the IDL versions.

FL, an open-source IDL-compatible interpreter with no license limits, is available as `tools/fl` and needs the same `CPU, TPOOL_NTHREADS` setting.

## Java

```console
$ module load tools/java          # default
$ module load tools/java/21
```

Versions 8, 17, 18 and 21 are installed. Java sizes its heap and thread pool for the whole node unless told otherwise, and a job without a heap limit fails with:

```text
Error occurred during initialization of VM
Could not reserve enough space for object heap
```

Start Java with an explicit heap limit that fits inside the job's memory reservation:

```sh
java -d64 -server -XX:MaxHeapSize=1g -jar program.jar
```

Java uses more than the heap; reserve memory for the job above `MaxHeapSize` (see [Reserve memory](../jobs/request-resources.md#reserve-memory)). Oracle's documentation at <https://docs.oracle.com/en/java/javase/> lists the options.
