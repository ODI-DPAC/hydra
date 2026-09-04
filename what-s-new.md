---
title: "What's New"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152215/What+s+New"
categories: ["hydra7"]
---

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
        - Information on scrubbing is available [here](https://confluence.si.edu/display/HPC/Scrubber+and+How+to+Request+Scrubbed+Files+to+be+Restored).
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
        - [How to Use GPUs](https://confluence.si.edu/display/HPC/How+to+Use+GPUs)
        - [2025 Data Center Move](https://confluence.si.edu/display/HPC/2025+Data+Center+Move)
- **Oct 6, 2025**
    - Hydra is back and operational
        - updates are described in detail at the [HPC Wiki 2025 Data Center Move page](https://confluence.si.edu/display/HPC/2025+Data+Center+Move).
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
        - Please read [this page](https://confluence.si.edu/display/HPC/2025+Data+Center+Move) for important details.
- **Aug 15, 2025**
    - User quota on /home was reduced from 512GB to 384GB.
        - Users that have more than 384GB on `/home` have been contacted directly and were asked to trim down their use.
        - There are a dozen or so users with close to 300GB under `/home` that should consider trimming their usage, as we may have to further reduce that quota.
    - Please try to limit what you keep on `/home` to 200GB or less.
    - You can check your quota usage with the command `quota+ -f $HOME`, as explained in the [disk space usage page documentation](https://confluence.si.edu/display/HPC/Disks+Space+and+Usage).
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
    - See updates under [2025 Data Center Move](https://confluence.si.edu/display/HPC/2025+Data+Center+Move).
- **Feb 13, 2025**
    - We have increased the limit per user on the number of concurrent interactive sessions from one to four (still up to 6 slots/CPUs/cores).
    - ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) We may reduce this number if the interactive queue gets filled or may decide to add more nodes to that queue.
- **Feb 10, 2025**
    - To address a problem that arose lately (i.e., job that creates an excessive number of threads), we have changed a section of [Hydra's Usage Policy.](https://confluence.si.edu/display/HPC/Hydra+Policies)


Last updated //SGK
