---
title: "Interactive Use"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/276398281/Interactive+Use"
date-modified: "2026-02-26"
author: "SGK"
categories: ["hydra7"]
---

## Introduction


- You can use Hydra for interactive use.
    - We ask users not to run long programs or analysis on either of the login nodes,
    - instead use the interactive queue to start an interactive session on a compute node,
    - processes running on a login node for a long time and consuming resources get slowed down and eventually killed.


- You start an interactive session with the command


`qrsh`


If you plan to use more than one thread, or will need more memory than the per slot limit, you can request more than one slot with


`qrsh -pe mthread N`


where N is the number of slots (CPUs, cores) or memory limit multiplier you need.


- If you add `-l gpu` , you will get an interactive session on a compute node that has a GPU.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) if you need X11 capabilities, use `qlogin` instead of `qrsh` - although your ssh connection to Hydra via a login node must allow X-tunneling.


See also the description of the [Interactive Queue](https://confluence.si.edu/display/HPC/Available+Queues#AvailableQueues-InteractiveQueue) under [Available Queues](https://confluence.si.edu/display/HPC/Available+Queues).


## Using a Jupyter lab Server and Notebook


- [Using a Jupyter Notebook on Hydra.](interactive-use/using-a-jupyter-notebook-on-hydra.md)


## Using RStudio


RStudio can be started or accessed in various ways:


- [Using Hydra's node(s)](https://confluence.si.edu/display/HPC/Using+the+RStudio+Server)
- [Using the RStudio server](https://confluence.si.edu/display/HPC/Using+the+RStudio+Server)


## Using VSCode


- [Using VSCode on Hydra](interactive-use/using-vscode-on-hydra.md)


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) These interactive tools do not work when accessing Hydra via [telework.si.edu](http://telework.si.edu), except for the VSCode tunnel.
