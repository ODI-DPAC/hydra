# Python and conda

Modules provide several Python installations, and conda installs anything else into your own space. What is specific to Hydra is which Python modules exist, how to keep NumPy and similar packages to the CPUs a job requested, and how to use conda in sessions and in jobs. How conda itself works is in the conda documentation at <https://docs.conda.io/>.

## Use an installed Python

| Module | Python | Note |
|---|---|---|
| `tools/python` | 3.11.4, Anaconda | default; many packages preinstalled |
| `tools/python/3.13` | 3.13.5, Anaconda | |
| `tools/python/3.14` | 3.14.0 | built from source, base packages only; run it as `python3` |
| `tools/python/3.9`, `3.10` | 3.9.8, 3.10.0 | built from source; run them as `python3` |
| `tools/python/3.7`, `3.8` | 3.7.3, 3.8.8, Anaconda | |
| `tools/python/2.7` | 2.7.16, Anaconda | |
| `intel/python/39-24.0` | 3.9.18, Intel | with the Intel 2024.0 compilers |

Run `module load tools/python` in a session or a job file. The three builds from source provide `python3` and no `python`. With one of them loaded, `python` is still the system's Python 3.6.8. `module -t avail 2>&1 | grep python` lists every version. The Anaconda builds include NumPy, SciPy, pandas, matplotlib and the rest of the Anaconda distribution. `pip list` after loading shows what is there. Packages you install with `pip install --user` go to `~/.local`, where only that Python version finds them.

## Keep NumPy to the requested CPUs

NumPy, SciPy and other packages built on BLAS start one thread per CPU on the node unless told otherwise, which oversubscribes the node and gets the job killed (see [Warning emails](../jobs/efficiency.md#oversubscribed-jobs)). Load one of two modules after the Python module:

| Job | Load |
|---|---|
| serial, or MPI with one process per slot | `tools/python/use-single-thread` |
| `-pe mthread N` | `tools/python/use-multi-thread`, which sets the thread count to `$NSLOTS` |

```sh title="numpy.job"
#$ -S /bin/sh
#$ -N numpy -cwd -j y -o numpy.log
#$ -pe mthread 4
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
module load tools/python
module load tools/python/use-multi-thread
python crunch.py
echo = `date` job $JOB_NAME done
```

`module show tools/python/use-multi-thread` prints the variables it sets. The older names `tools/single-thread-numpy` and `tools/mthread-numpy` still work.

## Use conda

There are two ways to get conda, and they do not mix. One is the preinstalled conda or mamba through a module. The other is a Miniconda you install yourself. Pick one. A `conda init` from one installation writes a block into `~/.bashrc` that breaks the other. If you switch, delete the block between `# >>> conda initialize >>>` and `# <<< conda initialize <<<`.

!!! warning "Run `conda install` under `qrsh`, not on a login node"

    Solving an environment uses a full CPU for minutes, which gets the process killed on a login node (see [Warning emails](../jobs/efficiency.md#high-cpu-use-on-a-login-node)). Start an [interactive session](../interactive/qrsh.md) first. `mamba` solves faster than `conda`.

### Preinstalled conda or mamba

1. In a session, load the module and enable conda:

    ```console
    $ module load tools/conda
    $ start-conda
    (base) $
    ```

    `tools/conda` loads Miniconda 23.1.0 by default. `tools/conda/25.9.1` is the newest, and `tools/conda/3.13` is the full Anaconda distribution. `tools/mamba` (default 25.9.1) is the same with `mamba` in place of `conda`. `module -t avail 2>&1 | grep -E 'tools/(conda|mamba)'` lists them.

2. Create an environment for each project or pipeline and install into it. Environments go under `~/.conda/envs`, which counts against your `/home` quota:

    ```console
    (base) $ conda create -n iqtree-v1 -c bioconda -c conda-forge iqtree=1
    (base) $ source activate iqtree-v1
    (iqtree-v1) $ iqtree --version
    ```

    Use `source activate` rather than `conda activate`, because it works in job files as well as in sessions.

3. In a job file, repeat the three lines:

    ```sh title="iqtree.job"
    #$ -S /bin/sh
    #$ -N iqtree -cwd -j y -o iqtree.log
    #$ -pe mthread 4
    #$ -l mres=8G,h_data=2G,h_vmem=2G
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    module load tools/conda
    start-conda
    source activate iqtree-v1
    iqtree -s alignment.phy -nt $NSLOTS
    echo = `date` job $JOB_NAME done
    ```

Adding `module load tools/conda` and `start-conda` to `~/.bashrc` enables conda in every session. The job file still needs its own lines.

### Your own Miniconda

1. Install Miniconda under your home directory, following the installer's instructions at <https://docs.conda.io/en/latest/miniconda.html>. `/home` is not scrubbed, and a Miniconda with a few environments fits in its quota.

2. Write a [module file](custom-modules.md) that puts it on the path:

    ```tcl title="~/modulefiles/miniconda"
    #%Module1.0
    prepend-path PATH /home/USERNAME/miniconda3/bin
    ```

3. In a job file, load the module, then activate the environment:

    ```sh
    module load ~/modulefiles/miniconda
    source activate iqtree-v1
    ```

## Packages without a conda recipe

Install into an environment with `pip` after activating it, so the package lands in the environment and not in `~/.local`:

```console
(iqtree-v1) $ pip install PACKAGE
```

For software that needs a compiler, load the compiler module first (see [Compilers, libraries and MPI](compilers.md)). For software that needs a license, a build against the cluster's MPI or CUDA libraries, or a shared database, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).

## Jupyter

Jupyter runs on a compute node through an interactive session, with the notebook served to your browser through an ssh tunnel. See [Jupyter](../interactive/jupyter.md).

## Further reading

- [Jupyter](../interactive/jupyter.md) for notebooks on a compute node
- [Submit a parallel job](../jobs/parallel.md) for keeping NumPy and similar packages to the CPUs a job requested
- [conda documentation](https://docs.conda.io/) from the conda project
