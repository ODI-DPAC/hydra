# Bioinformatics guides

Notes on running specific packages on Hydra: the module to load, the queue and memory to request, and a job file.

- [ALLPATHS-LG](allpaths-lg.md)
- [BEAST](beast.md)
- [BLAST](blast.md)
- [BLAST2GO](blast2go.md)
- [BUSCO](busco.md)
- [GeneMark-ES](genemark-es.md)
- [MaSuRCA](masurca.md)
- [SMC++](smc.md)
- [SPAdes](spades.md)
- [Local databases](databases.md): BLAST, RefSeq and other databases kept on Hydra

[Bioinformatics modules](../bio-modules.md) lists every installed package. `module help bio/NAME` on a login node prints a package's executables and how to run it; `module avail bio/NAME` lists its versions.

Packages on Bioconda or conda-forge install into your own environment; see [Python and conda](../python.md). For software that needs a license, a build against the cluster's MPI or CUDA libraries, or a shared database, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).
