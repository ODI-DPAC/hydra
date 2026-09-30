# SMC++

[SMC++](https://github.com/popgenmethods/smcpp) infers population size history from whole-genome sequences. The module `bio/smc++` provides release 1.15.2. The developers publish later releases only as a [Docker image](https://hub.docker.com/r/terhorst/smcpp), which runs on Hydra under Singularity (see [Containers](../containers.md)).

## Run the current version from the container

1. Build the `.sif` file from the Docker image, once, on a login node:

    ```console
    $ singularity pull smcpp.sif docker://terhorst/smcpp:latest
    $ ls -l smcpp.sif
    -rwxrwxr-x 1 USERNAME USERNAME 257298432 Sep 20 13:09 smcpp.sif
    ```

2. Check it runs:

    ```console
    $ singularity run -C smcpp.sif vcf2smc
    usage: smc++ vcf2smc [-h] [-v] [--cores CORES] [-d sample_id sample_id]
    ...
    smc++ vcf2smc: error: the following arguments are required: vcf.gz, out[.gz], contig, pop1
    ```

3. Run a command with the current directory bound to `/mnt` in the container. Only directories you bind are visible inside it:

    ```sh
    singularity run -C --bind $PWD:/mnt smcpp.sif vcf2smc /mnt/vcf.gz /mnt/chr1.smc.gz chr1 CEU:NA12878,NA12879
    ```

    This is the container form of `smc++ vcf2smc vcf.gz chr1.smc.gz chr1 CEU:NA12878,NA12879` with `vcf.gz` in the current directory.

Put step 3 in a job file for anything longer than a test. A `singularity run` line needs no module.
