---
title: "Resource Limits"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152297/Resource+Limits"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) While each queue has a set of limits (CPU, memory), the cluster also has some global limits.


1. [What are the Resource Limits](resource-limits.md)
2. [How to Check the Resource Limits](resource-limits.md)
3. [Notes](resource-limits.md)


## 1. What are the Resource Limits


There are limits on


1. how many jobs can be queued simultaneously:
    - there can't be more that 25,000 jobs queued at any time,
    - a single user can't queue more than 2,500 jobs, and
    - a job array can't request more that 10,000 tasks.
2. how many jobs can run simultaneously, in particular there is:
    - a limit on how many slots a single user can use (name=u_slots value=640)
    - a limit on how many slots a user can grab in each queue, with fewer slots allowed in queues with longer time limits.
3. how much memory can be simultaneously reserved, in particular
    - a limit on how much memory can be reserved by a single user in each queue.
4. and for some queues how many concurrent jobs a user can have
    - users are limited to one concurrent interactive job, two I/O jobs, and 3 in the uTxlM.q queue.


- The more resources a job uses (more CPU time, more memory), the fewer similar jobs a single user can run concurrently,
    - in other words you can run a lot of small jobs at the same time but fewer very big/long jobs.
- For example, users can't grab more than 71 slots (or CPUs) and 2.6TB of reserved memory concurrently for jobs running in the long-time high-memory queue (`lThM.q`).


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The actual limits are subject to change depending on the cluster usage and the hardware configuration


## 2. How to Check the Resource Limits


- To check the global limits:


`% qconf -sconf global | grep max`


and the explanation of these parameters can be found in


`% man 5 sge_conf`


- To check the queue specific resource limits, use


`% qconf -srqs`


- As of May 2024, this command returns:


```{.text title="qconf -srqs returns the following: (click on \"Expand source\" to view content) Expand source"}
{
   name         max_slots_per_user
   description  Limit slots/user for all queues
   enabled      TRUE
   limit        users {*} to slots=840
}
{
   name         max_hC_slots_per_user
   description  Limit slots/user in hiCPU queues
   enabled      TRUE
   limit        users {*} queues {sThC.q} to slots=840
   limit        users {*} queues {mThC.q} to slots=840
   limit        users {*} queues {lThC.q} to slots=417
   limit        users {*} queues {uThC.q} to slots=139
}
{
   name         max_hM_slots_per_user
   description  Limit slots/user for hiMem queues
   enabled      TRUE
   limit        users {*} queues {sThM.q} to slots=840
   limit        users {*} queues {mThM.q} to slots=569
   limit        users {*} queues {lThM.q} to slots=379
   limit        users {*} queues {uThM.q} to slots=71
}
{
   name         max_xlM_slots_per_user
   description  Limit slots/user for xlMem restricted queue
   enabled      TRUE
   limit        users {*} queues {uTxlM.rq} to slots=480
}
{
   name         qrsh_u_slots
   description  Limit slots/user for interactive (qrsh) queues
   enabled      TRUE
   limit        users {*} queues {qrsh.iq} to slots=16
}
{
   name         total_gpu
   description  Limit GPUs for all users in GPU queues
   enabled      TRUE
   limit        users * queues {qgpu.iq} to num_gpu=4
   limit        users * queues {sTgpu.q,mTgpu.q,lTgpu.q,uTgpu.q} to num_gpu=4
}
{
   name         max_gpu_per_user
   description  Limit GPUs per user in GPU queues
   enabled      TRUE
   limit        users {*} queues {qgpu.iq} to num_gpu=1
   limit        users {*} queues {sTgpu.q} to num_gpu=4
   limit        users {*} queues {mTgpu.q} to num_gpu=3
   limit        users {*} queues {lTgpu.q} to num_gpu=2
   limit        users {*} queues {uTgpu.q} to num_gpu=1
}
{
   name         blast2GO
   description  Limit to set aside a slot for blast2GO
   enabled      TRUE
   limit        users * queues !lTb2g.q hosts {@b2g-hosts} to slots=110
   limit        users * queues lTb2g.q hosts {@b2g-hosts} to slots=1
   limit        users {*} queues lTb2g.q hosts {@b2g-hosts} to slots=1
}
{
   name         bigtmp_space_per_user
   description  Limit total bigtmp concurrent request per user
   enabled      TRUE
   limit        users {*} to big_tmp=25
}
{
   name         idlrt_license_per_user
   description  Limit total number of idl licenses per user
   enabled      TRUE
   limit        users {*} to idlrt_license=102
}
{
   name         io_slots_per_user
   description  Limit slots for io queue per user
   enabled      TRUE
   limit        users {*} queues {lTIO.sq} to slots=8
}
{
   name         max_concurrent_jobs_per_user
   description  Limit the number of concurrent jobs per user for some queues
   enabled      TRUE
   limit        users {*} queues {uTxlM.rq} to no_concurrent_jobs=3
   limit        users {*} queues {lTIO.sq} to no_concurrent_jobs=2
   limit        users {*} queues {qrsh.iq} to no_concurrent_jobs=1
   limit        users {*} queues {qgpu.iq} to no_concurrent_jobs=1
}
```


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Note that these values get adjusted as needed.


- The explanation of the resource quota set (rqs) can be found in


`% man 5 sge_resource_quota`


- To check how much of these resources (queues quota) are used overall, or by your job(s), use:


`% qquota`


or


`% qquota -u $USER`


- You can also inquire about a specific resource (`qquota -l mem_res`), and use the local tools (`module load tools/local`) `qquota+` to


1. 
    - get a nicer printout of the reserved memory,
    - get the % of usage with respect to its limit


- like in


`% qquota+ +% -l slots -u hpc`


(more info via `qquota+ -help` or `man qquota+`.)


- To check the limits of a specific queue (CPU and memory), use


`% qconf -sq sThC.q`


and the explanation of these parameters can be found in


`% man 5 queue_conf`


under the `RESOURCE LIMITS` heading.


## 3. NOTES


- You can submit a job and tell the GE to let it start only after another job has completed, using `-hold_jid <jobid>` flag to `qsub`: 

```
% qsub -N FirstOne pre-process.job
Your job 12345678 ("FirstOne") has been submitted
% qsub -hold_jid 12345678 -N SecondOne post-process.job
Your job 12345679 ("SecondOne") has been submitted 
```


- You can be more sophisticated (or use `qchain` see below):


```{.text title="Script that submit 3 jobs that must run sequentially, using C-shell syntax"}
#!/bin/csh
#
set parameter = $1
set name = $2
#
set jid1 = `qsub -terse -N "pre-process-$name" pre-process.job $parameter`
echo $jid1 submitted '("'pre-process-$name'")'
set jid2 = `qsub -terse -hold_jid $jid1 -N "process-$name" process.job $parameter`
echo $jid2 submitted '("'pre-process-$name'")'
set jid3 = `qsub -terse -hold_jid $jid2 -N "post-process-$name" post-process.job $parameter`
echo $jid3 submitted '("'post-process-$name'")'
```


This example will submit 3 jobs: `pre-process.job`, `process.job` and `post-process.job` to be run sequentially,


- 
    - each takes one argument, the parameter,
    - and is given a compounded name.
    - The embedded directives in the three job scripts may request different resources, like 
This way a task is broken up to avoid grabbing more resources than needed at each step.
        - lots of memory for pre-processing,
        - lots of CPUs for processing, and
        - neither for post processing.


- You can use the `qchain` tool by loading the `tools/local` module, to submit jobs that must run sequentially.


```
module load tools/local
qchain *.job
```


will submit the job files that match "`*.job`" in the order given by "`echo *.job`".


By using quotes, as follows:


```
module load tools/local
qchain '-N start first.job 123' '-N crunch second.job 123' '-N post-process finish.job 123'
```


`qchain` allows you to pass arguments to both `qsub` and the job scripts.


- You can limit how many jobs you submit with the following trick:


```{.text title="How to limit the number of jobs submitted, using C-shell syntax"}
# define how many jobs to queue 
@ NMAX = 250 
#
loop:
 @ N = `qstat -u $USER | tail --lines=+3 | wc -l`
 if ($N >= $NMAX) then
 sleep 180
 goto loop
 endif
#
```


This example counts how many jobs you have in the queue (running and waiting) using `the command qstat` (and `tail` and `wc -l`) and pauses for 3 minutes (180 seconds) if that count is 250 or higher.


You would include these lines in a script that submits a slew of jobs, but should not queue more than a given number at any time (to count only the queued jobs, add `-s p` to `qsub`).
- Or you can use the tool `q-wait` (needs the module `tools/local`), that takes an argument and two options: 
`% q-wait blah` 
will pause until you have no job whose name has the string '`blah`' left queued or running.
- The options allow you to specify the number of jobs, and how often to check, i.e.: 
`% q-wait -N 125 -wait 3600 crunch` 
will pause until there are 250 or fewer jobs whose name has the string '`crunch`' left queued or running, checking once an hour.
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Avoid using the `-V` flag to `qsub`
    - The `-V` flag passes all the active environment variables to the script.
    - While it may be convenient in some instances, it creates a dependency on the precise environment configuration when submitting the job, 
thus the same job script may fail when it is submitted at a later time (or from a different log in) from a different configuration.
