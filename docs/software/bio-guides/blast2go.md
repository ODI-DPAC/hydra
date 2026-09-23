# Blast2GO

Hydra has a license to run [BLAST2GO Command Line](https://www.biobam.com/blast2go-command-line-tools/) ([manual here](https://help.biobam.com/space/BCD/2239692845/User+Manual+v.1.5) here). A key advantage of BLAST2GO on Hydra over workstation versions is that the GO information is stored on a local database rather than using a server on the internet, this greatly increases the speed of mapping and annotation.


- License Information
- Limiting Use to Essential Stages
- How to Submit Jobs
- cli.prop and Local Database Access
- Local Database Policy
- Outputting Graphs and Statistics


#### License Information


The Hydra BLAST2GO license allows a **single execution** of the command line version of the program on one licensed node. If there is another job using the license, your job will wait in queue until it is available.


#### Limiting Use to Essential Stages


Because of licensing limitations, it is essential to limit the use of BLAST2GO to essential steps, that is, mapping and annotation, but not BLAST.


The BLAST step can be run on Hydra independently of BLAST2GO. A good strategy for running BLAST on Hydra is to split a fasta file and run each part on a different compute node. With this strategy the BLAST output format 5 (BLAST XML) works well. Combine multiple XML output files with the python script `blastXMLmerge.py` that is available when you load the BLAST2GO module. This script takes the name of output file as the first argument and then the list of XML files to be merged: `blastXMLmerge.py combined.xml *.xml` Use the BLAST2GO option `-loadblast <path>` to load your BLAST results.


How to Submit Jobs


##### Queue specification


- We have created a special queue for BLAST2GO: `-q lTb2g.q`
- You must also request the resource "b2g": `-l b2g`
- Job time limits are the same as other 'long' queues. Memory is limited to 24GB


##### Command line


- Use the module `bioinformatics/blast2go` to load the dependencies for BLAST2GO
- This will create an alias `runblast2go` which incorporates the java options needed for the program.
- A java `maxheapsize` of 2048m for JAVA is used by default. This can be overridden by setting the environmental variable `BLAST2GO_HEAP_SIZE`
- The `-tempfolder` (where logs and temporary files are put) is set to the current working directory. This can be changed with the environmental variable `BLAST2GO_TEMP`
- An OBO file to match the locally stored mapping database version has been downloaded [from the biobam website.](http://resources.biobam.com/b2g_res/obo_files/index.html) You can refer to this local copy of the OBO file with the environmental variable `$BLAST2GO_OBO` 
``


```
## /bin/sh
## ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -q lTb2g.q
#$ -l b2g,mres=32G,h_data=32G,h_vmem=32G
#$ -cwd -j y -N b2g-test -o b2g-test.log
#
## ----------------Modules------------------------- #
#
module load bioinformatics/blast2go
#
## ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
#
#

## Make local copy of cli.prop
## (this overwrites any existing cli.prop file in the current directory and only needs to be done once)
hydracliprop

## Run example dataset:
runblast2go \
  -properties cli.prop \
  -loadfasta /share/apps/bioinformatics/blast2go/1.5.1/example_data/plant_nucleotide.fasta \
  -loadblast31 /share/apps/bioinformatics/blast2go/1.5.1/example_data/plant_blast_31.zip \
  -useobo $BLAST2GO_OBO \
  -mapping \
  -annotation \
  -savebox example.box \
  -savereport example.pdf

#
echo = `date` job $JOB_NAME done
```


#### cli.prop and Local Database Access


The file `cli.prop` gives the settings for the execution of the program. A template configured with the database access information for running BLAST2GO on the Hydra cluster can be copied to your current directory with the command `hydracliprop` after you load the BLAST2GO module.


#### Local Database Policy


The local database is large and system constraints limit us from keeping old versions. When the database is updated, the old version will no longer be available.


#### Outputting Graphs and Statistics


The command line version of BLAST2GO can produce many types of graphs as well as a summary report. The option `-statistics all` will produce all available statistics as png images, csv and .b2g files. Start BLAST2GO with `-statistics` (committing any options) to see a list of available charts. The option `--savereport <name>` creates a PDF with common summary statistics. Creating a combined graph can only be done with the GUI based [BLAST2GO Basic](https://www.blast2go.com/blast2go-pro/b2g-register-basic) which has a free license. This program can also be used to work with the .b2g files created by the command line version.


20 May 2024 MPK
