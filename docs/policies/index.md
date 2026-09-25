# Policies & Support

Hydra is a shared system. We require every user to follow the [usage policies](usage.md); please read them before you begin. We also provide instructions for [citing Hydra](citing.md) in your publications.

[Cluster status](status.md) explains where to find the live view of the queues and disks. If you receive a warning email about your jobs, [Warning emails](../jobs/efficiency.md) explains what it means and what to do.

## Getting help

Email [SI-HPC@si.edu](mailto:SI-HPC@si.edu). Include the following, so that we can reproduce the problem:

- your Hydra username
- the job ID, from `qstat` for a running job or `qacct+ -j JOBID` for a finished one
- the full command or the job file, and the error message copied exactly
- what you expected to happen instead

Two things go to [SI-HPC-Admin@si.edu](mailto:SI-HPC-Admin@si.edu) instead: replies to warning emails about hosed or oversubscribed jobs (see [Usage policies](usage.md#oversubscribed-and-inefficient-jobs)), and requests to unlock an account whose password expired more than 14 days ago (see [Logging in and passwords](../getting-started/login.md)). For a new account or VPN access, see [Requesting an account](../getting-started/account.md).

## Before you write

Three questions come up often enough to answer here.

**Is a package installed, and how do I see the modules?** [Installed modules](../software/module-list.md) lists every `bio/` and `tools/` package. `module avail` on a login node lists everything. See [Find and load software](../software/modules.md).

**My job finished but I cannot find its output.** Without `-cwd` in the job file, the job runs in your home directory and writes its log there. See [Write and submit a job](../jobs/submit.md).

**Can I work interactively?** Yes, on a compute node through `qrsh`, within the limits of the interactive queue. See [Start an interactive session](../interactive/qrsh.md).

## Further reading

- [Cluster status](status.md), to check whether a queue or a disk is the problem before you write
- [Warning emails](../jobs/efficiency.md), for what an automated warning means
- [Training](../getting-started/training.md), for the quarterly introduction workshop
