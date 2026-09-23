# Modules



## 1.Introduction


- The purpose of a module file is to simplify how to configure/modify your Un*x environment to run or have access to some specific set of tools/applications/etc....
- A module file also allows users to change their configuration without worrying what shell is being used (i.e., `bash` or `csh`),
- Module files to access general purpose or supported tools/applications are written and maintained by the HPC support team.


So, instead editing your ~/`.bash_profile,` ~/`.profile` or `~/.cshrc file(s)` to configure your Un*x environment (`PATH,` `MANPATH,``LD_LIBRARY_PATH`, etc), you should use the command `module`.


- For example, to use the GNU compiler version 4.9.2, one simply needs to execute: 
`% module load gcc/4.9.2`


- The command `module` uses module files, files that lists what is needed to be done to your Un*x environment to use a given tool, including the location of the tool.
- A module can be loaded, unloaded, or you can switch to a different version without having to edit and/or source a configuration file.
- Also, if the location of a tool changes, one only has to edit the corresponding module file:
    - configuration changes are transparent to the users and to any script or job that uses that tool via the command `module`.
- There is no need to type long paths that include version numbers.
- Module files also allow to check for conflict: you can't use different versions of the same tool simultaneously.
- The command `module` works the same way whether you use use the `bash` or the `csh` shell,
    - so there is no need to explain what to do for each shell.
- Module files can also be used by `perl`, `cmake` or `python`.
- Users can augment the module files we offer by writing their own module files (written in `TCL).`
- To learn about the command module, read the module man page: 
 `% man module`


The key ways to use `module`are:


```
    module help               - show help on the command module itself
    module load   XXX         - load the module XXX
    module unload XXX         - unload the module XXX
    module switch XX/YYY      - switch to module XX/YYY
    module list               - list which modules are currently loaded
    module avail              - show which modules are available
    module -t avail           - show which modules are available, one per line
    module whatis             - show one line information about all the available modules
    module whatis ZZZ         - show one line information about the module ZZZ
    module help   ZZZ         - show the help information on the module ZZZ
    module show   ZZZ         - show what loading the module ZZZ does to your Unix environment.
```


- You can easily find out what software is available by "`grep`'ing" the output of `module`, i.e.: 
`% ( module -t avail ) | & grep bioinformatics`
- You can access the documentation built into a module file with: 
`% module help gcc/4.9.2`
- You can view how a module file will change your Un*x environment with: 
`% module show gcc/4.9.2`


#### Module shortcut and sticky modules


The command module has been upgraded to version 5.3.1. It works as before but has a few improvements:


- explicit sticky modules: two modules are preloaded and are sticky, i.e. you cannot unload them
- `ml` shortcut:
    - `module list, module load` and `module unload` can be shorten using `ml`as follows: 
| | |
| --- | --- |
| `ml` | `module list` |
| `ml tools/ffsend` | `module load tools/ffsend` |
| `ml -tools/ffsend` | `module unload tools/ffsend` |
- customization
    - `module list` is by default more verbose and in color
    - this can be customized and what is shown when loading a module can be also customized
    - the following modules customize the output of the module command:
| `ml module-nocolor` | do not use colors |
| --- | --- |
| `ml module-nowarn` | disable some warning |
| `ml module-simple-format` | simplify the output of module list |
| `ml module-simple` | load the 3 module above |
| `ml module-color` | specify a color scheme (red for sticky, green for auto-loaded) |
| `ml module-verbose` | set module in verbose mode, equiv to using the -v flag |
    - You can load and unload these module to your liking.


Details about the new version of module can be found in the module man page or the documentation about module [here](https://modules.readthedocs.io/en/v5.3.1/).


#### Module conflict


The command `module` implements the concept of conflict: i.e., you cannot load simultaneously `gcc/4.9.1` and `gcc/4.9.2`:


- to change versions use switch, i.e.: 
`% module load gcc/4.9.1` 
`[do your stuff]` 
`% module switch gcc/4.9.2`
- to use a different (b/c of conflict) tool, use `unload` first 
`% module load gcc/4.9.1` 
`[do your stuff that needs gcc ver 4.9.1]` 
`% module unload gcc/4.9.1` 
`% module load nvidia/23.9` 
[do the stuff that needs NVIDIA ver 23.9]


#### Module default and manpath


Module also implements the concept of default value:


- so `module load nvidia` is equivalent to `module load nvidias/23.9` if NVIDIA version 23.9 is set as the default nvid`ia` module.


Loading/unloading module(s) may set your MANPATH variable in such a way as to prevent you from accessing default man pages locations.


Loading the module `tools/manpath` will solve this.


### Available Module Files


For a current list of all available module files on Hydra, see the [list of module files](https://hydra.si.edu/tools/QSubGen/module-avail.html).


In the *bioinformatics* and *tools* categories, the [list of module files](https://hydra.si.edu/tools/QSubGen/module-avail.html) does not include every version of each software package installed. For these sections, you will need to run `module avail` on Hydra to see every available version.


### How to Write your Own Modules Files


Users can write their own module files to configure/modify their Un*x environment by loading or unloading a module.


This [page describe how to write your own (private) module(s), with examples.](custom-modules.md)
