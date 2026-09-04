---
title: "2024 Upgrade Details"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/261128426/2024+Upgrade+Details"
date-modified: "2024-05-03"
author: "SGK"
---

1. [New list of modules](2024-upgrade-details.md)
    1. Some modules have moved
    2. New set of compilers versions
    3. MPI
2. [Bio packages](2024-upgrade-details.md)
    1. Reduced packages from 200+ to ~100, adding 8 new ones.
    2. Moved some general use packages from `bio/` to `tools/`
3. [Queues](2024-upgrade-details.md): changes and new ones
4. [GPUs](2024-upgrade-details.md)
5. [New version of the command module](2024-upgrade-details.md)
6. [Disk space changes](2024-upgrade-details.md)
    1. Consolidation
    2. New quotas
7. [Misc](2024-upgrade-details.md)
    1. not everything was rebuild (like `gdl`, `plplot`, some libraries), check the list of modules
    2. utilities not available under Rocky 8


## New list of modules


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


::: {.information title="Information"}
We recommend recompiling codes built on Hydra-6 under CentOS 7.x with either the Intel or the NVIDIA compilers.


Codes built with GCC are likely to work fine, unless they use dynamic libraries that are no longer available or no longer available for that specific version.
:::


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


## Bio packages


1. We have tested and validated on Hydra-7, under Rocky 8 some 100 "bio" packages, a list we had to prune down from the 200+ that were over the years installed on Hydra-6:
    - the list is on the [Bio Packages](2024-upgrade-details/bio-packages.md) page, [here](https://confluence.si.edu/display/HPC/Bio+Packages#BioPackages-all-packages).
    - we added 8 new packages, the list is on that page, down [here](https://confluence.si.edu/display/HPC/Bio+Packages#BioPackages-new-packages)
2. As we reorganized things, we also moved some general use packages from `bio/` to `tools/`
    - that list is also on that page, [here](https://confluence.si.edu/display/HPC/Bio+Packages#BioPackages-bio-to-tool).
3. The list of packages that we pruned is also also on that page, [here](https://confluence.si.edu/display/HPC/Bio+Packages#BioPackages-pruned-packages).


## Queues: changes and new ones


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
    - ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) To use the I/O queues, you must now use
        - `-l use_ioq` or `-l ioq`
        - no longer `-l use_io` or `-l io`


## GPUs


- We now have 8 GPUs on 3 compute nodes, two dual GV100 (4), one quad L40S (4)
    - you can specify what type of GPU to use with
        - `-l gpu,gpu_arch=L40S`


or


- 
    - 
        - `-l gpu,gpu_arch=GV100`
- These servers run CUDA Version 12.4 (Driver Version 550.54.15) 12.2 (Driver Version: 535.154.05)
- The NVIDIA compilers come with various version of CUDA for each version of the compiler.


## New version of the command module


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


## Disk space changes


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


## Misc


- Not everything that was available on Hydra-6 (like `gdl, plplot`, and some libraries), was rebuild
    - check the list of modules.
- Some utilities are no longer available under Rocky 8, like
    - `finger`: check `pinky`, use `pinky -l`for an equivalent to `finger`
    - `ruptime`: we implemented a poor man version of `ruptime`, for the non compute nodes, since `qhost`returns the compute nodes load
