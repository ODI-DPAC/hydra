# Find and load software

This page covers finding a package among the installed modules, loading it in a session or a job, and switching versions. A module file sets the environment (`PATH`, `MANPATH`, `LD_LIBRARY_PATH` and any variables the package needs) for one package and version, and works the same under `bash` and `csh`. Modules for the packages the cluster provides are maintained by the HPC team; [Write a module file](custom-modules.md) covers your own.

Modules are grouped by prefix: `bio/` for bioinformatics packages (`bioinformatics/` is an alias), `tools/` for general tools and languages, `gcc/`, `intel/` and `nvidia/` for the compilers and their MPI builds, `idl/` and `matlab/` for those runtimes, `gis/` and `jupyter/` for a few more. The [list of module files](https://hydra.si.edu/tools/QSubGen/module-avail.html) is the complete inventory; the [installed modules](module-list.md) page lists the `bio/` and `tools/` prefixes.

## Find a package

1. Search the module names:

    ```console
    $ module -t avail 2>&1 | grep -i samtools
    bio/samtools/1.19.2(default)
    ```

    `module -t avail` prints one module per line; `2>&1` is needed because it writes to standard error. Without a pattern, `module avail` prints everything.

2. Read what the module provides and how to run it:

    ```console
    $ module whatis bio/samtools
    $ module help bio/samtools
    ```

    `module help` prints the executables the package installs and notes on running it on Hydra. `module show bio/samtools` prints what loading it changes in your environment.

## Load a package

1. Load the module, with a version or without. Without a version you get the one marked `(default)`:

    ```console
    $ module load bio/samtools
    $ module load bio/samtools/1.19.2
    ```

2. Check what is loaded:

    ```console
    $ ml
    Currently Loaded Modulefiles:
     1) uge/8.8.1   2) tools/local-user   3) bio/samtools/1.19.2
    ```

    `uge/8.8.1` and `tools/local-user` are sticky: every session loads them and they cannot be unloaded.

3. In a job file, put the same `module load` lines before the commands that use the package. Do not rely on modules loaded in your login shell; the job does not inherit them (see [Do not use `-V`](../jobs/job-scripts.md#do-not-use-v)).

`ml` is a shortcut: `ml` alone is `module list`, `ml bio/samtools` loads, `ml -bio/samtools` unloads.

## Switch or unload

Two versions of one package cannot be loaded at once; the module command reports a conflict. Switch versions instead of loading a second one, or unload first:

```console
$ module switch gcc/12.2.0 gcc/13.2.0
$ module unload gcc/13.2.0
$ module load nvidia/24.3
```

`module purge` unloads everything except the sticky modules.

## Change how module reports

| Module | Effect |
|---|---|
| `module-nocolor` | no colors |
| `module-nowarn` | fewer warnings |
| `module-simple-format` | shorter `module list` output |
| `module-simple` | the three above |
| `module-verbose` | the same as `module -v` |

Load or unload these like any other module. `tools/manpath` restores the default `man` page locations if loading a module has hidden them.

The module command can also be called from Perl, Python and CMake scripts; `man module` describes how. The Modules documentation at <https://modules.readthedocs.io/en/v5.3.1/> covers the version installed on Hydra.
