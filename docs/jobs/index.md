# Running Jobs

Hydra runs Grid Engine. You submit work as jobs from a login node with `qsub`, and the scheduler runs each job on the compute nodes and kills it if it exceeds the limits of its queue.

Start with the page that fits your job:

- For a first job, [Write and submit a job](submit.md), then [check on it](monitoring.md).
- For more than the default of 7 hours of CPU, 8 GB and one CPU, [Request a queue, memory and CPUs](request-resources.md).
- For many similar runs, [Submit a job array](arrays.md).
- For a threaded or MPI program, [Submit a parallel job](parallel.md).
- For a form in place of a hand-written job file, the [QSub Generator](qsubgen.md).

!!! warning "Do not compute on the login nodes"

    The login nodes slow, then kill, a process that computes on them. Run it as a job, or under `qrsh` in an [interactive session](../interactive/qrsh.md). [Warning emails](efficiency.md#high-cpu-use-on-a-login-node) gives the thresholds.

When you need to look something up, the reference pages in the sidebar cover the [queues](queues.md), the [job script options](job-scripts.md), the [per-user limits](limits.md), the [monitoring tools](tools.md) and the [warning emails](efficiency.md). If you want to understand how the pieces fit, or you know Slurm and want the differences, read [How the scheduler works](concepts.md). For a shell or a notebook on a compute node, see [Interactive Use](../interactive/index.md).
