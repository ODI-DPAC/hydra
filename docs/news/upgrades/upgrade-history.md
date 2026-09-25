# 2025 data center move

## Status


- Hydra has been successfully moved to the Ashburn Data Center (ADC):
    - Over 125 pieces of equipment have been relocated and re-cabled.
    - The NetApp was upgraded with new disks and disk enclosure; old disks were decommissioned.
    - The new GPFS (bigger and faster) is now in production.


- The cluster's OS had to be upgraded from Rocky Linux 8.9 to 8.10 due to compatibility issues with the ADC network infrastructure.
    - This should not impact any applications - as per our tests.


- The cluster is available for use with a slightly reduced capacity:
    - All storage units are up and running, although *the disk space was reorganized*.
    - The head node and both login nodes are up and running.
    - Some 69 compute nodes are up and running (abt 5300 CPus), although
        - only one of the interactive and I/O node is up and running for now,
        - the GPU nodes are up and running, but not yet available.
    - Some five nodes were down due to h/w failures and are being repaired and put in production.


- Globus services and the R Studio Server are up and running.
- Accessing Hydra remains unchanged, passwords remain valid, etc.


## Disk Space Reorganization


The storage architecture was reorganized to improve performance while maintaining backward compatibility whenever possible:


- `/home` and `/store` remain unchanged.
- `/pool` is deprecated, *you should no longer use it* (see below).
- most of `/scratch` was relocated to the new GPFS for improved performance and capacity (some directories remain on the old GPFS)
- `/data` was expanded and remains on the NetApp, with expanded capacity and (soon) increased user quotas.
- `/fast` will soon be available: a high performance storage that uses NVMe SSD disks in the new GPFS.
- 'bigtmp' will likely be phased out, once `/fast` become available.


### Details on the Disk Space Reorganization


- `/home` remains as it was
    - size: 23 TB
    - user's quota: 384 GB
    - use `/data/public/<group>/<username>` for long term storage
        - <group> stands for biology, genomics, nasm, odi or sao
        - <username> stands for your username on Hydra
    - `/home` is never scrubbed.


- `/data` remains on the NetApp
    - the size of `/data/public` has been increased to 330 TB, and is expected to grow to 450 TB
    - the user's quota will be raised to 10 TB (TBD)
    - `/data/public` is not scrubbed.


- `/scratch` is bigger and faster
    - most of `/scratch` is now on the new GPFS, (namely `/scratch02`)
    - some of it remained on the old GPFS (i.e., `/scratch01`)
    - the size of `/scratch/public` has been increased to 800TB
    - user's quota remains 15 TB, but might be raised later
    - best practice is to use `/scratch`, and not `/scratch01` or `/scratch02`


- `/pool` is deprecated (i.e., you should no longer use it)
    - please stop using `/pool`,
        - although for backward compatibility we created symlinks (aka symbolic links)
        - i.e., paths starting with /pool point to the new locations.
    - the content of `/pool/public` was moved to `/scratch/public/pool`,
        - hence users might have data under two locations now on the same storage unit
            - `/scratch/public/<group>/<username>`
            - `/pool/public/<group>/<username>` that is in reality `/scratch/public/pool/<group>/<username>`
        - you are encouraged to consolidate these two location in one, using `mv -i`
        - as a results, what you store under `/pool/public` and under `/scratch/public` now count against your quota on `/scratch/public`


- `/store` remains as it was
    - near-line storage, split over two NASes


- `/fast` is a new high performance disk space
    - it uses NVMe SSD disks in the new GPFS
        - current size 100 TB
        - uses some 70 TB of NVMe
        - aggregate bandwidth around 300 Gbps
    - will be available soon (TBD)


!!! note
    For this disk space reorganization, files and directories (over 500 million fiies) where copied over and verified, yet


    - special files, like stateless DB, might not have been copied right;
    - something else might have gone wrong;
    - the original copy has been preserved and will not be destroyed for a few months;
     - hence if something was not copied right, please contact us.



## GPU Queues and Nodes


The GPU nodes are up and running, and available as of Tuesday Oct 14 2025.


- Some things have changed, though, see below and the [documentation](../../software/gpus.md).
- What has changed:
    - you must specify `-l gpu,ngpus=1` to use and request 1 GPU (both)
        - `gpu` is an abbreviation for `use_gpu`
        - `ngpus` is equivalent to `GPUS` (notice the 's')
    - If you only use "`-l gpu`", the job will start and promptly end up in `Eqw` mode.
    - `ngpu` or `num_gpu` and `gpu_id` or `gpuid` are no longer available/needed!
    - `ngpus` (or `GPUS`) is an RSMAP, (i.e., equivalent to what `gpu_id` was)
    - `gpuarch` is now an abbreviation for `gpu_arch`
    - The following two environment variables are now set by the job scheduler
        - `SGE_HGR_GPUS`, will be set to something like "`gpu0 gpu1`"
        - `CUDA_VISIBLE_DEVICES`, will be set to something like "`0,1`"
    - Make sure your application uses the GPU(s) assigned to your job via one of these two environment variables.
- What has not changed:
    - names of the queues;
    - queue limits (memory, cpu, elapsed time);
    - sage limit (maximum of concurrent GPU per user).
- Local tools:
    - `get_gpu-info```- same as before
    - c`heck-gpu-usage```- replaces check-gpuse
    - `qacct+```- support GPU accounting


## Globus Services


Globus is available.


- It was moved to a new server and adjusted to accommodate the new storage architecture.


## R Studio Server


The R studio server is up and running.


- It was adjusted to accommodate the new storage architecture.


# 2024 upgrade to Hydra-7

This page lists the upgrades that will take place during the April 22 - May 2, 2024 upgrade.


While we are making every effort to set up the new configuration as backward compatible as possible, there will be changes, see below. 
We will adjust the Wiki once the changes are in place.


## What Is Being Upgraded


1. The OS version (& *flavor*) of the cluster (i.e., Rocky 8.9)
2. The version of the Grid Engine (i.e., v8.8.1 aka 2023.1.1)
3. The cluster management tool, i.e, Base Command Management (aka BCM v10.0)
4. The version of most tools (compilers, etc.)
5. new Hardware: fifteen new compute nodes will be added:
    1. two nodes with 2x96c or 192 cores (CPUs) and 1.5TB of memory
    2. twelve nodes with 2x64c or 128 cores (CPUs) and 1.0TB of memory
    3. One quad GPU servers, with 4x L50S NVIDIA GPUs
6. We have/will decommission our oldest compute nodes, namely
    1. the `compute-43-xx`series, and
    2. the `compute-00-xx` series.
7. This will:
    1. increase the number of CPUs from about 4900 to about 5900,
    2. increase the total memory from about 40 to 50TB,
    3. decrease the number of compute nodes from about 87 to 78.
    4. The new compute nodes have the latest generation architecture.
8. As a result of the hardware upgrades, we will adjust system configuration (queues, disk quota, modules, etc.)
9. We will use the downtime to upgrade any needed firmware and make other adjustments as needed.


## Details on Changes


Click on the links for details


1. New list of modules
    1. Some modules have moved
    2. New set of compilers versions
    3. MPI
2. Bio packages
    1. The list of packages has been pruned
    2. The list of modules has been trimmed
    3. Some generic tools have been moved
3. Queues: changes and new ones
    1. Changes in limits
    2. New GPU queues
    3. New `ompi` PE for NVIDIA MPI
    4. I/O queues changes, use `-l ioq`
4. GPUs
5. New version of the command `module`
    1. version 5.3.1 allows use of shortcut `ml`
    2. customization
6. Disk space changes
    1. Consolidation
    2. New quotas
7. Misc

## Upgrade Details

1. New list of modules
    1. Some modules have moved
    2. New set of compilers versions
    3. MPI
2. Bio packages
    1. Reduced packages from 200+ to ~100, adding 8 new ones.
    2. Moved some general use packages from `bio/` to `tools/`
3. Queues: changes and new ones
4. GPUs
5. New version of the command module
6. Disk space changes
    1. Consolidation
    2. New quotas
7. Misc
    1. not everything was rebuild (like `gdl`, `plplot`, some libraries), check the list of modules
    2. utilities not available under Rocky 8


### New list of modules


The list of available modules has changed, and is available


- as a [HTML document](https://hydra-7.si.edu/tools/misc/module-avail.html), or
- as a [text file.](https://hydra-7.si.edu/tools/misc/module-avail.txt)


Worth pointing out:


- Some modules have moved from `bio/` to`tools/`
- New modules: we have installed `mamba`, an alternative to `conda`and `miniconda`
- New set of compilers versions
    - We still support the 3 compilers: GCC, Intel,and NVIDIA.
    - The list of available versions for each compiler have changed.
    - We installed the most recent stable versions available to date.
    - The latest Intel compilers names have changed, you will get warnings when loading some modules.
    - We no longer support the (old) PGI compilers, they are superseded by the NVIDIA ones.


!!! note "Information"
    We recommend recompiling codes built on Hydra-6 under CentOS 7.x with either the Intel or the NVIDIA compilers.


    Codes built with GCC are likely to work fine, unless they use dynamic libraries that are no longer available or no longer available for that specific version.



- MPI support and module naming
    - We still support various flavors and versions of the MPI libraries with each compilers:
        - GCC: `mvapich`and `openmpi`
        - Intel & NVIDIA: vendor supplied, `mvapich`and `openmpi`
            - `mvapich`versions 2.3.6 and 2.3.7p1
            - `openmpi`versions 3.1.6, 4.1.6 and 5.0.1
        - The PE (parallel environment specified via `-pe`) is different depending on the flavor and in some cases the compiler
            - This will be properly documented when the Wiki is up to date, but
            - the new examples, in `~hpc/examples/`, show what to use for which combo
    - We reorganized the MPI module naming
        - module names include now both the MPI and the compiler version,
        - shorter names are pointers (links) to the most recent and stable version,
        - check the new module list.


### Bio packages


1. We have tested and validated on Hydra-7, under Rocky 8 some 100 "bio" packages, a list we had to prune down from the 200+ that were over the years installed on Hydra-6:
    - the list is on the Bio Packages page, here.
    - we added 8 new packages, the list is on that page, down here
2. As we reorganized things, we also moved some general use packages from `bio/` to `tools/`
    - that list is also on that page, here.
3. The list of packages that we pruned is also also on that page, here.


### Queues: changes and new ones


- We have increased the limit on the virtual memory for both the hi-CPU and hi-MEM queues:
    - hi-CPU limit remains 8GB/slot for resident memory, but has been increased to 64GB/slot for virtual memory.
    - hi-MEM limit remains 450GB/slot for resident memory, but has been increased to 900GB/slot for virtual memory.
- New queues"
    - We added 2 queues to use GPUs,
        - the GPU queues are now: `sTgpu.q, mTgpu.q,lTgpu.q`and `qgpu.iq`
        - like other queues, the batch queues `sTgpu.q, mTgpu.q,`and `lTgpu.q` correspond to short/medium/long time
        - `qgpu.iq` remains the interactive GPU queue/
    - You still need to`-l gpu` when submitting to the GPU queues
- New PE: `ompi`
    - The NVIDIA MPI libraries need to run using the `-pe ompi N` specification
- I/O queues
    - To use the I/O queues, you must now use
        - `-l use_ioq` or `-l ioq`
        - no longer `-l use_io` or `-l io`


### GPUs


- We now have 8 GPUs on 3 compute nodes, two dual GV100 (4), one quad L40S (4)
    - you can specify what type of GPU to use with
        - `-l gpu,gpu_arch=L40S`


or


- 
    - 
        - `-l gpu,gpu_arch=GV100`
- These servers run CUDA Version 12.4 (Driver Version 550.54.15) 12.2 (Driver Version: 535.154.05)
- The NVIDIA compilers come with various version of CUDA for each version of the compiler.


### New version of the command module


The command module has been upgraded to version 5.3.1. It works as before but has a few improvements:


- explicit sticky modules: two modules are preloaded and are sticky, i.e. you cannot unload them
- `ml` shortcut:
    - `module list, module load` and `module unload` can be shorten using `ml`as follows: 
| | is a shortcut to |
| --- | --- |
| `ml` | `module list` |
| `ml tools/ffsend` | `module load tools/ffsend` |
| `ml -tools/ffsend` | `module unload tools/ffsend` |
- customization
    - `module list` is by default more verbose and in color
    - this can be customized and what is shown when loading a module can be also customized
    - the following modules customize the output of the module command:
| `ml module-nocolor` | do not use colors |
| --- | --- |
| `ml module-nowarn` | disable some warning |
| `ml module-simple-format` | simplify the output of module list |
| `ml module-simple` | load the 3 module above |
| `ml module-color` | specify a color scheme (red for sticky, green for auto-loaded) |
| `ml module-verbose` | set module in verbose mode, equiv to using the -v flag |
    - You can load and unload these module to your liking.


Details about the new version of module can be found in the module man page or [here](https://modules.readthedocs.io/en/v5.3.1/).


### Disk space changes


- Consolidation:
    - the various public disks have been consolidated as single disks,
    - namely:
        - `/pool/sao`, `/pool/genomics`, etc.. are now on one single NetApp volume, called `/pool/public`
        - `/scratch/sao, /scratch/genomics`, etc... are now on one single GPGS fileset, called `/scratch/public`
        - `/data/sao, /data/genomics,` etc. are no one single NetApp volume `/data/public`
    - The new full paths are therefore `/pool/public/sao`, `/pool/public/genomics`, etc,
    - although the shorter names will still work and point to the right place/full path.


- New quotas:
    - disk space quotas have been increased as follow:
<table class="wrapped confluenceTable"><colgroup><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh" scope="col">disk space</th><th class="confluenceTh" colspan="2" scope="colgroup" style="text-align: center;">quota</th></tr><tr><th class="confluenceTh" scope="col">location</th><th class="confluenceTh" scope="col">was</th><th class="confluenceTh" scope="col">now</th></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">/pool</span></code></td><td class="confluenceTd" style="text-align: right;">5.0TB</td><td class="confluenceTd" style="text-align: right;">7.5TB</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">/scratch</span></code></td><td class="confluenceTd" style="text-align: right;">10.0TB</td><td class="confluenceTd" style="text-align: right;">15.0TB</td></tr><tr><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">/data</span></code></td><td class="confluenceTd" style="text-align: right;">2.0TB</td><td class="confluenceTd" style="text-align: right;">4.5TB</td></tr></tbody></table>


### Misc


- Not everything that was available on Hydra-6 (like `gdl, plplot`, and some libraries), was rebuild
    - check the list of modules.
- Some utilities are no longer available under Rocky 8, like
    - `finger`: check `pinky`, use `pinky -l`for an equivalent to `finger`
    - `ruptime`: we implemented a poor man version of `ruptime`, for the non compute nodes, since `qhost`returns the compute nodes load

## Bio Packages

1. We have tested and validated on Hydra-7, under Rocky 8 some 100 "bio" packages, a list we had to prune down from the 200+ that were over the years installed on Hydra-6:
    - the list is down this page, here.
    - we added 8 new packages, the list is on this page, down here
2. As we reorganized things, we also moved some general use packages from `bio/` to `tools/`
    - that list is also down this page, here.
3. The list of packages that we pruned is also down this page, here.


### General Packages Moved from bio/ to tools/


- The following packages had their modules under bio/ and have been moved to tools/:


`awscli, ffsend, julia, rclone, ruby`


### New Packages in bio/


- The following packages are now available on Hydra-7, they were not available on Hydra-6:


`admixtools, basespace, blobtoolkit, mitos, paup, quast, raxml-ng, rsem`


### Pruned Packages


- The following packages, that were available on hydra-6, *are no longer*available on Hydra-7:


`anuga, aster, atram, autoparts, bayesass, beagle_5.1, blasr, blast_taxa_backfill, blat, centrifuge, comp_popgen_sjsw, delimitr, discovista, dna-algorithm, dotnet-core, edirect, edta, eems, ervin, ete3, exabayes, fatotwobit, fsct, gadma, gatb-minia-pipeline, gblocks, genomescope, gnuparallel, goleft, gsutil, haystac, hifiadapterfilt, hmmer, hybphylomaker, hyde, hyphy, ibpp, imagemagick, insector, ivis, jags, jbrowse, kakapo, makehub, manta, mauve, mcscanx, megadetector, metamaps, metamorpheus, metapop2, mitogeneextractor, mitohifi, ml_derkarabetian, mpboot, mptp, msmc2, multiqc, ngsadmix, ngstools, opt-sne, orthomcl, paml, partitionfinder, patchwork, pbsuite, pcangsd, phast, phrapl, phylobayes, phylobayes-mpi, phyloflash, phylomad, phylonet, phyparts, phyx, pilon, prokka, proteinortho, pyrad, ragout, relernn, rjags, rsem-eval, salmon, salsa, seq-seq-pan, shapeit, sharkmer, smc++, spruceup, sspace, stampy, star, strauto, stringtie, supernova, tabix, transrate_1.0.3, trinotate, vcflib, velvet, viridal, w2rap-contigger, wgd`


- If you need one of these tools, contact us at `si-hpc@si.edu`


### Complete List of `bio/` Packages


- Here is the full list of `bio` packages available on Hydra-7 as we migrated to Rocky 8 (May 2024):


For many packages the default version has changed. In some cases. Please review your job files to ensure that the intended version is being used. | **Module** | **Version(s) on Hydra-7***"(def)" denotes default version***** | **Version(s) on Hydra-6***"(def)" denotes default version***** | **Change in default version?** | **Note** |
| --- | --- | --- | --- | --- |
| ```
abyss
``` | 2.3.7(def) | 2.2.4(def) | yes |  |
| ```
admixtools
``` | 7.0.2(def) |  |  |  |
| ```
admixture
``` | 1.3.0(def) | 1.3.0(def) |  |  |
| ```
angsd
``` | 0.941(def) | 0.921, 0.931, 0.937(def), 0.94 | yes |  |
| ```
assembly_stats
``` | 0.1.4(def) | 0_1_3(def) | yes |  |
| ```
astral
``` | 5.7.8(def), 5.15.5-MP | 5.7.8(def), mp-5.15.5 |  |  |
| ```
augustus
``` | 3.5.0(def) | 3.3.2(def) | yes |  |
| ```
basespace
``` | 1.5.4(def) |  |  |  |
| ```
bayescan
``` | 2.1(def) | 2.1(def) |  |  |
| ```
bbmap
``` | 39.06(def) | 38.67(def) | yes |  |
| ```
bcftools
``` | 1.19(def) | 1.9(def) | yes |  |
| ```
beagle
``` | 4.0.1(def) | 3.2(def), 4.0.1 | yes |  |
| ```
beast
``` | 2.6.7, 2.7.6(def) | 1.10.4, 2.6.0, 2.6.0-no-beagle, 2.6.1, 2.6.3, 2.6.6, 2.6.7(def), 2.7.5-no-beagle, 2.7.6-beagle | yes |  |
| ```
bedtools
``` | 2.31.1(def) | 2.28.0(def) | yes |  |
| ```
bioawk
``` | 1.0(def) | 1.0(def) |  |  |
| ```
bioperl
``` | 1.7.8(def) | 1.7.2(def) | yes |  |
| ```
biopython
``` | 1.83(def) | 1.74(def), 1.74_python2.7 | yes |  |
| ```
blast
``` | 2.15.0(def) | 2.6.0, 2.6.0_old_db, 2.8.1, 2.8.1-precompiled, 2.9.0, 2.9.0_v5, 2.10.1(def), 2.13.0 | yes |  |
| ```
blast2go
``` | To be installed | 1.4.4, 1.5.1(def) |  | This will be installed after the deployment of Hydra77 |
| ```
blobtoolkit
``` | 3.3.10(def) |  |  |  |
| ```
blobtools
``` | 1.1.1(def) | 1.0.1(def), 2, 2.6.3 | yes | This is for blobtools 1.x, later versions are in the module bio/blobtoolkit |
| ```
bowtie2
``` | 2.5.3(def) | 2.3.5(def), 2.5.1 | yes |  |
| ```
bpp
``` | 4.7.0(def) | 1, 4.6.1(def) | yes |  |
| ```
busco
``` | 5.7.0(def) | 3.0.2(def), 4.0.2, 5.1.3, 5.2.2, 5.3.2, 5.4.3 | yes |  |
| ```
bwa
``` | 0.7.17(def) | 0.7.17(def) |  |  |
| ```
cactus
``` | 2.8.0(def) | 2019.03.01, 2020(def), cactus_test | yes |  |
| ```
canu
``` | 2.2(def) | 1.8(def), 2.1.1 | yes |  |
| ```
cd-hit
``` | 4.8.1(def) | 4.8.1 | yes |  |
| ```
cutadapt
``` | 4.7(def) | 2.4(def) | yes |  |
| ```
dates
``` | 753(def) | 753(def) |  |  |
| ```
diamond
``` | 2.1.9(def) | 1.0(def) | yes |  |
| ```
exonerate
``` | 2.4.0(def) | 2.4.0(def) |  |  |
| ```
fastp
``` | 0.23.4(def) | 0.23.4 | yes |  |
| ```
fastqc
``` | 0.12.1(def) | 0.11.8(def) | yes |  |
| ```
faststructure
``` | 1.0(def) | 1.0(def) |  |  |
| ```
fasttree
``` | 2.1.11(def) | 2.1.11(def) |  |  |
| ```
gatk
``` | 3.8.1.0, 4.5.0.0(def) | 3.8.1.0(def), 4.1.3.0 | yes |  |
| ```
gemoma
``` | 1.9(def) | 1.0(def), 1.7.1, 1.9 | yes |  |
| ```
getorganelle
``` | 1.7.7.0(def) | 1.6.2d(def), 1.7.5 | yes |  |
| ```
guppy
``` | 6.5.7(def) | 5.0.16(def) | yes |  |
| ```
hifiasm
``` | 0.19.8(def) | 0.14.2(def), 0.16.1 | yes |  |
| ```
hisat2
``` | 2.2.1(def) | 2.2.1(def) |  |  |
| ```
htslib
``` | 1.19.1(def) | 1.9(def) | yes |  |
| ```
hybpiper
``` | 1.3.1_final, 2.1.6(def) | 1.3.1(def), 2.0.1, 2.1.6 | yes |  |
| ```
illumiprocessor
``` | 2.10(def) | 2.0.9_trimgalore, 2.10_trimgalore, 2.10_trimgalore_2023-02-17(def) | yes |  |
| ```
ipyrad
``` | 0.9.94(def) | 0.7.30(def), 0.9, 0.9.74 | yes |  |
| ```
iqtree
``` | 1.6.12, 2.3.1(def) | 1.6.12, 2.0.4, 2.0.6, 2.1.1, 2.1.2, 2.1.3(def), 2.rc.1 | yes |  |
| ```
jellyfish
``` | 2.3.1(def) | 2.3.0(def) | yes |  |
| ```
kraken
``` | 2.1.3(def) | 2.0(def), 2.1.2 | yes |  |
| ```
krakenuniq
``` | 1.0.4(def) | 1.0.1(def) | yes |  |
| ```
mafft
``` | 7.525(def) | 7.407(def) | yes |  |
| ```
maker
``` | 3.01.03(def) | 2.31.10(def) | yes |  |
| ```
mapdamage2
``` | 2.2.2(def) | 2.2.1(def) | yes |  |
| ```
masurca
``` | 4.1.1(def) | 3.2.2, 3.3.3, 3.3.3_test, 3.3.8(def), 3.3.9, 4.0.0, 4.0.9, 4.1.0 | yes |  |
| ```
merqury
``` | 1.3(def) | 1.3(def) |  |  |
| ```
migrate
``` | 3.7.2, 5.0.6(def) | 3.6.11, 3.7.2, 4.4.4 |  |  |
| ```
minimap2
``` | 2.28(def) | 2.24(def) | yes |  |
| ```
mitofinder
``` | 1.4.1(def) | 1.2(def), 1.4 | yes |  |
| ```
mitos
``` | 2.1.8(def) |  |  |  |
| ```
mitoz
``` | 3.6(def) | 3.5(def) | yes |  |
| ```
mrbayes
``` | 3.2.7a(def) | 3.2.7_beagle, 3.2.7a(def) | yes |  |
| ```
nucmer
``` | 3.2.3, 4.0.0rc1(def) | 3.23(def) | yes |  |
| ```
oma
``` | 2.6.0(def) | 2.3.1, 2.4.1, 2.4.2 |  |  |
| ```
orthofinder
``` | 2.5.5(def) | 2.0.9, 2.5.4 |  |  |
| ```
paup
``` | 4a168(def) |  |  |  |
| ```
phyluce
``` | 1.6.8, 1.7.3(def) | 1.5_tg, 1.6.7(def), 1.7.0, 1.7.1 | yes |  |
| ```
picard-tools
``` | 2.20.6, 3.1.1(def) | 2.20.6(def) | yes |  |
| ```
plink
``` | 1.90b7.2(def) | 1.90b4(def) | yes |  |
| ```
psmc
``` | 0.6.5(def) | 0.6.5(def) |  |  |
| ```
purge_dups
``` | 1.2.6(def) | 1.0(def) | yes |  |
| ```
qiime2
``` | 2024.2-amplicon(def), 2024.2-shotgun | 2019.7, 2019.1, 2020.8, 2021.11(def) | yes | qiime2 now has separate amplicon and shotgun sequencing packages |
| ```
quast
``` | 5.2.0(def) |  |  |  |
| ```
R
``` | 4.3.3(def) | 3.5.2_rgdal, 3.6.0_conda, 3.6.1(def) | yes |  |
| ```
raxml
``` | 8.2.13(def) | 8.2.12(def), 8.2.12-mpi, ng-0.9.0 | yes |  |
| ```
raxml-ng
``` | 1.2.1(def) |  |  |  |
| ```
repeatmasker
``` | 4.1.5, 4.1.6(def) | 4.0.9(def) | yes |  |
| ```
repeatmodeler
``` | 2.0.5(def) | 1.74(def) | yes |  |
| ```
revbayes
``` | 1.2.2(def) | 1.0.11(def), 1.0.13 | yes |  |
| ```
rohan
``` | 1.0.1(def) | 1.0.1(def) |  |  |
| ```
rsem
``` | 1.3.3(def) |  |  |  |
| ```
samtools
``` | 1.19.2(def) | 1.9, 1.17(def) | yes |  |
| ```
seqkit
``` | 2.8.1(def) | 0.13.2, 2.3.1(def) | yes |  |
| ```
seqtk
``` | 1.4(def) | 1.0(def) | yes |  |
| ```
spades
``` | 3.15.5(def) | 3.11.1, 3.12.0, 3.14.0(def), 3.15.5 | yes |  |
| ```
sratoolkit
``` | 3.1.0(def) | 2.9.6, 2.11.0(def) | yes |  |
| ```
stacks
``` | 2.66(def) | 1.48, 2.6.5, 2.41(def) | yes |  |
| ```
structure
``` | 2.3.4(def) | 2.3.4(def) |  |  |
| ```
transabyss
``` | 2.0.1(def) | 2.0.1(def) |  |  |
| ```
transdecoder
``` | 5.7.1(def) | 5.5.0(def) | yes |  |
| ```
transrate
``` | 1.0.3 | 1.0.3, 1.0.3.2, 1.0.3_mamba, 1.0.3_orp |  |  |
| ```
trim_galore
``` | 0.6.10(def) | 0.6.4(def) | yes |  |
| ```
trimmomatic
``` | 0.39(def) | 0.39(def) |  |  |
| ```
trinity
``` | 2.15.1(def) | 2.8.5(def), 2.9.0, 2.9.1, 2.13.2, r2013_2_25 | yes |  |
| ```
vcftools
``` | 0.1.16(def) | 0.1.16(def) |  |  |
| ```
wtdbg2
``` | 2.5(def) | 2.5(def) |  |  |


# 2021 upgrade to Hydra-6

This page lists the upgrades that took between August 30th 2021 and September 14th.


- While we are making every effort to set up the new configuration as backward compatible as possible, there will be changes, see below.
- We anticipate a rewrite of the Wiki (organization and content) soon.


### What Has Been Upgraded


1. The OS version of cluster (CentOS 7.9)
2. The Grid Engine (v8.6.18);
3. The cluster management tool, i.e, Bright Cluster Management (v9.1);
4. The NetApp controller (FAS8300); we replaced some of the oldest disks with new ones;
5. The firmware in some components of the GPFS;
6. Etc


### Access


- Access to Hydra has not changed, ssh into `hydra-login01.si.edu` or `hydra-login02.si.edu`.
- Your credentials (username and password) have not changed.
- The web pages under `https://hydra-5.si.edu` have been moved to `https://hydra-6.si.edu.`
    - In most cases you should be redirected, but if you are not, please update your bookmarks accordingly.


## List of Changes


#### Main Software Upgrade


**What**: upgrade of the operating system, the cluster management tool and the grid engine versions


**Impact**: access to a more recent software release and updated versions of the associated tools.


**Details**: upgraded O/S to CentOS 7.9 (release upgrade), UGE to v8.6.18 (newer release), BCM to v9.1 (new version).


**NOTE**: users will see a warning when logging on either login node that the host key has changed.


**This is normal.**You can either edit the known hosts file, delete it or hit OK when prompted to update it.


On most systems the known host file is `~/.ssh/known_hosts` .


**Also**, some mail readers (like GMail) have marked email coming from `hydra-6` as spam.


Check your spam folder and set your mail reader to accept all emails from `hydra-6.si.edu` and from `hydra-6a.si.edu`.


#### Installed a New NetApp Controller with Some New Disks


**What**: replaced the aging NetApp controller by a new one, and added some disks.


**Impact**: faster access to files under `/home`, `/data` and `/pool`. We also increased the capacity of `/home`,


and of the public space under `/data` and `/pool`. We have (or will) also increase(d) some of the quotas.


**Details**: upgraded the FAS8040 with a FAS8300 with some new disk shelves, while migrating most of the older


disk shelves from the old controller to the new one, increasing the NetApp capacity to 600TB.


Also, the filesystems `/data/biology` and `/data/nasm` and now on separate volumes, while we added


`/data/data_science` , `/pool/data_science` , `/data/fellows` and `/pool/fellows` to match


`/scratch/data_science` and `/scratch/fellows` .


**NOTE**: We are now backing up the content of `/home` to Amazon's Glacier storage.


This is a low cost backup option aimed at disaster recovery (i.e., recover the content of `/home` if the storage system that 
 holds the content of `/home` fails in our data center). In other words, what is stored currently under `/home` is quite safe, because 
 /home is on a highly reliable disk system (NetApp) and a copy of it exists on Amazon Glacier.


Snapshots are still enabled for the `/home` file system, hence files under `/home` deleted within 4 weeks can, in most cases, be restored 
 by the users. Beyond that period, we plan to keep backups of `/home` for up to a year, but restoring files from these backups are costly, 
 both in terms of support manpower and actual billing by Amazon. Users who would need to recover data from this backup would need proper 
 justification and may need to contribute to the actual recovery costs. Feel free to contact us if need be.


We plan next to investigate the feasibility of backing up `/data` to Glacier as well.


#### Queue Changes


**What**: removed the uTSSD.tq and uTGPU.tq queues.


**Impact**: access to local SSD storage is now integrated with the high-CPU and high-memory queues.


GPU servers and associated software have yet to be re-installed on Hydra-6.


**Details**: request for SSD storage is similar, but you only need to specify `-l ssdres=XXX`, and no longer "`-q uTSSD.tq -l ssd"`.


As for access to GPUs, we will soon migrate the GPU servers to Hydra-6 and install the required software. We also plan to use the Grid Engine 
native GPU support, stay tuned and/or contact us.


#### Modules Changes


**What**: the module `tools/local` has been split into `tools/local-users` and `tool/local-admin`,


and the module `tools/local-users` is always loaded, like the `uge` module.


**Impact**: users have access to some Hydra-specific tool without having to load an extra module.


**Details**: we decided to split what was available with `module load tools/local` into `tools/local-users` and 
 `tool/local-admin` and load the `tools/local-users` module for all users. You can still load `tools/local` that will 
 load `tools/local-user` and `tools/local-admin,` and `tools/local+` remains unchanged.


#### Changes Affecting Bioinformatics Modules


**What**: you can now load any module previously know as `bioinformatics/XXX` using the `bio/XXX` shortcut.


**Impact**: bio is now a shortcut to bioinformatics.


**Details**: a symbolic link `bio`, pointing to `bioinformatics,`has been created as a shortcut. We plan to migrate all the 
 bio-informatics tools to `bio/` in the future, hence we recommend that you start using `bio/` in lieu of `bioinformatics/`


#### Changes Affecting IDL


**What**: IDL versions prior to version 8.6 are no longer available. 
 
 **Impact**: IDL users must use version 8.6 or higher, 8.8 is the most recent version (default and recommended version). 
 
 **Details**: IDL changed the license manager as of 8.6 and we decided not to migrate the old, unsupported and obsolete licence manager,


hence only version 8.6 or higher are available. The default IDL version is 8.8 (8.8.0), version 8.8.1 will be installed soon and will become the default value.


Note that most likely version 8.9 will come with a new license manager.


#### Changes Affecting R


**What**: R versions prior to version 3.5.2 are no longer available.


**Impact**: R user will need to switch to the supported version or use conda to install a different version.


**Details:** We removed old versions to streamline availability of R, under bio/R or tools/R, the default version is 3.6.1.


#### Changes Affecting MPI Users of OpenMPI


**What**: a workaround is needed for users whose login shell is `/bin/csh` and use OpenMPI using `-pe orte` for parallel jobs


**Impact**: users whose login shell is `/bin/csh` need to add a line to their `~/.cshrc`


**Details**: A "*feature"* of UGE version 8.6.18 is causing a mysterious `Unmatch ".`error message for users whole login shell is `/bin/csh`


when submitting jobs with `-pe orte` (OpenMPI jobs). There is a simple fix to avoid this problem, simply add the line


`if ($?JOB_ID) set backslash_quote`


to your `~/.cshrc` file. Explanations can be found under the `execd_params` section of `man sge_conf,` see E`NABLE_BACKSLASH_ESCAPE`,


and the Lexical structure section of `man csh`.


#### Changes Affecting the qacct+ Local Tool


**What**: `qacct+` now use the GE's native DB ARCo and has been modified accordingly.


**Impact**: Almost no delay between `qacct` and `qacct+,` and the arguments to `qacct+` have changed.


**Details**: `qacct+` is now using the ARCo DB, a GE native product that is updated nearly in real time by the GE.


`qacct+` has been modified to query ARCo, hence some types of queries are no longer available, and the arguments to `qacct+` have been modified accordingly.


In the process most of the argument syntax has been changed, see `man qacct+` or `qacct+ -help` .


#### Changes Affecting the Compilers


**What**: we are no longer supporting old versions of some of the compilers and plan to install the most recent versions of these compilers soon.


**Impact**: Users need to use the more recent versions of the GCC, PGI/NVIDIA, Intel compilers


**Details**: Rather than delaying the reopening, we have not yet, but will soon install the most recent versions of the NVIDIA and Intel compilers and


will consider installing the most recent GCC compilers. We no longer support some of the old version of the PGI and Intel compilers, and have


removed some of the associated modules . Once we have installed and validated the most recent versions of the compilers we will consolidate


which versions of each compiler will be supported, notify the users and update the documentation.


#### **Changes Affecting Blast2GO**


**What**: Blast2GO has been upgraded from 1.4.4 to 1.5.1. The reference GO database has been upgraded from 2019_10 to the latest, 2021_06.


**Impact**: Newer database will give you the most up to date annotations. You will need to re-run `hydracliprop` after loading the module to generate an up to date cli.prop file. In Blast2GO, the argument `-saveb2g <path>` has been changed to `-savebox <path>` (OmicsBox format).


**Details:** The new module is `bio/blast2go/1.5.1` . The previous version’s module `bio/blast2go/1.4.4` and its database are currently still available, but will be removed soon.


#### Coming Up


**What**: more compute servers and more GPFS disk space and rewritten documentation


**Impact**: more CPUs, more disk space under /`scratch` and better documentation


**Details**: We have ordered eight new 64-core servers and an extra ~500TB of GPFS disk space.


Because of a shortage of computer parts and the current supply chain disruption, these will likely be delivered by the end of 2021.


We will rewrite the documentation hosted on the HPC wiki; it will be reorganized and updated to reflect the most recent upgrade.

## Nov 2021 Updates: Compilers, Tools and More

### Introduction


- New versions of the compilers (Intel, NVIDIA and GCC) and tools (Java, Python, IDL, MATLAB, Julia, CUDA), have been installed and tested on Hydra
- New modules are available to access these new compilers and tools
- The list of available modules has been updated and reorganized, it is now linked from the cluster status pages:
    - [Hydra-6](https://hydra-6.si.edu) → [Tools](https://hydra-6.si.edu/tools/) → [List of Available Modules](https://galaxy.si.edu/tools/QSubGen/module-avail.html)
    - [Status page (\@si.edu)](https://hydra-6.si.edu/tools/status/) → [List of Available Modules](https://hydra-6.si.edu/tools/status/module-avail.html)
    - Status page (cfa.harvard.edu, retired) → [List of Available Modules](https://hydra.si.edu/tools/QSubGen/module-avail.html)
    - That list is updated nightly. You can get that list with the command `module avail`
- Access to GPUs has been simplified
- Singularity is now available on a set of compute nodes
- Password Requirement Change
    - We adjusted the password requirement on Hydra to conform to SI's policy (only one digit).
- We have updated the modules description (`whatis`) for some modules to be more informative and consistent, and
    - for 7 modules we will change the default versions when loading that module without version specification - on Monday November 29, 2021


### Compilers


#### Intel


- Intel 2021.3 and 2021.4 have been installed, and 2021 → 2021.4
    - As of 2021.x, Intel is matching NVIDIA and releasing their compiler and more for free under the OneAPI name
    - Intel's modules are a bit of a mess, I've cleaned them up but they are very chatty
    - As before Intel also offers their version of Python
- Previous versions are still available (2015.x to 2021.x, check the list of available modules on the pages listed above or with with `module avail intel)`


#### PGI/NVIDIA


NVIDIA has acquired PGI and has repackaged these compilers as of 2020.


These compilers are now free and include CUDA support. This transition hasn't been the smoothest.


- The PGI compilers up to version 20.4 are still available (`module avail pgi`)
- As of 20.7 the compilers are NVIDIA (20.7 and 20.9), although they are available as pgi too
- NVIDIA versions 21.1, 21.2, 21.3, 21.5, 21.7 and 21.9 are now available (`module avail nvidia`)
- CUDA up to version 11.4 is available (CUDA 11.4 comes with NVIDIA 21.9)


#### GCC


- Versions 10.1. 10.2.0 and 11.2.0 are now available
- Previous versions are still available (`module avail gcc`)
- Version 8.2.0 is not longer available on Hydra-6, it has been substituted by 10.2.0 by BCM


#### MPI: Vendor, OpenMPI and MVAPICH


- Intel's MPI distributions are not working on Hydra - we've logged this with Intel's support.
- NVIDIA MPI distribution (OpenMPI 3.x) is working on Hydra (not their OpenMPI 4.x versions)
- Built from source versions of OpenMPI (4.x) and MVAPICH (2.3.x) are available for all 3 compilers/
- The following combinations are working and supported, other versions are available, look at the list of available modules for additional details:


`mvapich/intel/2019.5 - BFS | openmpi/intel/* - VFV DNW | openmpi4/intel/2019.4 - BFS` 
`/2020.4 - BFS | - VFV DNW | /2020.4 - BFS` 
`/2021.4 - BFS | - VFV DNW | /2021.4 - BFS` 
`mvapich/pgi/19.9 - BFS | openmpi/pgi/19.9 - VFV | openmpi4/pgi/19.9 - BFS` 
`/20.4 - BFS | /20.4 - VFV | /20.4 - BFS RDW` 
`mvapich/nvidia/20.9 - BFS | openmpi/nvidia/20.9 - VFV | openmpi4/nvidia/20.9 - BFS RDW` 
`/21.9 - BFS | /21.9 - VFV | /21.9 - BFS` 
`mvapich/gcc/4.8.5 - BFS | openmpi/gcc/4.8.5 - BFS | openmpi4/gcc/* - use openmpi/gcc instead` 
`/4.9.1 - BFS | /4.9.1 - BFS |` 
`/4.9.2 - BFS | /4.9.2 - BFS |` 
`/5.3.0 - BFS | /5.3.0 - BFS |` 
`/6.1.0 - BFS | /6.1.0 - BFS |` 
`/7.3.0 - BFS | /7.3.0 - BFS |` 
`/9.2.0 - BFS | /9.2.0 - BFS |` 
`/10.1.0 - BFS | /10.1.0 - BFS |` 
`/10.2.0 - BFS | /10.2.0 - BFS |` 
`/11.2.0 - BFS | /11.2.0 - BFS |`


**Notes**:


- BFS: built from source; VFV: version from vendor; DNW: do not work; RDW: runs despite warnings
    - mvapich uses -pe mpich
    - openmpi uses -pe orte,
        - except for pgi & nvdia VFV (openmpi) that needs -pe mpich
- Examples are on hydra under `/home/hpc/examples/mpi`


### Tools


#### Java


- Java 17.0.1 is available, as well as version 1.8.0_45


#### Python


- Versions 3.8, 3.9. 3.10 are available:
    - 3.8 is the most recent Anaconda version (2021.05),
    - 3.9 and 3.10 were built from source.
- Intel's version 3.7.11 is also available, distributed by Intel's OneAPI 2021.4


#### IDL


- version 8.8.1 is available
- IDL licensing mechanism is currently a simpler one, hence `idl` issues the following message:


`Licensed for use by: Harvard-Smithsonian Astrophysical Observatory (Main)` 
`License: 100554-5516875-BUF` 
`License expires 30-Nov-2022.`


#### MATLAB


- Matlab runtime version 2021a and 2021b are available


#### Julia


- Version 1.6.2 and 1.6.3 are available


#### CUDA


- CUDA is now included with the NVIDIA compilers,
- Version 11.4 comes with the 21.9 version of the compilers


### GPU


- Access to the nodes with GPUs has been simplified, just specify `-l gpu` to `qsub` or `qrsh`
- More details on this in the [GPU section](../../software/gpus.md) of the Reference pages


### Containers: singularity


- Singularity has been installed on a handful of node, you can access it by specifying the `@container-hosts` host group
- More details on this in the [Containers section](../../software/containers.md) of the Reference pages


### Password Requirement Change


- We adjusted the password requirement on Hydra to conform to SI's policy (only one digit).
- Passwords must conform to SI password policies and meet the following requirements:
    - at least 12 characters in length, and include at least:
        1. *one digit*,
        2. one upper case,
        3. one lower case, and
        4. one special character;
    - moreover, new passwords cannot be too similar to old passwords.


### Modules Description and Default Version


- We have updated the modules description (`module whatis` ) for some modules to be more informative and consistent, and
- We will change the default version when loading a module without version specification (7 cases).
    - These 7 changes are:


```
      idl/8.8 -> 8.8.0  -> 8.8.1
    matlab/rt -> R2020a -> R2021b
 intel/python -> 36     -> 37
        intel -> 2020   -> 2021
  tools/julia -> 1.0.5  -> 1.6.3
 tools/python -> 3.7    -> 3.8
          pgi -> 19.9   -> 20.4
```


and will occur on Monday November 29, 2021**.**


# 2019 upgrade to Hydra-5

## The Hydra cluster has been upgraded as follows:


- Software
    - Upgrade OS to CentOS 7.6,
    - Change our management tool (from Rocks 6.x to Bright Cluster, aka BCM 8.2),
    - Switch from SGE to UGE (Univa) version 8.6.6, a commercially supported version of SGE (backward compatible).


- Hardware
    - Added 16 new nodes (40c/380GB) for a total of 640 cores,
    - Decommissioned oldest nodes (old compute-6* and compute-4-*),
    - Add ed1.5PB of high performance storage (parallel file system GPFS, aka Spectrum Scale),
    - This is in addition to the 500TB of NetApp and the 950TB of near-line storage (NAS),
    - The `/scratch` disk has been moved to the GPFS and increase in size from 100TB to 900TB (450TB+450TB for `/scratch/genomics` and `/scratch/sao`)
    - Moved all the nodes to a 10Gb/s Ethernet connection (was 1Gb/s).


!!! note "Please Note"
    - While we made every effort to set up the new configuration as backward compatible as possible, there are changes.
    - Read the migration notes!
    - The upgrade will take place from August 26th through September 2nd, 2019.
    - During this time, Hydra will be inaccessible to users and as of 9am on Monday August 26th any remaining running jobs will be killed.
    - We hope to have Hydra back up before September 2nd, but that decision won’t be made until the upgrade work is completed.
    - During the down time, access to files stored on Hydra will be limited, and at times unavailable. Note that none of your files will be deleted.


    Plan your use of Hydra accordingly.



Please read this page carefully, and after the upgrade, do not hesitate to contact us (at [SI-HPC-Admin\@si.edu](mailto:SI-HPC-Admin@si.edu)) if something is not working as it should any longer.


- For biology and genomics software issues and/or incompatibilities that arise, please contact [SI-HPC\@si.edu](mailto:SI-HPC@si.edu),
- SAO users please contact Sylvain at [hpc\@cfa.harvard.edu](mailto:hpc@cfa.harvard.edu).


## List of Software Changes


- Implementation of user account management using LDAP
    - The procedure to change your password has changed:
        - You can use `passwd` on either the login node and that's it, or
        - Use the [Self Service Password (SSP) page](https://hydra-adm01.si.edu/ssp), listed at [https://hydra-5.si.edu](https://hydra-5.si.edu/)
    - Email [SI-HPC-Admin\@si.edu](mailto:SI-HPC-Admin@si.edu) ***only if this fails***.


- Switching from Rocks to BCM
    - BCM locates things differently from Rocks;
        - for example `/opt` is no longer used, instead BCM uses `/cm`
    - If you use modules, everything should work the same;
        - but if you hardwired locations, things may no longer work the same;
    - The compute nodes will be renamed as follows:
        - `compute-NN-MM,`
        - *i.e.* the "`N`", or logical rack number, and
        - M the node *index* are both two-digit numbers;
    - You should use modules as much as possible.


- Job Scheduler
    - We switched to UGE, or Univa Grid Engine; that
        - is backward compatible with SGE;
        - offers some additional features;
        - although the output of some commands will look different, and
        - some have different options .


- The list of queues and their limits will not changed,
    - a few *complex values* will change (to use local SSD and GPU usage)
    - One important change is that


```{.text title="the memory reservation value will no longer be specified per slots, but per jobs:"}
the specification "-pe mthread 10 -l mres=20G,h_data=20G,h_vmem=20G,himem"
must be changed to "-pe mthread 10 -l mres=200G,h_data=20G,h_vmem=20G,himem"
to reserve 200GB of memory for this job, asking the scheduler to start on a node that has 20G per thread of free memory
```


- Compilers
    - The default compiler versions has changes, and
    - they had to be reloaded.
    - For MPI jobs the compiler/flavor/version combos has also changed.


- Local tools
    - The tools accessible with the `tools/local` module have been split into two groups and
    - some of the names have been changed or simplified
    - Use `module help tools/local` and `module help tools/local+` to see what the split is and what the names are.
    - Use `module help tools/local-bc` to see the correspondence
    - Loading `tools/local-bc` will
        - load `tools/loca`l and `tools/local`+ and
        - create aliases to be backward compatible (-bc)
    - use the new names whenever possible
