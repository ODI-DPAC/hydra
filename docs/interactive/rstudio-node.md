# RStudio on a compute node

RStudio can also run on a compute node of your choosing, with the CPUs and memory of an [interactive session](qrsh.md), served to your browser through an ssh tunnel. Use it when the [RStudio server](rstudio.md) does not fit, which means a different R, more than one session, or CPUs and memory scheduled to you alone.

## Start RStudio in a session

1. On a login node, start an interactive session and load the module:

    ```console
    $ qrsh -pe mthread 4
    $ module load tools/R/RStudio/server
    ```

2. The first time only, create the server's configuration file:

    ```console
    $ init-rstudio-server
    init-rstudio-server: db.conf file created:
    -rw-rw-r--. 1 USERNAME USERNAME 433 Oct  3 16:24 /home/USERNAME/.local/share/rstudio/rstudio-server/db.conf
    ```

    Without it the server does not start, and says `db.conf not found, you need to run init-rstudio-server first`.

3. Start the server:

    ```console
    $ start-rstudio-server -port 8123
    start-rstudio-server: starting RStudio server on host=compute-64-11 and port=8123
      you need to create a ssh tunnel on your local machine with
        ssh -N -L 8123:compute-64-11:8123 USERNAME@hydra-login01.si.edu

    Point your browser to http://localhost:8123 on your local machine.
    Use Control+C in this window to kill the server when done.
    ```

    `-port` chooses the port, and the default is 8787. `Address already in use` means another user has that port on the node. Choose another, between 1025 and 65535. `start-rstudio-server -help` lists the options.

4. On your own machine, open the tunnel the script printed, in a terminal you leave alone:

    ```console
    $ ssh -N -L 8123:compute-64-11:8123 USERNAME@hydra-login01.si.edu
    ```

5. Open `http://localhost:8123` in a browser and sign in with your Hydra username and password.

6. When done, sign out in the browser, `Ctrl-C` in the server's window, `Ctrl-C` in the tunnel's terminal, then `exit` the session. Do not leave a server running unattended.

The module loads R 4.4.1 (`tools/R/4.4.1`). `module load tools/R` gives 4.4.0. If a sign-out leaves you unable to sign back in, stop and restart the server. If that fails, clear the browser's cookies.

## RStudio desktop over X11

`tools/R/RStudio/desktop` provides the windowed RStudio, drawn on your machine through X11. It needs an X server on your machine and an `ssh -Y` connection, is slow, and does not work with Xming on Windows (Cygwin/X and WSL work). Start it from a `qlogin` session with `rstudio --no-sandbox --disable-gpu`.
