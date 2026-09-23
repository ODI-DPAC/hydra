# Job efficiency and warning emails

    - Warning: your disk usage is above 95% of your quota on some disk(s), consider trimming down your usage.
- Disk usage is over 95% on 1 disk
    - Warning: disk usage check found 1 disk with %Use or %IUse >= 95%


## High CPU usage on login nodes


- *What is monitored:* User processes running on the login nodes with high CPU usage for a long time.
- *User action:* Stop the process/command that produced high-CPU usage on the login node and submit as a job or run in the interactive queue.
- *Note*: If the process keeps running, it will be "reniced" twice (priority reduced) and eventually be killed.


### "Process X priority was lowered on hydra-login0[12].si.edu"


```{.text title="Example email"}
Subject: Process 1259315 priority was lowered on hydra-login01.si.edu

  Your command '/process/causing/high-CPU' (PID=1259315 on hydra-login01.si.edu) priority was lowered (renice +5) because:
     used TIME = 26.6 > 20 min
     used %CPU = 98.4 > 45 %

  Remember: jobs/long computations should be submitted to a queue, or run in the interactive queue, not on a login node.
```


*What it means:*


- You have started a process (command) on one of the login nodes that exceeds the allowed CPU time and usage limits.
- The command is still running, but its priority has been reduced (`renice`).
- If the process does not complete or is not terminated within the hard limit on CPU usage on the login node, *it will be automatically killed*.


*Actions to take:*


- What you're doing is using high CPU for a sustained period of time, and this should not be running on one of the login node.
    - *Analyses*: These should be run in the interactive queue or submitted as a job.
    - *File transfers*: Some file transfer programs can produce high CPU. Please contact [si-hpc\@si.edu](mailto:si-hpc@si.edu) for alternative programs that use less CPU.
    - *Conda*: c`onda` commands can use high CPU in the 'solving environment' stage of installing packages.
        - Run the `conda` command in an interactive session.
        - Consider using `mamba` which is much more efficient in the 'solving environment' stage.
        - Create a new conda environment for the installation rather than modifying an existing environment.
    - *File compression and management, e.g. `gzip, zip` `or` `tar`:* Run your commands in an interactive job or submit it as a job.


### "Process X was killed on hydra-login0[12].si.edu"


```{.text title="Example email"}
Subject: [Hydra - alert] Process 1259315 was killed on hydra-login02.si.edu

Dear USER:

  Your command '/process/causing/high-CPU' (PID=1259315 on hydra-login02.si.edu) was killed (kill -9) because:
     used %CPU = 95.4 > 85 %
     used %MEM = 65.9 > 55 %

  Remember: jobs/long computations should be submitted to a queue, or run in the interactive queue, not on a login node.
```


*What it means:*


- The process (command) you were running on one of the login nodes that used too much CPU **was killed (terminated)**.
- This message is preceded by two warning messages.


*Actions to take:*


- Follow the recommendations from the "Process X priority was lowered on hydra-login0[12].si.edu" warning to run the job on the interactive node or as submitted job.
- Confirm that the process that was killed did not produce partial or corrupt files.
    - If the process was related to file transfers, there could partially transferred files and files that were not transferred.
    - For processes like `tar`, a tar file being created may be incomplete and corrupt.


## Inefficient CPU usage of job


- *What is monitored:* Jobs that are using less CPU resources than requested. **When the cluster is heavily loaded, these inefficient jobs may be killed.**
- *User action:* Review resources requested and program-specific arguments that affect CPU usage. Typically, it is fine to adjust these parameters in subsequent jobs that use similar processes rather than deleting your job and re-submitting it.


### "Your inefficient job(s) on Hydra"


```
Dear USER,
You have/had the following number of inefficient jobs running on Hydra over the past 7d:

module load tools/local
check-qlogs ineff -from -7d -user USER

Checking inefficient jobs for unused CPUs (cpuT=33% xtraT=1 ageM=0.5 user='USER')
      from Mon Sep 16 10:20:10 2024
report for Mon Sep 16 10:22:03 2024 to Mon Sep 23 10:12:02 2024

userName             #jobs    total  average unused CPUs [day]
-------------------- ----- -------- -------- 
USER                    3    120.9     40.3

 details are shown only for jobs with unused CPUs > 1 per job [in day]
     jobID name            user              age    nPEs     cpu% queue    node  taskID date/time            unused CPUs
---------- --------------- ---------------- ------ --------- ---- -------- ----- ------ -------------------- ------
   1234567 job1            USER              7:00   12       17.1% lThC.q  75-03        Sep 22 08:20:25 2024   69.6
   1234568 job2            USER             +2:19   12       26.5% lThC.q  84-01        Sep 23 10:12:02 2024   24.6
   1234569 job3            USER             +2:19   12       20.6% lThC.q  64-02        Sep 23 10:12:02 2024   26.6

Review your inefficient job(s), if they are still running, as they do not use as much resources as requested.
Hint: when the cpu% value is equal or close to 100/nPEs your job is not making use of the number of CPUs (aka cores, threads or slots) you have requested. You may not have have passed on the correct argument(s) to your application.
This check is run once a week.
```


*What it means:*


- You've had inefficient jobs, as defined in the [Hydra Policies](../../policies/usage.md), in the last 7 days. This email is sent out weekly and will include inefficient jobs that are still running and recently completed.


*What is shown in the email:*


- The top table is the summary of all your inefficient jobs showing the number of unused (wasted) CPU days.
- In the bottom table, each inefficient job with that had at least one day of unused CPU is listed.
    - `age`: Length the job has been running, in either HH:MM or +DD:HH format.
    - `nPEs`: the number of CPUs requested (aka number or processing elements).
    - `cpu%`: The percentage of `nPEs` that were actually used, i.e. the job's efficiency. For example, 50% means that, on average, half of the CPUs requested were used.
    - `unused CPUs`: the number of CPU days that were not used (wasted).


*User action:*


- Further examine the job scripts and usage statistics for the jobs that are listed in the lower table.
- See the section on [Job Monitoring](monitoring.md) for how to assess your job's CPU use.
    - Are you correctly specifying the number of CPUs for the analysis program to use?
    - Adjust your CPU request or job script for similar jobs that you submit in the future.


### 'You have X running job(s) that use almost no CPU cycles: "hosed"'


```
Dear USER,
The following job is running but using almost no CPU cycles i.e.: efficiency (CPU/age) < 10% and age > 36hr

     jobID name            user                age nPEs      cpu% queue     node taskID
   1234570 job4            USER              +3:13   10      9.9% lThM.q   64-17       
The job is not using all the requested slots (CPUs/cores) or is 'hosed' - consider killing it.
For parallel jobs, when the efficiency (cpu%) value is close 100/nPEs, the job is not making effective use of parallelization, hence poor efficiency.
This check is run once a day to flag very inefficient jobs (i.e.: eff. < 10% and age > 36hr)
```


*What it means:*


- The jobs listed are using CPUs *very* inefficiently. The CPU usage efficiency is <10% and the job has been running more than 36 hours.
    - `age`: Length the job has been running, in either HH:MM or +DD:HH format.
    - `nPEs`: the number of CPUs requested.
    - `cpu%`: The percentage of `nPEs` that were actually used, i.e. the job's efficiency. For example, 50% means on average half of the CPUs requested were used.


*User action:*


- This message can indicate:
    - The job has performed some analyses, but it is now in state where it is no longer using CPUs, that is, it's 'hosed.' You should kill this kind of job.
    - You may not have specified the number of CPUs for the analysis code to use, so the code is only using 1 CPU.
        - This is likely the case if the 100/nPEs is close to the cpu%.
        - This is the case in the example warning message above: `nPEs` = 10 and `cpu%` = 9.9, so `100/nPEs` = 10, which is very close to `cpu%`, which is 9.9.
    - Your analysis software's use of CPUs is not constant throughout the analysis.
        - This can be the case in analysis pipelines where only some processes are able to utilize multiple CPUs.


## Over-use of CPUs by a job


- *What is monitored:* Jobs that are using *more* CPU resources than requested. These jobs can negatively impact other jobs on the compute node.
- *User action:* Since this can negatively impact other users of the compute node, examine the offending job as soon as possible. These jobs may be killed by admins if they are deemed to be negatively impacting the cluster.


### "Your oversubscribed job(s) on Hydra"


```
Dear USER,
You have/had the following number of oversubscribed jobs running on Hydra over the past 7d:

module load tools/local
check-qlogs osub -from -7d -user USER

Checking oversubscribed jobs for excess CPU use (cpuT=133% xtraT=1 ageM=0.5 user='USER')
      from Mon Jul 15 10:20:02 2024
report for Mon Jul 15 10:22:03 2024 to Mon Jul 22 10:12:04 2024

userName             #jobs    total  average excess CPU use [day]
-------------------- ----- -------- -------- 
USER                  1     10.3     10.3

 details are shown only for jobs with excess CPU use > 1 per job [in day]
     jobID name            user              age    nPEs     cpu% queue    node  taskID date/time            excess CPU use
---------- --------------- ---------------- ------ --------- ---- -------- ----- ------ -------------------- ------
   1234571 job5            USER              17:33    8    275.8% mThM.q   64-18        Jul 18 02:57:04 2024   10.3

Consider killing your oversubscribed job(s), if they are still running, and restarting them by requesting the correct resources, or passing on the correct argument(s) to your application. We may, in the future, kill automatically oversubscribed job(s) that have exceeded some CPU usage threshold, especially if/when the cluster load is high.
This check is run once a week.
```


*What it means:*


- You've had jobs in the past week that use more CPUs than requested (oversubscribed). This email is sent out weekly and will include jobs that are still running and recently completed.
    - The top table is the summary of all your oversubscribed jobs showing the number of excess CPU days.
    - In the bottom table, each oversubscribed job with that had at least one day of excess CPU use is listed.
        - `age`: Length the job has been running, in either HH:MM or +DD:HH format.
        - `nPEs`: the number of CPUs requested.
        - `cpu%`: The percentage of `nPEs` that were actually used, i.e. the job's efficiency. These jobs use are >100% meaning that that they used more CPU than requested in the qsub command.
        - `excess CPU use`: the number of extra CPU days that were.


*User action:*


- Further examine the job scripts and usage data for the jobs that are listed in the lower table.
    - See the section on [Job Monitoring](monitoring.md) for how to assess your job's CPU use.
    - Are you correctly specifying the number of CPUs for the analysis program to use?
    - For example, there are some analysis programs that will use all the compute node's CPUs unless you specify otherwise.
    - Adjust your CPU request or job script for similar jobs that you submit in the future.


## Over-reservation of memory


*What is monitored:*Jobs in the himem queues that reserve much more memory than the job uses.


### "Memory Over-Reservation Warning - X job(s) reserved Y times MAXVMEM"


```
Dear USER,
1 of your job(s) reserved 3.0 times the used MAXVMEM so far, on average, as per:

check-memres -details -u USER

 showing all jobs with age > 0.5 day && resd mem > 2.5 maxvmem for user 'USER'
jobid     no of    age    cpu     resd     avg    vmem maxvmem   ratio    eff% user
          slots  [day]  [day]     [GB]    [GB]    [GB]    [GB]   resd/maxvmem  name
--------- ------------  ----- -------- ------- ------- -------   -----   ----- -------
1234572.1     5   25.6   54.2    100.0    33.3    33.4    33.8     3.0    42.3 USER
--------- ------------        -------- ------- ------- -------   -----         -------
In the future, please optimize your memory reservation when submitting jobs since over-reserving memory prevents others from running jobs in the high memory queues.
You can use:

 module load tools/local
 man check-memres
 check-memres -details
to check yourself, and/or consult the HPC Wiki.
This check is run twice a week (Tue & Fri) and issues a warning only if you have jobs, at least 12hr old, that reserved more than 2.5 the amount of memory they have used so far, on average.
```


*What it means:*


- You have one or more running jobs that have reserved (with `m_res`) >2.5x more memory than they are using (`maxvmem`) *and* have been running for more than 12 hours.


*User action:*


- Consult the section on [Job Monitoring](monitoring.md) to review how to assess the resources used by a job.
- Since memory use can fluctuate during analysis, this is best done when the job has completed using a tool like `qacct+`.
- In future submissions of similar analyses, optimize (lower) the amount of memory reserved based on the actual memory use of this job that is triggering a warning.


## Disk(s) quota over 95%


Warning: your disk usage is above 95% of your quota on some disk(s), consider trimming down your usage.


Note that when your quota reaches or exceeds 100% (see ***) you won't be able to write to that disk any longer.


```
Disk quota report: show usage above 95% of quota, as of Fri Oct 31 03:00:11 2025.

Volume=NetApp:vol_home, mounted as /home
                     --  disk   --     --  #files --     default quota: 384.0GB/10.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/home                385.0GB 100.3%     0.05M   0.5% *** NAME, UNIT - USERNAME
/home                371.3GB  96.7%     2.82M  28.2%     NAME, UNIT - USERNAME

Volume=GPFS:scratch_public, mounted as /scratch/public
                     --  disk   --     --  #files --     default quota: 15.00TB/39.8M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/scratch/public      17.20TB 114.7%     3.02M   0.0% *** NAME, UNIT - USERNAME
/scratch/public      15.00TB 100.0%     4.26M   0.0% *** NAME, UNIT - USERNAME

Volume=GPFS:scratch_stri_ap, mounted as /scratch/stri_ap
                     --  disk   --     --  #files --     default quota:  5.00TB/12.6M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/scratch/stri_ap     14.60TB 292.0%     0.05M   0.0% *** NAME, UNIT - USERNAME

Volume=NAS:store_public, mounted as /store/public
                     --  disk   --     --  #files --     default quota:   0.0MB/0.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/store/public         4.80TB  96.1%        -      -      NAME, UNIT - USERNAME
```


*What it means:*


- You are close or have exceeded your quota on one or more disks, whether disk space or number of files.
- Lines with `***` mark quota exceeded


*User action:*


- Trim down your disk usage.
- If you have too many small files, consolidate them into an archive.
- See documentation on disk space and usage.


## Disk usage is over 95% on 1 disk


Warning: disk usage check found 1 disk with %Use or %IUse >= 95%


```
Filesystem                     Type  Size  Used Avail   Use% Inodes IUsed IFree  IUse% File [shown only when Use% or IUse% >= 95%]
gpfs02:sao_atmos               gpfs  350T  331T   20T    95%   280M   27M  254M    10% /scratch/sao_atmos

Details for /scratch/sao_atmos
Disk quota report: show usage above 5% of quota, (warning when quota > 95%),
   on /scratch/sao_atmos (scratch_sao_atmos),
   show only top 5 users, as of Thu Oct 30 15:00:10 2025.

Volume=GPFS:scratch_sao_atmos, mounted as /scratch/sao_atmos
                     --  disk   --     --  #files --     default quota: 350.0TB/307.2M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/scratch/sao_atmos   92.80TB  26.5%     3.03M   0.0%     NAME, UNIT - USERNAME
/scratch/sao_atmos   50.40TB  14.4%     0.32M   0.0%     NAME, UNIT - USERNAME
/scratch/sao_atmos   50.30TB  14.4%     0.93M   0.0%     NAME, UNIT - USERNAME
/scratch/sao_atmos   47.10TB  13.5%    11.14M   0.0%     NAME, UNIT - USERNAME
/scratch/sao_atmos   21.60TB   6.2%     1.77M   0.0%     NAME, UNIT - USERNAME
```


*What it means:*


- One or more disks are close to being full.
- You have files on at least one of them.


*User action:*


- Trim down your disk usage.
- If you have too many small files, consolidate them into an archive.
- See documentation on disk space and usage.


