---
title: Hydra user documentation
hide:
  - navigation
  - toc
  - footer
---

<div class="hero" markdown>
<div class="hero__inner" markdown>

<p class="hero__kicker">Smithsonian High Performance Computing</p>

# <span class="hero__name">Hydra</span> <span class="hydra-status"></span>

The SI HPC cluster contains 74 compute nodes, including GPU nodes, with 5,840 CPU cores and 49 TB of memory. The system is designed and operated by the Data Platforms and Advanced Computing team in the Office of Digital and Innovation.

</div>
</div>

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } [**Getting Started**](getting-started/index.md)

    ---

    Request an account, log in, submit your first job.

-   :material-format-list-checks:{ .lg .middle } [**Running Jobs**](jobs/index.md)

    ---

    Queues, job scripts, memory and CPU requests.

-   :material-monitor:{ .lg .middle } [**Interactive Use**](interactive/index.md)

    ---

    Jupyter, RStudio, VS Code, interactive shells on compute nodes.

-   :material-harddisk:{ .lg .middle } [**Storage**](storage/index.md)

    ---

    Which filesystem to use, quotas, snapshots, the scrubber.

-   :material-package-variant:{ .lg .middle } [**Software**](software/index.md)

    ---

    Modules, compilers, Python and R, bioinformatics packages, and CUDA for GPUs.

-   :material-swap-horizontal:{ .lg .middle } [**Data Transfer**](data-transfer/index.md)

    ---

    Moving data on and off the cluster with scp, rsync, Globus, or rclone.

</div>

<div class="grid meta" markdown>

<div class="card" markdown>

## Help

- [Getting help](policies/index.md#getting-help), [usage policies](policies/usage.md) and [cluster status](policies/status.md)
- Email **SI-HPC@si.edu** with your username, job ID, and the error text
- [PDF of this site](hydra-documentation.pdf), regenerated on every update

</div>

<div class="card card--link" markdown>

## [News](news/index.md)

<!-- news:start -->
**August 25, 2026.** GPU jobs that request more CPU slots than GPUs, such as -pe mthread 4 -l gpu,ngpus=1, now start as soon as the GPUs and CPUs they request are free.

**October 19, 2026.** The Hydra user documentation is now at https://computing.si.edu/hydra/ and supersedes the pages on the Confluence wiki.

**May 15, 2026.** Disaster-recovery backups of /home and /data to the cloud resumed, ending the pause noted on December 5, 2025.
<!-- news:end -->

</div>

</div>
