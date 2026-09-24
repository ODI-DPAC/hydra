# Software

Software on Hydra is provided through environment modules: `module avail` lists what is installed, and `module load NAME/VERSION` puts one package on your path for the session or the job. Most packages install into your own environment with conda instead.

To use a package the cluster provides, [find and load its module](modules.md). For Python packages and anything on conda-forge or Bioconda, [set up conda](python.md) in your own space. [R](r.md), [Julia, MATLAB, IDL and Java](other-languages.md), [GPUs](gpus.md) and [containers](containers.md) each have a page. Software you built yourself gets a [module file of your own](custom-modules.md) so jobs can load it.

!!! warning "Set the thread count from `$NSLOTS`"

    NumPy, R's linear-algebra libraries, IDL, Java and many other packages start one thread per CPU on the node unless told otherwise. A job that does this is oversubscribed and can be killed; see [Warning emails](../jobs/efficiency.md#oversubscribed-jobs). Each page below says how to set the count for that software.

The reference pages list the [compilers, libraries and MPI implementations](compilers.md) and the [installed modules](module-list.md), and the [software guides](guides/index.md) give a job file for specific packages. For software that needs a license, a build against the cluster's MPI or CUDA libraries, or a shared database, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).
