---
title: "A Better Quota: quota+"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/374604070/A+Better+Quota+quota"
date-modified: "2025-10-23"
author: "SGK"
categories: ["hydra7"]
---

- The Linux command `quota` is not working on the GPFS (/scratch) or the NAS (/store).
- `quota+` will report disk quota information on all the disks (NFS, GPFS or NAS)


```{.text title="quota+ help"}
quota+ [options]
  where options are:
   -u|--user user        return quotas for given user (must be root)
   -v|--verbose          display quotas on filesystems where no storage is allocated
   -a|--all              display quotas on filesystems that are not mounted
   -%                    show Use% instead of Used
   +%                    show Use% as well as Used
   -f filesys            return quotas for given file system only
   -device               show device name only
   +device               show mount point and device name
   -terse                show only Used/Use% and Quota Limit, disable +%

Ver 2.6/1 May 2024
```
