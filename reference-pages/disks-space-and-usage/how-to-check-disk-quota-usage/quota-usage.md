---
title: "Quota Usage"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152318/Quota+Usage"
date-modified: "2025-10-06"
author: "SGK/PBF"
categories: ["hydra7"]
---

# Quota


The Linux command `quota` is working with the NetApp (`/home` & `/data`), but not on the GPFS (`/scratch`) or the NAS (`/store`).


For example:


```{.text title="% quota -s"}
Disk quotas for user hpc (uid 7235): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
netapp-fas83:/vol_home
                   118G    350G    384G            307k   9000k  10000k        
netapp-fas83:/vol_home/hpc/.snapshot/daily.2025-09-30_0010
                   118G    350G    384G            307k   9000k  10000k        
10.61.83.219:/vol_data_public
                   292G   4378G   4608G           63018   9500k  10000k        
10.61.83.219:/vol_data_admin
                  1141M   1434G   1536G           38723   1800k   2000k         
```


reports your quotas. The `-s` stands for `--human-readable`, hence the 'k' and 'G'. While


% quota -q


will print only information on filesystems where your usage is over the quota. (`man quota`)


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)The command `quota+` (need to load `tools/local`) return disk quota for all the disks (see the [quota+ section in Additional Tool](../../additional-tools.md)).


# Other Tools


Hydra-specific tools, (i.e., requires that you load the `tools/local` module), to help manage quotas are:


- `quota+` - show quota values
- `parse-disk-quota-reports` - parse quota reports


**Note**: we compile a quota report 4x/day and provide tools to parse the quota report.


- The daily quota report is written around 3:00, 9:00, 15:00, and 21:00
    - in a file called `quota_report_YYDDMM_HH.txt, located in /data/sao/hpc/quota-reports/unified/`.``
- The string `YYDDMM_HH`corresponds to the date & hour of the report: "`160120_09`" for Jan 20 2016 9am report.
- The format of this file is not very user friendly and users are listed by their user ID.


## Examples


- `quota+` - show quota values:


```
% quota+
Disk quotas for user sylvain (uid 10541):
Mounted on                             Used   Quota   Limit   Grace   Files   Quota   Limit   Grace
----------                          ------- ------- ------- ------- ------- ------- ------- -------
/data/admin                            none   1.40T   1.50T       0       7   1.80M   2.00M       0
/data/public                          4.89T  22.50T  23.00T       0  118.0M  280.0M  290.0M       0
/home                                14.41G  350.0G  384.0G       0  136.6k   9.00M  10.00M       0
/store/admin                          1.00G    none    none
/store/sylvain                        8.41T    none    none
```


Use `quota+ -h,`or read the man page (`man quota+`), for the complete usage info.


- `parse-disk-quota-reports` will parse the disk quota report file and produce a more concise report:


```
% parse-disk-quota-reports
Disk quota report: show usage above 85% of quota, (warning when quota > 95%), as of Mon Oct  6 15:00:09 2025.

Volume=NetApp:vol_data_public, mounted as /data/public
                     --  disk   --     --  #files --     default quota:  4.50TB/10.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/data/public          4.13TB  91.8%     5.07M  50.7%     Alicia Talavera, NMNH - talaveraa

Volume=NetApp:vol_home, mounted as /home
                     --  disk   --     --  #files --     default quota: 384.0GB/10.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/home                361.1GB  94.0%     2.73M  27.3%     Brian Bourke, WRBU - bourkeb
/home                360.7GB  93.9%     0.24M   2.4%     Juan Uribe, NMNH - uribeje
/home                348.5GB  90.8%     2.06M  20.6%     Michael Trizna, NMNH/BOL - triznam
/home                344.2GB  89.6%     0.30M   3.0%     Paul Cristofari, SAO/SSP - pcristof
/home                328.1GB  85.4%     0.00M   0.0%     Allan Cabrero, NMNH - cabreroa

Volume=NetApp:vol_pool_nmnh_ggi, mounted as /pool/nmnh_ggi
                     --  disk   --     --  #files --     default quota: 16.00TB/39.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/pool/nmnh_ggi       13.76TB  86.0%     6.08M  15.6%     Vanessa Gonzalez, NMNH/LAB - gonzalezv

Volume=NetApp:vol_pool_public, mounted as /pool/public
                     --  disk   --     --  #files --     default quota:  7.50TB/18.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/pool/public          5.66TB  75.5%    17.31M  96.2% *** Alberto Coello Garrido, NMNH - coellogarridoa

Volume=NAS:store_public, mounted as /store/public
                     --  disk   --     --  #files --     default quota:   0.0MB/0.0M
Disk                 usage   %quota    usage  %quota     name, affiliation - username (indiv. quota)
-------------------- ------- ------    ------ ------     -------------------------------------------
/store/public         4.80TB  96.1%        -      -  *** Madeline Bursell, OCIO - bursellm (5.0TB/0M)
/store/public         4.51TB  90.1%        -      -      Alicia Talavera, NMNH - talaveraa (5.0TB/0M)
/store/public         4.39TB  87.8%        -      -      Mirian Tsuchiya, NMNH/Botany - tsuchiyam (5.0TB/0M)
```


reports disk usage when it is above 85% of the quota.


Use `parse-disk-quota-reports -h`, or read the man page (`man parse-disk-quota-reports`). for the complete usage info.


## Note


- Users whose quotas are above the 85% threshold will receive a warning email one a week (issued on Monday mornings).
    - This is a warning, as long as you are below 100% you are OK.
    - Users won't be able to write on disks on which they have exceeded their hard limits.
