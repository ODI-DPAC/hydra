# Queues

Every job runs in a queue, and each queue limits CPU time, elapsed time and memory per CPU. The scheduler selects a queue from the resources a job requests unless the job names one with `-q`; with no options a job runs in `sThC.q`. The default Grid Engine queue `all.q` exists but has no slots. If you are deciding which queue to use, see [Request a queue, memory and CPUs](request-resources.md). If you want to know which nodes and how many slots stand behind each queue, see [Cluster hardware](hardware.md).

## Time classes

The high-CPU, high-memory and GPU queues each come in four time classes, named by the first letter of the queue.

| Class | Letter | Soft CPU time per slot | Soft elapsed time |
|---|---|---|---|
| short | `s` | 7 h | 14 h |
| medium | `m` | 6 d | 12 d |
| long | `l` | 30 d | 60 d |
| unlimited | `u` | none | none |

The hard limits are 15 minutes longer than the soft ones. At a soft limit the scheduler signals the job; at the hard limit it kills the job. For a parallel job the scheduler multiplies the CPU limit by the number of slots and leaves the elapsed limit alone.

## Queue sets

| Queues | Memory per slot, resident / virtual | Parallel environments | For | Required option |
|---|---|---|---|---|
| `sThC.q` `mThC.q` `lThC.q` `uThC.q` | 8 GB / 64 GB | `mthread`, `orte`, `ompi`, `mpich`, `hN` | serial or parallel jobs needing less than 8 GB per CPU | `-l lopri` for `uThC.q` |
| `sThM.q` `mThM.q` `lThM.q` `uThM.q` | 450 GB / 900 GB | `mthread` | jobs needing 8 GB to 450 GB per CPU | `-l himem`; `-l lopri` for `uThM.q` |
| `uTxlM.rq` | 2 TB / 2 TB | `mthread` | jobs needing more than 450 GB; approved users only | `-l himem` |
| `sTgpu.q` `mTgpu.q` `lTgpu.q` | 64 GB / 128 GB | `mthread` | jobs that use a GPU | `-l gpu,ngpus=N` |
| `qrsh.iq` | 8 GB / 64 GB | `mthread` | interactive sessions; 12 h CPU, 24 h elapsed | started with `qrsh` |
| `qgpu.iq` | 64 GB / 128 GB | `mthread` | interactive sessions with a GPU | `qrsh -l gpu,ngpus=N` |
| `lTIO.sq` | 8 GB / 64 GB | `mthread` | jobs that read or write `/store`; 12 h CPU, 72 h elapsed | `-q lTIO.sq -l ioq` |
| `lTWFM.sq` | 8 GB / 64 GB | `mthread` | a workflow manager that submits jobs; 6 d CPU, 30 d elapsed, 2 slots | `-q lTWFM.sq -l wfmq` |

Memory limits are per slot: a job with `-pe mthread 4` in a high-CPU queue may use 4 × 8 GB. Only the high-CPU queues run multi-node (MPI and hybrid) jobs; in every other queue a parallel job fits on one node.

[qrsh sessions](../interactive/qrsh.md) describes the interactive queues, [Use /store and the I/O queue](../storage/store.md) the I/O queue, and [GPUs](../software/gpus.md) the GPU queues. Jobs in `lTWFM.sq` run on the `@wfm-hosts` nodes, which can run `qsub`; one such job per user at a time.

## Host groups

A host group is a named list of nodes. `-q QUEUE@@GROUP` restricts a job to the group; see [Restrict the job to certain nodes](request-resources.md#restrict-the-job-to-certain-nodes). `qconf -shgrpl` lists the groups; `qconf -shgrp @GROUP` lists a group's nodes.

| Host group | Nodes |
|---|---|
| `@all-hosts` | all nodes |
| `@hicpu-hosts` | high-CPU nodes |
| `@himem-hosts` | high-memory nodes, 512 GB per node |
| `@xlmem-hosts` | extra-large-memory nodes, 1 TB or more per node |
| `@io-hosts` | nodes in the I/O queue |
| `@wfm-hosts` | nodes in the workflow-manager queue |
| `@gpu-hosts` | nodes with GPUs |
| `@qrsh-hosts` | nodes in the interactive queue |
| `@himemx-hosts` | the largest-memory nodes |
| `@b2g-hosts` | the Blast2GO node |
| `@ssd-hosts` | nodes with a local SSD |
| `@ib-hosts` | nodes with InfiniBand |
| `@24c-hosts`, `@NNc-hosts` | nodes with NN CPUs, up to 192 |
| `@avx-hosts`, `@avx2-hosts` | nodes whose CPUs support AVX or AVX2 |

## CPU architectures

`-l cpu_arch=NAME` restricts a job to one architecture; `!NAME` excludes one; `A|B` allows either.

| Nodes | `cpu_arch` | CPU |
|---|---|---|
| `compute-50-*` | `icelake` | Intel Xeon (four L40S GPUs) |
| `compute-64-*` | `skylake` | Intel Xeon Gold 6148, 2.40 GHz |
| `compute-65-*` | `zen` | AMD EPYC 7713P 64-core, 1.94 GHz |
| `compute-75-*` | `zen` | AMD EPYC 7H12 64-core, 2.53 GHz |
| `compute-76-*` | `zen` | AMD EPYC 9654 and 9534 64-core |
| `compute-79-*` | `skylake` | Intel Xeon Silver 4114, 2.20 GHz |
| `compute-84-*` | `skylake` | Intel Xeon Platinum 8280, 2.70 GHz |
| `compute-93-*` | `haswell`, `broadwell` | Intel Xeon E7-8867 v3, 2.50 GHz; E7-8860 v4, 2.20 GHz |

## Resource value formats

| Resource | Format | Examples |
|---|---|---|
| memory | number and unit | `13.4G`, `100M` |
| CPU or elapsed time | `hours:minutes:seconds` | `100:00:00` or `100::` is 100 hours; `100` is 100 seconds |

A memory value with no unit is in bytes. `man sge_types` documents the formats.

## Query the queue configuration

```console
$ qconf -sql                          # queue names
$ qconf -sq sThC.q                    # one queue's configuration and limits
$ qconf -sq '?ThM.q' | egrep 'qname|s_cpu|s_rt'
$ qconf -spl                          # parallel environments
$ qconf -sp mthread                   # one PE
$ qconf -shgrpl                       # host groups
$ qconf -sc | egrep 'cpu_arch|gpu|himem|lopri|mres'   # complexes (the -l resources)
```

`man 5 queue_conf` and `man 5 sge_pe` explain the output.
