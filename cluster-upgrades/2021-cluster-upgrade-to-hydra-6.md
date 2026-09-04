---
title: "2021 Cluster Upgrade to Hydra-6"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152359/2021+Cluster+Upgrade+to+Hydra-6"
date-modified: "2021-09-13"
author: "SGK"
---

This page lists the upgrades that took between August 30th 2021 and September 14th.


- While we are making every effort to set up the new configuration as backward compatible as possible, there will be changes, see below.
- We anticipate a rewrite of the Wiki (organization and content) soon.


## What Has Been Upgraded


1. The OS version of cluster (CentOS 7.9)
2. The Grid Engine (v8.6.18);
3. The cluster management tool, i.e, Bright Cluster Management (v9.1);
4. The NetApp controller (FAS8300); we replaced some of the oldest disks with new ones;
5. The firmware in some components of the GPFS;
6. Etc


## Access


- Access to Hydra has not changed, ssh into `hydra-login01.si.edu` or `hydra-login02.si.edu`.
- Your credentials (username and password) have not changed.
- The web pages under `https://hydra-5.si.edu` have been moved to `https://hydra-6.si.edu.`
    - In most cases you should be redirected, but if you are not, please update your bookmarks accordingly.


# List of Changes


### Main Software Upgrade


**What**: upgrade of the operating system, the cluster management tool and the grid engine versions


**Impact**: access to a more recent software release and updated versions of the associated tools.


**Details**: upgraded O/S to CentOS 7.9 (release upgrade), UGE to v8.6.18 (newer release), BCM to v9.1 (new version).


**NOTE**: users will see a warning when logging on either login node that the host key has changed.


**This is normal.**You can either edit the known hosts file, delete it or hit OK when prompted to update it.


On most systems the known host file is `~/.ssh/known_hosts` .


**Also**, some mail readers (like GMail) have marked email coming from `hydra-6` as spam.


Check your spam folder and set your mail reader to accept all emails from `hydra-6.si.edu` and from `hydra-6a.si.edu`.


### Installed a New NetApp Controller with Some New Disks


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


### Queue Changes


**What**: removed the uTSSD.tq and uTGPU.tq queues.


**Impact**: access to local SSD storage is now integrated with the high-CPU and high-memory queues.


GPU servers and associated software have yet to be re-installed on Hydra-6.


**Details**: request for SSD storage is similar, but you only need to specify `-l ssdres=XXX`, and no longer "`-q uTSSD.tq -l ssd"`.


As for access to GPUs, we will soon migrate the GPU servers to Hydra-6 and install the required software. We also plan to use the Grid Engine 
native GPU support, stay tuned and/or contact us.


### Modules Changes


**What**: the module `tools/local` has been split into `tools/local-users` and `tool/local-admin`,


and the module `tools/local-users` is always loaded, like the `uge` module.


**Impact**: users have access to some Hydra-specific tool without having to load an extra module.


**Details**: we decided to split what was available with `module load tools/local` into `tools/local-users` and 
 `tool/local-admin` and load the `tools/local-users` module for all users. You can still load `tools/local` that will 
 load `tools/local-user` and `tools/local-admin,` and `tools/local+` remains unchanged.


### Changes Affecting Bioinformatics Modules


**What**: you can now load any module previously know as `bioinformatics/XXX` using the `bio/XXX` shortcut.


**Impact**: bio is now a shortcut to bioinformatics.


**Details**: a symbolic link `bio`, pointing to `bioinformatics,`has been created as a shortcut. We plan to migrate all the 
 bio-informatics tools to `bio/` in the future, hence we recommend that you start using `bio/` in lieu of `bioinformatics/`


### Changes Affecting IDL


**What**: IDL versions prior to version 8.6 are no longer available. 
 
 **Impact**: IDL users must use version 8.6 or higher, 8.8 is the most recent version (default and recommended version). 
 
 **Details**: IDL changed the license manager as of 8.6 and we decided not to migrate the old, unsupported and obsolete licence manager,


hence only version 8.6 or higher are available. The default IDL version is 8.8 (8.8.0), version 8.8.1 will be installed soon and will become the default value.


Note that most likely version 8.9 will come with a new license manager.


### Changes Affecting R


**What**: R versions prior to version 3.5.2 are no longer available.


**Impact**: R user will need to switch to the supported version or use conda to install a different version.


**Details:** We removed old versions to streamline availability of R, under bio/R or tools/R, the default version is 3.6.1.


### Changes Affecting MPI Users of OpenMPI


**What**: a workaround is needed for users whose login shell is `/bin/csh` and use OpenMPI using `-pe orte` for parallel jobs


**Impact**: users whose login shell is `/bin/csh` need to add a line to their `~/.cshrc`


**Details**: A "*feature"* of UGE version 8.6.18 is causing a mysterious `Unmatch ".`error message for users whole login shell is `/bin/csh`


when submitting jobs with `-pe orte` (OpenMPI jobs). There is a simple fix to avoid this problem, simply add the line


`if ($?JOB_ID) set backslash_quote`


to your `~/.cshrc` file. Explanations can be found under the `execd_params` section of `man sge_conf,` see E`NABLE_BACKSLASH_ESCAPE`,


and the Lexical structure section of `man csh`.


### Changes Affecting the qacct+ Local Tool


**What**: `qacct+` now use the GE's native DB ARCo and has been modified accordingly.


**Impact**: Almost no delay between `qacct` and `qacct+,` and the arguments to `qacct+` have changed.


**Details**: `qacct+` is now using the ARCo DB, a GE native product that is updated nearly in real time by the GE.


`qacct+` has been modified to query ARCo, hence some types of queries are no longer available, and the arguments to `qacct+` have been modified accordingly.


In the process most of the argument syntax has been changed, see `man qacct+` or `qacct+ -help` .


### Changes Affecting the Compilers


**What**: we are no longer supporting old versions of some of the compilers and plan to install the most recent versions of these compilers soon.


**Impact**: Users need to use the more recent versions of the GCC, PGI/NVIDIA, Intel compilers


**Details**: Rather than delaying the reopening, we have not yet, but will soon install the most recent versions of the NVIDIA and Intel compilers and


will consider installing the most recent GCC compilers. We no longer support some of the old version of the PGI and Intel compilers, and have


removed some of the associated modules . Once we have installed and validated the most recent versions of the compilers we will consolidate


which versions of each compiler will be supported, notify the users and update the documentation.


### **Changes Affecting Blast2GO**


**What**: Blast2GO has been upgraded from 1.4.4 to 1.5.1. The reference GO database has been upgraded from 2019_10 to the latest, 2021_06.


**Impact**: Newer database will give you the most up to date annotations. You will need to re-run `hydracliprop` after loading the module to generate an up to date cli.prop file. In Blast2GO, the argument `-saveb2g <path>` has been changed to `-savebox <path>` (OmicsBox format).


**Details:** The new module is `bio/blast2go/1.5.1` . The previous version’s module `bio/blast2go/1.4.4` and its database are currently still available, but will be removed soon.


### Coming Up


**What**: more compute servers and more GPFS disk space and rewritten documentation


**Impact**: more CPUs, more disk space under /`scratch` and better documentation


**Details**: We have ordered eight new 64-core servers and an extra ~500TB of GPFS disk space.


Because of a shortage of computer parts and the current supply chain disruption, these will likely be delivered by the end of 2021.


We will rewrite the documentation hosted on [confluence.si.edu/display/HPC](http://confluence.si.edu/display/HPC); it will be reorganized and updated to reflect the most recent upgrade.
