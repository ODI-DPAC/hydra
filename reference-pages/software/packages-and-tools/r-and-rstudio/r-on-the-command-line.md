---
title: "R on the Command Line"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/385975489/R+on+the+Command+Line"
date-modified: "2026-02-26"
author: "AEW/MPK/SGK"
---

1. [Overview](r-on-the-command-line.md)
2. [Installing Packages](r-on-the-command-line.md)
3. [Multi-threading](r-on-the-command-line.md)
4. [Examples](r-on-the-command-line.md)
5. [Getting help and providing feedback](r-on-the-command-line.md)


### 1. Overview


- R version 4.4.0 (built with Rocky 8 default gcc, i.e. 8.5.0) is available by loading the corresponding module: 
`% module load bio/R`
- The `tools/R` module is now equivalent to `bio/R` and `bioinformatics/R`, and will default to version 4.4.0
- Users who need a more recent version of R should consider using Anaconda to install R and needed packages in their space. See below for info on[Anaconda on Hydra](http://confluence.si.edu#conda).


### 2. Installing Packages


- Users can install packages their own packages in a user-specific library. When the `install.packages()` command is used, there will be a notification that the system-wide library is not writable and you will prompted to create a personal library in your home folder. All future packages that you install will be installed into your personal library. You will then be prompted to choose a repository.
- Packages only need to be installed one time to be accessible to all of your R jobs on all nodes on the cluster. Packages can be installed with the `install.packages()` command interactively from the login node or an interactive job. In some cases the development ("-devel") packages required to compile R packages are installed only on these nodes while the corresponding runtime packages (needed to execute the compiled packages) are on all the compute nodes.
- $NSLOTS in R scripts 
It is best practice to use the environmental variable `NSLOTS` in your scripts to specify the number of cores to use for R commands that supports multiple cores. By using `NSLOTS` rather than hard-coding the number of cores in your R script, your job will utilize the requested number of slots, even if you change your qsub submission parameters.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Use the R Base function `Sys.getenv()` to access the value of `$NSLOTS` from within your script.


```
## Script using Sys.gentenv() to read the value of $NSLOTS

numcores <- Sys.getenv("NSLOTS")
```
- Proper parallelization of `makeCluster()`: 
R packages that incorprate the `makeCluster()` function must specify `type="FORK"` as an argument. Without this, Hydra's scripts that kill zombie jobs will terminate the R processes created by `makeCluster()`.


```
cl <- makeCluster(numcores, type="FORK")
```
- Multiple jobs activating your R conda environment at one time: 
If you are using R through a conda environment, multiple jobs activating the environment at the same time may cause jobs to hang. When you execute `conda activate env_name`, scripts in the environment's `etc/conda/activate.d/` directory are executed. With R environments, there is a script, `activate-r-base.sh` which runs `R CMD javareconf` to configure R for the current java environment. If this is run more than once at a time, the configuration files that are produced will overwrite each other and hang the `activate` process. To avoid this, you can edit `etc/conda/activate.d/activate-r-base.sh`and comment out this line. 

```
# R CMD javareconf > /dev/null 2>&1 || true
```

Another option is to modify your `PATH` environmental variable rather than activating the environment. This method will work in many cases, but by skipping the `activate` process other environmental variables that some R and conda packages need will not be set.


### 3. Multi-threading


Some R packages use parallelized libraries that use multithreading (like LAPACK), and by default will use all the cores on the compute node.


This is not the way to run on a shared resource.


To limit the number of threads, you should set the value of `OMP_NUM_THREADS` to the number of threads it should use:


- 
    - for serial cases, set it to 1;
    - if you use `-pe mthread N`, set it to `$NSLOTS;`
    - if you use `makeCluster()` and use all the slots, set it to 1;
    - alternatively to can combine `makeCluster()` and `OMP_NUM_TREADS (`aka hybrid mode) and set them to values whose product corresponds to the value of $NSLOTS.


### 4. Examples


```{.text title="bash example:"}
export OMP_NUM_THREADS=1
```


or


```{.text title="csh example:"}
setenv OMP_NUM_THREADS 1
```
