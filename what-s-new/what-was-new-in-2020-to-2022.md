---
title: "What was New in 2020 to 2022"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/378274044/What+was+New+in+2020+to+2022"
date-modified: "2025-12-16"
author: "SGK"
categories: ["hydra7"]
---

- **November 15, 2022**


The migration of the 'disks' /home and /share/apps to a hybrid aggregate (a more performant set of disks that combines SSD and HDDs) was completed this past weekend. This will speed up access to the files stored under /home and /share/apps.


- 
    - 
        - As a result, the total size of /home is slightly smaller, while the sizes of /data/sao and /data/genomics have been increased.
        - Quotas****have not been changed.
        - If /home fills up too quickly we may have to reduce the quota on /home.
        - Users who want to use /data need to request access (up to 2TB of un-scrubbed space); non-SAO users should contact Rebecca, SAO users should contact Sylvain,


Please refer to [Disks Space and Usage](https://confluence.si.edu/display/HPC/Disks+Space+and+Usage) on the [Wiki's Reference pages](https://confluence.si.edu/display/HPC/Reference+Pages) as to what disks to use and what to store where.


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
        - default versions will get shortly updated, [details are here](../cluster-upgrades/nov-2021-updates-compilers-tools-and-more.md).
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
    - Please look at the [2021 Cluster Upgrade page](https://confluence.si.edu/display/HPC/2021+Cluster+Upgrade) for details.
- **Jun 24 2021**
    - The next major upgrade of the SI/HPC cluster, Hydra, will take place from **August 30th through September 14th, 2021.**


While we are making every effort to set up the new configuration as backward compatible as possible, there will be changes. We hope to have Hydra back up before September 8th, but that decision won’t be made until the upgrade work is completed. During the downtime, access to files stored on Hydra will be limited, and at times unavailable, although none of your files will be deleted.
        - During the upgrade, Hydra will be inaccessible to users, and
        - as of 9am EDT on Monday August 30th any running jobs will be killed and any queued jobs will be deleted.
    - Please look at the [2021 Cluster Upgrade page](https://confluence.si.edu/display/HPC/2021+Cluster+Upgrade) for additional details.
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
If you run jobs/codes that can only run on (a) specific type(s) of processors, look at the new section [CPU Architecture](https://confluence.si.edu/display/HPC/Available+Queues#AvailableQueues-CPUArchitecture) under the [Available Queues](https://confluence.si.edu/display/HPC/Available+Queues) page.
    - IDL version 8.7.3 has been installed on Hydra, and is accessible via the idl/8.7.3 module. The idl/8.7 module is now pointing to idl/8.7.3
- **January 14, 2020** - Increased total slot limit
    - The total number of slots (CPUs) a user can grab has been increased from 512 to 640.
