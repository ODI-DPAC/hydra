# Software

Hydra provides software through environment modules. You list what is installed with `module avail` and put one package on your path with `module load NAME/VERSION`. Most other packages you install yourself, into a conda environment in your own space.

- For a package that is installed, [find and load its module](modules.md).
- For a Python package, or anything on conda-forge or Bioconda, [set up conda](python.md) and install it there.
- For software you built yourself, [write a module file](custom-modules.md) so that your jobs can load it.

We have a page each for [R](r.md), for [Julia, MATLAB, IDL and Java](other-languages.md), for [GPUs](gpus.md) and for [containers](containers.md).

!!! warning "Set the thread count from `$NSLOTS`"

    NumPy, R's linear-algebra libraries, IDL, Java and many other packages start one thread per CPU on the node unless told otherwise. A job that does this is oversubscribed and we can kill it. See [Warning emails](../jobs/efficiency.md#oversubscribed-jobs). Each page below says how to set the count for that software.

When you need to look something up, the reference pages cover the [compilers, libraries and MPI implementations](compilers.md) and the [installed modules](module-list.md). For a handful of packages we provide a [guide](guides/index.md) with a working job file. If you need software that requires a license, a build against the cluster's MPI or CUDA libraries, or a shared database, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).
