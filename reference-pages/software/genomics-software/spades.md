---
title: "SPAdes"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/249331797/SPAdes"
date-modified: "2026-03-16"
author: "MPK"
---

The [SPAdes assembler](https://github.com/ablab/spades) is often used for microbial and organelle genome assembly as well as target enrichment methods such as UCE or exon capture.


## Specifying memory


the `-m <int>` option for `spades.py` should be used to specify the amount of memory (in GB) you have reserved in your `qsub` submission (`mres`). The default value of `-m` if you do not specify a value is 250. By specifying a value for `-m` that matches what you reserved, SPAdes will adjust buffer size usage to reduce RAM usage.


## SPAdes temporary files and `--careful` option


`spades.py` can create many temporary files, more that one million in some cases. This is seen when using the `--careful` option in the assembly. During the mismatch correction phase that this option adds, a separate file is created for each contig, which can number more than 105. Additional intermediate files for each contig can then increase the total number of temporary files to more than a million. By default, these temporary files are placed in a `tmp` directory in the output directory you specify with `-o`. The large number of files can cause you to exceed your inode quota or adversely affect the operation of the GPFS ( `/scratch` et al.) and NetApp ( `/data` et al.).


To avoid this, it is recommended to use the [local SSD space](../../disks-space-and-usage/how-to-use-local-ssd-space.md) for the SPAdes temporary files.


This examples requests 200GB of local SSD from the scheduler (`-l ssd_res=200G`) and then uses this for the `spades.py` tmp directory by adding `--tmp-dir $SSD_DIR`


The addition of `-v SSD_SAVE_MAX=0` directs the job scheduler to not save any of the files from the SSD storage space. The temporary files `spades.py` creates do not need to be retained.


```{.text title="Example spades.py script using local SSD"}
# /bin/sh
# ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -pe mthread 8
#$ -q lThM.q
#$ -l mres=96G,h_data=12G,h_vmem=12G,himem
#$ -l ssd_res=200G -v SSD_SAVE_MAX=0
#$ -cwd
#$ -j y
#$ -N spades
#$ -o spades.log
#
# ----------------Modules------------------------- #
 module load bio/spades
 module load tools/ssd
# ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS

spades.py  \
  -o sample \
  --pe1-1 sample_R1_PE_trimmed.fastq.gz \
  --pe1-2 sample_R2_PE_trimmed.fastq.gz \
  --tmp-dir $SSD_DIR \
  -m 96 \
  -t $NSLOTS

#
echo = `date` job $JOB_NAME done
```


## Special case: specifying --tmp-dir if using Phyluce


If you use the [Phyluce](https://github.com/faircloth-lab/phyluce)script [phyluce_assembly_assemblo_spades](https://github.com/faircloth-lab/phyluce/blob/main/bin/assembly/phyluce_assembly_assemblo_spades) to assemble using SPAdes, there is not a direct way to specify the temporary directory spades.py uses. 
One option is to create a spades.py wrapper script, like the spades-tmp.sh example below and then have phyluce_assembly_assemblo_spades call that.


```
!/bin/sh

if [ -n "$SSD_DIR" ]; then
    SPADES_TMP="--tmp-dir $SSD_DIR"
else
    SPADES_TMP=""
fi

spades.py $SPADES_TMP "$@"
```


Then, to have [phyluce_assembly_assemblo_spades](https://github.com/faircloth-lab/phyluce/blob/main/bin/assembly/phyluce_assembly_assemblo_spades) use that wrapper, create a `~/.phyluce.conf` file with:


```{.text title="Wrapper for spades.py for use with phyluce"}
[binaries]
spades:/path/to/spades-tmp.sh
```
