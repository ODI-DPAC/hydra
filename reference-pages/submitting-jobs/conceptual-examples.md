---
title: "Conceptual Examples"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152289/Conceptual+Examples"
date-modified: "2025-10-07"
author: "SGK"
categories: ["hydra7"]
---

1. [A trivial example](conceptual-examples.md)
2. [A better example](conceptual-examples.md)
3. [Example with Embedded Directives](conceptual-examples.md)
4. [Example with Embedded Directives and Arguments](conceptual-examples.md)
5. [Notes](conceptual-examples.md)
    1. [Shell Selection](conceptual-examples.md)
    2. [Passing Options](conceptual-examples.md) to `qsub`
    3. [Email Notification](conceptual-examples.md)
    4. [Environment Variables](conceptual-examples.md)
    5. [Catching Time Limits](conceptual-examples.md)
    6. [Miscellaneous](conceptual-examples.md)


## 1. A Trivial Example


Let us assume that


- you have a program that you have successfully compiled/installed on the cluster``and that you want to run, we will call it`crunch`;
- the executable `crunch` and all the files needed to run it are in one directory, and/or the files produced will go there.


The simplest way to submit this computation would be to write a two line job script, in a file located in a directory like `/scratch/public/sao/hpc/demo` and name it `crunch.job`:


```{.text title="A trivial crunch.job"}
cd /scratch/public/sao/hpc/demo
./crunch
```


You start the computation by submitting the job script file with:


```
% cd /scratch/public/sao/hpc/demo
% qsub crunch.job
Your job NNNNNNN ("crunch.job") has been submitted
```


The qsub command, if successful, will produce the "*Your job ... has been submitted*" message where *`NNNNNNN`* is a unique number, the job ID assigned to that job.


By default, the output and error files associated with that job will be located in your home directory and named `crunch.job.oNNNNNNN` and `crunch.job.eNNNNNNN`


## 2. A Better Example


A better approach is to specify more parameters associated to your job and save more information about the job as follow:


```{.text title="A better crunch.job"}
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
./crunch
echo = `date` job $JOB_NAME done
```


and start the computation with:


```
% cd /scratch/public/sao/hpc/demo
% qsub -N crunch -cwd -j y -o crunch.log crunch.job
Your job NNNNNNN ("crunch") has been submitted
```


With this approach:


- you specify the name of the job (`-N crunch`);
- you join error and output in a single file (`-j y`);
- you give a name to the output file (`-o crunch.log`); and
- you tell `qsub` to start the job in the current working directory, and to write the output file there (`-cwd`).


You also, this way, keep track, by saving it in the log file, of


- the job name and job id,
- in which queue the job ran, and on which compute node (host), and,
- when it started and when it ended.


## 3. Example with Embedded Directives


You can put it all in one file as follows:


```{.text title="A better crunch.job with embedded directives"}
#
#$ -N crunch -cwd -j y -o crunch.log
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
./crunch
echo = `date` job $JOB_NAME done
```


and you submit your job with simply:


```
% cd /scratch/public/sao/hpc/demo
% qsub crunch.job
Your job NNNNNNN ("crunch") has been submitted
```


The command `qsub` will look for lines starting with `#$` (that are otherwise comments in the script) and parse these embedded directives as if they were options passed to the command itself.


## 4. Example with Embedded Directives and Arguments


Finally, the job file is a script: it has to be written according to a specific syntax (C-shell, or Bourne shell) and can take arguments.


Let's now assume that crunch takes two arguments:


- you can either write a different job file for each case you want to run, or
- you can write your job script to use arguments, like this:


```{.text title="A better crunch.job with embedded directives and arguments"}
# /bin/csh
#
# this script takes two arguments and is written using the C-shell syntax
#
#$ -N crunch -cwd -j y -o crunch.log
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
set OPTIONS = (-from $1 -to $2)
echo starting crunch $OPTIONS
./crunch $OPTIONS
echo = `date` job $JOB_NAME done
```


and you can start several jobs as follow:


```
% cd /scratch/public/sao/hpc/demo
% qsub -N crunch-20-50 -o crunch-20-50.log crunch.job 20 50
Your job NNNNNNN ("crunch-20-50") has been submitted
% qsub -N crunch-100-150 -o crunch-100-150.log crunch.job 100 150
Your job NNNNNNN ("crunch-100-150") has been submitted
[etc...]
```


In this example the job name and the log file name are redefined to be specific to each job by specifying them on the `qsub` command line.


## 5. Notes


- Your job script can be an elaborate script, or can start an elaborate and/or convoluted script - how to write Un*x scripts is beyond the scope of this documentation.


### Shell Selection


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The GE is setup to use by default the C-shell (`csh`) syntax for job scripts.


- If you prefer using the Bourne shell syntax (`sh` or `bash`), you need to tell `qsub` to use that shell by passing the option `-S /bin/sh`, or 
adding it as an embedded directive as follows:


```{.text title="A better crunch.job with embedded directives and arguments, using Bourne shell syntax"}
# /bin/sh
#
# this script takes two arguments and is written using the Bourne-shell syntax
#
#$ -S /bin/sh
#$ -N crunch -cwd -j y -o crunch.log
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
OPTIONS="from $1 to $2"
echo starting crunch $OPTIONS
./crunch $OPTIONS
echo = `date` job $JOB_NAME done
```


- Unlike executable script, a # followed by ! on the first line of job scripts is ignored (hence in the the examples I use `# /bin/csh` or `# /bin/sh` as reminders, not as specifiers);
- Unless you are fully versed in the idiosyncrasies of Linux and how `/bin/bash` differs from `/bin/sh` at startup, it is highly recommended to use `/bin/sh` and not `/bin/bash`. 
There are no syntax differences, the only differences are which initialization files are read at startup.


### Passing Options to Qsub


- The options passed to the `qsub` command are setup as follow:
    1. as specified in the system wide file `$SGE_ROOT/$SGE_CELL/common/sge_request` (lines not starting w/ #);
    2. as specified in a `.sge_request` file, located in the current working directory (if there is one);
    3. as specified in a `~/sge_request` file, (located in your home directory, if there is one);
    4. as per the embedded options in the submitted job script (lines starting with `#$`);
    5. options passed to `qsub`.


For example, you can write a`~/.sge_request` file with the line


`-cwd -j y`


and all your jobs will include `-cwd -j y`as options. At each step you can override a set option.


### Email Notifications


You can request that the GE notify you by email when a job


- is started (**b**eginning of the job)
- **e**nds, or
- is **a**borted.


This is accomplished by adding the `-m abe` option to `qsub`.


You can specify the list of users to which the GE will send mail, with the `-M <email_address>` option to `qsub`, by default mail is sent to the job owner, and will be redirected to the email in your `~/.forward` file (see [Introduction](../introduction.md)).


These options can be set as an embedded directive in the job script file.


### Environment Variables


When a job is started, the GE defines a slew of environment variables.


![(grey lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb.svg) The following is a subset of these variables that your job scripts may want to use:


<table class="wrapped confluenceTable"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh">Name</th><th class="confluenceTh">Description</th><th class="confluenceTh" colspan="1">Example of Value</th></tr><tr><td class="confluenceTd"><code>JOB_NAME</code></td><td class="confluenceTd">The job name</td><td class="confluenceTd" colspan="1"><code>test</code></td></tr><tr><td class="confluenceTd" colspan="1"><code>JOB_ID</code></td><td class="confluenceTd" colspan="1">A unique job identifier</td><td class="confluenceTd" colspan="1"><code>8736123</code></td></tr><tr><td class="confluenceTd" colspan="1"><code>HOSTNAME</code></td><td class="confluenceTd" colspan="1">The name of the (master) node the job is running on</td><td class="confluenceTd" colspan="1"><code>compute-43-11</code></td></tr><tr><td class="confluenceTd" colspan="1"><code>QUEUE</code></td><td class="confluenceTd" colspan="1">The name of the cluster queue in which the job is running</td><td class="confluenceTd" colspan="1"><code>sTHC.q</code></td></tr><tr><td class="confluenceTd" colspan="1"><code>NSLOTS</code></td><td class="confluenceTd" colspan="1">The number of queue slots allocated to the job</td><td class="confluenceTd" colspan="1"><code>1</code></td></tr><tr><td class="confluenceTd" colspan="1"><code>TMPDIR</code></td><td class="confluenceTd" colspan="1">The absolute path to the job's temporary working directory</td><td class="confluenceTd" colspan="1"><code>/tmp/8736126.1.sThC.q</code></td></tr></tbody></table>


![(info)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/information.svg) You can find a complete list at the bottom of the `qsub` manual - or man page - `man qsub`.


### Catching Time Limits


- All the queues, except a few, have time limits: a job will get killed if it exceeds either a CPU limit or an elapsed time (aka real time, wall clock) limit. What those limits are is explained elsewhere ([Available Queues](available-queues.md) and [resource limits](../submitting-jobs.md).)
- All time-limited queues have a soft limit and a hard limit. When the soft limit is reached, a signal is sent by the GE to the script. That signal can be caught to execute something before reaching the hard limit (job termination).
- Jobs using the Bourne-shell syntax (`sh`) can catch the signal, jobs using the C-shell (`csh`) can't (a shortcoming of `Linux`' implementation of `csh`).
- So, especially for `csh` jobs, it is recommended to end the job script with a line like '`echo job done`' that will indicate that the job (script) completed.
- For `sh` jobs, the following example illustrates how to catch signals at the script level:


```
#
#$ -S /bin/sh
#
warn()
{
 echo @ `date` warning, received $1 signal.
}
#
trap "warn xcpu" SIGXCPU
trap "warn usr1" SIGUSR1
trap "warn kill" SIGKILL
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo sleeping $1
sleep $1
echo = `date` job $JOB_NAME done
```


- You can check
    - the status of a job with with the `qstat` command ,
    - the exit status of a job, and the resources it used (CPU, elapsed time, memory, I/Os), once it completed, with the `qacct` command 
(see the [Jobs Monitoring](job-monitoring.md) page).


### Miscellaneous


- As you queue more than one job beware of "*name space*":
    - jobs will run concurrently (on different compute nodes, or not), so they should not write to the same file(s) and you can keep track of them better if they do not have the same job names.
- Also, especially for `Emacs` users, the last line of a job file must be properly terminated with a newline character (in Unix the return key insert a NL, not a CR) 
The `csh` does not execute a line not properly terminated, and thus the last line of your script may not be executed if it is not followed by a blank line.
- Include the following in your `~/.emacs` file to make sure the last line ends with a NL:


```{.text title="Add the following lines in your ~/.emacs file"}
;; always end a file with a newline character
(setq require-final-newline t)
```
- A job is likely to need resources (CPU time, memory, etc.) and to run in a specific queue. What queues to use and how to request resources is explained in the [Available Queues](available-queues.md) page. 
How to monitor your job(s) and the cluster is explained elsewhere ([Job Monitoring](job-monitoring.md) and [Cluster Monitoring](../cluster-monitoring.md)).
- Long jobs should, whenever possible, use *check-pointing*: save intermediate results so one can resume a computation from where it stopped.
