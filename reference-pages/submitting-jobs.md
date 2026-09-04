---
title: "Submitting Jobs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152288/Submitting+Jobs"
date-modified: "2021-11-20"
author: "SGK"
---

1. [Introduction](submitting-jobs.md)
    1. [Conceptual Examples](submitting-jobs/conceptual-examples.md)
    2. [Serial Jobs](submitting-jobs/serial-jobs.md)
    3. [Parallel Jobs](submitting-jobs/parallel-jobs.md)
    4. [Job Arrays](submitting-jobs/job-arrays.md)
2. [Available Queues](submitting-jobs/available-queues.md)
3. [Resource Limits](submitting-jobs/resource-limits.md)
4. [Job Monitoring](submitting-jobs/job-monitoring.md)
5. [Help Choosing a Queue](submitting-jobs/help-choosing-a-queue.md)
6. [Help Writing a Job Script](submitting-jobs/help-writing-a-job-script.md)
7. [Where to Find Examples](submitting-jobs/where-to-find-examples.md)


# 1. Introduction


Most computations on Hydra are run in batch mode using a job scheduler (aka workload manager).


Hydra uses the Univa Grid Engine (GE or UGE) as the job scheduler:


- Jobs are submitted from either login node to the job scheduler using the command `qsub` and a job file;
- submitted jobs may wait in the queue:
    - until the requested resource(s) is/are available, or
    - if a user has reached a resource usage limit, until that limit has cleared.
- The scheduler will eventually run each job, starting it on one or several compute nodes:
    - the job will run in batch, not interactive, mode;
    - it is the scheduler that selects on which compute(s) node to run a job on, and
    - if the job exceeds a limit, like it uses too much memory, or consumes too much CPU time, the scheduler will kill the job.


To run a computation (a job) on Hydra users must write a list of instructions, that specifies the step(s) needed to perform the said computation and if needed pass instructions (aka directives) to the job scheduler as to which resources are required to complete the said computation (like the amount of memory, CPU time, number of CPUs, etc.).


These steps are typically written in a file, aka the job script, while the directives are either passed as options to the `qsub` command or included in the job script, as embedded directives.


A job is thus submitted with the command `qsub`, with the required options (or embedded directives) followed by the name of the file containing the job script.


The different types of jobs are:


- serial jobs: computations that use only one CPU;
- parallel jobs: computation that use more than one CPU (either all on the same node, using multi-threading, or distributed across nodes, using message passing)
- job arrays: a set of similar computations, aka tasks, that use a single unique job script file and a number that identifies each task to be performed.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) A few compute nodes are set aside for interactive use, consult the section on using the interactive queue.


![(info)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/information.svg) The [Available Queues](submitting-jobs/available-queues.md) page describes in detail the available queues.


Every job running on the cluster is started in a queue.


- The GE will select a queue based on the resources requested and the usage in each queue.
- If you don't specify the right queues or the right resource(s), your job will either
    - not get queued,
    - wait forever and never run, or
    - start and get killed when it exceeds one of the limit of the queue it was started in.


The set of available queues is a matrix of queues:


- Four sets of queues: a high-CPU and a high-memory set of queues, complemented by a very-high-memory restricted queue and *special* queues.
- The high-CPU and a high-memory sets of queues have different time limits: short, medium, long and unlimited.


<table class="wrapped confluenceTable"><colgroup><col/><col/></colgroup><thead><tr><th class="confluenceTh" colspan="1" style="text-align: left;"><p>Type</p></th><th class="confluenceTh" colspan="1" style="text-align: left;"><p>Description</p></th></tr></thead><tbody><tr><td class="confluenceTd" colspan="1" style="text-align: left;">high-CPU</td><td class="confluenceTd" colspan="1" style="text-align: left;">for serial or parallel jobs that do not need a lot of memory,</td></tr><tr><td class="confluenceTd" colspan="1" style="text-align: left;">high-memory</td><td class="confluenceTd" colspan="1" style="text-align: left;">for serial or multi-threaded parallel jobs that require a lot of memory,</td></tr><tr><td class="confluenceTd" colspan="1" style="text-align: left;">very-high-memory</td><td class="confluenceTd" colspan="1" style="text-align: left;">reserved for jobs that need a very large amount of memory,</td></tr><tr><td class="confluenceTd" colspan="1" style="text-align: left;">other</td><td class="confluenceTd" colspan="1" style="text-align: left;">for interactive use or projects that need special resources (GPUs, I/O, etc).</td></tr></tbody></table>


# Notes


::: {.note title="Note"}
1. A job will run in a queue. Each queue has some form of limit:
 - in most cases, a job won't be allowed to run forever, nor grab as much memory as it may want to.
 - How to specify resources and what queues to use is explained at the [Available Queues](submitting-jobs/available-queues.md) page.
2. There is some overhead in starting a job, so it is bad practice to submit a large number of very small jobs. 
While you may find it convenient to submit 10,000 five-minute-long jobs, the system will end up taking as much time starting the jobs as the jobs will take to run. 
As a precaution to prevent clobbering the system there is a limit on how many jobs a single user can submit to any of the queues (see explanations in the sections about [hardware limits](submitting-jobs/available-queues.md) and [resource limits](submitting-jobs.md) ).
3. The cluster is a shared resource:
 - there are limits on how much of the cluster resources (total amount of CPUs, memory, etc) a single user can grab at any time (concurrent use).
4. In most cases your job script also needs to load a module or a set of modules.
5. Do not use the login nodes to run any substantive computation:
 - the login nodes are monitored and processes running on one of the the login node that consume too much resources will have at first their priority reduced, and eventually terminated.
:::
