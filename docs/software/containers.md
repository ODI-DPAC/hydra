# Containers

The login, interactive and compute nodes have Singularity CE 4.4, with no module to load. You pull a container image on a login node and run it in a job.

1. Pull or copy the image on a login node, into a directory under `/scratch` or `/data`. Pulling downloads and converts the image, which takes minutes and up to several gigabytes:

    ```console
    $ cd /scratch/genomics/USERNAME/images
    $ singularity pull docker://quay.io/biocontainers/samtools:1.19.2--h50ea8bc_0
    ```

2. Run it in a job. The container sees your home directory and the current directory; bind other directories with `--bind`:

    ```sh title="samtools.job"
    #$ -S /bin/sh
    #$ -N samtools -cwd -j y -o samtools.log
    #
    echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
    singularity exec --bind /scratch /scratch/genomics/USERNAME/images/samtools_1.19.2--h50ea8bc_0.sif samtools view -c reads.bam
    echo = `date` job $JOB_NAME done
    ```

A container that uses a GPU needs `--nv` on the `singularity` command and a [GPU request](gpus.md) on the job. `~hpc/examples/containers` has working examples (`lolcow.job`, `test1.job`, `test2.job`) with their logs. The Singularity CE user guide at <https://docs.sylabs.io/guides/latest/user-guide/> covers the command itself.
