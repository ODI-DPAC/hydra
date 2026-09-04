---
title: "Available Queues"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152296/Available+Queues"
date-modified: "2024-11-07"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](available-queues.md)
2. [Matrix of Queues](available-queues.md)
    - [Notes](available-queues.md)
3. [How to Specify a Queue](available-queues.md)
    - [Examples](available-queues.md)
4. [Interactive Queue](available-queues.md)
5. [Workflow Manager Queue](available-queues.md)
6. [Memory Reservation](available-queues.md)
    - [Resources Format Specifications](available-queues.md)
7. [Host Groups](available-queues.md)
8. [CPU architecture](available-queues.md)
9. [Queue Selection Validation and/or Verification](available-queues.md)
10. [Hardware Limits](available-queues.md)
    - [Notes](available-queues.md)


# 1. Introduction


Every job running on the cluster is started in a queue.


- The GE will select a queue based on the resources requested and the current usage in each queue.
- If you don't specify the right queue or the right resource(s), your job will either
    - not get queued,
    - wait forever and never run, or
    - start and get killed when it exceeds one the limits of the queue it ran in.


All jobs run in batch mode, unless you use the interactive queue, and the default GE queue (`all.q`) is not available.


# 2. Matrix of Queues


The set of available queues is a matrix of queues:


- Five sets of queues:
    1. a high-CPU set,
    2. a high-memory set, complemented by
        - a very-high-memory restricted queue,
    3. a GPU set,
    4. an interactive queue, and
    5. a special I/O queue.
- The high-cpu, high-memory and GPU sets of queues have different time limits: short, medium, long and unlimited.
    - the high-cpu queues are for serial or parallel jobs that do not need a lot of memory (less than 8GB per CPU),
    - the high-memory queues are for serial or multi-threaded parallel jobs that require a lot of memory (more then 6GB, but limited to 450GB),
    - the very-high-memory queue is reserved for jobs that need a very large amount of memory (over 450GB),
- interactive queues, to run interactively on a compute node (w/out or w/ a GPU), although it also has limits, and
- a special queue reserved for projects that need special resources (I/Os).


The list of queues and their characteristics (time versus memory limits) are:


<table class="wrapped fixed-width confluenceTable" style="width: 79.3669%;"><colgroup><col style="width: 12.3433%;"/><col style="width: 6.87379%;"/><col style="width: 7.539%;"/><col style="width: 7.539%;"/><col style="width: 7.61291%;"/><col style="width: 12.3433%;"/><col style="width: 45.7488%;"/></colgroup><tbody><tr><th class="confluenceTh" rowspan="3"><p>Memory<br/>limit<br/>per CPU</p><p>resident / virtual</p></th><th class="confluenceTh" colspan="4" style="text-align: center;">Time limit (soft CPU/elapsed time)</th><th class="confluenceTh" rowspan="3">Available<br/>parallel<br/>environments</th><th class="confluenceTh" rowspan="3" style="text-align: center;"> Type of jobs</th></tr><tr><th class="confluenceTh">short</th><th class="confluenceTh">medium</th><th class="confluenceTh">long</th><th class="confluenceTh">unlimited</th></tr><tr><th class="confluenceTh">T&lt;7h/14h</th><th class="confluenceTh">T&lt;6d/12d</th><th class="confluenceTh">T&lt;30d/60d</th><th class="confluenceTh"><br/></th></tr><tr><th class="confluenceTh" style="text-align: center;">8GB / 64GB</th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">sThC.q</span></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">mThC.q</span></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">lThC.q</span></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">uThC.q</span></th><td class="confluenceTd"><p><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mpich</span></code>, <code><span style="color:var(--ds-text-accent-blue,#0055cc);">orte</span></code>, <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>mthread, hybrid</code></span></p></td><td class="confluenceTd">serial or parallel, that needs less than 8GB of memory per CPU</td></tr><tr><th class="confluenceTh" style="text-align: center;">450GB / 900GB</th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">sThM.q</span></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">mThM.q</span></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">lThM.q</span></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">uThM.q</span></th><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd">serial or multi-threaded, 8GB &lt; memory needed &lt; 450GB</td></tr><tr><th class="confluenceTh" style="text-align: center;">2TB / 2TB</th><th class="highlight-grey confluenceTh" data-highlight-colour="grey"><br/></th><th class="highlight-grey confluenceTh" data-highlight-colour="grey"><br/></th><th class="highlight-grey confluenceTh" data-highlight-colour="grey"><br/></th><th class="highlight-yellow confluenceTh" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);">uTxlM.rq</span></th><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd">serial or multi-threaded, memory needed &gt; 450GB, restricted</td></tr><tr><th class="confluenceTh" style="text-align: center;">64GB / 128G</th><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6"><strong><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>sTgpu.q</code></span></strong></td><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6"><strong><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>mTgpu.q</code></span></strong></td><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6"><strong><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>lTgpu.q</code></span></strong></td><td class="highlight-#f4f5f7 confluenceTd" data-highlight-colour="#f4f5f7" title="Background color : Light grey 100%"><br/></td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd">queue to access GPUs</td></tr><tr><th class="confluenceTh" style="text-align: center;"><br/></th><th class="confluenceTh"><br/></th><th class="confluenceTh">T&lt;12h/24h</th><th class="confluenceTh">T&lt;12h/72h</th><th class="confluenceTh"><br/></th><td class="highlight-grey confluenceTd" colspan="2" data-highlight-colour="grey" title="Background colour : Grey"><br/></td></tr><tr><th class="confluenceTh" style="text-align: center;">8GB / 64GB</th><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><span style="color:var(--ds-text-accent-blue,#0055cc);"><strong><code>qrsh.iq</code></strong></span></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd">interactive queue, use <code><span style="color:var(--ds-text-accent-blue,#0055cc);">qrsh</span></code> or <code><span style="color:var(--ds-text-accent-blue,#0055cc);">qlogin</span></code>; 12h of CPU 24h of wallclock.</td></tr><tr><th class="confluenceTh" style="text-align: center;">64GB / 65GB</th><td class="highlight-grey confluenceTd" data-highlight-colour="grey" title="Background colour : Grey"><br/></td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow" title="Background colour : Yellow"><code title=""><span style="color:var(--ds-text-accent-blue,#0055cc);"><strong>qgpu.iq</strong></span></code></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey" title="Background colour : Grey"><br/></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey" title="Background colour : Grey"><br/></td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd">interactive queue to access GPUs, restricted; 12h of CPU 24h of wallclock.</td></tr><tr><th class="confluenceTh" style="text-align: center;">8GB / 64 GB</th><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><strong><span style="color:var(--ds-text-accent-blue,#0055cc);" title=""><code>lTIO.sq</code></span></strong></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd"><p>I/O queue, to access <code>/store</code>; 12h of CPU, 72h of wallclock.</p></td></tr><tr><th class="confluenceTh" style="text-align: center;">8GB / 64 GB</th><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><strong><span style="color:var(--ds-text-accent-blue,#0055cc);" title=""><code>lTWFM.sq</code></span></strong></td><td class="highlight-grey confluenceTd" data-highlight-colour="grey"><br/></td><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">mthread</span></code></td><td class="confluenceTd"><p>Workflow manager queue, to run a job that will submit jobs (6d/30d CPU/wallclock.)</p></td></tr></tbody></table>


## Notes


- the listed time limit is the soft CPU limit (`s_cpu`), and elapsed time (s_rt)
    - the soft elapsed time limit (aka real time, `s_rt`) is twice the soft CPU limit for all the queues.
    - the hard time limits are 15m longer than the soft ones (i.e., `h_cpu`, and `h_rt`). 
Namely, in the short-time limit queues
        - a serial job is warned if it has exceeded 7 hours of consumed CPU, and killed after it has consumed 7 hours and 15 minutes of CPU, or
        - warned if it has spent 14 hours in the queue and killed after spending 14 hours and 15 minutes in the queue.
        - For parallel jobs the consumed CPU time is scaled by the number of allocated slots,
        - the elapsed time is not.
- memory limits are per CPU,
    - so a parallel job, in a high-cpu queue can use up to `NSLOTS` x 6 GB, where `NSLOTS` is the number of allocated slots (CPUs)
    - parallel jobs in the other queues are limited to multi-threaded jobs (no multi-node jobs)
    - the limit on the virtual memory (vmem) is set to be higher that the resident memory (rss)
- memory usage is also limited by the available memory on a given node.
- If you believe that you need access to a restricted or test queue, [contact us](../introduction.md).


# 3. How to Specify a Queue


- By default jobs are most likely to run in the short high-cpu queue (`sThC.q`).
- To select a different queue you need to either
    - specify the name of the queue (via `-q <name>`), or
    - pass a requested time limit (via `-l s_cpu=<value>` or `-l s_rt=<value>`).
- To use a high-memory queue, you need to
    - specify the memory requirement (with `-l mres=X,h_data=X,h_vmem=X`)
    - confirm that you need a high-memory queue (`-l himem`)
    - select the time limit either by
        - specifying the queue name, or (via `-q <name>`), or
        - pass a requested time limit (via `-l s_cpu=<value>` or `-l s_rt=<value>`).
- To use a GPU queue, you need to specify -l gpu
- To use the unlimited queues, i.e., uThC.q or uThM.q, you need to confirm that you request a low priority queue (`-l lopri`)


![(grey lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb.svg) Why do I need to add `-l himem,-l gpu` or `-l lopri`?


- This prevents the GridEngine from submitting a job to these queues that did not request the associated resources, just because one of these queues are less used. 
It prevent the scheduler from "*wasting*" valuable resources.


## Examples


<table class="wrapped fixed-table confluenceTable"><colgroup><col style="width: 439.0px;"/><col style="width: 488.0px;"/></colgroup><tbody><tr><th class="confluenceTh"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">qsub</span></code> flags</th><th class="confluenceTh">Meaning of the request</th></tr><tr><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l s_cpu=48:00:00</span></code></td><td class="confluenceTd">48 hour of consumed CPU (per slot)</td></tr><tr><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l s_rt=200:00:00</span></code></td><td class="confluenceTd">200 hour of elapsed time</td></tr><tr><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-q mThC.q</span></code></td><td class="confluenceTd">use the <code><span style="color:var(--ds-text-accent-blue,#0055cc);">mThC.q</span></code> queue</td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l mres=120G,h_data=12G,h_vmem=12G -pe mthread 10</span></code></td><td class="confluenceTd" colspan="1">12GB of memory (per CPU),  for a 10 CPUs parallel job will reserve 120GB</td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-q mThM.q -l mres=12G,h_data=12G,h_vmem=12G,himem</span></code></td><td class="confluenceTd" colspan="1"><p>to run in the medium-time high-memory queue.</p><p>This is a correct, i.e., complete, specification (memory use specs and <code><span style="color:var(--ds-text-accent-blue,#0055cc);">himem</span></code>)</p></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-q uThC.q -l lopri</span></code></td><td class="confluenceTd" colspan="1">to run in the unlimited high-cpu queue, note the <code><span style="color:var(--ds-text-accent-blue,#0055cc);">-l lopri</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">-q uTxlM.rq -l himem</span></code></td><td class="confluenceTd" colspan="1">unlimited-time, extra-large-memory, restricted to a subset of users</td></tr></tbody></table>


All jobs that use more than 2 GB of memory (per CPU) should include a memory reservation and requirement with `-l mres=X,h_data=X,h_vmem=X`.


- If you do not, your job(s) may not be able to grab the memory they need at run-time and crash, or crash the node.
- memory reservation is for serial and mthread jobs, not MPI.
    - MPI jobs can specify `h_data=X` and `h_vmem=X` resources.
- X is a number followed by a unit, like 100M or 10G, if you specify h_vmem=5 (no unit) your job can only use 5 bytes and will die right away.


# 4. Interactive Queue


You can start an interactive session on a compute node using the command `qrsh` or `qlogin` (not `qsub`, nor `qsh`)


- Some compute nodes are set aside for interactive use,
    - the corresponding queue is named `qrsh.iq`
- To start an interactive session, use `qrsh` or `qlogin`
    - `qrsh` will start an interactive session on one of the interactive nodes,
        - it takes both options and arguments (like `qsub)`
    - `qlogin` is similar to `qrsh`, although
        - it will propagate the `$DISPLAY` variable, so you can use X-enabled applications (like to plot to the screen) if you've enabled X-forwarding, and
        - it does not take any argument, but will take options.
- Unless you need X-forwarding, use `qrsh`


#### Limits on the Interactive Queue:


- Like any other queue, the interactive queue has its own limits:


| CPU | 12h per slot (CPU/core) |
| --- | --- |
| Elapsed Time | 24h per session |
| Memory | 8GB/64GB per slot (CPU/core) |
- Like for `qsub`, you can request more than one slot (CPU/thread) with the `-pe mthread N`option,
    - where `N` is a number between 2 and 16, as in:


`qrsh -pe mthread 4`


- 
    - requesting more slots allows you also to use more memory (4 slots means up to 4 x 8G = 32G).
- Each user is limited to one four (4) concurrent interactive sessions, and up to 16 slots (CPUs/cores).
- The overall limits of slots/user include all the queues (so if you use them all in batch mode, you won't be able to get an interactive session).


#### The NSLOTS Variable


- As of Feb 3, 2020, `$NSLOTS` is properly propagated by `qrsh`, but not by `qlogin.`
    - There is no mechanism to propagate `$NSLOTS` with `qlogin` and enable X-forwarding.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Remember, Hydra is a shared resource, do not "*waste*" interactive slots by keeping your `qlogin` or `qrsh` session idle.


# 5. Workflow Manager Queue


Users who want to use such a workflow manager (like NextFlow and Snakemake) can submit a job to the workflow manager (WFM) special queue `lTWFM.sq`.


- This queue allows you to run a job that will in turn submit jobs.
- You can use that queue for any other WFM, including your own scripts.
- Jobs can be submitted from the hosts in the workflow manager queue (`@wfm-hosts`).


To run a job in the workflow manager queue, you will need to specify `-q lTWFM.sq -l wfmq`to `qsub` or add these as embedded directives in your job file.


#### Limits on the Workflow Manage queue:


- Like any other queue, the WFM queue has its own limits:


| CPU | 144hr (6 days) per slot (CPU/core) |
| --- | --- |
| Elapsed Time | 720h (30 days) of elapsed time |
| Memory | 8GB/64GB per slot (CPU/core) |
- You can request more than one slot (CPU/thread) with the `-pe mthread N`option,
    - where `N` is currently limited to 2;
    - requesting more slots allows you also to use more memory (2 slots means up to 2 x 8G/64G = 16G/128G res/vmem).


- Each user is limited to one concurrent interactive session, and up to 2 slots (CPUs/cores).


# 6. Memory Reservation


- We have implemented a memory reservation mechanism, (via `-l mres=XT`)
    - This allows the job scheduler to guarantee that the requested amount of memory is available for your job on the compute node(s), 
by keeping track of the reserved memory and not scheduling jobs that reserve more memory than available.
    - Hence reserving more than you will use prevents others (including your own other jobs) from accessing the available memory and 
indirectly the available CPUs (like if you use one, or even just a few, CPUs but grab most of the memory of a given compute node).
- We have at least 2GB/CPUs, but more often 4GB/CPUs on the compute node, still 
![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) it is recommended to reserve memory if your job will use more than 2GB/CPU, and 
set `h_data=X` and `h_vmem=X` to the value used in `mres=XT`.
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Remember:
    - The memory specification is
        - per JOB in `mres=XT` (total)
        - per CPU in `h_data=X` and `h_vmem=X`, it should be `XT` divided by the number of requested slots.
    - Memory is a scarce and expensive resource, compared to CPU, as we have fewer nodes with a lot of memory.
    - Try to *guesstimate* the best you can your memory usage, and
    - monitor the memory use of your job(s) (see [Job Monitoring](job-monitoring.md)).
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Note:
    - Do not hesitate to re-queue a job if it uses a lot more or a lot less than your initial guess, esp. if you plan to queue a slew of jobs;
    - often, memory usage scales with the problem in predictable ways, or the documentation might indicate memory requirements, 
consider running some test cases to help you *guesstimate*, and 
trim down your memory reservation whenever possible: a job that requests oodles of memory may wait for a long time in the queue for that resource to free up.
    - Consider breaking down a long task into separate jobs if different steps need different type of resources.


## Resources Format Specifications


- The format forsee `man sge_types`.
    - memory specification is a positive (decimal) number followed by a unit (aka a multiplier), like `13.4G` for 13.4 GB;
    - CPU or RT time specification is `h:m:s`, like `100:00:00` for 100 hours (or "`100::`", while`"100`" means 100 seconds).


# 7. Host Groups


The GridEngine supports the concept of a host group, i.e., a list of hosts (compute nodes).


- You can request that a job run only on computers in a given a host group, and 
we use these host groups to restrict queues to specific list of hosts.
- To request computers of a given host group, use something like this "`-q mThC.q@@ib-hosts`" (*yes* there is a double "`@`"),
- In fact the queue specification to `qsub` can be a RE, so`-q '?ThC.q@@ib-hosts`', means any high-cpu queue but only hosts on IB.


- You can get the list of all the host groups with (show host group list) 
`% qconf -shgrpl`
- and get the list of hosts for a specific host group with 
`% qconf -shgrp <host-group-name>`


- Here is the list of host groups:


| Name | Description |
| --- | --- |
| `@all-hosts` | all the hosts |
| `@hicpu-hosts` | high CPU hosts |
| `@himem-hosts` | high memory hosts (521GB/host) |
| `@xlmem-hosts` | extra large memory hosts (>=1TB/host) |
| `@io-hosts` | hosts in the IO queue |
| `@wfm-hosts` | hosts in the WFM queue |
| | |
| `@gpu-hosts` | hosts with GPUs |
| `@ssd-hosts` | hosts with local SSD |
| | |
| `@24c-hosts` | hosts with 24 CPUs |
| `@NNc-hosts` | hosts with NN CPUs (NN=value up to 192) |
| | |
| `@avx-hosts` | hosts with AVX-capable CPUs |
| `@avx2-hosts` | hosts with AVX2-capable CPUs |


# 8. CPU Architecture


- The cluster is composed of compute nodes with different CPU architectures.
- You can tell the scheduler to run your job on specific CPU architecture(s) using the `cpu_arch` resource.


### Composition


- The cluster's CPU architecture composition is as follows:


<table class="wrapped confluenceTable" style="margin-left: 30.0px;"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Compute Nodes</th><th class="confluenceTh">CPU Arch.</th><th class="confluenceTh">CPU Model Name</th></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-64-xx</code></span></td><td class="confluenceTd"><code>skylake</code></td><td class="confluenceTd">Intel(R) Xeon(R) Gold 6148 CPU \@ 2.40GHz</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-65-xx</code></span></td><td class="confluenceTd">zen</td><td class="confluenceTd">AMD EPYC 7713P 64-Core \@1.94GHz</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-75-xx</code></span></td><td class="confluenceTd">zen</td><td class="confluenceTd">AMD EPYC 7H12 64-Core \@ 2.53GHz</td></tr><tr><td class="confluenceTd" rowspan="2"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-76-xx</code></span></td><td class="confluenceTd">zen</td><td class="confluenceTd">AMD EPYC 9654 64-Core</td></tr><tr><td class="confluenceTd">zen</td><td class="confluenceTd">AMD EPYC 9534 64-Core</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-79-xx</code></span></td><td class="confluenceTd"><code>skylake</code></td><td class="confluenceTd">Intel(R) Xeon(R) Silver 4114 CPU \@ 2.20GHz</td></tr><tr><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-84-xx</code></span></td><td class="confluenceTd"><code>skylake</code></td><td class="confluenceTd">Intel(R) Xeon(R) Platinum 8280 CPU \@ 2.70GHz</td></tr><tr><td class="confluenceTd" rowspan="2"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>compute-93-xx</code></span></td><td class="confluenceTd"><code>haswell</code></td><td class="confluenceTd">Intel(R) Xeon(R) CPU E7-8867 v3 \@ 2.50GHz</td></tr><tr><td class="confluenceTd"><code>broadwell</code></td><td class="confluenceTd">Intel(R) Xeon(R) CPU E7-8860 v4 \@ 2.20GHz</td></tr></tbody></table>


### Usage


#### Grid Engine/Qsub


- You can use the `cpu_arch` resource to request a specific architecture or a set of architectures or avoid specific architecture(a), like in


`qsub -l cpu_arch=haswell`


such job will only run on nodes with a `haswell` CPU architecture.


- Alternatively, you can use logic constructs as follows:


`qsub -l cpu_arch=\!broadwell` - any CPU, except `broadwell`.


`qsub -l cpu_arch='haswell|skylake'` - either `haswell` OR `skylake` CPUs.


#### Tools


- You can retrieve the node's CPU architecture with the command `get-cpu_arch`, accessible after loading the module `tools/local.`
- You can query the `cpu_arch` list within a queue with, for example,


`qstat -F cpu_arch -q sThC.q`


- You can set the environment variable `cpu_arch` by loading the module `tools/cpu_arch`.


#### Compilers


- Each compiler allows you to specify specific target processors (aka CPU architectures).
- The syntax is different for each compiler, read carefully the compiler's user guide.


### Examples


- Run only on two types of architectures:


```{.text title="Restrict to some type of arch"}
#
#$ -cwd -j y -N demo1 -o demo1.log
#$ -l cpu_arch='haswell|skylake'
#
./crunch
#
```


- Run a different executable depending on the node's CPU architecture, and tell the scheduler to avoid AMD processors:


```{.text title="Run different code for different arch"}
#
#$ -cwd -j y -N demo2 -o demo2.log
#$ -l cpu_arch='!broadwell'
#
module load tools/cpu_arch
bin/$cpu_arch/crunch
#
```


# 9. Queue Selection Validation and/or Verification


- You can submit a job script and verify if the GE can run it, i.e., 
![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) can the GE find the adequate queue and allocate the requested resources?
- The qsub flag "`-w v`" will run a verification, while "`-w p`" will poke whether the job can run, but *the job will not be submitted*: 
`% qsub -w v my_test.job` 
or 
`% qsub -w p my_test.job` 
The difference being that "`-w v"` checks against an *empty* cluster, while `"-w p`" validates against the cluster *as is* status.
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) By default all jobs are submitted with "-w e", producing an error for invalid requests. 
Overriding it with `"-w w`" or "-w n" can result in jobs that are queued but will never run 
as they request more resources than will ever be available.
- ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) You can also use the `-verify` flag, to print detailed information about the would-be job as though `qstat -j`was used, 
including the effects of command-line parameters and the external environment, *instead* of submitting job: 
`% qsub -verify my_test.job`


# 10. Hardware Limits


The following table shows the current hardware limits:


<table class="wrapped relative-table confluenceTable" style="width: 59.0551%;"><colgroup><col style="width: 12.4583%;"/><col style="width: 8.56507%;"/><col style="width: 7.89766%;"/><col style="width: 13.6819%;"/><col style="width: 15.2392%;"/><col style="width: 42.158%;"/></colgroup><tbody><tr><th class="confluenceTh" rowspan="2" style="text-align: center;">Queue<br/>name</th><th class="confluenceTh" colspan="2" style="text-align: center;">Number of</th><th class="confluenceTh" rowspan="2" style="text-align: center;">Number of<br/>CPU per node</th><th class="confluenceTh" rowspan="2" style="text-align: center;">Available<br/>Memory</th><th class="confluenceTh"><br/></th></tr><tr><th class="confluenceTh" style="text-align: center;">nodes</th><th class="confluenceTh" style="text-align: center;">slots</th><th class="confluenceTh">Comment                                                       </th></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">?ThC.q</span></code></th><td class="confluenceTd" style="text-align: right;"> 60</td><td class="confluenceTd" style="text-align: right;">5000</td><td class="confluenceTd" style="text-align: center;"> 40 to 128</td><td class="confluenceTd" style="text-align: center;"> &gt;4GB/CPU</td><td class="confluenceTd">high-CPU queues</td></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">?ThM.q</span></code></th><td class="confluenceTd" style="text-align: right;">50</td><td class="confluenceTd" style="text-align: right;">4552</td><td class="confluenceTd" style="text-align: center;"> 32 to 192</td><td class="confluenceTd" style="text-align: center;"> &gt;512GB per node</td><td class="confluenceTd">high-memory queues</td></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">uTxlM.rq</span></code></th><td class="confluenceTd" style="text-align: right;"> 3</td><td class="confluenceTd" style="text-align: right;">480</td><td class="confluenceTd" style="text-align: center;">96 to 192</td><td class="confluenceTd" style="text-align: center;"> &gt;1TB per node</td><td class="confluenceTd">extra large memory queue, restricted</td></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">?Tgpu.q</span></code></th><td class="confluenceTd" style="text-align: right;">3</td><td class="confluenceTd" style="text-align: right;">8 GPUs</td><td class="confluenceTd" style="text-align: center;"><p>-</p></td><td class="confluenceTd" style="text-align: center;">-</td><td class="confluenceTd">GPU queues, need <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>-l gpu</code></span> </td></tr><tr><th class="confluenceTh" style="text-align: right;"><br/></th><td class="confluenceTd" style="text-align: right;"><br/></td><td class="confluenceTd" style="text-align: right;"><br/></td><td class="confluenceTd" style="text-align: center;"><br/></td><td class="confluenceTd" style="text-align: center;"><br/></td><td class="confluenceTd"><br/></td></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">lTIO.sq</span></code></th><td class="confluenceTd" style="text-align: right;">2</td><td class="confluenceTd" style="text-align: right;">8</td><td class="confluenceTd" style="text-align: center;">-</td><td class="confluenceTd" style="text-align: center;">-</td><td class="confluenceTd">I/O queue to access <code>/store</code> </td></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">qrsh.iq</span></code></th><td class="confluenceTd" style="text-align: right;">2</td><td class="confluenceTd" style="text-align: right;">40</td><td class="confluenceTd" style="text-align: center;">-</td><td class="confluenceTd" style="text-align: center;">256GB per node</td><td class="confluenceTd"><div class="content-wrapper"><p class="auto-cursor-target">use <code><span style="color:var(--ds-text-accent-blue,#0055cc);">qrsh</span></code> or <code>qlogin</code> <span>(not </span><code><span style="color:var(--ds-text-accent-blue,#0055cc);">qsh</span></code><span> or </span><code><span style="color:var(--ds-text-accent-blue,#0055cc);">qsub</span></code><span>)</span></p></div></td></tr><tr><th class="confluenceTh" style="text-align: right;"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">qgpu.iq</span></code></th><td class="confluenceTd" style="text-align: right;">3</td><td class="confluenceTd" style="text-align: right;">8 GPUs</td><td class="confluenceTd" style="text-align: center;">-</td><td class="confluenceTd" style="text-align: center;">-</td><td class="confluenceTd">GPU interactive queue, use <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>qrsh -l gpu</code></span> </td></tr></tbody></table>


The values in this table change as we modify the hardware configuration, you can verify them with either


`% qstat -g c`


or


`% qstat+ -gc`


and


`% qhost`


or


`% qhost+`


## Notes


- We also impose software limits, namely how much of the cluster a single user can grab (see [resource limits in Submitting Jobs](../submitting-jobs.md). )
- If your pending requests will exceed these limits, your queued jobs will wait;
- If you request inconsistent or unavailable resources, you will get the following error message: 
`Unable to run job: error: no suitable queues.` 
You can use "`-w v"` or "`-verify`" to track down why the GE can't find a suitable queue, as described elsewhere on this page.
