---
title: "How to Use NAS Storage and the I/O Queue"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152325/How+to+Use+NAS+Storage+and+the+I+O+Queue"
date-modified: "2019-07-04"
author: "SGK"
---

# Near Line Storage or NAS


- A large near-line storage of about 950TB has been added to Hydra in July 2019 as NAS and mounted via NFS.
- This storage is mounted as `/store`, *but only* on both login nodes. the head node and the interactive nodes.
- It is not (*and will not be*) mounted to the rest of the compute nodes.
    - Hence data stored on the NAS are to be copied to active storage (e.g. `/data`, or `/scratch`) before processing and/or analyzing your data, and vice-versa (active storage can be offloaded to `/store`).
- Most of that disk space is project-specific space, but there is a small amount of space on that system available to all other users upon request and at no cost.
- Approved users will receive up to 5TB of un-scrubbed space, with a daily snapshot up to 14 days.
    - Note that we reserve the right to clean up old stuff that is likely to accumulate in the future, with proper notification, once it fills up.


Users interested in receiving an allocation in `/store/public` should contact [Hydra admin](mailto:si-hpc-admin@si.edu).


## Additional Technical Details


- This NAS is storage is build on a zfs file system and runs FreeNAS (a dedicated Linux version for NAS/NFS).
- It supports quotas and snapshots, although not the full gamut that NetApp and GPFS offers.
- This system is fault tolerant (when a disk fails it keeps running fine) but not high availability (i.e. there is no full hardware redundancy), so it is intrinsically less robust (hence less expensive) than the NetApp and the soon to arrive GPFS.
- Like all the disks on Hydra, its content is NOT backed up, and while we do not expect catastrophic failures, keep all this in mind.
- It is to be thought of as a “*cheap bucket*” to keep things around awaiting processing, not for backup, archiving or any other form of reliable & long term storage.


Also, the Linux command `quota` does work with the NAS/zfs, instead use `quota+.pl` (part of the `tools/local` module).


# Accessing `/store`


- You can access `/store` from either login node. You can also access via the interactive queue, using `qrsh`.
    - Remember that the limits on login node usage and on `qrsh`jobs are in effect.
- Alternatively, you can also access `/store` via the IO queue with its specific limits.
- Submitting jobs to the IO queue allows you to (1) have larger limits, (2) queue a slew of IO jobs and (3) chain IO and processing jobs using the scheduler.


## The IO Queue


- We have added an IO queue, called `lTIO.q`, so users can do copy data to/from the NAS through batch jobs (`qsub`).
- The IO queue runs on the interactive compute nodes, using a limited number of slots.


To submit an IO job, specify `-q lTIO.q -l ioq` as arguments to `qsub` or as an embedded directive in the job file.


```{.text title="Here is a trivial IO job file:"}
#
#$ -cwd -j y -N testIO
#$ -o testIO.log
#$ -q lTIO.sq -l ioq
#
echo + `date` $JOB_NAME running on $HOSTNAME in $QUEUE with jobID=$JOB_ID
set echo
ls -ld /store/sylvain
ls -l /store/sylvain/*
df -h /store/sylvain
unset echo
echo = `date` $JOB_NAME done
```


### Limits


- Jobs in the IO queue can run for 72 hours, and are limited to consuming no more than 12h of CPU and 8GB of memory (per slot).
    - hence IO jobs are not meant to be used to run computations on data stored on the NAS
- Users can run only 2 IO jobs concurrently and use up to 6 slots.
- You can submit as many IO jobs as needed, keeping in mind the total limit of 2,000 running and queued jobs per user.


### Hints


- You can tell the scheduler to chain jobs to run sequentially, using the `-hold_jid NNN` argument to `qsub`, where NNN is a job number, the number of the job to wait for completion).
- Here is a conceptual example to chain an analysis job to start only after an IO job completes, and then run a save and clean job.


```
% qsub getData.job
Your job 7437744 ("getData") has been submitted
% qsub -hold_jid 7437744 analyze.job
Your job 7437745 ("analyze") has been submitted
% qsub -hold_jid 7437745 saveNClean.job
Your job 7437746 ("saveNClean") has been submitted
```


- and `qstat+.pl +a%` returns:


```
Total running (PEs/jobs) = 1/1, 2 queued (jobs) for user 'hpc'.
   jobID name                     stat     age nPEs      cpu% queue     node taskID
 7437744 getData                     r   00:01    1           lTIO.sq  8-31
 7437745 analyze                   hqw   00:00    1           sThC.q
 7437746 saveNClean                hqw   00:00    1           lTIO.sq
```


where `hqw` indicates a wait in the queue on a hold.


- Or you can use `qchain`to do this for you:


```
% qchain getData.job  analyze.job saveNClean.job
qsub getData.job
Your job 7437747 ("getData") has been submitted
qsub -hold_jid 7437747 analyze.job
Your job 7437748 ("analyze") has been submitted
qsub -hold_jid 7437748 saveNClean.job
Your job 7437749 ("saveNClean") has been submitted
```


- resulting as above in:


```
% q+ +a%
Total running (PEs/jobs) = 1/1, 2 queued (jobs) for user 'hpc'.
   jobID name                     stat     age nPEs      cpu% queue     node taskID
 7437747 getData                     r   00:00    1          lTIO.sq   8-32
 7437748 analyze                   hqw   00:00    1          sThC.q
 7437749 saveNClean                hqw   00:00    1          lTIO.sq
```


- Use `man` qchain for more info.
