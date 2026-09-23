# Limits table

The nodes, slots and memory behind each queue set. These figures change with the hardware; the [Queues](../jobs/queues.md) page gives the per-job limits, and [Resource limits](../jobs/limits.md) the per-user limits.

| Queues | Nodes | Slots | CPUs per node | Memory | Note |
|---|---|---|---|---|---|
| `?ThC.q` | 60 | 5,000 | 40 to 128 | more than 4 GB per CPU | high-CPU queues |
| `?ThM.q` | 50 | 4,552 | 32 to 192 | more than 512 GB per node | high-memory queues |
| `uTxlM.rq` | 3 | 480 | 96 to 192 | more than 1 TB per node | extra-large-memory queue, restricted |
| `?Tgpu.q` | 3 | 8 GPUs | | | GPU queues; `-l gpu` |
| `lTIO.sq` | 2 | 8 | | | I/O queue for `/store` |
| `qrsh.iq` | 2 | 40 | | 256 GB per node | interactive queue; `qrsh` or `qlogin` |
| `qgpu.iq` | 3 | 8 GPUs | | | interactive GPU queue; `qrsh -l gpu` |

`?` stands for the time class: `s` (short), `m` (medium), `l` (long) or `u` (unlimited). The four queues of a set share the same nodes.

Check the current values with:

```bash
qstat -g c
qstat+ -gc
qhost
```

A request for resources that no node has, or that exceed a queue's limit, is rejected with `Unable to run job: error: no suitable queues.` Run `qsub -w v` or `qsub -verify` on the job file to see which resource; see [Check a request before submitting](../jobs/request-resources.md#check-a-request-before-submitting).
