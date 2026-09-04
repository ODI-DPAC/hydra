---
title: "A Better Qstat: qstat+"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/374604068/A+Better+Qstat+qstat"
date-modified: "2025-12-09"
author: "SGK"
categories: ["hydra7"]
---

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
