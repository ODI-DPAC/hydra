# Write a module file

A **module file** is a short text file that sets the environment for one package. Write one for software you installed yourself, such as a package built under your home directory or a Miniconda, so that one `module load` line puts it on your path in a session or a job, in either shell.

Module files are written in Tcl, and most need three or four lines. The first line must be `#%Module1.0`, and the rest set or extend environment variables. `man modulefile` lists every command.

## Write the file

1. Create a directory for your module files:

    ```bash
    mkdir -p ~/modulefiles
    ```

2. Write the file, named for the package. To put a Miniconda installation on the path:

    ```tcl title="~/modulefiles/miniconda"
    #%Module1.0
    prepend-path PATH /home/USERNAME/miniconda3/bin
    ```

    To add a library directory:

    ```tcl title="~/modulefiles/geos"
    #%Module1.0
    prepend-path LD_LIBRARY_PATH /home/USERNAME/geos/lib
    ```

    To set several variables from one base directory:

    ```tcl title="~/modulefiles/crunch"
    #%Module1.0
    set base /home/USERNAME/crunch
    prepend-path PATH $base/bin
    prepend-path LD_LIBRARY_PATH $base/lib
    setenv CRUNCH $base
    ```

    `set` makes a Tcl variable, used only inside the file. `setenv` exports a variable to the shell. `prepend-path` puts the directory first, `append-path` last. `remove-path`, `unsetenv`, `conflict` and `module load` are the other commands used in practice.

3. Load it by path and check the result:

    ```console
    $ module load ~/modulefiles/crunch
    $ echo $CRUNCH
    /home/USERNAME/crunch
    ```

## Load it by name

1. Tell the module command where your files are, once, with a `~/.modulerc` file:

    ```tcl title="~/.modulerc"
    #%Module1.0
    module use --append /home/USERNAME/modulefiles
    ```

2. Load by name from then on, in sessions and in job files:

    ```bash
    module load crunch
    ```

The system module files are under `/share/apps/modulefiles` and are the best examples of what a module file can do. `module show NAME` prints what any of them does.
