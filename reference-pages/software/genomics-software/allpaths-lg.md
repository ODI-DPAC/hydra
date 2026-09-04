---
title: "ALLPATHS-LG"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152344/ALLPATHS-LG"
---

<under construction>


ALLPATHS-LG is a genome assembly program that requires at least two different kinds of Illumina libraries (e.g. paired-end and mate-pair).


Here is a link to the software and documentation: [http://software.broadinstitute.org/allpaths-lg/blog/](http://software.broadinstitute.org/allpaths-lg/blog/)


Parallel Support


Parts of ALLPATHS-LG can run in parallel and performance seems to improve up to 32 threads. More than that does not seem to help.


## Memory


ALLPATHS-LG requires running on at least the high-memory queue (512GB), and sometimes the ultra-high-memory queue (1TB). Genome size and coverage depth will determine the amount of RAM you need.


## Invoking the program


### ALLPATHS-LG runs with two separate commands:


1. ### PrepareAllPathsInputs.pl (required arguments)


Resources: Can usually run on sThM.q, unless you have very high coverage data, then you might need mThM.q


Module: module load bioinformatics/allpaths-lg/52415


Options: PLOIDY=2 for diploid, PLOIDY=1 for haploid


HOSTS=$NSLOTS (# threads)


DATA_DIR=


IN_GROUPS_CSV=


IN_LIBS_CSV=


PHRED_64=True/False depending on type of quality scoring


#### 2. RunAllPathsLG (required arguments)


PRE=


DATA_SUBDIR=


REFERENCE_NAME=


RUN=


THREADS=$NSLOTS


OVERWRITE=True


Sample in_groups.csv file


```
file_name,library_name,group_nameSRR946954_*.fastq,G10cloDADDLAAPE,SRR946954SRR946955_*.fastq,G10cloDAODBAAPE,SRR946955SRR946957_*.fastq,G10cloDAODIAAPE,SRR946957SRR946958_*.fastq,G10cloDAODIABPE,SRR946958SRR946959_*.fastq,G10cloDAODLAAPE,SRR946959SRR946960_*.fastq,G10cloDAODMAAPE,SRR946960SRR946961_*.fastq,G10cloDAODTAAPE,SRR946961SRR946962_*.fastq,G10cloDAODUAAPE,SRR946962SRR946963_*.fastq,G10cloDAODWAAPE,SRR946963SRR946964_*.fastq,G10cloDAODWAAPE,SRR946964
```


Sample in_libs.csv file


```
library_name,project_name,organism_name,type,paired,frag_size,frag_stddev,insert_size,insert_stddev,read_orientation,genomic_start,genomic_endG10cloDAODBAAPE,Manakin,Manacusvitellinus,fragment,1,170,17,,,inward,,G10cloDADDLAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,5000,500,outward,,G10cloDAODIAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,500,50,outward,,G10cloDAODIABPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,500,50,outward,,G10cloDAODLAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,500,50,outward,,G10cloDAODMAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,800,80,outward,,G10cloDAODTAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,10000,1000,outward,,G10cloDAODUAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,20000,2000,outward,,G10cloDAODWAAPE,Manakin,Manacusvitellinus,jumping(sheared),1,,,2000,200,outward,,
```


## Sample qsub scripts


PrepareAllPathsInputs.pl step:


```
# /bin/sh# ----------------Parameters---------------------- ##$ -S /bin/sh#$ -pe mthread 4#$ -q sThM.q#$ -l mres=30G,h_data=30G,h_vmem=30G,himem#$ -j y#$ -N allpaths_prepare#$ -cwd ## ----------------Modules------------------------- #module load bioinformatics/allpaths-lg/52415## ----------------Your Commands------------------- ##echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAMEecho + NSLOTS = $NSLOTS#perl PrepareAllPathsInputs.pl DATA_DIR=/path/to/data/ IN_GROUPS_CSV=/path/to/in_groups_manakin.csv IN_LIBS_CSV=/path/to/in_libs_manakin.csv PHRED_64=True PLOIDY=2 HOSTS=$NSLOTS#echo = `date` job $JOB_NAME done
```


RunAllPathsLG step:


```
 
```


```
# /bin/sh# ----------------Parameters---------------------- ##$ -S /bin/sh#$ -pe mthread 8#$ -q lThM.q#$ -l mres=60G,h_data=60G,h_vmem=60G,himem#$ -j y#$ -cwd#$ -N allpaths## ----------------Modules------------------------- #module load bioinformatics/allpaths-lg/52415## ----------------Your Commands------------------- ##echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAMEecho + NSLOTS = $NSLOTS#RunAllPathsLG PRE=/path/to/data/ DATA_SUBDIR=/ REFERENCE_NAME= RUN=run1 THREADS=$NSLOTS OVERWRITE=True #echo = `date` job $JOB_NAME done
```


```

```


## Special notes
