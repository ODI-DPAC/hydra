# BEAST

### Performance


Please see: [http://www.beast2.org/performance-suggestions/index.html](http://www.beast2.org/performance-suggestions/index.html) for information about optimizing performance. The [BEAGLE](https://github.com/beagle-dev/beagle-lib) libraries will be available when you load the BEAST module and BEAGLE is enabled used by default. There are BEAGLE options such as -beage_SSE which may help performance.


### Confirm version of BEAST that is running


Make sure that the intended version of BEAST shows in the log file. The first time beast is run, the program makes a copy of beast.jar and beast.src.jar into `~/.beast/2.x/BEAST/lib` . A separate subdirectory in `~/.beast` is created for versions 2.6 and 2.7. Minor revisions within these releases are not automatically updated when you re-run 2.6 or 2.7. For example, if you run beast 2.6.6, a copy of this jar file is put into `~/.beast/2.6/BEAST/lib` . If you subsequently use the 2.6.7 module, the 2.6.6 version in your `~/.beast/2.6` will be used instead of 2.6.7. To resolve this remove `~/.beast/2.6/BEAST` before running to get a new copy of the minor revision.


### `beagle` module


The [beagle library](https://github.com/beagle-dev/beagle-lib) is available as an additional module that can be loaded along with the beast module. The java components of the beagle library have been compiled with the JDK 8 for use with Beast 2.6.x in the module `bio/beagle/4.0.1-j8` and with JDK 17 in the module `bio/beagle/4.0.1-j17` for use with Beast 2.7.6.


At this time the beagle libraries have not been compiled with GPU support. Please contact us if you need this functionality.


### Add-ons


To add a beast add-on use the following command after you've loaded the beast module (`module load bioinformatics/beast`) first list available add-ons:


```
packagemanager -list
```


and then add one with


```
packagemanager -add SNAPP
```


The add-on will be downloaded to ~/.beast


### Tips on running SNAPP


The SNAPP add-on documentation for BEAST has information on [running analyses on a cluster](https://www.beast2.org/path-sampling/#:~:text=Setting%20up%20an%20analysis%20for%20a%20cluster).


1. Add `doNotRun='true'` to the `run` section of your BEAST XML file.
2. Start an interactive session with enough memory to start the BEAST job: `qrsh -pe mthread 8`
3. In the interactive session, load the BEAST module and start the execution of your XML file. In the `-threads` option, specify the number of SNAPP steps you specific in your XML (in the example it is 48)


```
module load bio/beast
beast -threads 48 your_file.xml
```
4. This creates 48 step directories and a `run<number>.sh` script for each one. You can submit a separate job for each of the bash scripts. A sample job file (beast_step_run.job) and a bash script to submit the jobs are below.


```{.text title="beast_step_run.job"}
## /bin/sh
## ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -q lThM.q
#$ -l mres=16G,h_data=16G,h_vmem=16G,himem
#$ -cwd
#$ -j y
#$ -N beast_step_run
#$ -o beast_step_run.log
#
## ----------------Modules------------------------- #
module load bioinformatics/beast
#
## ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS

#
if [ -z $1 ]; then
 echo "Give the run number as an argument: e.g. qsub beast_step_run.job 0"
 exit 1
fi

source ./run${1}.sh
#
echo = `date` job $JOB_NAME done
```


```{.text title="submit.sou"}
for x in $(seq 0 47); do
 qsub -o run${x}.log beast_step_run.job ${x}
 sleep 0.1
done
```


Change the `seq` command to match the range of steps. Shown here is for 48 steps which are numbered `run0.sh` to `run47.sh`
5. Submit the steps as separate cluster jobs with: `source submit.sou`
6. When all the jobs are complete, run the `PathSampleAnalyser` to get the final output. In the below example, the output is redirected to the file `pathsampler.out` . You should of course adjust the arguments (like `alpha` and `burnInPercentage` to suite your analysis.


```{.text title="PathSampleAnalyser"}
qrsh -pe mthread 8
module load bio/beast
applauncher PathSampleAnalyser -nrOfSteps 48 -alpha 0.3 -rootdir /path/to/your/runs -burnInPercentage 25 >pathsampler.out 2>&1
```


You can see all the `PathSampleAnalyser` arguments with: `applauncher PathSampleAnalyser -help`
