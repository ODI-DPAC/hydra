# Local bioinformatics databases

Hydra keeps large, widely used reference databases under `/scratch/dbs`, so that each user does not download a copy. Email [SI-HPC@si.edu](mailto:SI-HPC@si.edu) to request a database.

!!! warning "Old versions are not kept"

    An update removes the previous copy. If your pipeline depends on a particular version, record the version from the `README` in the database directory.

## `/scratch/dbs/blast`

This directory holds the databases for [BLAST](https://www.ncbi.nlm.nih.gov/books/NBK279690/) and [diamond](https://github.com/bbuchfink/diamond).

```text
/scratch/dbs/blast
└── v5/            # v5 of the nr, nt, refseq_protein, swissprot, taxdb databases
    ├── README     # download commands, database and version information
    ├── mito/      # v5 of mito
    └── core_nt    # v5 of core_nt
```

Loading `bio/blast` sets `BLASTDB` to `/scratch/dbs/blast/v5`, so `-db nt` finds the local copy. See [BLAST](blast.md).

## `/scratch/dbs/dfam`

```text
/scratch/dbs/dfam
├── README           # database and version information
├── 3.8/             # Dfam FamDB 3.8
└── 3.9/             # Dfam FamDB 3.9
```

Local copies of the [Dfam](https://www.dfam.org/) [FamDB](https://www.dfam.org/help/family) transposable-element partitions, used by the RepeatMasker modules: Dfam 3.8 for RepeatMasker 4.1.x, from <https://www.dfam.org/releases/Dfam_3.8/families/FamDB/>, and Dfam 3.9 for RepeatMasker 4.2.x, from <https://www.dfam.org/releases/Dfam_3.9/families/FamDB/>. `README.txt` in each directory lists the taxonomic grouping of the partitions. In the RepeatMasker installations under `/share/apps/bioinformatics/repeatmasker`, these `.h5` files are linked into `share/RepeatMasker/Libraries/famdb`.

## `/scratch/dbs/kraken`

```text
/scratch/dbs/kraken
├── README         # database and version information
├── core_nt/       # "very large collection, inclusive of GenBank, RefSeq, TPA and PDB"
└── standard/      # "RefSeq archaea, bacteria, viral, plasmid, human, UniVec_Core"
```

Local copies of the `standard` and [`core_nt`](https://ncbiinsights.ncbi.nlm.nih.gov/2024/07/18/new-blast-core-nucleotide-database/) Kraken 2 indexes from <https://benlangmead.github.io/aws-indexes/k2>.

## `/scratch/dbs/kraken-uniq`

```text
/scratch/dbs/kraken-uniq
├── README         # database and version information
└── standard/      # "archaea, bacteria, viral, human, UniVec_Core"
```

A local copy of the `standard` [KrakenUniq](https://github.com/fbreitwieser/krakenuniq) index from <https://benlangmead.github.io/aws-indexes/k2>.
