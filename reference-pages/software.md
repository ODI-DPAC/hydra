---
title: "Software"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152327/Software"
date-modified: "2024-05-15"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](software.md)
    1. [Unix Basic Configuration](software.md)
    2. [Module](software.md)
    3. [EMail forwarding](software.md)
    4. [The plan/project files](software.md)
2. [The "module" Command](software/the-module-command.md)
    1. Introduction
    2. Available Module Files
    3. How to Write your Own Modules Files
3. [Compilers & Libraries](software/compilers-libraries-and-mpi-or-multi-threaded-programs.md)
    1. How to build and run MPI programs
    2. How to build and run multi-threaded programs
4. [Packages and Tools](software/packages-and-tools.md)
    1. [IDL & FL](software/packages-and-tools/idl-gdl-fl.md)
    2. [Java](software/packages-and-tools/java.md)
    3. [Julia](software/packages-and-tools/julia.md)
    4. [Matlab](software/packages-and-tools/matlab.md)
    5. [Python](software/packages-and-tools/python.md)
    6. [R (old)](https://confluence.si.edu/pages/viewpage.action?pageId=163152339)
    7. [Conda: Anaconda & Miniconda](software/packages-and-tools/conda-anaconda-miniconda.md)
5. [Genomics Software](software/genomics-software.md)
    1. [BLAST](software/genomics-software/blast.md)
    2. [BLAST2GO](software/genomics-software/blast2go.md)


# 1. Introduction


Hydra is a Linux cluster running Rocky 8.9, while the software installation is managed using Bright Cluster management (BCM or CM).


Like any Linux machine, your Un*x environment on Hydra can be configured to your liking.


How to configure a Un*x environment is beyond the scope of this set of documentation.


### Unix Basic Configuration


A set of configuration files, located in your home directory, sets up your Un*x environment - a default set of such files is provided when a new account is created:


<table class="wrapped confluenceTable"><colgroup><col/><col/><col/><col/></colgroup><tbody><tr><th class="confluenceTh" colspan="3" style="text-align: center;">Login shell</th><th class="confluenceTh" colspan="1"><br/></th></tr><tr><th class="confluenceTh">Bash shell (<code><span style="color:var(--ds-text-accent-blue,#0055cc);">bash</span></code>)</th><th class="confluenceTh">Bourne shell (<code><span style="color:var(--ds-text-accent-blue,#0055cc);">sh</span></code>)</th><th class="confluenceTh">C-shell (<code><span style="color:var(--ds-text-accent-blue,#0055cc);">csh</span></code> or <code><span style="color:var(--ds-text-accent-blue,#0055cc);">tcsh</span></code>)</th><th class="confluenceTh">Action</th></tr><tr><td class="confluenceTd"><code>.bash_profile</code></td><td class="confluenceTd"><code>.profile</code></td><td class="confluenceTd"><code>.cshrc</code></td><td class="confluenceTd">read &amp; executed at startup to configure your environment</td></tr><tr><td class="confluenceTd"><code>.login</code></td><td class="confluenceTd"><code>.login</code></td><td class="confluenceTd"><code>.login</code></td><td class="confluenceTd">read &amp; executed at startup, next, but only by a login shell</td></tr><tr><td class="confluenceTd"><code>.emacs</code></td><td class="confluenceTd"><code>.emacs</code></td><td class="confluenceTd"><code>.emacs</code></td><td class="confluenceTd">configures the <code>emacs</code> editor</td></tr><tr><td class="confluenceTd"><code>.bash_logout</code></td><td class="confluenceTd"><code>.logout</code></td><td class="confluenceTd"><code>.logout</code></td><td class="confluenceTd"><p>read &amp; executed when logging out (login shell)</p></td></tr></tbody></table>


::: {.note title="Note"}
`qsub`'ed job scripts are not started as a login shell, hence unless you fully understand the idiosyncrasies of the bash shell startup rules,


it is recommended that you use the Bourne shell (`sh`) or the C-shell (`csh`), and not the bash shell (`bash`) when submitting jobs.
:::


### Module


The command `module` is available on Hydra:


- Instead of editing your `.bash_profile` file (or `.profile` or `.cshrc`) to configure your `PATH` (and `MANPATH` and `LD_LIBRARY_PATH`, etc), use the command `module` (as explained below).


### EMail Forwarding


- Email sent on the cluster is delivered to the head node (that you should not use),
- To access these emails (like job notifications), a `~/.forward` file was created with your "canonical/home" email address, i.e.:


`% echo DoeJ@si.edu > ~/.forward`


- While you are welcome to edit this file and change the forwarding email:
    - do not delete it, and
    - use an email address you will read.
- Note that by SD931, we must communicate with users via their work email, not their private one
- You "on file" email (used for things like password reset and HPCC-L listserv) will remain you "canonical/home" email (the one that ends in `.edu` )


### The plan/project files


- the content of the files `~/.plan` and `~/.project` are displayed by the command `pinky` (`man pinky`);
    - feel free to put relevant/pertinent information in them.
- The command finger is no longer available under Rocky 8:
    - the `tools/local-user`module offers a `finger` replacement.
- Try 
 `% pinky -l hpc`


or


`% finger hpc`
