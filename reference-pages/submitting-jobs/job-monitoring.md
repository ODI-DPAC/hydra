---
title: "Job Monitoring"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152298/Job+Monitoring"
date-modified: "2021-11-17"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](job-monitoring.md)
2. [How to Check on Jobs](job-monitoring.md)
3. [How to Delete/Kill a Job or Jobs](job-monitoring.md)
4. [Modifying Queued Jobs](job-monitoring.md)
5. [Checking on a Completed Job](job-monitoring.md)
6. [Additional Tool](job-monitoring.md)s


# 1. Introduction


After submitting a job, or a set of jobs, with `qsub`, you can


- check on your job(s) with the command `qstat,`
- kill your job(s) with the command `qdel,`
- alter the requested resources of a queued job with `qalter` ,
- check on a finished job with `qacct` ,
- use Hydra-specific home-grown tools`.`


# 2. How to Check on Jobs


The `qstat` command returns the status of jobs in the queue (`man qstat`), here are a few usage examples:


| `qstat -u $USER` | shows only your jobs. |
| --- | --- |
| `qstat -u '*'` | shows everybody's jobs. |
| `qstat -s r` | shows only running jobs. |
| `qstat -s p` | shows only pending jobs. |
| `qstat -r` | shows also requested resources and the full job name. |
| `qstat -s r -u $USER -g t` | shows master/slave info for parallel jobs |
| `qstat -s r -u $USER -g d` | shows task-ID for array jobs |
| `qstat -j 4615585` | produces a more detailed output, for a specific job ID. |
| `qstat -explain E -j 4615585` | produces the explanation for the error state of a specific job, specified by its job ID. |


The job status abbreviations, returned by `qstat,` correspond to


| `qw` | pending (waiting in queue) |
| --- | --- |
| `r` | running |
| `t` | in transfer (typically from `qw` to `r`) |
| `Eqw` | error and waiting in queue (for ever) |
| `d` | marked for deletion |


- Jobs in the `Eqw` status will not run, and the reason for the error status can be found via `qstat -explain E -j <jobid>`
- Jobs in the `qw` status are waiting for the requested resources to become available, or because you have reached some resource limit
    - These jobs can be `qalter`'ed
    - If your job is lingering in the queue (remains in `qw` for a long time, i.e., hours to days) and you have not reached some resource limit, 
you are most likely requested a scarce resource, or more of a resource than is available. In this case, feel free to [contact us](../introduction.md).
- Jobs in the `t`status are in most cases about to get started.
- Jobs in the `d` status are about to be deleted and/or killed.


We provide a tool, q+, that uses `qstat` to provide an easier way to monitor jobs and the status of the queue.


# 3. How to Delete/Kill a Job or Jobs


These are instructions for how to stop a running job or delete a submitted job that has not started running yet.


The `qdel` command (`man qdel`) allows you to either:


- delete a job from the queue (for job in the "`qw`" status), or
- kill a running job (for jobs in the `"r`" status).


You delete/kill a specific job by its job id as follows:


`% qdel 4615585`


or you can kill *all* your jobs (queued and running) with


`% qdel -u $USER`


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Here is a trick to kill a slew of jobs, but not all of them:


```
qstat -u $USER | grep $USER | awk '{print "qdel", $1} > qdel.sou
[edit the file qdel.sou]
source qdel.sou
```


This example


- uses `grep` to filter the lines from `qstat` that have your username, and then
- uses `awk` to produce a list of lines like "`qdel <jobid>`", and
- saves the result to a file `(qdel.sou`);


you then


- edit that file to keep the lines you want, and
- use `source` to execute each line of that edited file as if you had typed them.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) You can use `grep` to better filter the output of `qstat`, like this:


```
qstat -u $USER | grep $USER | grep rax | awk '{print "qdel", $1}' > qdel.sou
[edit the file qdel.sou]
source qdel.sou
```


This example


- filters the output of `qstat` for lines with your user name and
- with the string "`rax`" to identify a sub set of jobs via their job name.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) You can add `"-s r"` or "`-s p`" to `qstat` to limit the list of job IDs to only your running or pending (queued) jobs.


# 4. Modifying a Queued Job


The `qalter` command allows you to alter (modify) the properties of a job, namely its requested resources or parameters.


You can alter


- most of the properties of a queued job;
- and a few of its properties once it has started.


For example:


<table class="wrapped confluenceTable"><colgroup><col/><col/></colgroup><tbody><tr><th class="confluenceTh" colspan="1">you can</th><th class="confluenceTh" colspan="1">with</th></tr><tr><td class="confluenceTd" style="margin-left: 30.0px;">move a queued job to a different queue with</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -q mThC.q &lt;jobid&gt;</code></span></td></tr><tr><td class="confluenceTd">change the name of the job's output file</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -o run-3.log &lt;jobid&gt;</code></span></td></tr><tr><td class="confluenceTd">change whether you want email notifications</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -m abe &lt;jobid&gt;</code></span></td></tr><tr><td class="confluenceTd">change the requested amount of CPU</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -l s_cpu=240:: &lt;jobid&gt;</code></span></td></tr></tbody></table>


where `<jobid>` is the job ID (see `man qalter`.)


# 5. Checking on a Completed Job


The `qacct` command shows the GE accounting information and can be used to check on


- the resources used by a given job that has completed, and
- its exit status.


For example:


`% qacct -j <jobid>`


will list the accounting information for a finished job with the given job ID.


It will show the following useful information:


| `qname` | name of the queue the job ran in |
| --- | --- |
| `hostname` | name of the (master) compute node the job ran on |
| `taskid` | the task ID (for job arrays) |
| `qsub_time` | when the job was queued |
| `start_time` | when the job started |
| `end_time` | when the job ended |
| `granted_pe` | what parallel environment was used |
| `slots` | how many slots were allocated |
| `failed` | did the job fail to complete (1 means job did fail, i.e., was killed by GE b/c memory or time limit exceeded) |
| `exit_status` | the job script exit status (0 means job script completed OK) |
| `ru_wallclock` | wall clock time elapsed, in seconds |
| `ru_utime` | consumed user time, as reported by the O/S (actual CPU time), in seconds |
| `ru_stime` | consumed system time, as reported by the O/S (non-CPU time, usually related to I/O, or other system wait), in seconds |
| `cpu` | CPU time computed, as measured by the GE (ru_utime+ru_stime may not add to the cpu time), in seconds |
| `mem` | total memory*time used in GB seconds: the mean memory usage is mem/cpu in GB |
| `io` | a measure of the I/Os operations executed by the job |
| `maxvmem` | the maximum amount of memory used by the job at any time during its execution |


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Users that run jobs in the high memory queues can use this to check if they used close to the amount of memory they have reserved.


The `qacct` command can also be used to check on the past usage of a given user. For example:


`% qacct -d <ndays> -o <username>`


will return the usage statistics of the user specified in `<username>`, over the past `<ndays>` days (use `man qacct` for more details).


You can get details information for each job that ran, with the "`-j`" option, as follow:


`% qacct -d <ndays> -o <username> -j > qacct.log`


and save its output, if long, to a file `(``qacct.log`). You can parse that file with the command `egrep`.


For example, to check all the jobs the user `hpc` ran over the past 3 days:


`% qacct -d 3 -o hpc -j > qacct.log`


You than parse the output with:


`% egrep 'jobname|jobnumber|failed|exit_status|cpu|ru_w|===' qacct.log > qacct-filtered.log`


![(star)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/star_yellow.svg) The command `egrep` is used to print any line that has one of strings in the quoted list separated by the '|' ('|' that means "or" in this context, see `man egrep`).


# 6. Additional Tools


There is a "*better*" `qstat, namely` `qstat+` and a "*better*" `qacct, namely` `qacct+`


1. `qstat+` runs `qstat` but display things with more details and additional flexibility.
2. `qacct+` queries a database where the accounting info is ingested, it runs faster that `qacct` and returns more info and has additional flexibility.


See the [additional tools page](../additional-tools.md) for instruction how to use these.
