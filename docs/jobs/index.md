# Running Jobs

Hydra runs Grid Engine. You submit work as jobs from a login node with `qsub`, and the scheduler runs each job on the compute nodes and kills it if it exceeds the limits of its queue.

If this is your first job, start with [Write and submit a job](submit.md), then [check on it](monitoring.md). If your job needs more than the default of 7 hours of CPU, 8 GB and one CPU, you request more under [Request a queue, memory and CPUs](request-resources.md). If you have many similar runs, submit them as a [job array](arrays.md). If your program is threaded or uses MPI, see [Submit a parallel job](parallel.md). If you would rather fill in a form than write a job file, the [QSub Generator](qsubgen.md) writes one for you.

!!! warning "Do not compute on the login nodes"

    The login nodes slow, then kill, any process that runs on them for more than a few minutes. Run it as a job, or under `qrsh` in an [interactive session](../interactive/qrsh.md). [Warning emails](efficiency.md#high-cpu-use-on-a-login-node) gives the thresholds.

When you need to look something up, the reference pages in the sidebar cover the [queues](queues.md), the [job script options](job-scripts.md), the [per-user limits](limits.md), the [monitoring tools](tools.md) and the [warning emails](efficiency.md). If you want to understand how the pieces fit, or you know Slurm and want the differences, read [How the scheduler works](concepts.md). For a shell or a notebook on a compute node, see [Interactive Use](../interactive/index.md).
