# Monitoring jobs



## Introduction


After submitting a job, or a set of jobs, with `qsub`, you can


- check on your job(s) with the command `qstat,`
- kill your job(s) with the command `qdel,`
- alter the requested resources of a queued job with `qalter` ,
- check on a finished job with `qacct` ,
- use Hydra-specific home-grown tools`.`


## How to Check on Jobs


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
you are most likely requested a scarce resource, or more of a resource than is available. In this case, feel free to [contact us](concepts.md).
- Jobs in the `t`status are in most cases about to get started.
- Jobs in the `d` status are about to be deleted and/or killed.


We provide a tool, q+, that uses `qstat` to provide an easier way to monitor jobs and the status of the queue.


## How to Delete/Kill a Job or Jobs


These are instructions for how to stop a running job or delete a submitted job that has not started running yet.


The `qdel` command (`man qdel`) allows you to either:


- delete a job from the queue (for job in the "`qw`" status), or
- kill a running job (for jobs in the `"r`" status).


You delete/kill a specific job by its job id as follows:


`% qdel 4615585`


or you can kill *all* your jobs (queued and running) with


`% qdel -u $USER`


Here is a trick to kill a slew of jobs, but not all of them:


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


You can use `grep` to better filter the output of `qstat`, like this:


```
qstat -u $USER | grep $USER | grep rax | awk '{print "qdel", $1}' > qdel.sou
[edit the file qdel.sou]
source qdel.sou
```


This example


- filters the output of `qstat` for lines with your user name and
- with the string "`rax`" to identify a sub set of jobs via their job name.


You can add `"-s r"` or "`-s p`" to `qstat` to limit the list of job IDs to only your running or pending (queued) jobs.


## Modifying a Queued Job


The `qalter` command allows you to alter (modify) the properties of a job, namely its requested resources or parameters.


You can alter


- most of the properties of a queued job;
- and a few of its properties once it has started.


For example:


<table class="wrapped confluenceTable"><colgroup><col/><col/></colgroup><tbody><tr><th class="confluenceTh" colspan="1">you can</th><th class="confluenceTh" colspan="1">with</th></tr><tr><td class="confluenceTd" style="margin-left: 30.0px;">move a queued job to a different queue with</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -q mThC.q &lt;jobid&gt;</code></span></td></tr><tr><td class="confluenceTd">change the name of the job's output file</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -o run-3.log &lt;jobid&gt;</code></span></td></tr><tr><td class="confluenceTd">change whether you want email notifications</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -m abe &lt;jobid&gt;</code></span></td></tr><tr><td class="confluenceTd">change the requested amount of CPU</td><td class="confluenceTd"><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>% qalter -l s_cpu=240:: &lt;jobid&gt;</code></span></td></tr></tbody></table>


where `<jobid>` is the job ID (see `man qalter`.)


## Checking on a Completed Job


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


Users that run jobs in the high memory queues can use this to check if they used close to the amount of memory they have reserved.


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


The command `egrep` is used to print any line that has one of strings in the quoted list separated by the '|' ('|' that means "or" in this context, see `man egrep`).


## Additional Tools


There is a "*better*" `qstat, namely` `qstat+` and a "*better*" `qacct, namely` `qacct+`


1. `qstat+` runs `qstat` but display things with more details and additional flexibility.
2. `qacct+` queries a database where the accounting info is ingested, it runs faster that `qacct` and returns more info and has additional flexibility.


See the additional tools page for instruction how to use these.

## Cluster Monitoring



### Cluster Status


The command


`% qstat -g c`


returns the cluster status, in a tabular form, i.e.:


```
CLUSTER QUEUE                   CQLOAD   USED    RES  AVAIL  TOTAL aoACDS  cdsuE  
--------------------------------------------------------------------------------  
all.q                             -nan      0      0      0      0      0      0 
lTIO.sq                           0.00      0      0      8      8      0      0 
lTb2g.q                           0.27      0      0      2      2      0      0 
lTgpu.q                           0.00      0      0     64     64      0      0 
lThC.q                            0.38    634      0   4374   5008      0      0 
lThM.q                            0.37    390      0   4162   4552      0      0 
lThMuVM.tq                        0.28      0      0    384    384      0      0 
mTgpu.q                           0.00      0      0     64     64      0      0 
mThC.q                            0.38   1331      0   3677   5008      0      0 
mThM.q                            0.37     14      0   4538   4552      0      0 
qgpu.iq                           0.00      4      0     60     64      0      0 
qrsh.iq                           0.00     11      0     29     40      0      0 
sTgpu.q                           0.00      0      0     64     64      0      0 
sThC.q                            0.38      5      0   5003   5008      0      0 
sThM.q                            0.33      0      0   5032   5032      0      0 
uThC.q                            0.38      8      0   5000   5008      0      0 
uThM.q                            0.37     70      0   4482   4552      0      0 
uTxlM.rq                          0.00      0      0    480    480      0      0 
```


You can also use


`% qstat+ -gc`


(no space in `-gc) to get:`


```
   ---- queue ----  ----- #nodes ---- - ---------- #slots ----------- - ------------
    name       load  total avail  down - total used  resvd  down avail - %full  %eff

   sThC.q   1880.5     63    63     0 -  5008     5     0     0  5003 -   0.1
   mThC.q   1880.5     63    63     0 -  5008  1331     0     0  3677 -  26.6
   lThC.q   1880.5     63    63     0 -  5008   634     0     0  4374 -  12.7
   uThC.q   1880.5     63    63     0 -  5008     8     0     0  5000 -   0.2  95.1

   sThM.q   1662.8     55    55     0 -  5032     0     0     0  5032 -   0.0
   mThM.q   1662.5     52    52     0 -  4552    14     0     0  4538 -   0.3
   lThM.q   1662.5     52    52     0 -  4552   390     0     0  4162 -   8.6
   uThM.q   1662.5     52    52     0 -  4552    70     0     0  4482 -   1.5 350.7

   uTxlM.rq    0.2      3     3     0 -   480     0     0     0   480 -   0.0   0.0

   lTIO.sq     0.0      2     2     0 -     8     0     0     0     8 -   0.0   0.0

   sTgpu.q     0.0      1     1     0 -    64     0     0     0    64 -   0.0
   mTgpu.q     0.0      1     1     0 -    64     0     0     0    64 -   0.0
   lTgpu.q     0.0      1     1     0 -    64     0     0     0    64 -   0.0   0.0

   qgpu.iq     0.0      1     1     0 -    64     4     0     0    60 -   6.2
   qrsh.iq     0.1      2     2     0 -    40    11     0     0    29 -  27.5
```


the actual numeric values will be slightly different when you run these commands, since they reflect the precise configuration and the load.


### Compute Nodes Status


The command


`% qhost`


returns the list of hosts (compute nodes) and their respective properties.


Under UGE, `qhost` alone returns more columns (equiv to `qhost -cb` under SGE). The option `-ncb` returns the same columns as in SGE.


You can restrict the list by specifying the hosts, like


`% qhost -h compute-64-02 compute-64-03`


but you can't use `RE`s. So you use a filter, like `egrep`, to parse its output:


`% qhost | egrep 'LOAD|e-[46]'`


This will print any line with either the string '`LOAD`' or a line that matches the `RE` `"e-[46]`", and will thus match `compute-4`, `compute-6`, etc....


The utility`egrep` combined with `RE`s (regular expressions) can be a very powerful filter.


The command `qhost` takes the "`-q`" or the "`-j`" option to show the queues or the jobs associated with each host(s):


| `qhost -q -h compute-64-02` | show which queues include the compute node 64-02 |
| --- | --- |
| `qhost -j -h compute-64-02` | show which jobs are running on the compute node 64-02 |


There is also a `qhost+` command, see the Additional Tools page.


### Query the Cluster Configuration


The command `qconf` is used to both set and query the queue configuration.


All the options of `qconf` that start with `-s` correspond to a query: i.e., show something.


The following options may be useful:


| `-sc` | show complex attributes |
| --- | --- |
| `-sconfl` | show a list of all local configurations |
| `-sconf [host_list]` | show configurations |
| `-shgrpl` | show host group list |
| `-shgrp group` | show host group |
| `-srqsl` | show resource quota set list |
| `-srqs [rqs_list]` | show resource quota set(s) |
| `-spl` | show all parallel environments |
| `-sp pe-name` | show a parallel environment |
| `-sql` | show a list of all queues |
| `-sq [queue_list]` | show the given queue |
| `-ssconf` | show scheduler configuration |
| `-sul` | show a list of all userset lists |
| `-su listname_list` | show the given userset list |


Use the command


`% qconf -srqs`


to query the resource quota set, *i.e.* the limits on queues, or


`% qconf -srqs u_slots`


to query a specific quota.


Use the command


`% qconf -sq sThM.q`


to show the configuration of the `sThM.q` queue. Some of the options to the command `qconf` take `RE`s, so for example the command:


`% qconf -sq '?ThM.q' | egrep 'qname|s_cpu|s_rt'`


returns the soft CPU and R/T limits for all the hi-mem queues, using egrep to filter the output of `qconf`, namely:


```
qname                 lThM.q
s_rt                  1440:00:00
s_cpu                 720:00:00
qname                 mThM.q
s_rt                  144:00:00
s_cpu                 72:00:00
qname                 sThM.q
s_rt                  14:00:00
s_cpu                 7:00:00
qname                 uThM.q
s_rt                  INFINITY
s_cpu                 INFINITY
```


### Cluster Status Web Page


We also maintain a cluster status web page that can be accessed  at https://hydra-7.si.edu/tools/status/ as long as you are on SINet or the SI VPN.

- You can specify up to 3 arguments to the URL, especially useful if you bookmark it, to specify either:
    1. the sorting in the cluster snapshot graph with `sortby=`, like in `sortby=nCPU`
    2. the length of the plots vs time with `len=`, like in `len=7d`
    3. which user's job(s) to highlight with `user=`, like in `user=hpc`
- by adding "`?``sortby=nCPU&user=hpc&len=15d`" to the URL; valid values for each parameter are those listed in the corresponding drop down menus.


These pages give you a good overview of the cluster current status and past usage, and include the disk space usage information.

## A Better Qstat: qstat+

- `qstat+` is a PERL wrapper around `qstat`: it runs `qstat` for you and parses its output to display it in a more friendly format.
    - `q+` is a shorthand for `qstat+.```
- How to use `qstat+` is explained in the man page (`man qstat+` ) and is described by:


% qstat+ -help


or


% qstat+ -examples


- It can be used to
    - get useful info like the age and/or the cpu usage (in % of the job age) of running jobs,
    - get the list of nodes a parallel job is running on (if you haven't saved it),
    - get a filtered version of `qstat -j <jobid>`, and
    - get an overview of the cluster queues usage.


Namely:


```{.text title="qstat+ -help"}
usage: qstat+ [mode] [options]
  where modes are (exclusive list):
    -s|-sx|-sc      show summary (simple, extended or compact)
    -a              show all jobs
    -q              show queued jobs
    -r              show running jobs
    -X              show extra jobs (dr, Eqw, t)
    -j      JID     show info on a specific job
    -nlist  JID     show node list for a (set of) job(s)
    -hiload N       show node(s) with high load
    -gc             show global cluster status
    -es[x]          show empty slots, -esx: expanded info
    -down           show node(s) that are down
    -ores           show overreserved jobs, i.e.: resMem/maxVMem > 2.5, & age > 1 hr
    -osub           show oversubscribed jobs, i.e.: cpu% > 133%, & age > 1 hr
    -ineff          show inefficient jobs, i.e.: cpu% < 33%, & age > 1 hr
    -ssd            show SSD usage
    -h|-help--help  show help
    -examples       show examples

where options are:
    -u USER       limit to the specified user, you can use "*" or "all" to list everybody's jobs
                  or a coma-separated list
    -njobs        show counts in no. of jobs
    -npes         show counts in no. of PEs (slots)
    -nqpe         show jobs/PEs not jobs/tasks for queued jobs
    -nqxx         show jobs/tasks/PEs for queued jobs
    -load         show the nodes' load
    -sua          show the nodes' used/avail no of slots
    -age          show the age of the jobs, i.e., elapsed time vs starting/submit time
    -cpu          show the amount of CPU used by running job(s)
    -cpu%         show the amount of CPU/age/#PE in % (job efficiency)
    -cpur         show the ratio CPU/AGE, not scaled by #PE
    -mem          show the mean memory usage for running jobs, the total requested memory for queued jobs, in GB
    -memx         show more memory info for running jobs: reserved, mean, vmem and maxvmem (slow)
    -memr         show more memory info for running jobs: reserved, mean, maxvmem and res/mxvmem (slow)
    -io           show the I/O usage
    -iow          show the I/O wait usage (slow)
    -ioops        show the IOPs usage (slow)
    +lic          show license info (default), although not in detailed outputs
    -lic          do not show license info

    -Su           sort by user
    -Sn           sort by node
    -Ln    VAL    limit to node(s) given by VAL - RE OK

    -noheader     do not show the header
    -nofooter     do not show the footer
    -raw          print raw values (for easier parsing)
    -queue QSPEC  limit to jobs in queue QSPEC (RE ok)
    -oresF  VAL   change the overreserved factor to VAL
    -osubT  VAL   change the oversubscribed threshold to VAL, in %
    -osubE  VAL   set the oversubscribtion excess threshold to VAL, in hr x slots
    -ineffT VAL   change the inefficient threshold to VAL, in %
    -ageT   VAL   change the minimum age threshold to VAL, in hour

    -v|-verbose   set verbose mode
    -warn         show warnings
    -wide         wide output (132 cols, implies -notty)
    -notty        do not use the width of the terminal, as returned by stty
    -check-load   check the instantanous load (-hiload only)

shorthands:
    +a   is expanded to -a -u $USER -nofooter             show all your jobs
    +a%                 -a -u $USER -nofooter -age -cpu%  ibidem, with cpu on % of age
    +ax%                -a -u $USER -nofooter -age -cpu% -load -sua -mem -io
    +ar%                -a -u $USER -nofooter -age -cpu% -memr -io
    +r                  -r -u $USER -nofooter             show all your running jobs
    +r%                 -r -u $USER -nofooter -age -cpu%  ibidem, with cpu on % of age
    +rr%                -r -u $USER -nofooter -age -cpu% -memr -io -iow -ioops
    +rx%                -r -u $USER -nofooter -age -cpu% -load -sua -memx -io -iow -ioops
    +q                  -q -u $USER -nofooter             show all your queued jobs
    +q%                 -q -u $USER -nofooter -age        ibidem but show age
    +qx%                -q -u $USER -nofooter -age -mem   ibidem plus mem info
    +X                  -X -u $USER -nofooter             show all your extra jobs
    +n                  -notty -wide -noheader -nofooter

qstat+: Ver 5.8/1 - Dec 2025
```


```{.text title="qstat+ -examples"}
examples:
 qstat+ -a -u hpc                   show all of hpc's jobs
 qstat+ -r -cpu% -u hpc             show all of hpc's running jobs, cpu in %
 qstat+ -r -cpu% -load -sua -u hpc  show all of hpc's running jobs, cpu in %, and
                                the nodes' load and slot usage/availability
 qstat+ -q                          show all the queued jobs
 qstat+ -j 8683280,8683285          show info on specific job IDs
 qstat+ -nlist 8683280,8683285      show nodes list for specific job IDs
 qstat+ -hiload 1.5                 show nodes whose load is 1.5 greater than the number of slots used
 qstat+ -ineffT 50 -ineff           show jobs that are below a 50% efficiency threshold
 qstat+ -osubT 200 -ageT 48 -osub   show jobs that are above a 200% usage threshold and are older than 48 hours
 qstat+ -gc                         show the global cluster status
 qstat+ -es                         show the empty slots
 qstat+ -down                       show which nodes are down

        +ax% -u all                 is equiv to -a -u all -cpu% -load -sua -mem
                             etc... for the +XXX shorthands

qstat+: Ver 5.8/1 - Dec 2025
```

## A Better Qacct: qacct+

- The accounting information is ingested into a SQL compatible data base by the GridEngine (aka ARCo - for Accounting and Reporting Console)
    - The ingestion is done at regular intervals, hence the database is not instantaneously synchronized (less than a minute lag usually).
    - As of Hydra-7, we use GE's dbwriter (aka ARCo) and PostgreSQL as the DB engine
        - although we discovered some bugs under 8.8.1, where some fields are not properly ingested.
- That database can be queried with `qacct+`, hence
    - `qacct+` is often faster than `qacct`
    - `qacct+` its output can be customized, and
    - `qacct+` computes derived values.
- How to use `qacct+` is explained in the man page (`man qacct+`) and is described by:


`% qacct+ -help` 
or 
`% qacct+ -show help`


Namely:


```{.text title="qacct+ -help"}
usage: qacct+ [options] where options are

                   to limit query to
  -j|--job_number  <jobid>    given job  ID(s),    single value, comma separated list, or range like in n:m
  -t|--task_number <taskid>   given task ID(s),    single value, comma separated list, or range like in n:m
  -o|--owner       <owner>    given owner,         exact match

  -b|--back        <number>   jobs submitted  >= (now - n) days,  (def. 92 days ago)
  -s|--since       <date>     jobs submitted  >= date,   like "4/27/2016 10:00AM"
  -u|--until       <date>     jobs submitted  <= date,   like "4/27/2016 11:00AM"

                   to specify what to show
  -show            <string>                                       (def.: -show simple)
                   where <string> can be:
                     "simple", "simple+", "tab", "tab+", "gpu", "gpu+" or "raw",
                   or "fields", "explain", or "help", or a custom specification

                   to limit output to
  -m|--show_max    <number>   max number of entries to show (when querying more than one job)

  -w|--col_width   <number>   width of columns in tabular mode   (def.: 15)
  -d|--date_format <number>   how to format dates, n=-1,0,1 for YYYY/MM/DD, Mon DD YYY, MM/DD/YYYY, (def. 0)

  -n|--dry_run                dry run, use w/ -v to check the resulting SQL search
  -v[=value]                  verbose mode (repeat to increase verbosity, -v=2 equiv to -v -v)
  -i|--init         <file>    mysql initialization file(s),      (def.: /share/apps/tools/local-user/.qacct+.cnf, /home/hpc/.my.cnf)

  -h|--help                   show this help
  use -show help to get additional help on how to use -show <string>

  Ver. 5.3/1 (Oct 2025/SGK)
```


- and by


`% qacct+ -show help`


```{.text title="qacct+ -show help"}
  -show  <string> specify what to show

  i.e.
    -show simple  for simple format (default)
    -show simple+ for extension of the simple format
    -show tab     for tabular format
    -show tab+    for extension of the tabular format
    -show gpu     for GPU format
    -show gpu+    for extension of the GPU format
    -show raw     for raw format

  or a list of which keyword to show, with an optional format, where <string> is either
    +field1[=format1][,field2[=format2]]  for keyed format
  or
    %field1[=format1][,field2[=format2]]  for tabular format

  the format is either a C format specification like %d, %s, %.1f, or
  the values @DATE, @MEM, or @AGE to convert the numeric to a date, a memory (or volume) or an age,
  or @GPUSE or @GPUSE(var1|var2|...) to format the gpu_usage value,
     where varX is/are used to match a specific gpu_usage parameter

  for instance:
    -show +qname,slots,wallclock=@AGE,cpu=%.1f
  or
    -show %qname,slots,wallclock,cpu=%-15.1f,granted_pe
  or
    -show '+cpu,gpus,gpu_usage=@GPUSE(process|Util|therm|board)'

  use -show fields           to list all the available fields
  use -show explain_failed   to list the failed codes explanations
```

## Checking a Compute Node with rtop+

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

## Checking Memory and CPU Usage

- `plot-qmemuse:`a tool to plot the memory and CPU usage of jobs that ran recently or are running in the high memory queues.
- We monitor the jobs running in the high-memory queue, taking a usage snapshot every five minutes. This tool only applies to jobs in the high-memory queues
- The resulting statistics can be used to visualize the resources usage of a given job with the command `plot-qmemuse`, using


`% plot-qmemuse <jobid>`


``or


`% plot-qmemuse <jobid>.<taskid>`


For that command to run, you must load the `gnuplot module` first. By default this tool produces a plot in a 850x850 pixels `png` file.


You can specify the following options:


| `-l <label>` | to add your own label on the plot |
| --- | --- |
| `-s <size>` | to specify the plot size, in pixel (-s 1200 for a 1200x1200 plot) |
| `-o <filename>` | to specify the name of the `png` file |
| `-x` | to plot on the screen (using `X11`, assuming your connection to hydra allows `X11`) |


You can view the plot in the `png` file with the command `display <filename>`, assuming that your connection to hydra allows `X11`, or


you can copy that file to your local machine and view it with your browser or a png-compatible image viewer (like `xv`).

## More Tools



### Local Tools


The following tools are always available since the module `tools/local-user` is *always*loaded:


| `check-qwait` | show job(s) waiting in the queue and associated queue quota limits |  |
| --- | --- | --- |
| `check-gpu-use` | show cluster GPUs usage |  |
| `finger` | replacement for CentOS7 `finger` | use `pinky -l` |
| `get-gpu-info` | print information about GPU |  |
| `monitor-code-usage` | helps you monitor your code usage |  |
| `plot-qmemuse` | plot memory and cpu usage as a function of time for a given jobID |  |
| `plot-qssduse` | plot SSD usage as a function of time for a given jobID |  |
| `qacct+` | a "better" `qacct` | show accounting information for completed jobs |
| `qchain` | chains a set of jobs by adding the -hold_jid <jobID> to qsub for you |  |
| `qquota+` | a "better" `qquota` | show queue quota wrt queue limits |
| `qstat+` | a "better" `qstat` | show queue status |
| `quota+` | a "better" quo`t`a | show disk quota information for all type (NFS, GPFS, NAS) |
| `q-wait` | wait until some jobs are not found in the queue |  |
| `rpstree+` | remote `pstree -paul` | show process tree on given compute node |
| `rtop+` | remote `top` | show what is running on given compute node |
| `ruptime` | replacement for `ruptime` | limited to head, login and NSDs |
| `rwho` | replacement for `rwho` | limited to head, login and NSDs |
| `show-qmemuse` | show memory use statistics |  |
| `show-qslots` | shows how many slots are available in the queue(s) |  |
| `show-qssduse` | log statistics for `plot-qssduse` |  |


The following tools are available when loading the module `tools/local-admin:`


| `chage+` | substitute to `chage`, to query LDAP properties | ie: chage+ $USER |
| --- | --- | --- |
| `check-disks-usage` | check disks usage, and print warning when usage exceed a threshold | ie: `check-disks-usage -w 10` |
| `check-hi-memuse` | check for memory use versus reservation and CPU usage efficiency |  |
| `check-memres` | check for jobs that use less memory than the amount reserved |  |
| `check-memuse` | print the cluster usage (memory and CPUs) |  |
| `check-qlogs` | return a report on either oversubscribed or inefficient jobs |  |
| `disk-usage` | return information on disk usage |  |
| `find-all-zombies` | find zombies |  |
| `get-cpu_arch` | return CPU architecture |  |
| `parse-disk-quota-reports` | return report by parsing the disk quota report |  |
| `plot-disk-dev` | plot usage of a given device |  |
| `plot-disk-usage` | plot the usage of a given disk (volume) |  |
| `plot-gpfs-info` | plot GPFS information |  |
| `plot-ibtraffic` | plot IB traffic |  |
| `plot-qsnapshot` | plot a snapshot of cluster usage |  |
| `plot-qssduse-summary` | plot SSD usage summary as a function of time |  |
| `plot-qstat` | plot the queue status of the cluster |  |
| `plot-ruptime` | plot the load (output of `ruptime`) of the non-compute nodes |  |
| `qhost+` | a "better" qhost |  |
| `rkill` | remote `kill` |  |
| `rkillall` | remote `killall` |  |


Each tool has a man page, accessible after you load the module `tools/local`.


### Local+ Tools


The following tools are available when loading the module `tools/local+`;


<table class="wrapped fixed-width confluenceTable" style="width: 82.4688%;"><colgroup><col style="width: 18.5678%;"/><col style="width: 38.1715%;"/><col style="width: 43.2607%;"/></colgroup><tbody><tr><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><p><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>backup</code></span></p></td><td class="confluenceTd"><p>backup a file</p></td><td class="confluenceTd" colspan="1">ie: <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>mv </code><span style="color:var(--ds-text,#172b4d);">or</span></span><code><span style="color:var(--ds-text-accent-blue,#0055cc);"> cp file</span> to <span style="color:var(--ds-text-accent-blue,#0055cc);">file.&lt;n&gt;</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">centos-version</span></code></td><td class="confluenceTd" colspan="1">print the OS flavor &amp; version</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">check-hosts</span></code></td><td class="confluenceTd" colspan="1">print the cluster usage (memory and CPUs), as aggregate by logical rack</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">check-qacct</span></code></td><td class="confluenceTd" colspan="1">show statistics of resources usage for completed jobs</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">dus-report</span></code></td><td class="confluenceTd" colspan="1">run and parse <code><span style="color:var(--ds-text-accent-blue,#0055cc);">du</span></code> to produce a disk usage report</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">elapsed</span></code></td><td class="confluenceTd" colspan="1">print elapsed time between each call</td><td class="confluenceTd" colspan="1">ie; <code><span style="color:var(--ds-text-accent-blue,#0055cc);">elapsed; ...do something...; elapsed</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">fixFmt</span></code></td><td class="confluenceTd" colspan="1"><p>format a number with fixed number of digits</p></td><td class="confluenceTd" colspan="1"><p><code><span style="color:var(--ds-text,#172b4d);">csh:</span><span style="color:var(--ds-text-accent-blue,#0055cc);">    \@ n = 1; set N = `fixFmt 3 $n`</span></code></p><p><code><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#172b4d);">[ba]sh:</span> n=1; N=`fixFmt 3 $n`</span></code></p><p><code><span style="color:var(--ds-text-accent-blue,#0055cc);">        echo n=$n N=$N → n=1 N=001</span></code></p></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">get-jobhr</span></code></td><td class="confluenceTd" colspan="1">tool to retrieve a job hard resources (<code>mem_res h_data h_vmem</code>) in a job script</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">lsth</span></code></td><td class="confluenceTd" colspan="1"><p>show most recent files</p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">lsth <span>[-40]</span> <span>[&lt;spec&gt;</span>]</span> </code>→ <code><span style="color:var(--ds-text-accent-blue,#0055cc);">ls -lt &lt;spec&gt; | head -40</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">lswc</span></code></td><td class="confluenceTd" colspan="1"><p>count number of files in directories</p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">lswc dir/</span></code> → <code><span style="color:var(--ds-text-accent-blue,#0055cc);">ls dir/ | wc -l</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">noX</span></code></td><td class="confluenceTd" colspan="1">tool to unset <code>DISPLAY</code> (saved in <code>XDISPLAY</code>)</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">p-wait</span></code></td><td class="confluenceTd" colspan="1"><p>wait until given PID has completed</p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">p-wait <span>[check-time</span>] &lt;PID&gt;</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">pawk</span></code></td><td class="confluenceTd" colspan="1"><p>print with <code><span style="color:var(--ds-text-accent-blue,#0055cc);">awk</span></code><span class="error"><br/></span></p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">pawk 1,hello,3</span></code> → <code><span style="color:var(--ds-text-accent-blue,#0055cc);">awk '<span class="error">{print $1,"hello",$3}</span>'</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">print-proc-memory</span></code></td><td class="confluenceTd" colspan="1">print nicely content of <code><span style="color:var(--ds-text-accent-blue,#0055cc);">/proc/memory</span></code></td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">procinfo</span></code></td><td class="confluenceTd" colspan="1">print properties of local machine (#CPUs, memory, OS)</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">procinfo+</span></code></td><td class="confluenceTd" colspan="1">print properties of local machine (#CPUs, memory, OS, etc...)</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">tails</span></code></td><td class="confluenceTd" colspan="1"><p>run tail <span>[options</span>] on a set of files</p></td><td class="confluenceTd" colspan="1">ie: "<code><span style="color:var(--ds-text-accent-blue,#0055cc);">tail -3 *pl</span></code>" fails "<code><span style="color:var(--ds-text-accent-blue,#0055cc);">tails -3 *pl</span></code>" OK</td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">total</span></code></td><td class="confluenceTd" colspan="1">compute the total of values at given column of a file</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">useX</span></code></td><td class="confluenceTd" colspan="1">tool to reset <code>DISPLAY</code> (from <code>XDISPLAY</code>), revert effect of noX</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">xterm-config</span></code></td><td class="confluenceTd" colspan="1">tool to configure <code>xterm</code> window properties</td><td class="confluenceTd" colspan="1"><br/></td></tr></tbody></table>


Each tool has a man page, accessible after you load the module `tools/local+`.


### Misc Tools


- A set of tools are available by loading the `tools/misc` module.
- Currently these are disk usage analysis tools, namely:


| `dua` | a tool to learn about disk usage |
| --- | --- |
| `dus+` | disk usage report (same as `dus-report`in `tools/local+`) |
| `dut` | disk usage calculator |
| `gdu` | disk usage analyzer written in Go |
| `ncdu` | ncurses disk usage |


### Also Available


- The following tools are also available:


| module | command | description |
| --- | --- | --- |
| `tools/awscli` | aws, aws_completer | CLI to access AWS |
| `tools/cmake` | cmake |  |
| `tools/ffsend` | ffsend, ffupload, ffdownload |  |
| `tools/gv` | gv |  |
| `tools/rclone` | rclone |  |
| `tools/ruby` | ruby |  |
| `tools/svn` | svn |  |
| `tools/vscode` | vscode |  |
| `tools/wget` | wget |  |
| `tools/xv` | xv |  |


- use:


`module whatis <modulename>`to list the versions available,


`module help <modulename>` to get help
