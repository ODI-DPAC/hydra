# BLAST

BLAST matches query nucleotide or protein sequences against a database. The module is `bio/blast`, and loading it sets `BLASTDB` to the local copy of the NCBI databases under `/scratch/dbs/blast/v5` (nr, nt, refseq_protein, swissprot, taxdb, mito, core_nt; see [Local databases](databases.md)), so `-db nt` needs no path. NCBI's manual at <https://www.ncbi.nlm.nih.gov/books/NBK279675/> describes every option.

## Search a database

`blastn` for nucleotide queries, `blastp` for protein; the options are the same.

| Option | Meaning |
|---|---|
| `-task` | the search type, for example `megablast` |
| `-db` | the database, for example `nt` or `nr` |
| `-query` | the input FASTA file |
| `-outfmt` | the output format; `5` is XML, which Blast2GO and other tools read |
| `-out` | the output file |
| `-num_threads` | threads; set it to `$NSLOTS` in a job that requested `-pe mthread N` |

```sh title="blast.job"
#$ -S /bin/sh
#$ -N blast -cwd -j y -o blast.log
#$ -q lThM.q
#$ -l mres=32G,h_data=32G,h_vmem=32G,himem
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
module load bio/blast
blastn -task megablast -db nt -query queries.fa -outfmt 5 -out queries.xml
gzip queries.xml
echo = `date` job $JOB_NAME done
```

BLAST output is large and repetitive; compress it in the job, as above. Remove duplicate sequences from the input first. A query file in which most sequences hit uses memory in proportion to the hits and can exceed even a high-memory node; split such files (below).

## Build a database

`makeblastdb` builds a database from a FASTA file; `-dbtype nucl` for nucleotide, `prot` for protein.

```sh title="makedb.job"
#$ -S /bin/sh
#$ -N makedb -cwd -j y -o makedb.log
#$ -q sThM.q
#$ -l mres=12G,h_data=12G,h_vmem=12G,himem
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
module load bio/blast
makeblastdb -in sequences.fa -parse_seqids -dbtype nucl
echo = `date` job $JOB_NAME done
```

## Split a large search across jobs

`-num_threads` parallelises one search on one node. For a large input, splitting the FASTA into files of 1,000 to 10,000 sequences and searching each in its own job finishes sooner and uses less memory per job. Concatenate the results afterwards. A [job array](../../jobs/arrays.md) does this from one job file; the loop below does it with one job per file.

```sh title="blast-part.job"
#$ -S /bin/sh
#$ -cwd -j y
#$ -q mThC.q
#$ -l mres=4G,h_data=4G,h_vmem=4G
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
module load bio/blast
blastp -db nr -query $1 -outfmt 5 -out $1.out
echo = `date` job $JOB_NAME done
```

```console
$ for x in *.fa; do qsub -N blast-$x -o $x.log blast-part.job $x; done
```

`$1` is the file name passed after the job file on the `qsub` line; see [Pass arguments to the job](../../jobs/submit.md#pass-arguments-to-the-job).
