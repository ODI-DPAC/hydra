# SPAdes

The [SPAdes](https://github.com/ablab/spades) assembler is used for microbial and organelle genomes and for target-enrichment data such as UCE and exon capture. The module is `bio/spades`.

## Memory

Give `spades.py` the memory the job reserved, in GB, with `-m`: a job with `-l mres=96G` runs `spades.py -m 96`. Without `-m`, SPAdes assumes 250 GB and is killed when it exceeds the job's limit.

## Temporary files

`spades.py` creates many temporary files, over a million with the `--careful` option, whose mismatch-correction stage writes a separate file for each contig. On `/scratch` this is slow and counts against your file quota. Put them on the node's local SSD instead: request the space with `-l ssd_res=SIZE`, load `tools/ssd`, and pass `--tmp-dir $SSD_DIR` (see [Use a node's local SSD](../../storage/ssd.md)). `-v SSD_SAVE_MAX=0` tells the scheduler not to save anything left on the SSD when the job ends; the temporary files are not needed.

```sh title="spades.job"
#$ -S /bin/sh
#$ -N spades -cwd -j y -o spades.log
#$ -q lThM.q
#$ -pe mthread 8
#$ -l mres=96G,h_data=12G,h_vmem=12G,himem
#$ -l ssd_res=200G -v SSD_SAVE_MAX=0
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
module load bio/spades
module load tools/ssd
spades.py \
  -o sample \
  --pe1-1 sample_R1_PE_trimmed.fastq.gz \
  --pe1-2 sample_R2_PE_trimmed.fastq.gz \
  --tmp-dir $SSD_DIR \
  -m 96 \
  -t $NSLOTS
echo = `date` job $JOB_NAME done
```

## SPAdes under Phyluce

[Phyluce](https://github.com/faircloth-lab/phyluce)'s `phyluce_assembly_assemblo_spades` calls `spades.py` itself and has no option for `--tmp-dir`. Give it a wrapper that adds the option when the job has an SSD:

```sh title="spades-tmp.sh"
#!/bin/sh
if [ -n "$SSD_DIR" ]; then
    SPADES_TMP="--tmp-dir $SSD_DIR"
else
    SPADES_TMP=""
fi
spades.py $SPADES_TMP "$@"
```

Make it executable and name it in `~/.phyluce.conf`:

```ini title="~/.phyluce.conf"
[binaries]
spades:/scratch/genomics/USERNAME/bin/spades-tmp.sh
```
