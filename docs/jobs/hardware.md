# Cluster hardware

Hydra has 74 compute nodes, two login nodes and three storage systems, connected by Ethernet and InfiniBand. If you want to know which nodes a queue runs on or what a node has, the tables on this page answer that. For the live picture, `qhost` on a login node prints the node list and `qstat -g c` prints the slots per queue.

## Head and login nodes

| Node | Role |
|---|---|
| `hydra-7.si.edu` | head node: runs the scheduler and starts jobs. Do not log in to it. |
| `hydra-login01.si.edu`, `hydra-login02.si.edu` | login nodes: edit, compile, submit and monitor jobs, transfer data. 48 cores, 128 GB each; use either. |
| `hydra-globus01`, `hydra-globus02` | Globus endpoint nodes behind the Hydra collections; see [Globus](../data-transfer/globus.md). |

The login nodes slow, then [kill](efficiency.md#high-cpu-use-on-a-login-node), computations run on them.

## Compute nodes

74 nodes, 5,840 CPU cores, 49 TB of memory and 8 GPUs. Nodes are named `compute-NN-MM`; the first number groups a model. Jobs reach them only through the scheduler; see [How the scheduler works](concepts.md).

| Nodes | Count | Cores per node | Memory per node | CPU | Note |
|---|---|---|---|---|---|
| `compute-50-01` | 1 | 64 | 512 GB | Intel Xeon (`icelake`) | four NVIDIA L40S GPUs |
| `compute-64-03` to `-16` | 13 | 40 | 384 GB | Intel Xeon Gold 6148 (`skylake`) | |
| `compute-64-17`, `-18` | 2 | 32 | 512 GB | Intel Xeon Gold 6148 (`skylake`) | |
| `compute-65-02` to `-30` | 28 | 64 | 512 GB | AMD EPYC 7713P (`zen`) | |
| `compute-75-03` to `-07` | 5 | 128 | 768 GB | AMD EPYC 7H12 (`zen`) | |
| `compute-75-01`, `-02` | 2 | 128 | 1 TB | AMD EPYC 7H12 (`zen`) | |
| `compute-76-03` to `-14` | 12 | 128 | 1 TB | AMD EPYC 9654 and 9534 (`zen`) | |
| `compute-76-01`, `-02` | 2 | 192 | 1.5 TB | AMD EPYC 9654 (`zen`) | `-02` runs the [RStudio server](../interactive/rstudio.md) |
| `compute-79-01`, `-02` | 2 | 20 | 128 GB | Intel Xeon Silver 4114 (`skylake`) | two NVIDIA GV100 GPUs each |
| `compute-84-01` | 1 | 112 | 896 GB | Intel Xeon Platinum 8280 (`skylake`) | |
| `compute-93-01` | 1 | 64 | 512 GB | Intel Xeon E7 (`haswell`, `broadwell`) | |
| `compute-93-02` to `-04` | 3 | 72 | 768 GB | Intel Xeon E7 (`haswell`, `broadwell`) | |
| `compute-93-05` | 1 | 96 | 2 TB | Intel Xeon E7 (`haswell`, `broadwell`) | extra-large memory |
| `compute-93-06` | 1 | 56 | 3 TB | Intel Xeon E7 (`haswell`, `broadwell`) | extra-large memory |

The name in parentheses is the `cpu_arch` value for restricting a job to that architecture, as shown under [Restrict the job to certain nodes](request-resources.md#restrict-the-job-to-certain-nodes). A few nodes are set aside for [interactive sessions](../interactive/qrsh.md) and the [I/O queue](../storage/store.md). [GPUs](../software/gpus.md) describes the cards.

## Hardware behind each queue

Slots are from `qstat -g c`. A node serves several queues, so the same slots appear in more than one row.

| Queues | Slots | CPUs per node | Memory | Note |
|---|---|---|---|---|
| `sThC.q` `mThC.q` `lThC.q` `uThC.q` | 4,616 to 4,656 | 40 to 128 | more than 4 GB per CPU | high-CPU queues |
| `sThM.q` `mThM.q` `lThM.q` `uThM.q` | 4,616 to 5,064 | 32 to 192 | 512 GB or more per node | high-memory queues |
| `uTxlM.rq` | 536 | 96 to 192 | 1 TB or more per node | extra-large-memory queue, restricted |
| `sTgpu.q` `mTgpu.q` `lTgpu.q` | 104, with 8 GPUs | | | GPU queues; `-l gpu,ngpus=N` |
| `qgpu.iq` | 104, with 8 GPUs | | | interactive GPU queue; `qrsh -l gpu,ngpus=N` |
| `qrsh.iq` | 292 | | | interactive queue; `qrsh` |
| `lTIO.sq` | 34 | | | I/O queue for `/store` |
| `lTWFM.sq` | 18 | | | workflow-manager queue |

The per-job limits of each queue are under [Queues](queues.md) and the per-user limits under [Resource limits](limits.md).

## Network

All nodes are on 10 Gb Ethernet. The head, login and compute nodes are also on a 100 Gb InfiniBand director switch, which carries MPI traffic and I/O to `/scratch`.

## Storage systems

| System | Partitions | Access |
|---|---|---|
| NetApp FAS8300, two controllers, about 575 TB | `/home`, `/data` | all nodes, over NFS on Ethernet |
| GPFS, two NSD servers, about 3.2 PB | `/scratch` | all nodes, over InfiniBand |
| NAS, two systems, about 2.6 PB | `/store` | login, head, interactive and RStudio server nodes only |

The partitions, their quotas and retention rules are under [Filesystems](../storage/filesystems.md).
