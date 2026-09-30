# Monitoring tools

`qstat`, `qdel`, `qalter`, `qacct`, `qhost` and `qconf` are Grid Engine commands. `qstat+`, `qacct+` and the other tools on this page are Hydra's own, in the `tools/local-user` module, which every session loads. When you need an option or want to know what a field in the output means, look it up here. If you want to see the commands used in order, see [Monitor and manage jobs](monitoring.md).

## qstat

| Command | Shows |
|---|---|
| `qstat` | your jobs |
| `qstat -u '*'` | everyone's jobs |
| `qstat -s r`, `-s p` | only running, only pending jobs |
| `qstat -r` | requested resources and full job names |
| `qstat -s r -g t` | one line per slot of a parallel job, with the master and the nodes |
| `qstat -g d` | one line per task of a job array |
| `qstat -g c` | slots used, reserved and free in every queue |
| `qstat -j JOBID` | everything about one job, with why it is waiting |
| `qstat -explain E -j JOBID` | why a job is in error state |
| `qstat -F cpu_arch -q sThC.q` | a resource's value on every node of a queue |

## Job states

| State | Meaning |
|---|---|
| `qw` | waiting for resources, or held by a [resource limit](limits.md) |
| `hqw` | held by `-hold_jid` until another job finishes |
| `r` | running |
| `t` | being transferred to a node; about to start |
| `d` | being deleted |
| `Eqw` | in error, waiting; the job will not run |

## qstat+

`qstat+` (also `q+`) reformats `qstat` output, adding age, CPU efficiency, memory and I/O of running jobs, the node list of a parallel job, and cluster summaries. `qstat+ -help` lists the modes, `qstat+ -examples` shows examples, `man qstat+` has the details. Add `-u USERNAME` or `-u all` for other users' jobs.

| Command | Shows |
|---|---|
| `qstat+ +a` | all your jobs |
| `qstat+ +a%` | all your jobs with age and CPU use as a percentage of age |
| `qstat+ +r%` | running jobs with age and CPU efficiency |
| `qstat+ +rr%` | running jobs with efficiency, memory and I/O |
| `qstat+ +q` | queued jobs |
| `qstat+ -j JOBID` | a filtered `qstat -j` |
| `qstat+ -nlist JOBID` | the nodes a parallel job runs on |
| `qstat+ -ineff` | jobs using less than 33% of their requested CPUs after 1 hour |
| `qstat+ -osub` | jobs using more than 133% of their requested CPUs after 1 hour |
| `qstat+ -ores` | jobs that reserved more than 2.5 times the memory they use after 1 hour |
| `qstat+ -gc` | the state of every queue with node counts |
| `qstat+ -es` | empty slots |
| `qstat+ -down` | nodes that are down |

`cpu%` is CPU time divided by age and by the number of slots, so 100% means every requested slot is busy.

## qacct fields

`qacct -j JOBID` prints the accounting record of a finished job, and `-t TASKID` selects one array task. `qacct -d DAYS -o USERNAME [-j]` covers a user's jobs over DAYS days.

| Field | Meaning |
|---|---|
| `qname` | queue the job ran in |
| `hostname` | node, or master node of a parallel job |
| `taskid` | task ID of an array task |
| `qsub_time`, `start_time`, `end_time` | when the job was submitted, started, ended |
| `granted_pe`, `slots` | parallel environment and slots allocated |
| `failed` | `1` when the scheduler killed the job, for exceeding a memory or time limit |
| `exit_status` | exit status of the job script; `0` when it completed |
| `ru_wallclock` | elapsed time, seconds |
| `ru_utime`, `ru_stime` | user and system CPU time reported by the OS, seconds |
| `cpu` | CPU time as measured by the scheduler, seconds |
| `mem` | memory multiplied by time, GB·s; `mem/cpu` is the mean memory use in GB |
| `io` | a measure of the I/O the job performed |
| `maxvmem` | peak memory used |

## qacct+

A loader copies the accounting data into a PostgreSQL database within about a minute of each job finishing. `qacct+` queries the database, with selectable fields and derived values. Some fields are not loaded correctly from the Grid Engine 8.8.1 records. When a value looks wrong, compare it with `qacct -j JOBID`. `qacct+ -help` and `qacct+ -show help` list the options; `man qacct+` has the details.

| Command | Shows |
|---|---|
| `qacct+ -j JOBID` | one job |
| `qacct+ -j 8683280:8683290` | a range of job IDs |
| `qacct+ -o $USER -b 7` | your jobs submitted in the last 7 days |
| `qacct+ -o $USER -s "4/27/2026 10:00AM" -u "4/27/2026 11:00AM"` | your jobs submitted in a time window |
| `qacct+ -j JOBID -show tab+` | tabular output with more fields |
| `qacct+ -j JOBID -show +qname,slots,wallclock=@AGE,cpu=%.1f` | chosen fields with formats |
| `qacct+ -show fields` | every field available |
| `qacct+ -show explain_failed` | meanings of the `failed` codes |

The built-in formats are `simple`, `simple+`, `tab`, `tab+`, `gpu`, `gpu+`, `raw`. A custom `-show` takes `+field,...` for keyed output or `%field,...` for tabular, each field with an optional C format or an `@DATE`, `@MEM` or `@AGE` converter.

## qhost and qconf

| Command | Shows |
|---|---|
| `qhost` | every node: CPUs, load, memory |
| `qhost -h NODE ...` | named nodes |
| `qhost -q -h NODE` | the queues that include a node |
| `qhost -j -h NODE` | the jobs on a node |
| `qhost -ncb` | the classic column layout |
| `qconf -sql`, `qconf -sq QUEUE` | queue names; one queue's configuration |
| `qconf -spl`, `qconf -sp PE` | parallel environments; one PE |
| `qconf -shgrpl`, `qconf -shgrp @GROUP` | host groups; one group's nodes |
| `qconf -srqs [NAME]` | resource quotas |
| `qconf -sconf global \| grep max` | cluster-wide job limits |

`qhost` takes no patterns; filter with `egrep`.

## Hydra tools

Every session loads `tools/local-user`. `tools/local` adds `tools/local-admin`; `tools/local+` and `tools/misc` add more. Every tool has a man page; `module help tools/local-user` lists them.

| Tool | Module | Purpose |
|---|---|---|
| `qstat+`, `q+` | local-user | `qstat` with efficiency, memory and cluster summaries |
| `qacct+` | local-user | accounting from the database |
| `qquota+` | local-user | queue quotas against their limits, with `+%` for percentages |
| `quota+` | local-user | disk quotas on every filesystem; see [Quotas](../storage/quotas.md) |
| `check-qwait` | local-user | waiting jobs and the quota holding each |
| `check-gpu-use`, `get-gpu-info` | local-user | GPU use across the cluster; GPUs on the current node |
| `qchain` | local | submit jobs that run in sequence |
| `q-wait` | local | pause until jobs leave the queue |
| `plot-qmemuse`, `show-qmemuse` | local-user | memory and CPU of a high-memory job over time |
| `plot-qssduse`, `show-qssduse` | local-user | local SSD use of a job over time |
| `rtop+`, `rpstree+` | local-user | `top` and `pstree` on a compute node |
| `show-qslots` | local-user | free slots per queue |
| `monitor-code-usage` | local-user | how much a code of yours runs |
| `rwho`, `ruptime` | local-user | users and load on the head, login and storage nodes |
| `qhost+` | local-admin | `qhost` with more columns |
| `check-memres` | local-admin | memory reserved against memory used |
| `check-qlogs` | local-admin | the reports behind the [warning emails](efficiency.md) |
| `check-memuse`, `check-hi-memuse` | local-admin | cluster memory and CPU use |
| `get-cpu_arch` | local-admin | the current node's CPU architecture |
| `elapsed`, `lsth`, `lswc`, `tails`, `total`, `fixFmt`, `p-wait`, `procinfo`, `get-jobhr`, `noX`, `useX`, `dus-report`, `check-qacct` | local+ | shell utilities |
| `dua`, `dut`, `gdu`, `ncdu`, `dus+` | misc | disk-usage tools |
