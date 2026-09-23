# Older notices

- **Dec 16, 2025**
    - The production RStudio server was upgraded with an updated OS and R version.
- **Dec 8, 2025**
    - `QSubGen` was updated to include virtual memory and GPU.
    - `qstat+` has new sorting and limiting options.
- **Dec 5, 2005**
    - **1- Scrubber**


We will resume scrubbing old files (> 180 days) on the public disks this coming Sunday, Dec 7. Scrubbing was suspended just before moving Hydra to Ashburn.


**2- Disaster recovery (DR) Backups**


Due to admin/accounting issues, we have paused backing up /home and /data to the cloud. We will resume these as soon as the accounting issues are resolved.


Note that this is a DR (disaster recovery) backup. The storage unit that holds /home and /data (the NetApp filer) is very reliable.


**3- Tools Update**


We have updated various tools available on Hydra, namely:


The default version values have not been changed, hence you need to request a specific version when loading the corresponding module to use these new installs. We will change the default values in the near future (TDB).


For each compiler, besides the vendor's MPI version when available (i.e., Intel & NVIDIA), a few versions of MVAPICH and OpenMPI are also available.


We have updated the documentation on the Wiki accordingly.


**4- New Tools**


A new set of tools are available by loading the tools/misc module. Currently these are disk usage analysis tools, namely:


dua - a tool to learn about disk usage


dus+ - disk usage report (same as dus-report in tools/local+)


dut - disk usage calculator


gdu - disk usage analyzer written in Go


ncdu - ncurses disk usage


There is a man page for each tool, and with the exception of dus+, which is Hydra-specific, you can also learn more about these tools by searching for the developer's website.


We have updated/reorganized the documentation on the Wiki accordingly.


**5- RStudio server**


We have tested a new RStudio server with an updated image (OS) and R version (4.4.3 -> 4.5.1). We've tested this new OS and R release, but be aware that some R packages that you've installed in your R library may prompt to be updated for the new R version.

The production RStudio server will be offline on Tuesday December 16, 2025 for this upgrade. Let us know right away if this timing conflicts with your needs. We will notify users when it is back up and ready for use.
        - Information on scrubbing is available [here](../hydra/storage/scrubber.md).
        - IDL version 9.2.0
        - julia version 1.12.1
        - Matlab runtime versions 2025a and 2025b
        - Miniconda3 conda version 25.9.1
        - Miniforge mamba version 25.9.1
        - cmake version 4.2.0
        - vscode version 1.160.0
        - rclone version 1.71.2
        - awscli version 2.31.36
        - wget versions 2.0.1 and 2.2.0 (→ wget2, not wget)
        - HiFiasm version 0.25.0
        - python
        - Compilers:


- **Nov 13, 2025**
    - IDL 9.2.0 was installed, you can access it by loading the `idl/9.2` or `idl/9.2.0` module.
- **Oct 14, 2025**
    - GPU nodes and queues are available
    - Check these updated pages
        - [How to Use GPUs](../hydra/software/gpus.md)
        - [2025 Data Center Move](upgrades/2025-data-center-move.md)
- **Oct 6, 2025**
    - Hydra is back and operational
        - updates are described in detail at the [HPC Wiki 2025 Data Center Move page](upgrades/2025-data-center-move.md).
*Please take the time needed to read these pages before contacting us for support.*
    - Hydra has been successfully moved to the Ashburn Data Center:
        - Over 125 pieces of equipment have been relocated and re-cabled
        - The NetApp was upgraded with new disks and disk enclosure; old disks were decommissioned
        - The new GPFS (bigger and faster) is now in production
    - The cluster will be available for use with a slightly reduced capacity
        - All storage units are up and running, although *the disk space was reorganized.*
        - The head node and both login nodes are up and running.
        - some 69 compute nodes are up and running.
            - one one interactive and I/O node (for now);
            - the GPU nodes are up and running, but not yet available.
    - Globus services and R Studio Server are up and running.
    - Accessing Hydra remains unchanged, passwords remain valid, etc.
- **Please note:**
    - We upgraded the cluster's OS from RL 8.9 to RL 8.10 due to compatibility issues with the ADC network infrastructure.
        - This should not impact any applications - as per our tests.
    - The disk space on Hydra was reorganized (maintaining backward compatibility whenever possible) as follows:
        - Please read [this page](upgrades/2025-data-center-move.md) for important details.
- **Aug 15, 2025**
    - User quota on /home was reduced from 512GB to 384GB.
        - Users that have more than 384GB on `/home` have been contacted directly and were asked to trim down their use.
        - There are a dozen or so users with close to 300GB under `/home` that should consider trimming their usage, as we may have to further reduce that quota.
    - Please try to limit what you keep on `/home` to 200GB or less.
    - You can check your quota usage with the command `quota+ -f $HOME`, as explained in the disk space usage page documentation.
- **Jul 31, 2025**
    - **Hydra will be shut down Wednesday September 10 at 9am ET to be moved to the new data center**
    - All running and queued jobs will be deleted and logins to either login nodes disabled. During the move there will be no access to any of Hydra's resources, including compute nodes, R server, Globus, or any file stored on Hydra. If you anticipate needing access to some of these files, now is the time to copy them somewhere else.
    - If all goes well we anticipate that the move will be done by Monday September 22, although we can't guarantee it. This is a complex operation involving over a 100 pieces of equipment that need to be physically moved to a new location. We will send an update during the week of September 15.
    - In preparation for the move we will soon start making a second copy of the data stored on Hydra on our new GPFS system. This may slow down I/O operations on the disk systems being copied.
    - Also, a lot is stored on Hydra, hence we are asking you to ***delete anything you no longer need ASAP***.
    - All scrubbed files will be permanently deleted *ten days after being scrubbed*, except for what is scrubbed during the last 2 weeks prior to the shutdown, so *do not delay requests to restore files*.
- **May 21, 2025**
    - OCIO had to decommission the listserv we used to communicate with our users (aka HPCC-L) as of Friday 5/16 at COB.
    - We have set up a Google group email hosted at SAO ([hppc-l\@cfa.harvard.edu](mailto:hpcc-l@cfa.harvard.edu)) to send such emails.
        - You should have received a test email saying "New HPCC distribution list/method"
        - Please make sure that your mail reader is not sending those to spam.
    - This is a moderated groups email, hence users can post messages/questions to everyone on the list, and
        - the group moderator will distribute the message if deemed appropriate.
    - As before, you can still contact the Hydra support team via the following email addresses, based on your needs: 
 [SI-HPC-Admin\@si.edu](mailto:SI-HPC-Admin@si.edu) for SysAdmin related issues, 
 [SI-HPC\@si.edu](mailto:SI-HPC@si.edu) for Bioinformatic/Genomics questions, 
 [hpc\@cfa.harvard.edu](mailto:hpc@cfa.harvard.edu) for SAO/CfA users who need help.
- **Mar 5, 2025**
    - Hydra will be down while moving to a new data center location.
    - Current best guess
        - a 2 to 4 weeks downtime,
        - sometime between June and September 2025.
    - See updates under [2025 Data Center Move](upgrades/2025-data-center-move.md).
- **Feb 13, 2025**
    - We have increased the limit per user on the number of concurrent interactive sessions from one to four (still up to 6 slots/CPUs/cores).
    - We may reduce this number if the interactive queue gets filled or may decide to add more nodes to that queue.
- **Feb 10, 2025**
    - To address a problem that arose lately (i.e., job that creates an excessive number of threads), we have changed a section of [Hydra's Usage Policy.](../policies/usage.md)



## What was New in 2024

- **Nov 22, 2024**
    - MATLAB runtime R2024a and R2024b are now available,
    - load the `matlab/R2024b` or `matlab/2024a` module to access them.
- **Nov 7, 2024**
    - The command dos2unix is accessible without the need to load any module and the man page is available (man dos2unix).
    - We have added a workflow manager ("WFM") special queue, please consult the relevant [documentation](../hydra/jobs/queues.md).


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
    - See the "[2024 Cluster Upgrade to Hydra-7"](upgrades/2024-hydra-7.md) page for details.
    - *Please take the time needed to read these pages before contacting us for support.*
    - **Hardware Changes**


****We added 15 new compute nodes (2 nodes with 192 CPUs and 1.5TB of memory, 12 nodes with 128 CPUs and 1.0TB of memory, and 1 node with 4 GPUs - NVIDIA L40S, 48GB).


- 
    - **Software Changes**


****Hydra's OS was updated from CentOS 7.9 to Rocky 8.9 to support the new compute nodes and the latest software offerings.


****Rocky 8 is the successor to CentOS 7. Both Linux distributions are based on Red Hat Enterprise Linux and share many similarities. We will also upgrade various packages to the most recent versions, including the job scheduler (i.e., the Grid Engine), and many of the modules. We will no longer support old versions of some software packages.


****We are updating the documentation on the Wiki and update the "[2024 Cluster Upgrade to Hydra-7"](upgrades/2024-hydra-7.md) page with details on what has changed including new module versions.


****As always we are striving to make this transition as smooth as possible, while leveraging the opportunities and challenges of using a new version of the OS.

## What was New in 2023

- **November 27, 2023**
    - We have completed the FY23 hardware purchases and started work on upgrading the cluster's OS from CentOS 7 to Rocky 8.
    - We will add 15 new compute nodes, including a quad GPU server, and retire the oldest compute nodes.
    - The [2024 Upgrade page](upgrades/2024-hydra-7.md) details the planned changes and will describe them once completed.
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

## What was New in 2020 to 2022

- **November 15, 2022**


The migration of the 'disks' /home and /share/apps to a hybrid aggregate (a more performant set of disks that combines SSD and HDDs) was completed this past weekend. This will speed up access to the files stored under /home and /share/apps.


- 
    - 
        - As a result, the total size of /home is slightly smaller, while the sizes of /data/sao and /data/genomics have been increased.
        - Quotas****have not been changed.
        - If /home fills up too quickly we may have to reduce the quota on /home.
        - Users who want to use /data need to request access (up to 2TB of un-scrubbed space); non-SAO users should contact Rebecca, SAO users should contact Sylvain,


Please refer to Disks Space and Usage on the Wiki's Reference pages as to what disks to use and what to store where.


- **November 7, 2022**
    - 21 new compute nodes were added to Hydra as compute-65-xx (Dell R6515: AMD EPYC CPUs, 64 cores, 512GB memory).
    - All compute nodes with an AMD EPYC CPU have their "cpu_arch" set to "zen."
    - All the old compute-81-xx nodes (Dell R815) have been retired.
- **May 9, 2022**
    - The latest versions of the NVIDIA and Intel compilers (22.1, 22.2, 22.3 & 2022.1, 2022.2 respectively) have been installed,
    - The latest version of IDL (8.2.2) and MATLAB runtime (R2022a) have been installed,
    - The required modules are available, the default version have not yet been changed,
    - The examples have yet to be expanded to the new versions (the required changes should be obvious).
    - We plan to change the default versions some time in early June.
- **January 6 2022**
    - Since we have increased the cluster capacity, the maximum number of CPUs (slots) a user can use concurrently has been increased from 640 to 840.
- **December 17 2021**
    - Eight new compute nodes have been added to Hydra, bringing the totals to 5,408 CPUs for 98 nodes, and 42TB of memory.
    - We have noticed a read performance problem on the GPFS and are working with the vendor to resolve it as soon as possible.
- **December 2, 2021**
    - Look of the status pages has been update, and URL can now take up to 3 arguments.
    - New hardware (8 servers and 56 GPFS disks) has been delivered and will be deployed soon.
- **November 29, 2021**
    - The default version for 7 modules has been updated as announced in the Nov 22 update (see below.)
- **Nov 22 2021**
    - The documentation has been updated and reorganized to reflect the most recent changes.
    - New versions of the compilers and several tools have been installed,
        - default versions will get shortly updated, [details are here](upgrades/2021-hydra-6.md).
- **Sep 25 2021**
    - IDL 8.8.1 is available, use: `module load idl/8.8.1`
    - Loading idl/8.8 will still load 8.8.0 for a little while. Also the IDL licensing method has changed, you will now see the message:


| `License: 100554-5516875-BUF` 
`License expires 30-Nov-2021.` |
| --- |


which is normal (similar to SAO/CfA/CF's installation).
- **Sep 14 2021**
    - The next major upgrade of the SI/HPC cluster is completed.
    - We have made every effort to set up the new configuration as backward compatible as possible, although a few things have changed.
    - Please look at the [2021 Cluster Upgrade page](upgrades/2021-hydra-6.md) for details.
- **Jun 24 2021**
    - The next major upgrade of the SI/HPC cluster, Hydra, will take place from **August 30th through September 14th, 2021.**


While we are making every effort to set up the new configuration as backward compatible as possible, there will be changes. We hope to have Hydra back up before September 8th, but that decision won’t be made until the upgrade work is completed. During the downtime, access to files stored on Hydra will be limited, and at times unavailable, although none of your files will be deleted.
        - During the upgrade, Hydra will be inaccessible to users, and
        - as of 9am EDT on Monday August 30th any running jobs will be killed and any queued jobs will be deleted.
    - Please look at the [2021 Cluster Upgrade page](upgrades/2021-hydra-6.md) for additional details.
- **Sep 15 2020**
    - Scrubbing on /scratch has resumed: files older than 180 days are scrubbed
    - The GPFS s/w is in the process of being upgraded from v4 to v5, on a rolling basis and transparent to the users
    - IDL v 8.8[.0] is available
- **Apr 3 2020** - Hydra DOI
    - We have setup a DOI for Hydra ([https://doi.org/10.25572/SIHPC](https://doi.org/10.25572/SIHPC)) 
You are now able and encouraged to cite Hydra whenever research has benefited from its use and add a DOI link to that citation or acknowledgment.
- **Mar 24 2020**- Hydra status while teleworking
    - Hydra remains up and running.
    - We will address problems that require on-site staff as fast as possible.
    - We will answer people's questions and requests as promptly as possible.
    - Access to Hydra via VPN:
        - users are asked to limit the strain on the institutional VPN resources when ever appropriate.
    - Hydra can be accessed without VPN:
        - use the "*Hydra*" link under "*It Tools*" (or use RDP) at [telework.si.edu](http://telework.si.edu/).
        - SAO users can use [login.cfa.harvard.edu](http://login.cfa.harvard.edu/) to `ssh` to Hydra.
        - Access to the self serve password page is now working.
        - How to use Dropbox or Firefox Send (`ffsend`) to copy files to/from Hydra is documented on the Wiki.
    - The scrubbing policy has been modified as follows:
        - the scrubber will run on `/pool/sao` and `/pool/genomics` as usual, but
        - the scrubbed content will not be deleted for at least 21 days, and
        - we will accept requests to preserve what was scrubbed (beyond 21 days) as long as needed. To get your files restored, follow the usual instructions.
    - Users are asked to remain in contact via their SI email.
- **February 27, 2020** - `cpu_arch` resource and IDL 8.7.3
    - We have added a new resource, called `cpu_arch`, to allow users to direct jobs on nodes with CPUs of a specific (list of) architecture(s). 
If you run jobs/codes that can only run on (a) specific type(s) of processors, look at the new section [CPU Architecture](../hydra/jobs/queues.md) under the [Available Queues](../hydra/jobs/queues.md) page.
    - IDL version 8.7.3 has been installed on Hydra, and is accessible via the idl/8.7.3 module. The idl/8.7 module is now pointing to idl/8.7.3
- **January 14, 2020** - Increased total slot limit
    - The total number of slots (CPUs) a user can grab has been increased from 512 to 640.
