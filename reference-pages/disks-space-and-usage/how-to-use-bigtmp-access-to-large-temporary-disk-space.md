---
title: "How to Use \"bigtmp\" - Access to Large Temporary Disk Space"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152326/How+to+Use+bigtmp+-+Access+to+Large+Temporary+Disk+Space"
date-modified: "2025-04-25"
author: "SGK/MPK"
---

***Update: "bigtmp" is obsolete and will be removed in late 2025. Users are encouraged to use their disk allocation on `/scratch`, or [local SSD storage](how-to-use-local-ssd-space.md)******instead.***


# Introduction


- We have set aside some temporary disk space on the GPFS for jobs who need large temporary disk space, that will not fit on `/tmp` (aka `bigtmp`).
- To manage that space we've implemented a consumable so the job scheduler will not start more jobs requesting space than there is.
- A user can't request more than 25G at a time, in either a single job or as the total of all the job from that user requesting `bigtmp` space.


# How To


- To request large temporary disk space, use `-l bigtmp=XX`, where XX is the amount of disk space needed in GB, like in `-l bigtmp=10` (no unit).
- Use the module `tools/bigtmp` to store the location of the temporary disk space in the `BIGTMP`environment variable.
- Use `$BIGTMP` to specify the temporary disk space location.
- The content of the temporary disk space location is deleted when the job is done.


# Example


Let's assume that `doMyThing`is some application that needs lots of temporary space, and whose location cab be specified with the `-tmp` flag:


```
# /bin/csh
#$ -cwd -j y -o test-bigtmp.log -N test-bigtmp
#$ -l bigtmp=10
#
echo + `date` $JOB_NAME started on $HOSTNAME in $QUEUE with id=$JOB_ID
#
module load tools/bigtmp
#
doMyThing -tmp $BIGTMP
#
echo = `date` $JOB_NAME done.
```
