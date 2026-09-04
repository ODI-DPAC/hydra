---
title: "Checking a Compute Node with rtop+"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/374604072/Checking+a+Compute+Node+with+rtop"
date-modified: "2025-10-23"
author: "SGK"
categories: ["hydra7"]
---

`rtop+`: a script to run the command `top` on a compute node (aka remote `top`.)


- The Un*x command `top` can be used to look at what processes are running on a given machine (it reports the "top" processes running at any time).
- To check what processes are running on a compute node, (to check CPU and/or memory usage, you can use: 
`% rtop+ [-u <username>] [-<number>] NN-MM` 
like in`` 
`% rtop+ -u hpc -50 43-05` 
 
and you will see the `<number>` lines listing the processes owned by `<username>` on the compute node `compute-NN-MM`, or 
(second example) the first 50 lines when running `top`, limited to user `hpc`, on `compute-43-50`. 
If you omit `-<number>` you will see only the first 10 lines, if you omit `-u <username>` you will see everybody's processes.


Check `man top` to better understand the output of `top`.
