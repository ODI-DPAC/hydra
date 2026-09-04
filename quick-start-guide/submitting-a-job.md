---
title: "Submitting a Job"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152261/Submitting+a+Job"
date-modified: "2021-10-13"
author: "SGK/MPK"
categories: ["hydra7"]
---

::: {.note title="Note:"}
The material on this page is part of the Quick Start Guide and is not exhaustive. For more details, please see the [Reference Pages](../reference-pages.md).
:::


To submit your job you will need to have [created your job file](the-qsub-generator.md) and have your job file and data files copied to Hydra.


Follows the following steps:


1. [Transfer job file and data files to Hydra](transferring-files-to-from-hydra.md). All data files should go into your folder in `/scratch` or `/data`. 
![(thumbs up)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/thumbs_up.svg) It is recommended for beginner users to create a new directory for each analysis. Create a directory using `Filezilla`or `mkdir` from the command line.
2. [Log into Hydra](logging-into-hydra.md) via a terminal and navigate to the directory with your data files.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Throughout this tutorial replace `username` your Hydra username, the name you log into Hydra with, typically the same as your SI email account name (all lower case).


```
[username@hydra-login01 ~]$ cd /scratch/genomics/username/raxmltest/
[username@hydra-login01 raxmltest]$
```
3. Use `ls` to confirm your job and data files are present and use `cat` (or another text file viewer like `more`or `less`) to inspect your job file.


```
[username@hydra-login01 raxmltest]$ ls
input.fasta raxmltest.job
[username@hydra-login-1 raxmltest]$ cat raxmltest.job
# /bin/sh
# ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -q mThC.q
#$ -l mres=2G,h_data=2G,h_vmem=2G
#$ -cwd
#$ -j y
#$ -N raxmltest
#$ -o raxmltest.log
#$ -m abe
#$ -M user@si.edu
#
# ----------------Modules------------------------- #
module load bioinformatics/raxml
#
# ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
#
raxmlHPC-SSE3 -f a -p 12345 -s input.fasta -x 12345 -N 100 -m GTRCAT -n testrun
#
echo = `date` job $JOB_NAME done
```
4. Submit your job to the cluster with the `qsub` command.


```
[username@hydra-login01 raxmltest]$ qsub raxmltest.job
Your job 825184 ("raxmltest") has been submitted
```
5. Check your job status with the `qstat` command and `ls`


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Errors in the job file will often cause the job to fail quickly, so check `qstat` during the first few minutes of a job run to confirm that it was submitted successfully. If nothing is displayed then you have no current jobs.


```
[username@hydra-login01 raxmltest]$ qstat
job-ID prior name user state submit/start at queue slots ja-task-ID
-----------------------------------------------------------------------------------------------------------------
 825184 0.55500 raxmltest username r 09/22/2015 10:18:01 mThC.q@compute-81-01.cm.clust 1
[username@hydra-login01 raxmltest]$ ls
input.fasta RAxML_bootstrap.testrun RAxML_info.testrun raxmltest.job raxmltest.log
```


![(thumbs up)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/thumbs_up.svg) You can now logout of Hydra with the `exit` command and log back in later to check your job progress
6. When your job is complete the job will no longer appear in qstat and you will receive an email if you configured your job file to send email notifications. Inspect the output files to confirm that job was successful.


```
[username@hydra-login01 raxmltest]$ qstat
[username@hydra-login01 raxmltest]$ tail raxmltest.log
Best-scoring ML tree written to: /scratch/genomics/username/raxmltest/RAxML_bestTree.testrun
Best-scoring ML tree with support values written to: /scratch/genomics/username/raxmltest/RAxML_bipartitions.testrun
Best-scoring ML tree with support values as branch labels written to: /scratch/genomics/username/raxmltest/RAxML_bipartitionsBranchLabels.testrun
Overall execution time for full ML analysis: 149.352777 secs or 0.041487 hours or 0.001729 days
= Tue Sep 22 10:20:30 EDT 2015 job raxmltest done
```
7. [Transfer the output files to your computer](transferring-files-to-from-hydra.md) or continue with further analysis of the dataset on Hydra. 
![(thumbs up)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/thumbs_up.svg) It is recommended to compress your output before transferring to your local computer


```
[username@hydra-login01 raxmltest]$ cd ..
[username@hydra-login01 username]$ tar -czvf raxmltest.tar.gz raxmltest
raxmltest/
raxmltest/raxmltest.job
raxmltest/input.fasta
raxmltest/raxmltest.log
raxmltest/RAxML_info.testrun
raxmltest/RAxML_bootstrap.testrun
raxmltest/RAxML_bestTree.testrun
raxmltest/RAxML_bipartitions.testrun
raxmltest/RAxML_bipartitionsBranchLabels.testrun
```


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Storage on Hydra is not for long-term data storage. Please transfer and remove your data files and output when your analyses are complete.
