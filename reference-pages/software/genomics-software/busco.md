---
title: "BUSCO"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152348/BUSCO"
date-modified: "2026-01-27"
author: "SGK/MPK"
---

BUSCO (Benchmarking Universal Single-Copy Orthologs) assesses genome assembly completeness by searching for universal and lineage-specific single-copy orthologs in [OrthoDB](http://www.orthodb.org). It can also be used to train gene prediction models for AUGUSTUS. BUSCO requires a genome assembly (in fasta format) and an ortholog database from OrthoDB (see documentation [here](http://busco.ezlab.org) for best database choices).


## Augustus (optional)


If you plan on using Augustus with BUSCO you will need to make a copy of the Augustus `config` directory to your working space.


- The alias `cp_aug_config` is available when you load the busco module. It copies the `config` directory into the current working directory.
- Loading the busco module sets the env variable `AUGUSTUS_CONFIG_PATH` to the `config` directory of the current directory.
    - You can change this: `export AUGUSTUS_CONFIG_PATH="/path/to/your/workspace/config"`


## Example Job File


```
#$ -S /bin/sh
#$ -pe mthread 24
#$ -q mThM.q
#$ -l mres=240G,h_data=10G,h_vmem=10G,himem
#$ -cwd
#$ -j y
#$ -N busco
#$ -o busco.log
#
# ----------------Modules------------------------- #
module load bio/busco/6.0.0
#
# ----------------Your Commands------------------- #
#
echo + $(date) job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
#

busco -i assembly.fa.gz -m genome -l vertebrata --cpu $NSLOTS

#
echo = $(date) job $JOB_NAME done
```
