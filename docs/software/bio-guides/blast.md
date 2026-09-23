# BLAST

BLAST (Basic Local Alignment Search Tool) is a greedy aligner used to match query nucleotide/amino acid sequences against a database. Databases include the complete non-redundant protein/nucleotide databases (nr/nt), single genome databases, and custom databases.


### Nucleotide Query


Nucleotide queries use the 'blastn' command (available in the module bioinformatics/blast). Important options include:


```
-task # Specifies the type of query (e.g. "megablast")
```


```
-db # Specifies the database to query (e.g.  nt)
```


```
-query # Specifies the input file in fasta format
```


```
-outfmt # Specifies the format to output hits in (e.g. 5 for xml)
```


```
-out # Specifies the name of the output file
```


**Example commands:**


```
module load bioinformatics/blast
```


```
blastn -help # Print help file for all options
```


```
blastn -task "megablast" -db nt -query <yourfastafile> -outfmt 5 -out <yourfastahitsinxml> # Megablasts your sequences against the nt database and outputs hits in xml
```


**Example qsub file**


```
#!/bin/sh
## ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -j y -cwd
#$ -q lThM.q
#$ -l mres=32G,h_data=32G,h_vmem=32G,himem
#$ -N blast_against_nt
#
## ----------------Modules------------------------- #
module load bioinformatics/blast
#
## ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
blastn -task "megablast" -db nt -query <yourfastafile> -outfmt 5 -out <yourfastahitsinxml>
gzip <yourfastahitsinxml>
echo + `date` job $JOB_NAME done
```


```

```


### Protein Query


Protein queries use the command 'blastp'. Other syntax is similar to blastn. See 'Nucleotide Query' section above for more details for Hydra job creation.


### Generating a Custom Database


Custom blast databases can be generated from fasta files using 'makeblastdb' (available in the module bioinformatics/blast).


**Example commands:**


```
module load bioinformatics/blast
```


```
makeblastdb -help # Print help file for all options
```


```
makeblastdb -in <yourfastafile> -parse_seqids -dbtype <nucl or prot> # Use 'nucl' for a nucleotide database, 'prot' for a protein database
```


**Example qsub file**


```
#!/bin/sh
## ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -j y -cwd
#$ -q sThM.q
#$ -l mres=12G,h_data=12G,h_vmem=12G,himem
#$ -N custom_db
#
## ----------------Modules------------------------- #
module load bioinformatics/blast
#
## ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
makeblastdb -in <yourfastafile> -parse_seqids -dbtype <nucl or prot>
echo + `date` job $JOB_NAME done
```


****


```

```


### Parallelization


Although BLAST jobs can be natively parallelized using the -num_threads option, often it is better to split large BLAST jobs into smaller files and concatenate the results afterwards. Files containing 1000 to 10,000 sequences each have performed well on Hydra. The jobs can be run using [job arrays](../../jobs/arrays.md) or using a bash or csh loop to submit a separate job for each sequence file.


#### Submitting separate jobs for each input file


**Example qsub file**


```
## /bin/sh
## ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -q mThC.q
#$ -l mres=4G,h_data=4G,h_vmem=4G
#$ -cwd
#$ -j y
#
## ----------------Modules------------------------- #
module load bioinformatics/blast
#
## ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
#
blastp -db nr -query $1 -outfmt 5 -out $1.out
#
echo = `date` job $JOB_NAME done
```


The `$1` variable in the blastp command above will contain the name of the sequence file when called with the bash command below.


**Example bash script to execute qsub**


```
for x in *.fa; do qsub -N blast-${x} -o ${x}.log blast.job ${x}; done
```


This script should be run from the Hydra login node command line. In the example it will submit a seperate qsub for each file ending in .fa in the current directory and the qsub job file is named `blast.job`. These should be adjusted for your case. The input file name will be available to the qsub file as `$1`. The qsub command specifies the job name (`-N`) and log file (`-o`) for the scheduler.


### Memory and Disk Space Considerations


It is often best to remove duplicate molecules BEFORE BLAST analysis to reduce run-time and results file size.


BLAST jobs are not memory efficient and will easily exceed the capabilities of even high-memory nodes if there are sufficient hits within a query file. If you have a file where you expect most sequences to be identified (e.g. a barcoding project), you should reduce the number of sequences per individual blast job and run more jobs.


BLAST output files are highly redundant. Always compress your files afterwards to reduce disk usage.


### Further Information


Detailed explanations of all the BLAST parameters are available from the NCBI: [http://www.ncbi.nlm.nih.gov/books/NBK279675/](http://www.ncbi.nlm.nih.gov/books/NBK279675/)
