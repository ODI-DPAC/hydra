# Interactive Use

Interactive work runs on a compute node, not on a login node. You get there with `qrsh`, which gives you a shell on a node for up to 24 hours. Jupyter, VS Code and RStudio run on that node too, and an ssh tunnel shows them in a browser on your own machine. The [RStudio server](rstudio.md) is the exception: it is a dedicated node with its own web address and needs no tunnel.

!!! warning "Do not run interactive work on the login nodes"

    The login nodes slow and then kill processes that run on them for more than a few minutes, which ends a notebook or an editor session with it. Start a [session on a compute node](qrsh.md) first.

Read [Start an interactive session](qrsh.md) first: it covers `qrsh`, the per-user limits, and the tunnel the other pages use. Then [Jupyter](jupyter.md), [VS Code](vscode.md), the [RStudio server](rstudio.md) or [RStudio on a compute node](rstudio-node.md). Batch jobs are under [Running Jobs](../jobs/index.md).
