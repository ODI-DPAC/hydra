# GPUs

A job requests a GPU like any other resource, and the scheduler assigns it specific cards. This page shows you how to make the request, what your job is given, and how to build and watch GPU code. A GPU helps only a program written for NVIDIA GPUs, through CUDA or a framework built on it. A program that does not use a GPU gains nothing from a GPU queue.

Hydra has 8 GPUs on three nodes:

| Node | GPUs | GPU memory | CPU slots | Node memory |
|---|---|---|---|---|
| `compute-50-01` | 4 × NVIDIA L40S | 48 GB each | 64 | 503 GB |
| `compute-79-01`, `compute-79-02` | 2 × NVIDIA GV100 each | 32 GB each | 20 | 125 GB each |

## Request a GPU

1. Add the two required resources to the job. `gpu` admits the job to a GPU queue, and `ngpus=N` is the number of GPUs the job uses. The scheduler requires both; a job with `gpu` but no `ngpus` goes into `Eqw` and never runs.

    ```sh
    #$ -q sTgpu.q
    #$ -l gpu,ngpus=1
    ```

2. Add CPU slots on the same node if the program uses more than one CPU, with `-pe mthread Z`. Leave it off for a serial program. `ngpus` is per job, not per slot, so `-pe mthread 8 -l gpu,ngpus=2` is 8 CPUs and 2 GPUs.

3. Pick the queue by the time the job needs. `sTgpu.q` allows 7 hours of CPU time and 14 hours elapsed, `mTgpu.q` 6 and 12 days, and `lTgpu.q` 30 and 60 days, each with 64 GB resident and 128 GB virtual memory per slot. Memory limits multiply by `Z`, and the GV100 nodes have 125 GB in total, so a large per-slot request with several slots fits only on `compute-50-01`.

4. To require a specific card, add `gpuarch`:

    ```sh
    #$ -l gpu,ngpus=1,gpuarch=L40S
    ```

    Leave it off otherwise; the job then takes whichever GPU is free first.

A complete job file is:

```sh title="gpu.job"
#$ -S /bin/sh
#$ -N gpu -cwd -j y -o gpu.log
#$ -q sTgpu.q
#$ -pe mthread 4
#$ -l gpu,ngpus=1
#$ -l mres=32G,h_data=8G,h_vmem=8G
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + GPUs: $SGE_HGR_GPUS, CUDA_VISIBLE_DEVICES=$CUDA_VISIBLE_DEVICES
module load nvidia
./julia-set -threads $NSLOTS
echo = `date` job $JOB_NAME done
```

For an interactive session with a GPU, in the `qgpu.iq` queue (12 h CPU, 24 h elapsed):

```console
$ qrsh -l gpu,ngpus=1
```

!!! warning "`ngpu` without an s is the old resource; delete it"

    Old job files may request `num_gpu` or its alias `ngpu`. That resource does nothing and is on its way out; once we remove it, the scheduler rejects a job that still names it with `unknown resource`. `ngpus`, with an s, is the current one. Delete `num_gpu=…` or `ngpu=…` from the `-l` list and keep `ngpus=N`; if a file has both, delete only the one without the s.

## What the job gets

The scheduler assigns specific GPUs and sets two variables. `SGE_HGR_GPUS` holds the assigned devices as `gpu0 gpu1`, and `CUDA_VISIBLE_DEVICES` holds the same as `0,1`. CUDA programs and frameworks read `CUDA_VISIBLE_DEVICES` and see only those GPUs. The scheduler does not confine the job to them, so a program that addresses a GPU by absolute index instead of through `CUDA_VISIBLE_DEVICES` collides with another job's GPU.

The GPUs run in exclusive-process mode, in which each GPU serves one process at a time. A program that starts more processes than the job has GPUs fails with `all CUDA-capable devices are busy or unavailable`. Request CPU slots in proportion to the GPUs the job uses. A job that holds most of a node's CPUs with one GPU leaves the node's other GPUs unusable.

## Limits

| Queue | GPUs per user |
|---|---|
| `sTgpu.q` | 4 |
| `mTgpu.q` | 3 |
| `lTgpu.q` | 2 |
| `qgpu.iq` | 1 |
| all GPU queues together | 4 |

`qquota -u $USER` shows your use against these; the full set is under [Resource limits](../jobs/limits.md).

## Build GPU code

`module load nvidia` provides `nvcc` (CUDA C++) and the NVIDIA C, C++ and Fortran compilers, which also accept OpenACC directives and CUDA Fortran. `nvidia/YY/cuda` adds the full CUDA toolkit of release `YY`. `module -t avail 2>&1 | grep '^nvidia/'` lists them, 21.9 to 25.9.

The two GPU models take different drivers, which bounds the CUDA toolkit a program may be built with:

| Node | Driver | CUDA toolkit up to |
|---|---|---|
| `compute-50-01` (L40S) | 595.71.05 | 13.2 |
| `compute-79-01`, `-02` (GV100) | 550.54.15 | 12.4 |

CUDA 13 dropped the Volta architecture, so build code for the GV100 nodes with a CUDA 12.x toolkit. For one binary that runs on both cards, build with `-gencode arch=compute_70,code=sm_70 -gencode arch=compute_89,code=sm_89`. `~hpc/examples/gpu` holds CUDA, Python, IDL and MATLAB examples with their job files, and `~hpc/examples/gpu/cuda` the OpenACC and CUDA Fortran variants.

## Watch a GPU

These commands run on a login node:

```console
$ check-gpu-use                # GPUs in use and free on each GPU node
$ get-gpu-info 50-01 -d        # the GPUs on compute-50-01 and the processes using them
$ qstat -s r -F gpuarch,ngpus -q '*gpu*'   # card type and free GPUs per queue instance
```

On the GPU node itself, inside a job or a `qrsh` session, `nvidia-smi` reports the cards:

```console
$ nvidia-smi
$ nvidia-smi dmon -d 30 -s pucm -o DT          # utilization every 30 s
$ nvidia-smi --query-gpu=name,index,memory.used,utilization.gpu --format=csv -l 15
```

`man nvidia-smi` is on the login nodes. `qacct+ -j JOBID -show +gpus,gpu_usage` reports a finished job's GPU assignment and use (see [Monitoring tools](../jobs/tools.md#qacct)).

## Further reading

- [Queues](../jobs/queues.md) for the GPU queues' limits
- [Cluster hardware](../jobs/hardware.md) for the nodes and their GPUs
- [Examples](../jobs/examples.md) for the tested GPU jobs under `~hpc/examples/gpu`
