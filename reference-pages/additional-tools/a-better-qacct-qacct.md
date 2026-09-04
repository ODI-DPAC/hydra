---
title: "A Better Qacct: qacct+"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/374604065/A+Better+Qacct+qacct"
date-modified: "2025-10-23"
author: "SGK"
categories: ["hydra7"]
---

- The accounting information is ingested into a SQL compatible data base by the GridEngine (aka ARCo - for Accounting and Reporting Console)
    - The ingestion is done at regular intervals, hence the database is not instantaneously synchronized (less than a minute lag usually).
    - As of Hydra-7, we use GE's dbwriter (aka ARCo) and PostgreSQL as the DB engine
        - although we discovered some bugs under 8.8.1, where some fields are not properly ingested.
- That database can be queried with `qacct+`, hence
    - `qacct+` is often faster than `qacct`
    - `qacct+` its output can be customized, and
    - `qacct+` computes derived values.
- How to use `qacct+` is explained in the man page (`man qacct+`) and is described by:


`% qacct+ -help` 
or 
`% qacct+ -show help`


Namely:


```{.text title="qacct+ -help"}
usage: qacct+ [options] where options are

                   to limit query to
  -j|--job_number  <jobid>    given job  ID(s),    single value, comma separated list, or range like in n:m
  -t|--task_number <taskid>   given task ID(s),    single value, comma separated list, or range like in n:m
  -o|--owner       <owner>    given owner,         exact match

  -b|--back        <number>   jobs submitted  >= (now - n) days,  (def. 92 days ago)
  -s|--since       <date>     jobs submitted  >= date,   like "4/27/2016 10:00AM"
  -u|--until       <date>     jobs submitted  <= date,   like "4/27/2016 11:00AM"

                   to specify what to show
  -show            <string>                                       (def.: -show simple)
                   where <string> can be:
                     "simple", "simple+", "tab", "tab+", "gpu", "gpu+" or "raw",
                   or "fields", "explain", or "help", or a custom specification

                   to limit output to
  -m|--show_max    <number>   max number of entries to show (when querying more than one job)

  -w|--col_width   <number>   width of columns in tabular mode   (def.: 15)
  -d|--date_format <number>   how to format dates, n=-1,0,1 for YYYY/MM/DD, Mon DD YYY, MM/DD/YYYY, (def. 0)

  -n|--dry_run                dry run, use w/ -v to check the resulting SQL search
  -v[=value]                  verbose mode (repeat to increase verbosity, -v=2 equiv to -v -v)
  -i|--init         <file>    mysql initialization file(s),      (def.: /share/apps/tools/local-user/.qacct+.cnf, /home/hpc/.my.cnf)

  -h|--help                   show this help
  use -show help to get additional help on how to use -show <string>

  Ver. 5.3/1 (Oct 2025/SGK)
```


- and by


`% qacct+ -show help`


```{.text title="qacct+ -show help"}
  -show  <string> specify what to show

  i.e.
    -show simple  for simple format (default)
    -show simple+ for extension of the simple format
    -show tab     for tabular format
    -show tab+    for extension of the tabular format
    -show gpu     for GPU format
    -show gpu+    for extension of the GPU format
    -show raw     for raw format

  or a list of which keyword to show, with an optional format, where <string> is either
    +field1[=format1][,field2[=format2]]  for keyed format
  or
    %field1[=format1][,field2[=format2]]  for tabular format

  the format is either a C format specification like %d, %s, %.1f, or
  the values @DATE, @MEM, or @AGE to convert the numeric to a date, a memory (or volume) or an age,
  or @GPUSE or @GPUSE(var1|var2|...) to format the gpu_usage value,
     where varX is/are used to match a specific gpu_usage parameter

  for instance:
    -show +qname,slots,wallclock=@AGE,cpu=%.1f
  or
    -show %qname,slots,wallclock,cpu=%-15.1f,granted_pe
  or
    -show '+cpu,gpus,gpu_usage=@GPUSE(process|Util|therm|board)'

  use -show fields           to list all the available fields
  use -show explain_failed   to list the failed codes explanations
```
