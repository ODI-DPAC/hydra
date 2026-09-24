# Software guides

Each guide gives, for one package, the module to load, the queue and memory to request, and a job file.

- [BEAST](beast.md)
- [BirdNET](birdnet.md)
- [BLAST](blast.md)
- [Blast2GO](blast2go.md)
- [BUSCO](busco.md)
- [MaSuRCA](masurca.md)
- [SMC++](smc.md)
- [SPAdes](spades.md)
- [Local databases](databases.md): BLAST, Dfam and Kraken databases kept on Hydra

[Installed modules](../module-list.md) lists every `bio/` and `tools/` package. `module help bio/NAME` on a login node prints a package's executables and how to run it; `module avail bio/NAME` lists its versions.

Packages on Bioconda or conda-forge install into your own environment; see [Python and conda](../python.md). For software that needs a license, a build against the cluster's MPI or CUDA libraries, or a shared database, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).
