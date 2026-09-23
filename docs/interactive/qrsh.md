# Interactive sessions (qrsh)

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


if you need X11 capabilities, use `qlogin` instead of `qrsh` - although your ssh connection to Hydra via a login node must allow X-tunneling.


See also the description of the [Interactive Queue](../jobs/queues.md) under [Available Queues](../jobs/queues.md).


## Using a Jupyter lab Server and Notebook


- [Using a Jupyter Notebook on Hydra.](jupyter.md)


## Using RStudio


RStudio can be started or accessed in various ways:


- [Using Hydra's node(s)](rstudio.md)
- [Using the RStudio server](rstudio.md)


## Using VSCode


- [Using VSCode on Hydra](vscode.md)


These interactive tools do not work when accessing Hydra via [telework.si.edu](http://telework.si.edu), except for the VSCode tunnel.
