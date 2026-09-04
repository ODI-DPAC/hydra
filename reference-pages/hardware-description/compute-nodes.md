---
title: "Compute Nodes"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152285/Compute+Nodes"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

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
