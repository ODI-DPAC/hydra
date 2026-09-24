# R

R runs from the command line and in jobs through the `bio/R` module. Packages install into your own library, and R has to be kept to the CPUs a job requested. RStudio, on the RStudio server or on a compute node, is under [RStudio](../interactive/rstudio.md).

## Load R

```console
$ module load bio/R
$ R --version
```

`bio/R` loads R 4.4.0; `bio/R/4.4.1` selects another version, and `module -t avail 2>&1 | grep 'bio/R/'` lists them. `tools/R` and `bioinformatics/R` are aliases of `bio/R`. For a newer R than the modules provide, install it in a conda environment (see [Python and conda](python.md)) with `conda create -n r-env -c conda-forge r-base`.

## Install packages

1. Start R on a login node or in an [interactive session](../interactive/qrsh.md) and install as usual:

    ```r
    install.packages("vegan")
    ```

    R reports that the system library is not writable and offers to create a personal library under your home directory; accept. Every package you install from then on goes there, and every job on every node sees it.

2. For a package that compiles C or Fortran code, install from a login node or an interactive session. Those nodes have the system development libraries such packages need and the compute nodes do not, so an install started inside a batch job fails at the compile step.

## Use the requested CPUs

R functions that run in parallel take the number of workers from `NSLOTS`, so the job uses the slots it requested however it was submitted:

```r
numcores <- as.integer(Sys.getenv("NSLOTS"))
cl <- makeCluster(numcores, type = "FORK")
```

`type = "FORK"` is required on Hydra: without it, the cluster's cleanup of orphaned processes kills the workers.

R's linear-algebra libraries start one thread per CPU on the node unless told otherwise, which oversubscribes the node. Set `OMP_NUM_THREADS` in the job file before starting R:

| Job | Set |
|---|---|
| serial | `export OMP_NUM_THREADS=1` |
| `-pe mthread N`, threads only | `export OMP_NUM_THREADS=$NSLOTS` |
| `-pe mthread N`, all slots used by `makeCluster()` | `export OMP_NUM_THREADS=1` |
| `makeCluster()` with K workers plus threads | `export OMP_NUM_THREADS=$((NSLOTS / K))` |

```sh title="model.job"
#$ -S /bin/sh
#$ -N model -cwd -j y -o model.log
#$ -pe mthread 8
#$ -l mres=16G,h_data=2G,h_vmem=2G
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
module load bio/R
export OMP_NUM_THREADS=1
Rscript model.R
echo = `date` job $JOB_NAME done
```

## R in a conda environment

Several jobs activating the same R conda environment at once can hang: the environment's `activate.d/activate-r-base.sh` runs `R CMD javareconf`, and concurrent runs overwrite each other's files. Either edit that script so the line reads

```sh
R CMD javareconf > /dev/null 2>&1 || true
```

or put the environment's `bin` directory on `PATH` in the job file instead of activating it, which works for most packages but skips the other variables activation sets.

For help, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu) with the full error message and whether you were using the RStudio server, RStudio on a node, or R from the command line.
