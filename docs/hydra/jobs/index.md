# Running jobs

Hydra runs the Altair Grid Engine (UGE 8.8). You log in to `hydra-login01.si.edu` or `hydra-login02.si.edu`, write a job script, submit it with `qsub`, and the scheduler runs it on a compute node when resources are free.

Start here if you are new:

1. [How the cluster and scheduler work](concepts.md)
2. [Queues and how to choose one](queues.md)
3. [Writing a job script](job-scripts.md), or let the [QSub Generator](qsubgen.md) write it
4. [Monitoring jobs](monitoring.md)

Reference: [resource limits](limits.md), [serial, parallel and array jobs](job-types.md), [example scripts](examples.md), [hardware](../hardware/index.md).

If you received an automated email about your jobs, [job efficiency and warning emails](efficiency.md) explains each one.
