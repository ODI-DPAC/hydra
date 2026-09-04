---
title: "Disk Usage"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152316/Disk+Usage"
date-modified: "2025-10-06"
author: "SGK/PBF"
categories: ["hydra7"]
---

1. [Commands `du, df`](disk-usage.md),
2. Local Tools
    1. [Command `disk-usage`](disk-usage.md)
    2. [Command `dus-report`](disk-usage.md)


# 1. Commands `du, df`


The output of `du` can be very long and confusing. It is best used with the option "`-hs`" to show the sum ("`-s`") and to print it in a human readable format ("`-h`").


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) If there is a lot of files/directory, `du` can take a while to complete.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) For example:


```
% du -sh dir/
136M    dir/
```


The output of `df` can be very long and confusing.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) You can use it to query a specific partition and get the output in a human readable format ("`-h`"), for example:


```
% df -h /scratch/public
Filesystem      Size  Used Avail Use% Mounted on
gpfs02          800T  350T  451T  44% /scratch02

or 

% df -h --output=source,fstype,size,used,avail,pcent,file /scratch/genomics
Filesystem     Type  Size  Used Avail Use% File
gpfs02         gpfs  800T  350T  451T  44% /scratch/genomics
```


# 2. Local Tools


## a. Command `disk-usage`


The tool `disk-usage`runs `df` and presents its output in a more friendly format:


```
% disk-usage -d all+
Filesystem                                Size     Used    Avail Capacity  Mounted on
netapp-fas83:/vol_home                  22.36T   14.45T    7.91T  65%/11%  /home
netapp-fas83-n02:/vol_data_public      332.50T   40.32T  292.18T  13%/2%   /data/public
gpfs02:public                          800.00T  349.32T  450.68T  44%/26%  /scratch/public
gpfs02:nmnh_bradys                      25.00T   19.24T    5.76T  77%/87%  /scratch/bradys
gpfs02:nmnh_kistlerl                   120.00T   97.94T   22.06T  82%/14%  /scratch/kistlerl
gpfs02:nmnh_meyerc                      25.00T   18.85T    6.15T  76%/7%   /scratch/meyerc
gpfs02:nmnh_corals                      60.00T   45.16T   14.84T  76%/22%  /scratch/nmnh_corals
gpfs02:nmnh_ggi                        130.00T   35.79T   94.21T  28%/15%  /scratch/nmnh_ggi
gpfs02:nmnh_lab                         25.00T   10.69T   14.31T  43%/11%  /scratch/nmnh_lab
gpfs02:nmnh_mammals                     35.00T   20.82T   14.18T  60%/39%  /scratch/nmnh_mammals
gpfs02:nmnh_mdbc                        50.00T   39.56T   10.44T  80%/16%  /scratch/nmnh_mdbc
gpfs02:nmnh_ocean_dna                   40.00T   36.92T    3.08T  93%/3%   /scratch/nmnh_ocean_dna
gpfs02:nzp_ccg                          45.00T   32.42T   12.58T  73%/3%   /scratch/nzp_ccg
gpfs01:ocio_dpo                         10.00T    0.00G   10.00T   1%/1%   /scratch/ocio_dpo
gpfs01:ocio_ids                          5.00T    0.00G    5.00T   0%/1%   /scratch/ocio_ids
gpfs02:pool_kozakk                      28.00T   10.67T   17.33T  39%/1%   /scratch/pool_kozakk
gpfs02:pool_sao_access                  50.00T    4.79T   45.21T  10%/9%   /scratch/pool_sao_access
gpfs02:pool_sao_rtdc                    20.00T  908.33G   19.11T   5%/1%   /scratch/pool_sao_rtdc
gpfs02:sao_atmos                       350.00T  263.46T   86.54T  76%/10%  /scratch/sao_atmos
gpfs02:sao_cga                          25.00T    9.44T   15.56T  38%/28%  /scratch/sao_cga
gpfs02:sao_tess                         50.00T   23.25T   26.75T  47%/83%  /scratch/sao_tess
gpfs02:scbi_gis                         80.00T   37.04T   42.96T  47%/15%  /scratch/scbi_gis
gpfs02:nmnh_schultzt                    35.00T   19.52T   15.48T  56%/75%  /scratch/schultzt
gpfs02:serc_cdelab                      15.00T   12.70T    2.30T  85%/19%  /scratch/serc_cdelab
gpfs02:stri_ap                          25.00T   18.96T    6.04T  76%/1%   /scratch/stri_ap
gpfs01:sao_sylvain                     145.00T   85.84T   59.16T  60%/59%  /scratch/sylvain
gpfs02:usda_sel                         25.00T    5.47T   19.53T  22%/30%  /scratch/usda_sel
gpfs02:wrbu                             50.00T   39.35T   10.65T  79%/14%  /scratch/wrbu
nas1:/mnt/pool/public                  175.00T   94.03T   80.97T  54%/1%   /store/public
nas1:/mnt/pool/nmnh_bradys              39.74T   13.78T   25.96T  35%/1%   /store/bradys
nas2:/mnt/pool/n1p3/nmnh_ggi            90.00T   36.28T   53.72T  41%/1%   /store/nmnh_ggi
nas2:/mnt/pool/nmnh_lab                 40.00T   13.88T   26.12T  35%/1%   /store/nmnh_lab
nas2:/mnt/pool/nmnh_ocean_dna           40.00T    2.25T   37.75T   6%/1%   /store/nmnh_ocean_dna
nas1:/mnt/pool/nzp_ccg                 265.00T  109.76T  155.23T  42%/1%   /store/nzp_ccg
nas2:/mnt/pool/n1p2/ocio_dpo            50.00T  182.85G   49.82T   1%/1%   /store/ocio_dpo
nas2:/mnt/pool/n1p1/sao_atmos          750.00T  369.07T  380.93T  50%/1%   /store/sao_atmos
nas2:/mnt/pool/n1p2/nmnh_schultzt       80.00T   24.96T   55.04T  32%/1%   /store/schultzt
nas1:/mnt/pool/sao_sylvain              50.00T    9.42T   40.58T  19%/1%   /store/sylvain
nas1:/mnt/pool/wrbu                     80.00T   10.02T   69.98T  13%/1%   /store/wrbu
nas1:/mnt/pool/admin                    20.00T    7.99T   12.01T  40%/1%   /store/admin
```


Use


`% disk-usage -help`


to see how else to use it.


You can, for instance, get the disk quotas and the max size, for all the disks, including `/store`, with:


```
% disk-usage -d all+ -quotas
                                                                   quotas:  disk space   #inodes   
Filesystem                                Size     Used    Avail Capacity    soft/hard   soft/hard Mounted on
netapp-fas83:/vol_home                  22.36T   14.45T    7.91T  65%/11%    350G/384G   9.0M/10M  /home
netapp-fas83-n02:/vol_data_public      332.50T   40.32T  292.18T  13%/2%     4.3T/4.5T   9.5M/10M  /data/public
gpfs02:public                          800.00T  349.33T  450.67T  44%/26%     14T/15T     37M/39M  /scratch/public
gpfs02:nmnh_bradys                      25.00T   19.24T    5.76T  77%/87%     23T/25T     52M/54M  /scratch/bradys
gpfs02:nmnh_kistlerl                   120.00T   97.94T   22.06T  82%/14%    114T/120T    99M/104M /scratch/kistlerl
gpfs02:nmnh_meyerc                      25.00T   18.85T    6.15T  76%/7%      23T/25T     19M/22M  /scratch/meyerc
gpfs02:nmnh_corals                      60.00T   45.16T   14.84T  76%/22%     57T/60T     49M/52M  /scratch/nmnh_corals
gpfs02:nmnh_ggi                        130.00T   35.79T   94.21T  28%/15%    123T/130T   107M/114M /scratch/nmnh_ggi
gpfs02:nmnh_lab                         25.00T   10.69T   14.31T  43%/11%     23T/25T     19M/22M  /scratch/nmnh_lab
gpfs02:nmnh_mammals                     35.00T   20.82T   14.18T  60%/39%     33T/35T     52M/54M  /scratch/nmnh_mammals
gpfs02:nmnh_mdbc                        50.00T   39.56T   10.44T  80%/16%     47T/50T     40M/43M  /scratch/nmnh_mdbc
gpfs02:nmnh_ocean_dna                   40.00T   36.93T    3.07T  93%/3%      38T/40T     32M/34M  /scratch/nmnh_ocean_dna
gpfs02:nzp_ccg                          45.00T   32.42T   12.58T  73%/3%      42T/45T     36M/38M  /scratch/nzp_ccg
gpfs01:ocio_dpo                         10.00T    0.00G   10.00T   1%/1%      9T/10T      51M/52M  /scratch/ocio_dpo
gpfs01:ocio_ids                          5.00T    0.00G    5.00T   0%/1%      4T/5T       18M/21M  /scratch/ocio_ids
gpfs02:pool_kozakk                      28.00T   10.67T   17.33T  39%/1%      27T/28T     23M/24M  /scratch/pool_kozakk
gpfs02:pool_sao_access                  50.00T    4.79T   45.21T  10%/9%      49T/50T     41M/43M  /scratch/pool_sao_access
gpfs02:pool_sao_rtdc                    20.00T  908.33G   19.11T   5%/1%      19T/20T     19M/22M  /scratch/pool_sao_rtdc
gpfs02:sao_atmos                       350.00T  263.46T   86.54T  76%/10%    332T/350T   291M/307M /scratch/sao_atmos
gpfs02:sao_cga                          25.00T    9.44T   15.56T  38%/28%     23T/25T     19M/22M  /scratch/sao_cga
gpfs02:sao_tess                         50.00T   23.25T   26.75T  47%/83%     47T/50T    107M/109M /scratch/sao_tess
gpfs02:scbi_gis                         80.00T   37.04T   42.96T  47%/15%     76T/80T     65M/70M  /scratch/scbi_gis
gpfs02:nmnh_schultzt                    35.00T   19.52T   15.48T  56%/75%     33T/35T    104M/109M /scratch/schultzt
gpfs02:serc_cdelab                      15.00T   12.70T    2.30T  85%/19%     14T/15T     11M/12M  /scratch/serc_cdelab
gpfs02:stri_ap                          25.00T   18.96T    6.04T  76%/1%       4T/5T      10M/12M  /scratch/stri_ap
gpfs01:sao_sylvain                     145.00T   85.84T   59.16T  60%/59%   138T/145T     24M/235M /scratch/sylvain
gpfs02:usda_sel                         25.00T    5.47T   19.53T  22%/30%     23T/25T     19M/22M  /scratch/usda_sel
gpfs02:wrbu                             50.00T   39.35T   10.65T  79%/14%     47T/50T     40M/43M  /scratch/wrbu
nas1:/mnt/pool/public                  175.00T   94.03T   80.97T  54%/1%         -           -     /store/public
nas1:/mnt/pool/nmnh_bradys              39.74T   13.78T   25.96T  35%/1%         -           -     /store/bradys
nas2:/mnt/pool/n1p3/nmnh_ggi            90.00T   36.28T   53.72T  41%/1%         -           -     /store/nmnh_ggi
nas2:/mnt/pool/nmnh_lab                 40.00T   13.88T   26.12T  35%/1%         -           -     /store/nmnh_lab
nas2:/mnt/pool/nmnh_ocean_dna           40.00T    2.25T   37.75T   6%/1%         -           -     /store/nmnh_ocean_dna
nas1:/mnt/pool/nzp_ccg                 265.00T  109.76T  155.23T  42%/1%         -           -     /store/nzp_ccg
nas2:/mnt/pool/n1p2/ocio_dpo            50.00T  182.85G   49.82T   1%/1%         -           -     /store/ocio_dpo
nas2:/mnt/pool/n1p1/sao_atmos          750.00T  369.07T  380.93T  50%/1%         -           -     /store/sao_atmos
nas2:/mnt/pool/n1p2/nmnh_schultzt       80.00T   24.96T   55.04T  32%/1%         -           -     /store/schultzt
nas1:/mnt/pool/sao_sylvain              50.00T    9.42T   40.58T  19%/1%         -           -     /store/sylvain
nas1:/mnt/pool/wrbu                     80.00T   10.02T   69.98T  13%/1%         -           -     /store/wrbu
nas1:/mnt/pool/admin                    20.00T    7.99T   12.01T  40%/1%         -           -     /store/admin
```


## b. Command `dus-report`


You can compile the output of `du` into a more useful report with the `dus-report` tool. This tool will run `du` for you (can take a while) and parse its output to produce a more concise/useful report.


For example, to see the directories that hold the most stuff in `/scratch/sao/hpc`:


```
% dus-report /scratch/sao/hpc
 612.372 GB            /scratch/sao/hpc
                       capac.   20.000 TB (75% full), avail.    5.088 TB
 447.026 GB  73.00 %   /scratch/sao/hpc/rtdc
 308.076 GB  50.31 %   /scratch/sao/hpc/rtdc/v4.4.0
 138.950 GB  22.69 %   /scratch/sao/hpc/rtdc/vX
 137.051 GB  22.38 %   /scratch/sao/hpc/rtdc/vX/M100-test-oob-2
 120.198 GB  19.63 %   /scratch/sao/hpc/rtdc/v4.4.0/test2
 120.198 GB  19.63 %   /scratch/sao/hpc/rtdc/v4.4.0/test2-2-9
  83.229 GB  13.59 %   /scratch/sao/hpc/c7
  83.229 GB  13.59 %   /scratch/sao/hpc/c7/hpc
  65.280 GB  10.66 %   /scratch/sao/hpc/sw
  64.235 GB  10.49 %   /scratch/sao/hpc/rtdc/v4.4.0/test1
  49.594 GB   8.10 %   /scratch/sao/hpc/sw/intel-cluster-studio
  46.851 GB   7.65 %   /scratch/sao/hpc/rtdc/vX/M100-test-oob-2/X54.ms
  46.851 GB   7.65 %   /scratch/sao/hpc/rtdc/vX/M100-test-oob-2/X54.ms/SUBMSS
  43.047 GB   7.03 %   /scratch/sao/hpc/rtdc/vX/M100-test-oob-2/X220.ms
  43.047 GB   7.03 %   /scratch/sao/hpc/rtdc/vX/M100-test-oob-2/X220.ms/SUBMSS
  42.261 GB   6.90 %   /scratch/sao/hpc/c7/hpc/sw
  36.409 GB   5.95 %   /scratch/sao/hpc/c7/hpc/tests
  30.965 GB   5.06 %   /scratch/sao/hpc/c7/hpc/sw/intel-cluster-studio
  23.576 GB   3.85 %   /scratch/sao/hpc/rtdc/v4.4.0/test2/X54.ms
  23.576 GB   3.85 %   /scratch/sao/hpc/rtdc/v4.4.0/test2-2-9/X54.ms
  23.576 GB   3.85 %   /scratch/sao/hpc/rtdc/v4.4.0/test2/X54.ms/SUBMSS
  23.576 GB   3.85 %   /scratch/sao/hpc/rtdc/v4.4.0/test2-2-9/X54.ms/SUBMSS
  22.931 GB   3.74 %   /scratch/sao/hpc/rtdc/v4.4.0/test2/X220.ms
  22.931 GB   3.74 %   /scratch/sao/hpc/rtdc/v4.4.0/test2-2-9/X220.ms
report in /tmp/dus.scratch.sao.hpc.hpc
```


You can rerun `dus-report` with different options on the same intermediate file, like


`% dus-report -n 999 -pc 1 /tmp/dus.scratch.sao.hpc.hpc`


to get a different report, to see the list down to 1%. Use


`% dus-report -help`


to see how else you can use it.
