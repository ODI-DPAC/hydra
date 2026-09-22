# Login, head and compute nodes; network

5. [Storage Systems (Disks)](../storage/filesystems.md)


## Introduction


As of May 2024, `Hydra-7` consists of:


- one head node and two login nodes;
- ~70 compute nodes that adds up to ~6,000 CPUs & 8 GPUs, ~45 TB memory;
- a set of 10Gbps network switches, all the nodes are on 10GbE;
- an InfiniBand (IB) director switch (144 ports, expandable to 256, at 100Gbps)
- a 3 tiers storage (disks) configuration:
    - a two nodes NetApp controller (FAS8300) with 8 shelves (total ~900TB):
        - a dedicated device that provides disk space to the cluster, i.e. to all the nodes using NFS (10GbE).
    - a GPFS system with two dedicated NSDs (total ~2PB):
        - a high performance general parallel file system (GPFS, aka IBM Spectrum Scale), using the InfiniBand for I/O.
    - Two NAS systems for near-line storage (total ~1.7PB):
        - a slower, more cost-effective storage available only on some nodes.
- all the nodes (head, login and compute nodes) are connected to the IB switch (except two).

## Login and Head Nodes

### The Head Node: hydra-7.si.edu


- manages the cluster;
- runs the job scheduler (the Grid Engine, aka UGE); and
- starts jobs.


It should never be accessed by users, except if directed by support staff for special operations.


### The Login Nodes: hydra-login0[12].si.edu


- These are the computers available to the users to access the cluster:
    - they are currently 48 cores 128GB Dell R730 servers.
    - do not run your computations on the login nodes.


You can use either node, depending on the node load.

## Compute Nodes

The compute nodes are named `compute-NN-MM`, where NN and MM are two numbers.


- These are the nodes (aka servers, hosts) on which jobs are being run, by submitting jobs to the scheduler, via `qsub`.
- A couple of nodes are dedicated for
    - interactive use (`qrsh`), and
    - I/O queue (for access to `/store`).
- Do not `ssh` to the compute node to start any computation "*out of band*" (we'll find and terminate them).


As of May 2024, we have deployed some 70 compute nodes that adds up to ~6,000 CPUs, 8 GPUs, ~45 TB memory as follows;


| # | Cores/node | Mem/node | Model | Name | Note |
| --- | --- | --- | --- | --- | --- |
| 1 | 72 | 512GB | R750XA | `compute-50-??` | 4x L40s GPUs |
| 16 | 40 | 384GB | R640 | `compute-64-??` |  |
| 2 | 32 | 512GB | R640 | `compute-64-??` |  |
| 29 | 64 | 512GB | R6515 | `compute-65-??` |  |
| 5 | 128 | 756GB | R7525 | `compute-75-??` |  |
| 2 | 128 | 1,024GB | R7525 | `compute-75-??` |  |
| 2 | 192 | 1,536GB | R7625 | `compute-76-??` |  |
| 12 | 128 | 1,024GV | R7625 | `compute-76-??` |  |
| 2 | 20 | 128GB | R790 | `compute-79-??` | 2x GV100GL GPUs |
| 1 | 112 | 896GB | R840 | `compute-84-??` |  |
| 1 | 64 | 512GB | R930 | `compute-93-??` |  |
| 3 | 72 | 760GB | R930 | `compute-93-??` |  |
| 1 | 96 | 2,048GB | R930 | `compute-93-??` |  |

## Network: Ethernet and InfiniBand

All the nodes (i.e., the compute nodes, the login nodes, and the head node) are interconnected using not only the regular 10GbE network (Ethernet), but also via a high-speed, low latency, communication fabric, known as the InfiniBand (IB):


- The IB switch is capable of a 100Gbps transfer rate, although the older nodes have IB card capable of 40Gbps only.
- The GPFS storage use the Infiniband fabric for for its I/O.
- To use the IB for message passing (MPI) you must
    - build the executable the right way, and
    - specify that you want to use the IB in your job script.
    - We have modules to do precisely that.
- A MPI program will not use *by default* the IB for message passing - you need to build it *right* to make it use the IB.
