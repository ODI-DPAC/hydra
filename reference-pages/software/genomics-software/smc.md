---
title: "SMC++"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/294454552/SMC"
date-modified: "2024-11-08"
author: "Last updated:  MK"
categories: ["hydra7"]
---

- An old version of [SMC++](https://github.com/popgenmethods/smcpp) ([https://github.com/popgenmethods/smcpp](https://github.com/popgenmethods/smcpp)) is installed as a module (bio/smc++/1.15.2) which was installed via conda.
- In recent versions of the software, the developers have dropped support for installing via conda.
- Newer versions of SMC++ can be used with the [Docker image](https://hub.docker.com/r/terhorst/smcpp) the developers make available.
- On Hydra, [Singularity is used as the container system](../../how-to-use-containers.md) to run docker images.
- Below are instructions for downloading the docker image for use with singularity.


## Instructions for using the SMC++ container


1. Create a singlurity `.sif` container from the docker image. This only needs to be done one time.
```
$ singularity pull smcpp.sif docker://terhorst/smcpp:latest
INFO: Using cached SIF image
$ ls -l smcpp.sif
-rwxrwxr-x 1 user user 257298432 Sep 20 13:09 smcpp.sif
```
2. Test the container with `singularity run` 

```
$ singularity run -C smcpp.sif vcf2smc
usage: smc++ vcf2smc [-h] [-v] [--cores CORES] [-d sample_id sample_id]
 [--length LENGTH] [--ignore-missing] [--missing-cutoff c]
 [--mask MASK] [--drop-first-last]
 vcf.gz out[.gz] contig pop1 [pop2]
smc++ vcf2smc: error: the following arguments are required: vcf.gz, out[.gz], contig, pop1
```
3. To run a command like `smc++ vcf2smc vcf.gz chr1.smc.gz chr1 CEU:NA12878,NA12879` use this singularity command if the input file, `vcf.gz` is in the current directory:
```
singularity run -C --bind $PWD:/mnt smcpp.sif vcf2smc /mnt/vcf.gz /mnt/chr1.smc.gz chr1 CEU:NA12878,NA12879
```
    1. --`bin $PWD/mnt` argument mounts the directory you're running the singularity command from to `/mnt` in the container. Only the directories you bind are available in the container.
