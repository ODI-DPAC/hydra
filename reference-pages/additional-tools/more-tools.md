---
title: "More Tools"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/374604004/More+Tools"
date-modified: "2025-12-03"
author: "SGK"
categories: ["hydra7"]
---

1. [Local Tools](more-tools.md)
2. [Local+ Tools](more-tools.md)
3. [Misc Tools](more-tools.md)
4. [Also Available](more-tools.md)


## 1. Local Tools


The following tools are always available since the module `tools/local-user` is *always*loaded:


| `check-qwait` | show job(s) waiting in the queue and associated queue quota limits |  |
| --- | --- | --- |
| `check-gpu-use` | show cluster GPUs usage |  |
| `finger` | replacement for CentOS7 `finger` | use `pinky -l` |
| `get-gpu-info` | print information about GPU |  |
| `monitor-code-usage` | helps you monitor your code usage |  |
| `plot-qmemuse` | plot memory and cpu usage as a function of time for a given jobID |  |
| `plot-qssduse` | plot SSD usage as a function of time for a given jobID |  |
| `qacct+` | a "better" `qacct` | show accounting information for completed jobs |
| `qchain` | chains a set of jobs by adding the -hold_jid <jobID> to qsub for you |  |
| `qquota+` | a "better" `qquota` | show queue quota wrt queue limits |
| `qstat+` | a "better" `qstat` | show queue status |
| `quota+` | a "better" quo`t`a | show disk quota information for all type (NFS, GPFS, NAS) |
| `q-wait` | wait until some jobs are not found in the queue |  |
| `rpstree+` | remote `pstree -paul` | show process tree on given compute node |
| `rtop+` | remote `top` | show what is running on given compute node |
| `ruptime` | replacement for `ruptime` | limited to head, login and NSDs |
| `rwho` | replacement for `rwho` | limited to head, login and NSDs |
| `show-qmemuse` | show memory use statistics |  |
| `show-qslots` | shows how many slots are available in the queue(s) |  |
| `show-qssduse` | log statistics for `plot-qssduse` |  |


The following tools are available when loading the module `tools/local-admin:`


| `chage+` | substitute to `chage`, to query LDAP properties | ie: chage+ $USER |
| --- | --- | --- |
| `check-disks-usage` | check disks usage, and print warning when usage exceed a threshold | ie: `check-disks-usage -w 10` |
| `check-hi-memuse` | check for memory use versus reservation and CPU usage efficiency |  |
| `check-memres` | check for jobs that use less memory than the amount reserved |  |
| `check-memuse` | print the cluster usage (memory and CPUs) |  |
| `check-qlogs` | return a report on either oversubscribed or inefficient jobs |  |
| `disk-usage` | return information on disk usage |  |
| `find-all-zombies` | find zombies |  |
| `get-cpu_arch` | return CPU architecture |  |
| `parse-disk-quota-reports` | return report by parsing the disk quota report |  |
| `plot-disk-dev` | plot usage of a given device |  |
| `plot-disk-usage` | plot the usage of a given disk (volume) |  |
| `plot-gpfs-info` | plot GPFS information |  |
| `plot-ibtraffic` | plot IB traffic |  |
| `plot-qsnapshot` | plot a snapshot of cluster usage |  |
| `plot-qssduse-summary` | plot SSD usage summary as a function of time |  |
| `plot-qstat` | plot the queue status of the cluster |  |
| `plot-ruptime` | plot the load (output of `ruptime`) of the non-compute nodes |  |
| `qhost+` | a "better" qhost |  |
| `rkill` | remote `kill` |  |
| `rkillall` | remote `killall` |  |


Each tool has a man page, accessible after you load the module `tools/local`.


## 2. Local+ Tools


The following tools are available when loading the module `tools/local+`;


<table class="wrapped fixed-width confluenceTable" style="width: 82.4688%;"><colgroup><col style="width: 18.5678%;"/><col style="width: 38.1715%;"/><col style="width: 43.2607%;"/></colgroup><tbody><tr><td class="highlight-yellow confluenceTd" data-highlight-colour="yellow"><p><span style="color:var(--ds-text-accent-blue,#0055cc);"><code>backup</code></span></p></td><td class="confluenceTd"><p>backup a file</p></td><td class="confluenceTd" colspan="1">ie: <span style="color:var(--ds-text-accent-blue,#0055cc);"><code>mv </code><span style="color:var(--ds-text,#172b4d);">or</span></span><code><span style="color:var(--ds-text-accent-blue,#0055cc);"> cp file</span> to <span style="color:var(--ds-text-accent-blue,#0055cc);">file.&lt;n&gt;</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">centos-version</span></code></td><td class="confluenceTd" colspan="1">print the OS flavor &amp; version</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">check-hosts</span></code></td><td class="confluenceTd" colspan="1">print the cluster usage (memory and CPUs), as aggregate by logical rack</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">check-qacct</span></code></td><td class="confluenceTd" colspan="1">show statistics of resources usage for completed jobs</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">dus-report</span></code></td><td class="confluenceTd" colspan="1">run and parse <code><span style="color:var(--ds-text-accent-blue,#0055cc);">du</span></code> to produce a disk usage report</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">elapsed</span></code></td><td class="confluenceTd" colspan="1">print elapsed time between each call</td><td class="confluenceTd" colspan="1">ie; <code><span style="color:var(--ds-text-accent-blue,#0055cc);">elapsed; ...do something...; elapsed</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">fixFmt</span></code></td><td class="confluenceTd" colspan="1"><p>format a number with fixed number of digits</p></td><td class="confluenceTd" colspan="1"><p><code><span style="color:var(--ds-text,#172b4d);">csh:</span><span style="color:var(--ds-text-accent-blue,#0055cc);">    \@ n = 1; set N = `fixFmt 3 $n`</span></code></p><p><code><span style="color:var(--ds-text-accent-blue,#0055cc);"><span style="color:var(--ds-text,#172b4d);">[ba]sh:</span> n=1; N=`fixFmt 3 $n`</span></code></p><p><code><span style="color:var(--ds-text-accent-blue,#0055cc);">        echo n=$n N=$N → n=1 N=001</span></code></p></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">get-jobhr</span></code></td><td class="confluenceTd" colspan="1">tool to retrieve a job hard resources (<code>mem_res h_data h_vmem</code>) in a job script</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">lsth</span></code></td><td class="confluenceTd" colspan="1"><p>show most recent files</p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">lsth <span>[-40]</span> <span>[&lt;spec&gt;</span>]</span> </code>→ <code><span style="color:var(--ds-text-accent-blue,#0055cc);">ls -lt &lt;spec&gt; | head -40</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">lswc</span></code></td><td class="confluenceTd" colspan="1"><p>count number of files in directories</p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">lswc dir/</span></code> → <code><span style="color:var(--ds-text-accent-blue,#0055cc);">ls dir/ | wc -l</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">noX</span></code></td><td class="confluenceTd" colspan="1">tool to unset <code>DISPLAY</code> (saved in <code>XDISPLAY</code>)</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">p-wait</span></code></td><td class="confluenceTd" colspan="1"><p>wait until given PID has completed</p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">p-wait <span>[check-time</span>] &lt;PID&gt;</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">pawk</span></code></td><td class="confluenceTd" colspan="1"><p>print with <code><span style="color:var(--ds-text-accent-blue,#0055cc);">awk</span></code><span class="error"><br/></span></p></td><td class="confluenceTd" colspan="1">ie: <code><span style="color:var(--ds-text-accent-blue,#0055cc);">pawk 1,hello,3</span></code> → <code><span style="color:var(--ds-text-accent-blue,#0055cc);">awk '<span class="error">{print $1,"hello",$3}</span>'</span></code></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">print-proc-memory</span></code></td><td class="confluenceTd" colspan="1">print nicely content of <code><span style="color:var(--ds-text-accent-blue,#0055cc);">/proc/memory</span></code></td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">procinfo</span></code></td><td class="confluenceTd" colspan="1">print properties of local machine (#CPUs, memory, OS)</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">procinfo+</span></code></td><td class="confluenceTd" colspan="1">print properties of local machine (#CPUs, memory, OS, etc...)</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">tails</span></code></td><td class="confluenceTd" colspan="1"><p>run tail <span>[options</span>] on a set of files</p></td><td class="confluenceTd" colspan="1">ie: "<code><span style="color:var(--ds-text-accent-blue,#0055cc);">tail -3 *pl</span></code>" fails "<code><span style="color:var(--ds-text-accent-blue,#0055cc);">tails -3 *pl</span></code>" OK</td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">total</span></code></td><td class="confluenceTd" colspan="1">compute the total of values at given column of a file</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">useX</span></code></td><td class="confluenceTd" colspan="1">tool to reset <code>DISPLAY</code> (from <code>XDISPLAY</code>), revert effect of noX</td><td class="confluenceTd" colspan="1"><br/></td></tr><tr><td class="highlight-yellow confluenceTd" colspan="1" data-highlight-colour="yellow" title="Background colour : Yellow"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">xterm-config</span></code></td><td class="confluenceTd" colspan="1">tool to configure <code>xterm</code> window properties</td><td class="confluenceTd" colspan="1"><br/></td></tr></tbody></table>


Each tool has a man page, accessible after you load the module `tools/local+`.


## 3. Misc Tools


- A set of tools are available by loading the `tools/misc` module.
- Currently these are disk usage analysis tools, namely:


| `dua` | a tool to learn about disk usage |
| --- | --- |
| `dus+` | disk usage report (same as `dus-report`in `tools/local+`) |
| `dut` | disk usage calculator |
| `gdu` | disk usage analyzer written in Go |
| `ncdu` | ncurses disk usage |


## 4. Also Available


- The following tools are also available:


| module | command | description |
| --- | --- | --- |
| `tools/awscli` | aws, aws_completer | CLI to access AWS |
| `tools/cmake` | cmake |  |
| `tools/ffsend` | ffsend, ffupload, ffdownload |  |
| `tools/gv` | gv |  |
| `tools/rclone` | rclone |  |
| `tools/ruby` | ruby |  |
| `tools/svn` | svn |  |
| `tools/vscode` | vscode |  |
| `tools/wget` | wget |  |
| `tools/xv` | xv |  |


- use:


`module whatis <modulename>`to list the versions available,


`module help <modulename>` to get help
