# Local bioinformatics databases

Several commonly used bioinformatics reference databases are maintained on Hydra for general use. These databases were chosen because of their large storage requirement and common use. By having a local copy available to Hydra users, there is not a need for individuals to download their own copy of these resources.


Note: When database versions are updated, older copies of the databases are *not* retained on Hydra.


Please contact [si-hpc\@si.edu](mailto:si-hpc@si.edu) for more information or if there is a database you suggest we add.


These databases are available at:


```
/scratch/dbs
```


## Available databases


### `/scratch/dbs/blast`


Databases for [BLAST](https://www.ncbi.nlm.nih.gov/books/NBK279690/) and [diamond](https://github.com/bbuchfink/diamond).


```
/scratch/dbs/blast
└── v5/            # v5 of the nr, nt, refseq_protein, swissprot, taxdb databases
    ├── README     # Download commands, DB and version information
    ├── mito/      # v5 of mito  
    └── core_nt    # v5 of core_nt
```


Note: Loading Hydra's BLAST modules sets the environmental variable `BLASTDB` to `/scratch/dbs/blast/v5`. See the Hydra [BLAST Documentation](blast.md)for more information.


### `/scratch/dbs/dfam`


```
/scratch/dbs/dfam
├── REAMDE           # DB and version information
├── 3.8/             # dfam FamDB 3.8
└── 3.9/             # dfam FamDB 3.9
```


Local copies of all of the [dfam](https://www.dfam.org/) [FamDB](https://www.dfam.org/help/family) transposable elements partitions. This is used in the Hydra RepeatMasker modules.


- dfam 3.8: for RepeatMasker 4.1.x: h5 files from [https://www.dfam.org/releases/Dfam_3.8/families/FamDB/](https://www.dfam.org/releases/Dfam_3.8/families/FamDB/)
- dfam 3.9: for RepeatMasker 4.2.x: h5 files from [https://www.dfam.org/releases/Dfam_3.9/families/FamDB/](https://www.dfam.org/releases/Dfam_3.9/families/FamDB/)
- See the file "README.txt" in these directories for dfam's listing of the taxonomic grouping for the partitions.


Note: in the RepeatMasker installations in `/share/apps/bio/repeatmasker`, these .h5 files are symlinked to the install's `share/RepeatMasker/Libraries/famdb` directory.


### `/scratch/dbs/kraken`


```
/scratch/dbs/kraken
├── REAMDE         # DB and version information
├── core_nt/       # "Very large collection, inclusive of GenBank, RefSeq, TPA and PDB"
└── standard/      # "Refseq archaea, bacteria, viral, plasmid, human, UniVec_Core"
```


A local copy of the "standard" and "[core_nt](https://ncbiinsights.ncbi.nlm.nih.gov/2024/07/18/new-blast-core-nucleotide-database/)" indexes from [https://benlangmead.github.io/aws-indexes/k2](https://benlangmead.github.io/aws-indexes/k2)


### `/scratch/dbs/kraken-uniq`


```
/scratch/dbs/kraken-uniq
├── REAMDE         # DB and version information
└── standard/      # "archaea, bacteria, viral, human, UniVec_Core"
```


A local copy of the "standard" [kraken-uniq](https://github.com/fbreitwieser/krakenuniq) index from [https://benlangmead.github.io/aws-indexes/k2](https://benlangmead.github.io/aws-indexes/k2)


12 Feb 2026 MPK
