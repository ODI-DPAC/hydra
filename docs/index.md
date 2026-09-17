---
title: Hydra user documentation
hide:
  - navigation
  - toc
---

# Hydra: Smithsonian High Performance Computing

Hydra is the Smithsonian Institution HPC cluster, run by the Data Platform and Advanced Computing Office under the Office of Digital and Innovation, and housed at the Ashburn Data Center in Virginia.

<div class="grid cards" markdown>

-   :material-account-plus:{ .lg .middle } **Get an account**

    ---

    Eligibility, the request form, password setup.

    [:octicons-arrow-right-24: Request an account](getting-started/account.md)

-   :material-rocket-launch:{ .lg .middle } **Quick start**

    ---

    `ssh` to a login node, copy a file, submit and check on your jobs.

    [:octicons-arrow-right-24: Quick start](getting-started/quick-start.md)

-   :material-format-list-checks:{ .lg .middle } **Run jobs**

    ---

    `qsub` and job scripts, queue selection, memory and CPU requests, resource limits, `qstat+`, warning emails.

    [:octicons-arrow-right-24: Running jobs](hydra/jobs/index.md)

-   :material-harddisk:{ .lg .middle } **Store and move data**

    ---

    `/home`, `/data`, `/scratch`, `/store`; quotas, snapshots, the 180-day scrubber; scp, Globus, rclone.

    [:octicons-arrow-right-24: Storage](hydra/storage/index.md)

-   :material-package-variant:{ .lg .middle } **Find software**

    ---

    `module avail`, compilers and MPI, Python and conda, R, the `bio/` packages, GPUs, containers.

    [:octicons-arrow-right-24: Software](hydra/software/index.md)

-   :material-lifebuoy:{ .lg .middle } **Get help**

    ---

    Usage policies, FAQ, cluster status, what to include when you email SI-HPC@si.edu.

    [:octicons-arrow-right-24: Policies and support](policies/index.md)

</div>

## Status and contact

- Cluster status: [status page](policies/status.md) (SI networks or VPN only)
- Questions and problems: **SI-HPC@si.edu**
- Job script builder: [QSub Generator](hydra/jobs/qsubgen.md)

## News

Change notices, upgrades and outages: [News](news/index.md).