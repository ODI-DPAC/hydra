# BEAST

BEAST 2 is the module `bio/beast`; `module -t avail 2>&1 | grep beast` lists the versions. BEAST's own guidance on performance is at <http://www.beast2.org/performance-suggestions/index.html>.

## Version and packages

The first time BEAST runs it copies `beast.jar` and `beast.src.jar` into `~/.beast/2.x/BEAST/lib`, one subdirectory per version, and later runs load from there. Check the log file of every run for the version it reports, because a version left over in `~/.beast` can differ from the module you loaded.

BEAST packages (add-ons) install into `~/.beast` with the package manager, after loading the module:

```console
$ module load bio/beast
$ packagemanager -list
$ packagemanager -add SNAPP
```

## BEAGLE

The [BEAGLE](https://github.com/beagle-dev/beagle-lib) library is the module `bio/beagle`. `bio/beast` does not load it, so add `module load bio/beagle` after `module load bio/beast` in the job file. The default build is for Java 17. The BEAGLE builds do not use the GPUs; email [SI-HPC@si.edu](mailto:SI-HPC@si.edu) if you need that.

## SNAPP path sampling as separate jobs

BEAST's [cluster instructions](https://www.beast2.org/path-sampling/#:~:text=Setting%20up%20an%20analysis%20for%20a%20cluster) for SNAPP path sampling produce one shell script per step, and each step runs as its own job on Hydra.

1. Add `doNotRun='true'` to the `run` element of the XML file.
2. In an interactive session with enough memory (`qrsh -pe mthread 8`), load the module and start the XML with `-threads` set to the number of steps in the file, 48 in this example:

    ```console
    $ module load bio/beast
    $ beast -threads 48 analysis.xml
    ```

    This writes 48 step directories, each with a `runN.sh`.

3. Submit one job per step with this job file and loop:

    ```sh title="beast_step_run.job"
    #$ -S /bin/sh
    #$ -N beast_step_run -cwd -j y
    #$ -q lThM.q
    #$ -l mres=16G,h_data=16G,h_vmem=16G,himem
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    module load bio/beast
    if [ -z "$1" ]; then
      echo "usage: qsub beast_step_run.job STEP"
      exit 1
    fi
    . ./run$1.sh
    echo = `date` job $JOB_NAME done
    ```

    ```sh title="submit.sh"
    #!/bin/sh
    for x in $(seq 0 47); do
      qsub -o run$x.log beast_step_run.job $x
      sleep 0.1
    done
    ```

    Set the `seq` range to the number of steps (`run0.sh` to `run47.sh` here) and run `sh submit.sh` on a login node.

4. When every step has finished, run the analyser in an interactive session, adjusting `-alpha` and `-burnInPercentage` to the analysis:

    ```console
    $ qrsh -pe mthread 8
    $ module load bio/beast
    $ applauncher PathSampleAnalyser -nrOfSteps 48 -alpha 0.3 -rootdir /scratch/genomics/USERNAME/runs -burnInPercentage 25 > pathsampler.out 2>&1
    ```

    `applauncher PathSampleAnalyser -help` lists the arguments.
