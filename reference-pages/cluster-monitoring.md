---
title: "Cluster Monitoring"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152302/Cluster+Monitoring"
date-modified: "2024-05-13"
author: "SGK/PBF"
categories: ["hydra7"]
---

1. [Cluster Status](cluster-monitoring.md)
2. [Compute Nodes Status](cluster-monitoring.md)
3. [Query the Cluster Configuration](cluster-monitoring.md)
4. [Cluster Status Web Page](cluster-monitoring.md)


# 1. Cluster Status


The command


`% qstat -g c`


returns the cluster status, in a tabular form, i.e.:


```
CLUSTER QUEUE                   CQLOAD   USED    RES  AVAIL  TOTAL aoACDS  cdsuE  
--------------------------------------------------------------------------------  
all.q                             -nan      0      0      0      0      0      0 
lTIO.sq                           0.00      0      0      8      8      0      0 
lTb2g.q                           0.27      0      0      2      2      0      0 
lTgpu.q                           0.00      0      0     64     64      0      0 
lThC.q                            0.38    634      0   4374   5008      0      0 
lThM.q                            0.37    390      0   4162   4552      0      0 
lThMuVM.tq                        0.28      0      0    384    384      0      0 
mTgpu.q                           0.00      0      0     64     64      0      0 
mThC.q                            0.38   1331      0   3677   5008      0      0 
mThM.q                            0.37     14      0   4538   4552      0      0 
qgpu.iq                           0.00      4      0     60     64      0      0 
qrsh.iq                           0.00     11      0     29     40      0      0 
sTgpu.q                           0.00      0      0     64     64      0      0 
sThC.q                            0.38      5      0   5003   5008      0      0 
sThM.q                            0.33      0      0   5032   5032      0      0 
uThC.q                            0.38      8      0   5000   5008      0      0 
uThM.q                            0.37     70      0   4482   4552      0      0 
uTxlM.rq                          0.00      0      0    480    480      0      0 
```


You can also use


`% qstat+ -gc`


(no space in `-gc) to get:`


```
   ---- queue ----  ----- #nodes ---- - ---------- #slots ----------- - ------------
    name       load  total avail  down - total used  resvd  down avail - %full  %eff

   sThC.q   1880.5     63    63     0 -  5008     5     0     0  5003 -   0.1
   mThC.q   1880.5     63    63     0 -  5008  1331     0     0  3677 -  26.6
   lThC.q   1880.5     63    63     0 -  5008   634     0     0  4374 -  12.7
   uThC.q   1880.5     63    63     0 -  5008     8     0     0  5000 -   0.2  95.1

   sThM.q   1662.8     55    55     0 -  5032     0     0     0  5032 -   0.0
   mThM.q   1662.5     52    52     0 -  4552    14     0     0  4538 -   0.3
   lThM.q   1662.5     52    52     0 -  4552   390     0     0  4162 -   8.6
   uThM.q   1662.5     52    52     0 -  4552    70     0     0  4482 -   1.5 350.7

   uTxlM.rq    0.2      3     3     0 -   480     0     0     0   480 -   0.0   0.0

   lTIO.sq     0.0      2     2     0 -     8     0     0     0     8 -   0.0   0.0

   sTgpu.q     0.0      1     1     0 -    64     0     0     0    64 -   0.0
   mTgpu.q     0.0      1     1     0 -    64     0     0     0    64 -   0.0
   lTgpu.q     0.0      1     1     0 -    64     0     0     0    64 -   0.0   0.0

   qgpu.iq     0.0      1     1     0 -    64     4     0     0    60 -   6.2
   qrsh.iq     0.1      2     2     0 -    40    11     0     0    29 -  27.5
```


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) the actual numeric values will be slightly different when you run these commands, since they reflect the precise configuration and the load.


# 2. Compute Nodes Status


The command


`% qhost`


returns the list of hosts (compute nodes) and their respective properties.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Under UGE, `qhost` alone returns more columns (equiv to `qhost -cb` under SGE). The option `-ncb` returns the same columns as in SGE.


You can restrict the list by specifying the hosts, like


`% qhost -h compute-64-02 compute-64-03`


but you can't use `RE`s. So you use a filter, like `egrep`, to parse its output:


`% qhost | egrep 'LOAD|e-[46]'`


This will print any line with either the string '`LOAD`' or a line that matches the `RE` `"e-[46]`", and will thus match `compute-4`, `compute-6`, etc....


The utility`egrep` combined with `RE`s (regular expressions) can be a very powerful filter.


The command `qhost` takes the "`-q`" or the "`-j`" option to show the queues or the jobs associated with each host(s):


| `qhost -q -h compute-64-02` | show which queues include the compute node 64-02 |
| --- | --- |
| `qhost -j -h compute-64-02` | show which jobs are running on the compute node 64-02 |


There is also a `qhost+` command, see the [Additional Tools page](additional-tools.md).


# 3. Query the Cluster Configuration


The command `qconf` is used to both set and query the queue configuration.


All the options of `qconf` that start with `-s` correspond to a query: i.e., show something.


The following options may be useful:


| `-sc` | show complex attributes |
| --- | --- |
| `-sconfl` | show a list of all local configurations |
| `-sconf [host_list]` | show configurations |
| `-shgrpl` | show host group list |
| `-shgrp group` | show host group |
| `-srqsl` | show resource quota set list |
| `-srqs [rqs_list]` | show resource quota set(s) |
| `-spl` | show all parallel environments |
| `-sp pe-name` | show a parallel environment |
| `-sql` | show a list of all queues |
| `-sq [queue_list]` | show the given queue |
| `-ssconf` | show scheduler configuration |
| `-sul` | show a list of all userset lists |
| `-su listname_list` | show the given userset list |


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Use the command


`% qconf -srqs`


to query the resource quota set, *i.e.* the limits on queues, or


`% qconf -srqs u_slots`


to query a specific quota.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Use the command


`% qconf -sq sThM.q`


to show the configuration of the `sThM.q` queue. Some of the options to the command `qconf` take `RE`s, so for example the command:


`% qconf -sq '?ThM.q' | egrep 'qname|s_cpu|s_rt'`


returns the soft CPU and R/T limits for all the hi-mem queues, using egrep to filter the output of `qconf`, namely:


```
qname                 lThM.q
s_rt                  1440:00:00
s_cpu                 720:00:00
qname                 mThM.q
s_rt                  144:00:00
s_cpu                 72:00:00
qname                 sThM.q
s_rt                  14:00:00
s_cpu                 7:00:00
qname                 uThM.q
s_rt                  INFINITY
s_cpu                 INFINITY
```


# 4. Cluster Status Web Page


We also maintain a cluster status web page that can be accessed  at https://hydra-7.si.edu/tools/status/ as long as you are on SINet or the SI VPN.

- You can specify up to 3 arguments to the URL, especially useful if you bookmark it, to specify either:
    1. the sorting in the cluster snapshot graph with `sortby=`, like in `sortby=nCPU`
    2. the length of the plots vs time with `len=`, like in `len=7d`
    3. which user's job(s) to highlight with `user=`, like in `user=hpc`
- by adding "`?``sortby=nCPU&user=hpc&len=15d`" to the URL; valid values for each parameter are those listed in the corresponding drop down menus.


These pages give you a good overview of the cluster current status and past usage, and include the disk space usage information.
