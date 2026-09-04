---
title: "What was New in 2024"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/378274038/What+was+New+in+2024"
date-modified: "2025-12-16"
author: "SGK"
categories: ["hydra7"]
---

- **Nov 22, 2024**
    - MATLAB runtime R2024a and R2024b are now available,
    - load the `matlab/R2024b` or `matlab/2024a` module to access them.
- **Nov 7, 2024**
    - The command dos2unix is accessible without the need to load any module and the man page is available (man dos2unix).
    - We have added a workflow manager ("WFM") special queue, please consult the relevant [documentation](https://confluence.si.edu/display/HPC/Available+Queues#AvailableQueues-WorkflowManagerQueue).


- **Oct 28, 2024**
    - A new web-based SSH terminal (WeTTY) for accessing Hydra through a browser (*e.g.*, [https://telework.si.edu](https://telework.si.edu/)). 
This new interface uses improved website technology for a better user experience: faster display of text to the screen; better support for pasting text into the browser, etc. compared to the web-based SSH interface we have been offering until now (shell-in-a-box).


Both the new and old systems are currently available, either on the Hydra landing page ([https://hydra.si.edu](https://hydra.si.edu/)) or via the "Hydra" option at [https://telework.si.edu](https://telework.si.edu/). 
The new system is labeled "New Web SSH terminal (WeTTY)".


**If you're a user of the web-based SSH terminal, please try out the new system and let us know if you encounter any issues. 
We will remove the old interface by December 1st if no major issues are identified.**


- **Oct 26 2024**
    - We have added a page explaining the automatic emails sent to users.
- **Sep 16 2024**
    - We have installed the following:


The examples, under `~hpc/examples`, have yet to be updated to include the latest versions of these compilers.
        - gnuplot on all the compute nodes (v5.2p4), not just the login nodes;
        - the latest version of awscli (v 2.17.43):
            - to access it load the tools/awscli module,
            - version 2.15.27 is available via the tools/awscli/2.15.27 module;
        - newest version of the compilers:
            - gnu 14.2.0 via the gcc/14.2.0 module,
                - the default version remains 8.5.0;
            - Nvidia 24.3 and 24.5, via the nvidia/24.3 or nvidia/24.5 modules,
                - the default version remains 23.9;
            - Intel 2024.1 and 2024.2, via the intel/2024.1 and intel/2024.2 modules,
                - the default version remains 2024.0.
        - The various MPI flavors (vendor's, OpenMPI and MVAPICH) are available for each compiler version, including several versions whenever possible.
            - refer to the module list, or use:
                - module whatis gcc/14.2/
                - module whatis nvidia/24/
                - module whatis intel/24/
        - The Nvidia compilers come with two different versions of cuda: 11.8 and 12.x.
        - The Intel compilers come with Intel's distribution of python and conda.
    - You can now use `hydra.si.edu` to reach `hydra-7.si.edu`
        - going forward, we will keep `hydra.si.edu` pointing to the latest version of `hydra-N.si.edu.`
    - A compute node with 3 TB of memory was added to the cluster
        - it was added to the extra large memory queue (`uTxlM.rq`)


- **Sep 6 2024**
    - We have shut down Hydra for 3 days on Tuesday September 10th at 9AM ET to perform system maintenance. Please plan accordingly.
        - During that time, access to Hydra, including its disks, will not be available. All running and queued jobs will be killed on Sep 10 at 9am.
        - Access will be restored as soon as the maintenance is completed and users will be notified.


- **Jul 15 2024**
    - We have implemented and documented several ways to use Hydra's interactive nodes with 3 browser-based development environments: `JupyterLab`, `RStudio` and `VSCode`.
        - These implementations are experimental and we welcome your feedback.
    - Please refer to the documentation under Reference Pages in the new Interactive Use section. Note that these interactive tools do not work when accessing Hydra via `telework.si.edu` except for the `VSCode` tunnel.
        - **`JupyterLab`**: there is now a simple script to help you start a JupyterLab server on Hydra, using an interactive node or a GPU node, with instructions on how to start the ssh tunnel on your local machine to access it.
        - **`RStudio`** is now available as a desktop or a server option, with a simple script to help you start it and with instructions on how to start the ssh tunnel on your local machine to access it. Note that you must use v4.4.1 of `R` as the back engine to `RStudio`, not v4.4.0 (see below).
        - **`VSCode`**: you can use `VSCode` several different ways, including as a server or via a tunnel, with simple scripts to help you set them up (and instructions on how to start the ssh tunnel on your local machine to access it when needed).
    - Version 4.4.1 of `R` is now available on Hydra and supports `RStudio`. To use it, you need to specify the version explicitly when loading the `R` module (`tools/R/4.4.1` or `bio/R/4.4.1`).
        - For backward compatibility, the default value remains 4.4.0 for now.
- **Jun 6, 2024**
    - The`dropbox_uploader` module was removed, neither versions we tried are working any longer.
        - we recommend users switch to `rclone`.
    - The IDL license server was relocated from `hydra-6` to `hydra-7`, hence there were intermittent unavailability of IDL today.
- **May 7, 2024** **-**Hydra was upgraded to Linux Rocky 8.9 and 15 new compute nodes were added.
    - See the "[2024 Cluster Upgrade to Hydra-7"](https://confluence.si.edu/display/HPC/2024+Cluster+Upgrade+to+Hydra-7) page for details.
    - *Please take the time needed to read these pages before contacting us for support.*
    - **Hardware Changes**


****We added 15 new compute nodes (2 nodes with 192 CPUs and 1.5TB of memory, 12 nodes with 128 CPUs and 1.0TB of memory, and 1 node with 4 GPUs - NVIDIA L40S, 48GB).


- 
    - **Software Changes**


****Hydra's OS was updated from CentOS 7.9 to Rocky 8.9 to support the new compute nodes and the latest software offerings.


****Rocky 8 is the successor to CentOS 7. Both Linux distributions are based on Red Hat Enterprise Linux and share many similarities. We will also upgrade various packages to the most recent versions, including the job scheduler (i.e., the Grid Engine), and many of the modules. We will no longer support old versions of some software packages.


****We are updating the documentation on the Wiki and update the "[2024 Cluster Upgrade to Hydra-7"](https://confluence.si.edu/display/HPC/2024+Cluster+Upgrade+to+Hydra-7) page with details on what has changed including new module versions.


****As always we are striving to make this transition as smooth as possible, while leveraging the opportunities and challenges of using a new version of the OS.
