# Quick start

This page covers submitting a job on Hydra: creating a working directory, writing a job file, submitting it with `qsub`, checking it with `qstat`, and reading its output. It assumes you have an [account](account.md) and can [log in](login.md). The example job needs no input data.

Replace `USERNAME` with your Hydra username throughout.

## 1. Log in and create a working directory

Jobs run from a directory under `/scratch`; the home directory has a small quota and is not for job input and output.

```bash
ssh USERNAME@hydra-login01.si.edu
mkdir -p /scratch/genomics/USERNAME/quickstart
cd /scratch/genomics/USERNAME/quickstart
```



## 2. Write a job file

A job file is a shell script. Lines beginning with `#$` are options to the scheduler. Create `hello.job` with a text editor (`nano hello.job` if you have no preference):

```sh title="hello.job"
#!/bin/sh
#$ -S /bin/sh
#$ -q mThC.q
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
| `-q mThC.q` | Queue. `mThC.q` is the medium-time, high-CPU queue |
| `-l mres=2G,h_data=2G,h_vmem=2G` | Reserve 2 GB of memory |
| `-cwd` | Run in the directory the job was submitted from |
| `-j y` | Write error output to the same file as standard output |
| `-N hello` | Job name |
| `-o hello.log` | Output file |

[Job scripts](../hydra/jobs/job-scripts.md) describes all options. The [QSub Generator](../hydra/jobs/qsubgen.md) produces a job file from a web form.

## 3. Submit the job

```console
$ qsub hello.job
Your job 825184 ("hello") has been submitted
```

The number is the job ID. `qstat`, `qdel` and `qacct` refer to jobs by this ID.

## 4. Check the job

```console
$ qstat
job-ID  prior   name   user     state submit/start at     queue                slots
------------------------------------------------------------------------------------
825184  0.55500 hello  USERNAME r     09/22/2025 10:18:01 mThC.q@compute-81-01   1
```

State `qw` is queued and waiting; `r` is running. A job with an error in its job file usually fails within seconds, so check `qstat` during the first minute after submitting. When the job has finished, `qstat` prints nothing.

You can log out with `exit` while a job is running.

## 5. Read the output

```console
$ cat hello.log
+ Mon Sep 22 10:18:01 EDT 2025 job hello started in mThC.q with jobID=825184 on compute-81-01
= Mon Sep 22 10:18:31 EDT 2025 job hello done
```

<!-- Sample output above is illustrative; replace with a capture from the cluster before publishing. -->

!!! warning "`/scratch` is not permanent storage"

    Files older than 180 days are deleted. Move results off the cluster when an analysis is complete. See [Storage](../hydra/storage/index.md).

## Next steps

- Copying data to Hydra and results back: [Data transfer](../data-transfer/index.md).
- Choosing a queue and memory for a production job: [Queues](../hydra/jobs/queues.md).
- Loading software: [Modules](../hydra/software/modules.md).
