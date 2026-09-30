# MaSuRCA

[MaSuRCA](https://github.com/alekseyzimin/masurca) assembles genomes by building super-reads from Illumina data and assembling those, with or without long reads (PacBio, Nanopore) for a hybrid assembly. The module is `bio/masurca`. The MaSuRCA manual covers the parameters; what follows is how to run it on Hydra.

MaSuRCA runs in two jobs. A short one turns the configuration file into an `assemble.sh` script, and a long one runs the script.

1. Put the reads under `/scratch` (see [Data transfer](../../data-transfer/index.md)), as FASTQ for Illumina and FASTA or FASTQ for long reads.

2. Generate a configuration file and edit it:

    ```console
    $ module load bio/masurca
    $ masurca -g masurca.config
    ```

    In the `DATA` section, give each library a unique two-letter prefix, the fragment mean and standard deviation, and the full paths of the read files. In `PARAMETERS`, keep `USE_GRID=0` (MaSuRCA's grid mode is not set up on Hydra) and set `NUM_THREADS` to the slot count you will request for the second job. The comments in the file explain the rest.

    ```text
    DATA
    PE= pe 500 50 /scratch/genomics/USERNAME/reads/frag_1.fastq /scratch/genomics/USERNAME/reads/frag_2.fastq
    JUMP= sh 3600 200 /scratch/genomics/USERNAME/reads/short_1.fastq /scratch/genomics/USERNAME/reads/short_2.fastq
    #NANOPORE=/scratch/genomics/USERNAME/reads/nanopore.fa
    END
    ```

3. Run the first job, which writes `assemble.sh` in seconds:

    ```sh title="masurca-config.job"
    #$ -S /bin/sh
    #$ -N masurca-config -cwd -j y -o masurca-config.log
    #$ -q sThC.q
    #$ -l mres=2G,h_data=2G,h_vmem=2G
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    module load bio/masurca
    masurca masurca.config
    echo = `date` job $JOB_NAME done
    ```

4. Run the assembly. Memory depends on the genome size. The high-memory queues allow up to 512 GB per job, and `uTxlM.rq` more, by request to [SI-HPC@si.edu](mailto:SI-HPC@si.edu). This job runs for hours to days.

    ```sh title="masurca-assemble.job"
    #$ -S /bin/sh
    #$ -N masurca-assemble -cwd -j y -o masurca-assemble.log
    #$ -q lThM.q
    #$ -pe mthread 16
    #$ -l mres=480G,h_data=30G,h_vmem=30G,himem
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    echo + NSLOTS = $NSLOTS
    module load bio/masurca
    ./assemble.sh
    echo = `date` job $JOB_NAME done
    ```
