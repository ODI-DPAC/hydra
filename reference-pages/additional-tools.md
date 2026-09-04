---
title: "Additional Tools"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152353/Additional+Tools"
date-modified: "2025-12-03"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](additional-tools.md)
2. [A Better Qstat: qstat+](additional-tools/a-better-qstat-qstat.md)
3. [A Better Qacct: qacct+](additional-tools/a-better-qacct-qacct.md)
4. [A Better Quota: quota+](additional-tools/a-better-quota-quota.md)
5. [Checking a Compute Node with rtop+](additional-tools/checking-a-compute-node-with-rtop.md)
6. [Checking Memory and CPU usage](additional-tools/checking-memory-and-cpu-usage.md)
7. More Tools
    1. [Local Tools](additional-tools/more-tools.md)
    2. [Local+ Tools](additional-tools/more-tools.md)
    3. [Misc Tools](additional-tools/more-tools.md)
    4. [Also Available](additional-tools/more-tools.md)


# 1. Introduction


- We offer a set of tools, written for Hydra, to help monitor jobs and the cluster and do some simple operations.
    - These are split into `tools/local-user` and `tools/local-admin;`
    - The modules `uge/8.8.1`&`tools/local-user` are 'sticky' and this always loaded.
    - The module `tools/loca`l is available for backward compatibility and loads `tools/local-user` and `tools/local-admin;`
    - The module `tools/local+` gives access to more local tools.
    - The module `tools/misc` gives access to more tools.
- Use the following commands for additional help:


`% module help tools/loca``l-user`


`% module help tools/local-admin`


`% module help tools/local+`


and


`% module help tools/misc`


- Each tool has a man page.
- A few of these tools are describe in more details in separate pages.
