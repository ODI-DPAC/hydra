# BUSCO

BUSCO (Benchmarking Universal Single-Copy Orthologs) assesses the completeness of a genome, transcriptome or protein set by searching for universal and lineage-specific single-copy orthologs from [OrthoDB](http://www.orthodb.org). The module is `bio/busco`; `module -t avail 2>&1 | grep busco` lists the versions.

## Augustus

BUSCO can run Augustus for gene prediction, which needs a writable copy of the Augustus `config` directory. Loading the module defines the alias `cp_aug_config`, which copies that directory into the current directory, and sets `AUGUSTUS_CONFIG_PATH` to `config` under the current directory. To keep one copy elsewhere, set the variable in the job file:

```sh
export AUGUSTUS_CONFIG_PATH=/scratch/genomics/USERNAME/augustus/config
```

## Job file

```sh title="busco.job"
#$ -S /bin/sh
#$ -N busco -cwd -j y -o busco.log
#$ -q mThM.q
#$ -pe mthread 24
#$ -l mres=240G,h_data=10G,h_vmem=10G,himem
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
module load bio/busco/6.0.0
busco -i assembly.fa.gz -m genome -l vertebrata --cpu $NSLOTS
echo = `date` job $JOB_NAME done
```
