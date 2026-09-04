---
title: "Nov 2021 Updates: Compilers, Tools and More"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152358/Nov+2021+Updates+Compilers+Tools+and+More"
date-modified: "2021-11-19"
author: "SGK"
---

# Introduction


- New versions of the compilers (Intel, NVIDIA and GCC) and tools (Java, Python, IDL, MATLAB, Julia, CUDA), have been installed and tested on Hydra
- New modules are available to access these new compilers and tools
- The list of available modules has been updated and reorganized, it is now linked from the cluster status pages:
    - [Hydra-6](https://hydra-6.si.edu) → [Tools](https://hydra-6.si.edu/tools/) → [List of Available Modules](https://galaxy.si.edu/tools/QSubGen/module-avail.html)
    - [Status page (\@si.edu)](https://hydra-6.si.edu/tools/status/) → [List of Available Modules](https://hydra-6.si.edu/tools/status/module-avail.html)
    - [Status page (\@cfa.harvard.edu)](https://www.cfa.harvard.edu/~sylvain/hydra/) → [List of Available Modules](https://lweb.cfa.harvard.edu/~sylvain/hydra/module-avail.html)
    - That list is updated nightly. You can get that list with the command `module avail`
- Access to GPUs has been simplified
- Singularity is now available on a set of compute nodes
- Password Requirement Change
    - We adjusted the password requirement on Hydra to conform to SI's policy (only one digit).
- We have updated the modules description (`whatis`) for some modules to be more informative and consistent, and
    - for 7 modules we will change the default versions when loading that module without version specification - on Monday November 29, 2021


# Compilers


## Intel


- Intel 2021.3 and 2021.4 have been installed, and 2021 → 2021.4
    - As of 2021.x, Intel is matching NVIDIA and releasing their compiler and more for free under the OneAPI name
    - Intel's modules are a bit of a mess, I've cleaned them up but they are very chatty
    - As before Intel also offers their version of Python
- Previous versions are still available (2015.x to 2021.x, check the list of available modules on the pages listed above or with with `module avail intel)`


## PGI/NVIDIA


NVIDIA has acquired PGI and has repackaged these compilers as of 2020.


These compilers are now free and include CUDA support. This transition hasn't been the smoothest.


- The PGI compilers up to version 20.4 are still available (`module avail pgi`)
- As of 20.7 the compilers are NVIDIA (20.7 and 20.9), although they are available as pgi too
- NVIDIA versions 21.1, 21.2, 21.3, 21.5, 21.7 and 21.9 are now available (`module avail nvidia`)
- CUDA up to version 11.4 is available (CUDA 11.4 comes with NVIDIA 21.9)


## GCC


- Versions 10.1. 10.2.0 and 11.2.0 are now available
- Previous versions are still available (`module avail gcc`)
- Version 8.2.0 is not longer available on Hydra-6, it has been substituted by 10.2.0 by BCM


## MPI: Vendor, OpenMPI and MVAPICH


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


# Tools


## Java


- Java 17.0.1 is available, as well as version 1.8.0_45


## Python


- Versions 3.8, 3.9. 3.10 are available:
    - 3.8 is the most recent Anaconda version (2021.05),
    - 3.9 and 3.10 were built from source.
- Intel's version 3.7.11 is also available, distributed by Intel's OneAPI 2021.4


## IDL


- version 8.8.1 is available
- IDL licensing mechanism is currently a simpler one, hence `idl` issues the following message:


`Licensed for use by: Harvard-Smithsonian Astrophysical Observatory (Main)` 
`License: 100554-5516875-BUF` 
`License expires 30-Nov-2022.`


## MATLAB


- Matlab runtime version 2021a and 2021b are available


## Julia


- Version 1.6.2 and 1.6.3 are available


## CUDA


- CUDA is now included with the NVIDIA compilers,
- Version 11.4 comes with the 21.9 version of the compilers


# GPU


- Access to the nodes with GPUs has been simplified, just specify `-l gpu` to `qsub` or `qrsh`
- More details on this in the [GPU section](../reference-pages/how-to-use-gpus.md) of the [Reference pages](../reference-pages.md)


# Containers: singularity


- Singularity has been installed on a handful of node, you can access it by specifying the `@container-hosts` host group
- More details on this in the [Containers section](../reference-pages/how-to-use-containers.md) of the [Reference pages](../reference-pages.md)


# Password Requirement Change


- We adjusted the password requirement on Hydra to conform to SI's policy (only one digit).
- Passwords must conform to SI password policies and meet the following requirements:
    - at least 12 characters in length, and include at least:
        1. *one digit*,
        2. one upper case,
        3. one lower case, and
        4. one special character;
    - moreover, new passwords cannot be too similar to old passwords.


# Modules Description and Default Version


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
