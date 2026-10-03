# Quick start

A first job on Hydra takes five steps. You make a working directory, write a job file, submit it with `qsub`, check on it with `qstat`, and read the output file at the end. You need an [account](account.md) and to be [logged in](login.md). The example job needs no input data and runs for 30 seconds.

Replace `USERNAME` with your Hydra username throughout.

## 1. Log in and create a working directory

Jobs run from a directory under `/scratch`. The home directory has a small quota and is not for job input and output.

Your directory on `/scratch` is under a group directory such as `/scratch/genomics`, `/scratch/sao` or `/scratch/odi`. Your welcome email tells you which one is yours. The examples on this site use `/scratch/genomics/USERNAME`. Substitute your own path.

```bash
ssh USERNAME@hydra-login01.si.edu
mkdir -p /scratch/genomics/USERNAME/quickstart
cd /scratch/genomics/USERNAME/quickstart
```

## 2. Write a job file

A **job file** is a shell script with extra lines at the top. Lines beginning with `#$` are options to the scheduler, and the rest is what the job runs. Create `hello.job` with a text editor (`nano hello.job` if you have no preference):

```sh title="hello.job"
#!/bin/sh
#$ -S /bin/sh
#$ -l mres=2G,h_data=2G,h_vmem=2G
#$ -cwd
#$ -j y
#$ -N hello
#$ -o hello.log
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
sleep 30
echo = `date` job $JOB_NAME done
```

| Option | Effect |
|---|---|
| `-S /bin/sh` | Shell used to run the script |
| `-l mres=2G,h_data=2G,h_vmem=2G` | Reserve 2 GB of memory |
| `-cwd` | Run in the directory the job was submitted from |
| `-j y` | Write error output to the same file as standard output |
| `-N hello` | Job name |
| `-o hello.log` | Output file |

There is no `-q` line, so the job goes to the default queue, `sThC.q`, which allows up to 7 hours of CPU time and is right for most first jobs. [Job scripts](../jobs/job-scripts.md) lists every option, and the [QSub Generator](../jobs/qsubgen.md) writes a job file for you from a web form.

## 3. Submit the job

```console
$ qsub hello.job
Your job 15497588 ("hello") has been submitted
```

The number is the **job ID**. `qstat`, `qdel` and `qacct` refer to jobs by this ID, and so will we if you write to us about a job.

## 4. Check the job

```console
$ qstat
job-ID     prior   name       user         state submit/start at     queue                          jclass                         slots ja-task-ID
------------------------------------------------------------------------------------------------------------------------------------------------
  15497588 0.50500 hello      USERNAME     r     09/30/2026 18:48:14 sThC.q@compute-93-02.cm.cluste                                    1
```

State `qw` means queued and waiting, `r` means running. A job with an error in its job file usually fails within seconds, so check `qstat` during the first minute after submitting. When the job has finished, `qstat` prints nothing.

You can log out with `exit` while a job is running. The scheduler owns the job, so it keeps running after you log out.

## 5. Read the output

```console
$ cat hello.log
+ Wed Sep 30 18:48:14 EDT 2026 job hello started in sThC.q with jobID=15497588 on compute-93-02
= Wed Sep 30 18:48:44 EDT 2026 job hello done
```

!!! warning "`/scratch` is not permanent storage"

    The scrubber deletes files older than 180 days. Move results off the cluster when an analysis is complete. See [Storage](../storage/index.md).

## Further reading

- [Data transfer](../data-transfer/index.md) for copying data to Hydra and results back
- [Request a queue, memory and CPUs](../jobs/request-resources.md) for a production job that needs more than the default
- [Find and load software](../software/modules.md) for the programs installed on the cluster
