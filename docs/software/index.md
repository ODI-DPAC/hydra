# Software

Software on Hydra is provided through environment modules. `module avail` lists everything; `module load NAME/VERSION` puts it on your path.

- [Modules](modules.md): the `module` command, defaults, conflicts, the `ml` shortcut
- [Compilers, libraries and MPI](compilers.md): GNU, Intel and NVIDIA compilers; building MPI and multithreaded programs
- [Python and conda](python.md)
- [R](r.md)
- [Julia, MATLAB, IDL and Java](other-languages.md)
- [Bioinformatics modules](bio-modules.md): the full list, generated from the cluster
- [Bioinformatics guides](bio-guides/index.md): per-tool notes for BLAST, BUSCO, SPAdes and others
- [GPUs](gpus.md)
- [Containers](containers.md)
- [Writing your own module file](custom-modules.md)

Most packages install into your own environment with conda; see [Python and conda](python.md). For software that needs a license, a build against the cluster's MPI or CUDA libraries, or a shared database, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).
