---
title: "How to Check Disk & Quota Usage"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152314/How+to+Check+Disk+Quota+Usage"
date-modified: "2021-10-08"
author: "SGK/PBF"
---

1. [Introduction](how-to-check-disk-quota-usage.md)
2. [Disk Usage](how-to-check-disk-quota-usage/disk-usage.md)
3. [Quota Usage](how-to-check-disk-quota-usage/quota-usage.md)


# 1. Introduction


The following tools can be used to monitor your disk usage.


- You can use the following Un*x commands:


| `du` | show disk use |
| --- | --- |
| `df` | show disk free |


or
- you can use Hydra-specific home-grown tools, (these require that you load the `tools/local` or `tools/local+` modules)


| `disk-usage` | run `df` and parse its output in a more user friendly format |
| --- | --- |
| `dus-report` | run `du` and parse its output in a more user friendly format |
- You can also view the disk status at the cluster status web pages, either
    - [here](https://www.cfa.harvard.edu/~sylvain/hydra/#disk) (at cfa.harvard.edu) 
or
    - [here](https://hydra-3.si.edu/tools/status/#disk) (at si.edu).


Each site shows the disk usage and a quota report, under the "Disk & Quota" tab, compiled 4x a day respectively, and has links to plots of disk usage vs time.
