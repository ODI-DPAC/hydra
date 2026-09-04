---
title: "Help Choosing a Queue"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152299/Help+Choosing+a+Queue"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

1. [What Queue Should I use?](help-choosing-a-queue.md)
2. [Why Can't I Queue that Job?](help-choosing-a-queue.md)
3. [Why Is my Job Queued but not Running?](help-choosing-a-queue.md)


## 1. What Queue Should I Use?


To choose a queue, you need to know


1. whether is it a serial (single CPU) or parallel (multiple CPUs) job,
2. if it is a parallel job, what kind,
3. how much memory this job will need,
4. how much CPU time it will require.


Indeed:


<table class="wrapped fixed-table confluenceTable"><colgroup><col style="width: 270.0px;"/><col style="width: 218.0px;"/><col style="width: 337.0px;"/></colgroup><tbody><tr><th class="confluenceTh" colspan="1">If your computation will use</th><th class="confluenceTh" colspan="1">your job script needs to</th><th class="confluenceTh" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">qsub</span></code> option needed/recommended</th></tr><tr><td class="confluenceTd">more than one CPU (parallel jobs need)</td><td class="confluenceTd" colspan="1">request a <code>PE</code> and <code>N</code> slots</td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-pe &lt;pe-name&gt; N or -pe &lt;pe-name&gt; N-M</span></code></td></tr><tr><td class="confluenceTd">more than 2GB/CPU of memory</td><td class="confluenceTd" colspan="1">reserve the required memory</td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l mres=X,h_data=X,h_vmem=X</span></code></td></tr><tr><td class="confluenceTd">more than 8GB/CPU of memory</td><td class="confluenceTd" colspan="1"><p>use a high-memory queue, and</p><p>reserve the required memory</p></td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l mres=X,h_data=X,h_vmem=X,himem</span></code></td></tr><tr><td class="confluenceTd">up to T hours of CPU (per CPU)</td><td class="confluenceTd" colspan="1">specify the required amount</td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l s_cpu=T:0:0</span></code></td></tr><tr><td class="confluenceTd" colspan="1"><br/></td><td class="confluenceTd" colspan="1">or specify the queue</td><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-q mThC.q</span></code></td></tr><tr><td class="confluenceTd">no idea how much CPU</td><td class="confluenceTd" colspan="1">use an unlimited, low priority queue</td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-q uThC.q -l lopri</span></code></td></tr></tbody></table>


- `X` can be something like 2GB
- `T` can be something like 240 (for 240 hours or 10 days)
- You may need to combine PE, memory and CPU resource requests.
- Remember, that the more resources your job requests, the fewer concurrent similar jobs can run at any tim
- Similar jobs will need similar resources, so when in doubt and before queuing a slew of similar jobs:
    - run one job and monitor its resource usage, then
    - queue the other jobs after trimming the requested resources (CPU and memory).


## 2. Why Can't I Queue that Job?


There can be different reasons why a job is rejected:


- inconsistency in your resources request, like asking for more CPU or memory that the limit of a given queue;
- unavailable resources, like asking for more CPUs or more memory on a single node than exists on any compute nodes;
- exceeding resource limits, like asking for more CPUs than are allowed per user in a given queue.


Use the `-w v` or the `-verify` flag to `qsub`, see [queue selection validation and/or verification](available-queues.md), to check a job script file.


## 3. Why Is my Job Queued but not Running?


There can be different reasons why a job remains in the queue:


- the requested resources are not available, like there is no compute node with the requested number of CPUs or amount of memory currently available;
- the user resource quota has been reached, like the allowed total amount of CPUs or memory used by a single user was reached.


Use the command `qconf -srqs` or `qquota`, see how to check under [resource limits](help-choosing-a-queue.md).
