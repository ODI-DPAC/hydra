# Use a node's local SSD

This page covers running a job on a compute node's local solid-state disk. It is for jobs that read and write intensively on their working files; a job whose time goes to computation gains nothing and takes a limited resource. The SSD is visible only to the job, only while it runs, and only from the node it runs on, so the job copies its input in at the start and its results out at the end.

!!! danger "Everything on the SSD is deleted when the job is killed"

    The SSD is cleared when the job is killed, crashes or reaches a time limit, and the login nodes cannot see it. Copy results back to `/scratch` inside the job, and checkpoint long runs there.

## Run a job on the SSD

1. Put the input the job needs, and only the I/O-intensive part, in one directory on `/scratch`, or in one compressed archive:

    ```bash
    cd /scratch/genomics/USERNAME/project-a
    tar -czf ../project-a.tgz .
    ```

    Files the job only reads occasionally, and configuration files, can stay on `/scratch`.

2. Request the SSD space the job needs, as `-l ssd_res=SIZE`. The scheduler then places the job on a node with an SSD and reserves that much; the job cannot write more than it reserved.

3. In the job file, load `tools/ssd` and copy or unpack the input into `$SSD_DIR`, the directory the module points at:

    ```sh
    module load tools/ssd
    cd $SSD_DIR
    tar -xf /scratch/genomics/USERNAME/project-a.tgz
    ```

4. Run the analysis with its input and output paths under `$SSD_DIR`. For a program that takes paths as options, use `$SSD_DIR` in the options; for one that reads them from a configuration file, write the file at run time from a template in which the path is a placeholder:

    ```sh
    sed "s=XXXX=$SSD_DIR=" wow.gen > wow.conf
    ```

5. Copy the results back to `/scratch` and delete everything on the SSD:

    ```sh
    cd $SSD_DIR
    tar -czf /scratch/genomics/USERNAME/project-a-results.tgz output/ logs/
    rm -rf *
    ```

The whole job file:

```sh title="wow.job"
#$ -S /bin/sh
#$ -N wow -o wow.log -cwd -j y
#$ -l ssd_res=2560G
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
#
module load tools/ssd
module load special/wow
sed "s=XXXX=$SSD_DIR=" $HOME/wow/project-a.gen > $HOME/wow/project-a.conf
#
cd $SSD_DIR
tar -xf /scratch/genomics/USERNAME/project-a.tgz
mkdir output logs
wow --params=$HOME/wow/parameters.dat --config=$HOME/wow/project-a.conf -o $SSD_DIR/output -l $SSD_DIR/logs
#
tar -czf /scratch/genomics/USERNAME/project-a-results.tgz output/ logs/
rm -rf *
#
echo = `date` job $JOB_NAME done
```

`~hpc/examples/ssd/test-ssd.job` is a runnable example. Writing results as one `.tgz` rather than moving files is faster when the data compresses, and takes less space on `/scratch`.

## Save only new files

To copy back only what the analysis wrote, create a timestamp file before it starts and use `tar --newer` or `find -newer` afterwards:

```sh
date > $SSD_DIR/started.txt
wow ...
cd $SSD_DIR
tar --newer=$SSD_DIR/started.txt -czf /scratch/genomics/USERNAME/project-a-results.tgz data/
rm -rf *
```

## What happens to the SSD when the job ends

If the job ends normally with less than 50 GB left on the SSD, the leftover is archived as a compressed tar file; with more, it is deleted. If the job is killed, it is deleted. Two variables, passed with `-v`, change this:

| Variable | Effect |
|---|---|
| `SSD_SAVE_DIR=DIR` | save the leftover into DIR, which must exist and be writable; `-` saves nothing |
| `SSD_SAVE_MAX=SIZE` | save only if the leftover is under SIZE (`21.4M`, `10G`); `0` saves nothing |

```sh
#$ -l ssd_res=10G -v SSD_SAVE_DIR=/scratch/genomics/USERNAME/save -v SSD_SAVE_MAX=10M
```

Keep `SSD_SAVE_MAX` under 80 GB; saving more takes too long at job exit. Copy large results back in the job script instead.

## Watch a job's SSD use

```console
$ plot-qssduse JOBID              # PNG of the job's SSD use over time
$ plot-qssduse -x JOBID           # on screen, over X11
$ plot-qssduse-summary            # SSD use across the cluster
```

`JOBID.TASKID` selects one task of an array. `man plot-qssduse` has the options.
