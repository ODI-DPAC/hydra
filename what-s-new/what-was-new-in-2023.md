---
title: "What was New in 2023"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/378274040/What+was+New+in+2023"
date-modified: "2025-12-16"
author: "SGK"
categories: ["hydra7"]
---

- **November 27, 2023**
    - We have completed the FY23 hardware purchases and started work on upgrading the cluster's OS from CentOS 7 to Rocky 8.
    - We will add 15 new compute nodes, including a quad GPU server, and retire the oldest compute nodes.
    - The [2024 Upgrade page](../cluster-upgrades/2024-cluster-upgrade-to-hydra-7.md) details the planned changes and will describe them once completed.
    - We are in the process of testing Rocky 8 and are currently aiming to transition Hydra to this OS in the end of January - beginning of February 2024 time-frame.
        - We anticipate the cluster being shut down for about 10 days for this work during which time no jobs will be running and there will be no access to the files stored on Hydra.
- **September 27, 2023**
    - **Software updates**
        - The latest version of Python available from Anaconda, namely version 3.11, has been installed. It can be accessed via the `tools/python/3.11` module.
            - The default version, `tools/python`, remains Anaconda's distribution version 3.8.
        - The latest version of IDL (8.9.0) has been installed as well as their latest license manager. IDL is accessed via the `idl` module.
            - The default version remains 8.8.1, you can access the more recent versions via the `idl/8.8.2` or `idl/8.9.0`modules. Note the oldest versions, i.e.. 8.6, will no longer work after Nov 30, 2023.
        - The latest versions of MATLAB runtime has been installed on Hydra: R2022b, R2023a and R2023b. They are accessible via the `matlab/2022b` and `matlab/2023[ab]`modules.
            - The default version remains 2021b.
        - The latest version of Julia has been installed on Hydra, namely version 1.9.3, via the `tools/julia/1.9.3`module.
            - The default version remains 1.6.3.
        - The latest NVIDIA compilers, formerly PGI, have been installed: versions 23.5 and 23.7, and are accessed via the `nvidia/23.5` and `nvidia/23.7` modules.
            - Note that all flavors of MPI for these new versions are not working on Hydra.
            - The default version remains 21.9, the newer available versions are 22.[1239] and 23.[357], with full MPI support up to 23.3.
        - We are unable to install the latest INTEL compilers, since INTEL only releases new versions for Rocky 8, and no longer for CentOS 7.
            - The latest INTEL compiler versions are 2022.[12], the default version remains 2021.4.
    - **Upgrade of Hydra to Rocky 8**
        - We will update Hydra's OS from CentOS 7 to Rocky 8, to fully support the latest hardware and software offerings.
            - The new compute nodes we are in the process of purchasing (see below) require Rocky 8 as well as various new software packages.
        - Note that the transition to Rocky 8 might not be as transparent as previous CentOS upgrades. We will strive to make it as smooth as possible.
        - We do not have yet any estimate of when we will transition to Rocky 8, so stay tuned.
        - As usual, we will give at least four weeks notice for any scheduled downtime.
    - **Hardware updates**
        - We plan to refresh 14 compute nodes with high end servers fitted with the latest AMD processors (Zen4), with 128 or 192 cores per server and 1 or 1.5TB of memory each (12 & 2 respectively).
        - We also plan on adding one GPU server with four A100 GPUs.
        - We will retire our oldest compute nodes (compute-43-xx). We thank Deron Burba, SI CIO, for contributing additional funding to make these purchases possible.
        - We have recently evaluated various storage options and anticipate expanding our storage on Hydra next year, adding more `/scratch`space and if possible adding a somewhat smaller but very fast different storage system.
    - **Personnel changes.**
        - After more than 7 years at the Office of Research Computing (ORC), Rebecca Dikow will leave ORC and move on to her next endeavor.
        - The ORC is putting in place a transition plan so as to avoid any disruptions this might cause. Please use [si-hpc\@si.edu](mailto:si-hpc@si.edu) or [si-hpc-admin\@si.edu](mailto:si-hpc-admin@si.edu) for communicating with us, instead of emailing Rebecca directly for issues/questions related to Hydra.
