# Start an interactive session

`qrsh` gives you a shell on a compute node, scheduled like a job into the interactive queue `qrsh.iq`. Use it for anything that runs longer than a few minutes and needs a terminal: compiling, testing a job before submitting it, `conda install`, a notebook or editor served to your browser.

## Start a session

1. On a login node, request a session. With no options you get one CPU and 8 GB:

    ```console
    $ qrsh
    ```

    For several CPUs on one node, or more memory, request slots; memory limits multiply with the slot count:

    ```console
    $ qrsh -pe mthread 4
    ```

    For a GPU, request one in the interactive GPU queue (see [GPUs](../software/gpus.md)):

    ```console
    $ qrsh -l gpu,ngpus=1
    ```

2. Wait for the prompt to change from the login node to a compute node:

    ```text
    [USERNAME@compute-64-15 ~]$
    ```

    The session starts in your home directory; `cd` to your working directory under `/scratch`.

3. Work as on a login node: load modules, run programs, edit files.

4. End the session with `exit`. A session also ends when it reaches its time limit.

For a program that opens X11 windows, use `qlogin` in place of `qrsh` and connect to the login node with X forwarding (`ssh -Y`). `qlogin` takes the same options.

## Limits

| Limit | Value |
|---|---|
| CPU time per session | 12 h per slot |
| Elapsed time per session | 24 h |
| Memory per slot | 8 GB resident, 64 GB virtual |
| Sessions per user at once | 12 |
| Slots per user across sessions | 64 |
| GPU sessions per user | 1, with 1 GPU |

The scheduler kills a session that reaches a limit, with whatever it was running. Save work in files as you go, and run anything longer than a day as a [job](../jobs/submit.md).

## Reach a service on the node from your browser

Jupyter, VS Code and RStudio run on the compute node and listen on a port there. The compute nodes are not reachable from outside the cluster, so you open an ssh tunnel from your own machine through a login node to that port, then point a browser at the local end. The tools' start scripts print the exact command; its shape is always:

```console
$ ssh -N -L PORT:compute-XX-XX:PORT USERNAME@hydra-login01.si.edu
```

`-N` opens no shell, `-L` forwards local `PORT` to `PORT` on the node. The command asks for your Hydra password and then prints nothing while the tunnel is open. Leave that terminal alone. Use the login node you connected to (`hydra-login01` or `hydra-login02`); the first `PORT` can be any free port on your machine if the same number is in use locally. To close the tunnel, press `Ctrl-C` in that terminal.

!!! warning "The tunnel does not work from telework.si.edu"

    A tunnel runs from your own machine, and the telework web terminal cannot start one. From telework, use the [RStudio server](rstudio.md) or a [VS Code tunnel](vscode.md#use-a-vs-code-tunnel) instead; neither needs an ssh tunnel.
