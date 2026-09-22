# Writing your own module file

## Rationale


- The purpose of a module file is to simplify how to configure/modify your Unix environment to run or have access to some specific set of tools/applications/etc....
- A module file also allows users to change their configuration without worrying what shell is being used (bash or csh),
- Module files to access general purpose or supported tools/applications are written and maintained by the HPC support team.


This being said:


- Users can create their own module file(s) to facilitate the use of software they have installed themselves (like in their own directories) or to simplify how to configure your environment for a type pf jobs.
- This page explains how to write your own, private, module file.


## Introduction


- Module files are simple text files written in `TCL` - the Tool Command Language.
- TCL is a very powerful programming language on its own, but in most cases you do not need to know it, you just need to know a few very simple command,
- simple module files can be created with minimal code, to simply update `PATH` or other environmental variables,
- You can read a complete set of instructions on module file with the command `man modulefile,`


## Examples


Here are a few simple examples:


1. To change your `PATH` variable to add `/home/USER/miniconda3/bin`


```
#%Module1.0
prepend-path PATH /home/USER/miniconda3/bin
```


This example is equivalent to


`PATH=/home/USER/miniconda3/bin:$PATH` (in `bash` or `sh`)


or


`setenv PATH /home/USER/miniconda3/bin:$PATH```(in `csh` or `tcsh`).
2. To change your `LD_LIBRARY_PATH` variable to add `/home/USER/geos/lib`


```
#%Module1.0
prepend-path LD_LIBRARY_PATH /home/USER/geos/lib
```


The instruction `prepend-path` will add the given path to the beginning of the specified variable.
3. To change both PATH and `LD_LIBRARY_PATH` variables, use an internal variable (for convenience) and set a variable:


```
#%Module1.0
set base /home/USER/crunch
prepend-path PATH $base/bin
prepend-path LD_LIBRARY_PATH $base/lib
setenv CRUNCH $base
```


The variable `$base` is only set and used by the TCL, it will **not** be passed to the shell as `$base`, but in this example passed as `$CRUNCH` by the `setenv` instruction.
4. Useful instructions (see `man modulefiles` for explanations):
    - `append-path/prepend-path`
    - `setenv/unsetenv`
    - `module`
    - `remove-path`
    - `conflict`


Note that in these examples (and the ones below) `/home/USER` should be replaced by a real directory name.


A module file **must** start with the so-called *magic* first line `#%Module1.0`


Books have been written about TCL, you can use Google to get more information, or go to [https://www.tcl.tk/](https://www.tcl.tk/) to learn everything about TCL (and Tk)


## Implementation


Once you have written a module file, you can load it with the command `module`, followed by the full path to the module file, like in:


`module load /home/USER/modulefiles/miniconda`


You can make things easier, by storing all your module files in a single location and instructing the command `module` where to look, by either


- modifying the environment variable MODULEPATH to include the location(s) where to look,


or by


- creating a `~/.modulerc`file that adds to the directories where modules are searched for


```{.text title="example of ~/.modulerc"}
#%Module1.0
module use --append /home/USER/modulefiles
```


With this `~/.modulerc`file, you can then load your module file `miniconda` with the command


`module load miniconda`


## More Examples


- The system-wide modules are located in `/share/apps/modulefiles`
- You can take a look there for more examples of what can be done with modules and see `man modulefile`for more information.


Last modified 14 Jun 2018 MK/SGK
