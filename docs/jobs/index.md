# Running Jobs

Hydra runs Grid Engine. You submit work as jobs from a login node with `qsub`. The scheduler runs each one on the compute nodes and kills it if it exceeds the limits of its queue.

For a first job, [write and submit a job](submit.md), then [check on it](monitoring.md). Anything larger than the default (7 hours of CPU, 8 GB, one CPU) needs a [queue, memory or CPU request](request-resources.md). Many similar runs go in a [job array](arrays.md). Threaded, MPI and hybrid programs are [parallel jobs](parallel.md). The [QSub Generator](qsubgen.md) writes a job file from a web form.

!!! warning "Do not compute on the login nodes"

    The login nodes slow, then kill, any process that runs on them for more than a few minutes. Run it as a job, or under `qrsh` in an [interactive session](../interactive/qrsh.md). [Warning emails](efficiency.md#high-cpu-use-on-a-login-node) gives the thresholds.

The reference pages in the sidebar list the [queues](queues.md), the [job script options](job-scripts.md), the [per-user limits](limits.md), the [monitoring tools](tools.md) and the [warning emails](efficiency.md). [How the scheduler works](concepts.md) explains the pieces, including what changes if you know Slurm. Interactive sessions on a compute node are under [Interactive Use](../interactive/index.md).
