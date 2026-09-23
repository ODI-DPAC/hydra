# Running jobs

Hydra runs Grid Engine. You submit work as jobs from a login node with `qsub`; the scheduler runs them on the compute nodes.

How to:

- [Write and submit a job](submit.md): a first job file, arguments, email, the time limit, jobs in sequence
- [Request a queue, memory and CPUs](request-resources.md): pick the queue, reserve memory, restrict to nodes, check the request
- [Submit a job array](arrays.md): many similar runs from one job file
- [Submit a parallel job](parallel.md): multi-threaded, MPI and hybrid jobs
- [Monitor and manage jobs](monitoring.md): `qstat`, `qdel`, `qalter`, `qacct`, nodes and cluster state
- [QSub Generator](qsubgen.md): a web form that writes a job file

Reference:

- [How the scheduler works](concepts.md): nodes, queues, limits, the rules for a shared cluster
- [Queues](queues.md): time classes, queue sets, host groups, CPU architectures
- [Job script reference](job-scripts.md): options, precedence, variables, signals, PEs, MPI modules
- [Resource limits](limits.md): slots, jobs, GPUs and memory one user may hold
- [Monitoring tools](tools.md): job states, `qstat+`, `qacct` fields, `qacct+`, the Hydra tools
- [Warning emails](efficiency.md): each automated warning and what to do
- [Examples](examples.md): the worked examples under `~hpc/examples`
- [Cluster hardware](../hardware/index.md): nodes, network, the hardware behind each queue

Interactive sessions on a compute node are under [Interactive Use](../interactive/index.md).
