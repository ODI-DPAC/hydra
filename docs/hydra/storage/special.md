# Local SSD, NAS and bigtmp

    1. How to Prepare my Data
    2. How to Adjust a Job Script to Use the SSD
    3. Controlling Saving the Content of the SSD at the End of the Job
3. Examples
    1. A trivial example
    2. A more sophisticated example
4. SSD Usage Monitoring


## Introduction


We have added SSDs, solid state disks, on a set of compute nodes:


- These are local fast disks that can speed up applications that preform a lot of intensive I/O operations,
    - hence such jobs should complete faster when using SSDs.
- Jobs that do not perform intensive I/Os should not use the SSDs - this is a limited shared resource.
- Since these disks are local to the compute nodes:
    - you cannot see the SSD from either login nodes,
    - your job will be able to use the SSD *only while the job is running*, hence
        - you need to prepare the files needed for a job prior to submitting the job, using /scratch, and
        - request the right amount of SSD disk space:
            - this is the maximum amount of disk space your job will need on the SSD at run-time, (similarly to the maximum of memory it will need).
            - You need to add something like `-l ssd_res=2560G` when submitting a job to request
                1. a compute node with (local) SSD,
                2. a quota of 2560GB (for example) on the SSD.
    - Your job script will have to
        - copy those files to the SSD before processing them,
        - be adjusted to use the SSD,
        - upon completion, copy the results from the SSD elsewhere (like /scratch), and
        - delete what you wrote on the SSD.
    - If you exceed the amount of disk space, i.e. your quota, your job won't be able to write any longer to the SSD, 
hence your job script should stop when encountering such error.
    - If the job completes normally and there is less than 50GB of 'stuff' left on the SSD, that stuff will be archived in a tar-compress set,
        - otherwise the content of the SSD is deleted (including if the job gets killed).


This remains a limited resource, so used it only if your application benefit from using it.


## How To Use SSDs


Since you can't access the SSDs from a login node, you must prepare the data the job will need somewhere else, like on `/scratch` before submitting a job.


Like for memory, you need to *guestimate* how much SSD space your job will need. You will not be able to use more SSD space than you requested.


Remember, your job will still be able to access the `/home, /data,` and `/scratch` disks, hence you don't have to copy everything on the SSD,


only the I/O intensive part of the analysis should use the SSD.


### How to Prepare my Data


1. Create a subdirectory in `/scratch` and move or copy the data you will need, for example (as user smart1) 
`cd /scratch/genomics/smart1` 
`mkdir -p great/project/wild-cat` 
Now is have a directory for this case, and would copy the I/O intensive part of the required data set in it.
2. While not required, you can pack these data in a compressed tar-ball 
`cd /scratch/genomics/smart1/great/project/wild-cat` 
`tar cfz ../wild-cat.tgz .` 
The file `/scratch/genomics/smart1/great/project/wild-cat.tgz`now holds you input data set, 
being compressed it is likely to be smaller than the content of `/scratch/genomics/smart1/great/project/wild-cat,` 
That directory can be deleted, unless you will need it later.
3. Ancillary data and/or configuration files that are not causing intensive I/O can stay on a location under `/scratch`


### How to Adjust a Job Script to Use the SSD


Your jobs script will need the following 4 parts


#### Part 1: Copy the Data to the SSD


- 
    - At the top of your job script, load the `tools/ssd` module and copy or extract your data set as follows:


```{.text title="example using recursive copy"}
module load tools/ssd
cp -pR /scratch/genomics/smart1/great/project/wild-cat/* $SSD_DIR/.
```


or


```{.text title="example using compressed tar-ball"}
module load tools/ssd
cd $SSD_DIR
tar xf /scratch/genomics/smart1/great/project/wild-cat.tgz
```


The advantage of the compressed tar-ball is that the `.tgz` file is likely to be smaller than the content of the directory, hence less I/O transfer from the`/scratch` disk, while un-compressing and writing to the SSD is fast,


#### Part 2: Adjust the Script or a Configuration File


- You need to replace all references to `/scratch/genomics/smart1/great/project/wild-cat` by $SSD_DIR,
- this can be easily done at the shell script level, but not in a configuration file, i.e., for flags/options 
`execute -o /scratch/genomics/smart1/great/project/wild-cat/result.dat` 
is replaced by 
`execute -o $SSD_DIR/result.dat`
- Here is a simple trick to modify a configuration file:
    - Let's assume that your analysis uses a file `wow.conf`, where for instance the full path of some files must be listed, like:


```{.text title="wow.conf"}
## this is the configuration file of the fabulous WOW package
input=/scratch/genomics/smart1/great/project/wild-cat/wiskers.dat
output=/scratch/genomics/smart1/great/project/wild-cat/tail.dat
paws=4
eyes=2
```
    - Replace the `wow.conf` file by a `wow.gen` file as follows:


```{.text title="wow.gen"}
## this is the configuration file of the fabulous WOW package
input=XXXX/wiskers.dat
output=XXXX/wild-cat/tail.dat
paws=4
eyes=2
```
    - And create the `wow.conf`file from the `wow.gen`at run-time by adding the following in the job script:


```
sed "s=XXXX=$SSD_DIR=" wow.gen > wow.conf
```


As long as `XXXX`is not used for anything else, this will replace every occurrence of `XXXX`by the value of the environment variable `SSD_DIR.`


#### Part 3: Run the Analysis


- With your data copied to the SSD and with your commands and configuration files adjusted to use the SSD, run your analysis.


#### Part 4: Copy the Results from the SSD


- At the end of the job script, you must add instructions to copy the results of your analysis back to `/scratch`(or `/scratch`, or `/data`).


If/when the results are easily identifiable, you can use `the commands mv` `or tar,` and `find`, here are a few examples:
    1. Move the directory where all the results are stored and the log file, delete the rest.****


```{.text title="moving identifiable results, delete the rest"}
## move results and log file back
cd $SSD_DIR
mv results /scratch/genomics/smart1/great/project/wild-cat/.
mv wow.log /scratch/genomics/smart1/great/project/wild-cat/.
#
## delete the rest
rm -rf *
```
    2. Move the directory where all the results are stored and the log file, delete the input (conservative approach, in case you missed something).


```{.text title="moving identifiable results, delete known input sets"}
## move results and log file back
cd $SSD_DIR
mv results /scratch/genomics/smart1/great/project/wild-cat/.
mv wow.log /scratch/genomics/smart1/great/project/wild-cat/.
#
## delete input set and other stuff
rm -rf input
rm wow.gen wow.conf
```
    3. Move using the `--update` flag of `mv` (see `man mv`)


```{.text title="moving using --update"}
## move results using --update
cd $SSD_DIR
mv --update * /scratch/genomics/smart1/great/project/wild-cat/.
#
## delete the rest
rm -rf *
```


Note, you can use `mv --update` on an explicit list (of files, directories, or file specification), not just * (everything), and you do not have to remove the rest, but can only remove what you know you can safely remove (conservative approach).
    4. Find newer files and move them: the trick is to create a 'timestamp' file *before* starting the analysis. 
 That file can be used later to find any newer file with the `--newer=` option of `tar` (see `man tar`):


```{.text title="Using a timestamp file and tar --newer="}
## set the timestamp
date > $SSD_DIR/started.txt
## run the analysis
...
## copy the new files in the subdir data/ to a compressed tar-ball
cd $SSD_DIR
tar --newer=$SSD_DIR/started.txt -cfz /scratch/genomics/smart1/great/project/wild-cat-results.tgz data/
## now remove it
rm -rf data/
## etc...
## delete everything, unless
rm -rf *
```


See previous comments and what to tar and what to remove: once you've `tar`'d new stuff in `data/`, remove `data/`, etc.
    5. Using the timestamp file and the `find` command (see `man find`):


```{.text title="Using find and a timestamp file"}
## set the timestamp
date > $SSD_DIR/started.txt
## run the analysis
...
## find the new files in the subdir data/
cd $SSD_DIR
find data/ -newer $SSD_DIR/started.txt -type f > /tmp/list
## do the same on logs/, append to the list
find logs/ -newer $SSD_DIR/started.txt -type f >> /tmp/list
## etc...
## now save what is in the list with one tar
tar --files-from=/tmp/list -cfz /scratch/genomics/smart1/great/project/wild-cat-results.tgz data/
## now remove data/ and logs/
rm -rf data/ logs/
## etc...
## delete everything, unless
rm -rf *
```


There are many more ways to accomplish this ....


BTW, the advantage of writing a `.tgz` file, rather than moving files is two fold, assuming your stuff is compressible:
        1. You write less in the .tgz file, so it should be done faster (reading and compressing should be fast, writing is the slow step)
        2. you need less disk space for your output (since it is compressed).


The drawback being that you need to know how to handle/view/deal with a `.tgz` file.


### Controlling Saving the Content of the SSD at the End of the Job


You can control where and how much of the content of the SSD to save at the end of the job to overwrote the default behavior with two variables:


1. `SSD_SAVE_DIR` to specify where to save the content of the SSD when the job finishes, or not to save anything, and
2. `SSD_SAVE_MAX` to specify the max size to save, namely if there is more than the given size left on the SSD, not to save it.


#### NOTE:


- `SSD_SAVE_DIR` must specify an existing directory in which you can write, or you can set the value to '-' (w/out the quotes) to disable the saving.
- `SSD_SAVE_MAX` must be a number (integer or float) followed by an optional unit - like k,K,M,G or T - for example `SSD_SAVE_MAX=21.4M`.
- Setting `SSD_SAVE_MAX` to 0 is equivalent to setting `SSD_SAVE_DIR` to '-', namely do not save what is left.
- Avoid setting `SSD_SAVE_MAX` to a value too large (i.e., > 80G), since saving the content of the SSD will take too long, instead save the contend of SSD in your job script.
- If you kill your job, the content of the SSD is *never*saved.


#### How to Specify these:


These must be passed via the `-v`flag of `qsub`, either explicitly to `qsub` or as an embedded directive in the job file, as in


```{.text title="Explicitly"}
% qsub -v SSD_SAVE_DIR=/scratch/sao/hpc/save -v SSD_SAVE_MAX=10M demo.job
```


or


```{.text title="Embedded directive in job file"}
#
#$ -l ssd_res=10G -v SSD_SAVE_DIR=/home/hpc/tmp -v SSD_SAVE_MAX=10M
```


### Examples


1. #### A trivial example is available on Hydra in `~hpc/examples/ssd` as `test-ssd.job` , i.e.:


```{.text title="Trivial Example"}
#
#$ -cwd -j y -o test-ssd.log -N test-ssd
#$ -l ssd_res=10G
#
echo + `date` $JOB_NAME started on $HOSTNAME in $QUEUE with id=$JOB_ID
echo NSLOTS = $NSLOTS
#
module load tools/ssd
ls -ld $SSD_DIR
ls -l  $SSD_DIR
#
date >  $SSD_DIR/date
dd if=/dev/zero of=$SSD_DIR/100M count=1024 bs=102400
#
ls -lh $SSD_DIR/*
#
echo = `date` $JOB_NAME done.
```


##### Here is what a more sophisticated job script might look like:


```{.text title="Pseudo Example"}
#
#$ -N example
#$ -o example.log -cwd -j y
#$ -l ssd_res=2560G
#
## pseudo example using a fake package WOW, on the SSD
#
echo $JOB_NAME started `date` on $HOSTNAME in $QUEUE jobID=$JOB_ID
#
module load tools/ssd
module load special/wow
#
## create a wow config file from a generic version, to insert the SSD temp dir value
sed "s=XXXX=$SSD_DIR=" ~/wow/wild-cat.gen > ~/wow/wild-cat.conf
#
## cd to the SSD temp dir and copy the data set to it, using the existing .tgz file
cd $SSD_DIR
tar xf /scratch/genomics/smart1/great/project/wild-cat.tgz
#
## create some sub dirs for output and logs
mkdir output
mkdir logs
#
## run the wow analysis (note how some files are not on the SSD)
wow --type=m --params=$HOME/wow/parameters.dat --config=$HOME/wow/wild-cat.conf -o $SSD_DIR/output -l $SSD_DIR/logs
#
## save the output and the logs in a tar compressed file
## (assumes wow did not change current working directory)
## otherwise insert: cd $SSD_DIR
tar -cfz /scratch/genomics/smart1/great/project/wild-cat-results.tgz output/ logs/
#
## remove everything (in $SSD_DIR), or remove what you know you can (conservative option)
rm -rf *
#
echo $JOB_NAME done `date`
```


## SSD Usage Monitoring Tools


- We have two tools to monitor SSD usage, one on a per-job basis, and one to view usage summary.
- To access them, you to load the `tools/local` module.


### Per Job Basis


```{.text title="plot-qssduse.pl"}
% module load tools/local
% plot-qssduse -x 7420073
```


This example plots the SSD usage of job 7420073 to the screen, assuming you have an X-windows capable connection,


- drop the `-x` to plot to a file,
- and use `NNNN.TTT`, instead of `NNNN` to show usage for a given task (`TTT`) of a job array (`NNNN`).
- Try `plot-qssduse -help` or `man plot-qssduse` for more information.


### Usage Summary


```{.text title="plot-qssduse-summary.pl"}
% module load tools/local
% plot-qssduse-summary -x
```


As above:


- drop the `-x` to plot to a file.
- Try `plot-qssduse-summary -help` or `man plot-qssduse-summary`for more information.

## How to Use NAS Storage and the I/O Queue

### Near Line Storage or NAS


- A large near-line storage of about 950TB has been added to Hydra in July 2019 as NAS and mounted via NFS.
- This storage is mounted as `/store`, *but only* on both login nodes. the head node and the interactive nodes.
- It is not (*and will not be*) mounted to the rest of the compute nodes.
    - Hence data stored on the NAS are to be copied to active storage (e.g. `/data`, or `/scratch`) before processing and/or analyzing your data, and vice-versa (active storage can be offloaded to `/store`).
- Most of that disk space is project-specific space, but there is a small amount of space on that system available to all other users upon request and at no cost.
- Approved users will receive up to 5TB of un-scrubbed space, with a daily snapshot up to 14 days.
    - Note that we reserve the right to clean up old stuff that is likely to accumulate in the future, with proper notification, once it fills up.


Users interested in receiving an allocation in `/store/public` should contact [Hydra admin](mailto:si-hpc-admin@si.edu).


#### Additional Technical Details


- This NAS is storage is build on a zfs file system and runs FreeNAS (a dedicated Linux version for NAS/NFS).
- It supports quotas and snapshots, although not the full gamut that NetApp and GPFS offers.
- This system is fault tolerant (when a disk fails it keeps running fine) but not high availability (i.e. there is no full hardware redundancy), so it is intrinsically less robust (hence less expensive) than the NetApp and the soon to arrive GPFS.
- Like all the disks on Hydra, its content is NOT backed up, and while we do not expect catastrophic failures, keep all this in mind.
- It is to be thought of as a “*cheap bucket*” to keep things around awaiting processing, not for backup, archiving or any other form of reliable & long term storage.


Also, the Linux command `quota` does work with the NAS/zfs, instead use `quota+.pl` (part of the `tools/local` module).


### Accessing `/store`


- You can access `/store` from either login node. You can also access via the interactive queue, using `qrsh`.
    - Remember that the limits on login node usage and on `qrsh`jobs are in effect.
- Alternatively, you can also access `/store` via the IO queue with its specific limits.
- Submitting jobs to the IO queue allows you to (1) have larger limits, (2) queue a slew of IO jobs and (3) chain IO and processing jobs using the scheduler.


#### The IO Queue


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


##### Limits


- Jobs in the IO queue can run for 72 hours, and are limited to consuming no more than 12h of CPU and 8GB of memory (per slot).
    - hence IO jobs are not meant to be used to run computations on data stored on the NAS
- Users can run only 2 IO jobs concurrently and use up to 6 slots.
- You can submit as many IO jobs as needed, keeping in mind the total limit of 2,000 running and queued jobs per user.


##### Hints


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

## How to Use \"bigtmp\" - Access to Large Temporary Disk Space

***Update: "bigtmp" is obsolete and will be removed in late 2025. Users are encouraged to use their disk allocation on `/scratch`, or local SSD storage******instead.***


### Introduction


- We have set aside some temporary disk space on the GPFS for jobs who need large temporary disk space, that will not fit on `/tmp` (aka `bigtmp`).
- To manage that space we've implemented a consumable so the job scheduler will not start more jobs requesting space than there is.
- A user can't request more than 25G at a time, in either a single job or as the total of all the job from that user requesting `bigtmp` space.


### How To


- To request large temporary disk space, use `-l bigtmp=XX`, where XX is the amount of disk space needed in GB, like in `-l bigtmp=10` (no unit).
- Use the module `tools/bigtmp` to store the location of the temporary disk space in the `BIGTMP`environment variable.
- Use `$BIGTMP` to specify the temporary disk space location.
- The content of the temporary disk space location is deleted when the job is done.


### Example


Let's assume that `doMyThing`is some application that needs lots of temporary space, and whose location cab be specified with the `-tmp` flag:


```
### /bin/csh
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
