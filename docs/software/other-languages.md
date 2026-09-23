# Julia, MATLAB, IDL and Java

- We have 5 interactive licenses and 128 run-time licenses for IDL (up to v 9.0.0), and have installed FL (up to version 0.79.54).
- GDL and FL are open-source (read no licenses needed) idl-like package.
    - GDL is no longer available on Hydra.


### IDL


- The interactive licenses are available for all versions of IDL, from v8.7 to v9.2, and should be used only on the login nodes for pre- or post processing.
- to access IDL, simply load the `idl` module: 
`% module load idl`
- to use a given version, specify the version, like: 
`% module load idl/9.1`
- To view all the available versions, use: 
`% ( module -t avail ) | & grep idl`


- Running IDL the normal way (i.e., interactively) in jobs submitted to the queue will quickly exhaust the available pool of licenses,
    - instead use the run-time licenses.


#### Using IDL with Run-Time Licenses


- To run IDL with a run-time license you must first compile your IDL code, and all the ancillary procedures and functions it may use and save it in a save set.
- The following example shows how to compile a procedure called `reduce`, stored in the file `reduce.pro`, to a complete save set that will be called `reduce.sav`


```{.text title="How to compile reduce.pro and save it as a save set"}
% module load idl/rt
% idl
IDL> .run reduce
IDL> resolve_all
IDL> save, /routine, file='reduce.sav'
```


- After creating a save set, changes to any segment of the code will not be reflected in the `.sav` file; you must recompile the code each time you modify it.
- To run IDL in run-time mode, you load the `idl/rt` module and use the `-rt=XXX` flag when invoking IDL.
- To let the GE know that you will pull an IDL run-time license, use the `-l idlrt=1` flag when `qsub`'ing. 
The GE will keep track of the number of licenses used and will limit accordingly the number of concurrent jobs using them to the number of available licenses.
- Here is an example of a job file `reduce.job` that will run the `reduce` procedure:


```{.text title="IDL run-time example job file"}
## /bin/csh
#
#$ -cwd -j y -o reduce.log -N reduce
#$ -l idlrt
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
#
module load idl/rt
#
idl -rt=reduce.sav
#
echo = `date` job $JOB_NAME done
```
- You then run that job with: 
`% qsub reduce.job`


#### **Notes**


- The name of the save file must match the name of the top procedure to run, and
- there is no way to pass arguments to that top level procedure, when started in with `-rt=name.sav`, i.e.: 
If you want to run the procedure `make_my_model`, you should write `make_my_model.pro` and compile it to a `make_my_model.sav` file.
- IDL procedures can read parameters from a file, or from standard input (`stdin`), for example:


```{.text title="Example of reading from stdin (standart input)"}
idl -rt=make_my_model.sav<<EOF
5943.
124.
sun
EOF
```


the corresponding procedure would look like this


```{.text title="Corresponding procedure make_my_model.pro"}
procedure make_my_model, temperature, density, name
;;
;; this procedure computes a model using a given temperature and density
;; and saves it to a file whose name is derived from given string
;;
if n_params() eq 0 then
 ;;
 ;; no parameters passed, so we need to read the parameters from stdin
 ;; let's initialize them to set the variable type (double and string)
 ;;
 temperature = 0.D0
 density = 0.0D0
 name = ''
 ;;
 read, temperature
 read, density
 read, name
endif
;;
fullName = name + '.dat'
print, 'running a model for T=', temperature,', rho=', density
print, 'saving it to "'+fullName+'"'
;;
[the code goes here]
;;
end
```
    - If the reference to the `.sav` file is to a different (sub)directory, IDL will execute a `cd` to that directory, namely 
`idl -rt=src/make_my_model` 
is in fact equivalent to 
`cd src` 
`idl -rt=make_my_model`
    - Some IDL procedures will use more than one thread (more than one CPU) if some operations can be parallelized. 
In fact IDL queries how many CPUs there are on the current machine to decide on the maximum number of threads it may start, assuming effectively that you are the sole user of that computer. 
This is not appropriate for a shared resource and it should not be used. 
To avoid this you must add the following instruction: 
 CPU, TPOOL_NTHREADS = 1 
to limit IDL to using only one thread (one CPU). 
 
Alternatively, you can request several slots (CPUs, threads) on a single compute node when submitting a job (`qsub -pe mthread N`, where N is a number between 2 and 64), 
and tell IDL to use that same number of threads with the `CPU` command. 
Of course, if your IDL code is not using N threads all the time, you will be grabbing more resources than you will be using, something that should be avoided.
    - You can check if IDL was started in run-time mode with 
`IF lmgr(/runtime) THEN message, /info, 'runtime mode is on'`
- Some IDL instructions are not allowed in run-time mode to prevent emulating interactive mode, consult the manual.
- You can check how many run-time licenses the GE thinks are still available with 
`% qhost -F idlrt -h global`


- All versions of IDL are now using the new IDL license manager.


### GDL & FL


- GDL & FL are an open source packages compatible with IDL:
    - GDL is compatible with version 7.1, see [http://sourceforge.net/projects/gnudatalanguage](http://sourceforge.net/projects/gnudatalanguage/), but is no longer available on Hydra;
    - FL is compatible with version 8, see [https://www.flxpert.hu/fl](https://www.flxpert.hu/fl/)
- These are free software:
    - you get what you paid for, but
    - there is no licensing nor run-time limitations.
- The version 0.79.54 (and a few other) of FL are available on Hydra, and is accessible by loading the respective modules: 
`% module load tools/gdl` 
or


`% module load tools/fl`


- The module will set variable `GDL_STARTUP` to either `~/.gdl.startup.0.9.5` or`~/.gdl.startu`p, if either file exists (checked in that order). 
Any GDL commands in the startup file will be executed every time GDL is started as if typed at the prompt.
- Like IDL, some GDL procedures will use more than one thread (more than one CPU) if some operations can be parallelized. 
GDL queries how many CPUs there are on the current machine to decide on the maximum number of threads it may start, assuming effectively that you are the sole user of that computer. 
This is not appropriate for a shared resource and it should not be used. To avoid this you must add the following instruction: 
 CPU, TPOOL_NTHREADS = 1 
to limit GDL to using only one thread (one CPU). 
 
Alternatively, you can request several slots, as described for IDL above, with the same caveats.



## Java

- Java versions 17, 18 & 21 are available on Hydra by loading the appropriate module: 
`% module load tools/java`


or


`% module load tools/java/18`


or


`% module load tools/java/21`


- java is now under tools/
- java 18 does not play nice with the GridEngine:
    - Java, by default, wants to starts as many threads and grab as much memory as possible.
    - By not specifying some memory related parameters, java fails in every submitted job, with the following message:


```
Error occurred during initialization of VM
Could not reserve enough space for object heap
```
    - You should always start java with the following options:


```
java -d64 -server -XX:MaxHeapSize=1g
```


where the value "`1g`" should be adjusted to the memory needed by the application and for the job to fit within the queue and the requested resources memory constraints.


The total amount of memory used by java is not just the maximum heap size.
    - If you need more memory, be sure to adjust the memory resource request accordingly (`-l memres=X,h_data=X,h_vmem=X`), see the section about memory reservation in the [Available Queues](../jobs/queues.md) page.


The complete documentation for all of `java` options (all versions) is posted [at Oracle's web site.](https://docs.oracle.com/en/java/javase/).



## Julia

- Several versions of julia (up to 1.12.1, see [julialang.org](http://julialang.org/)) are available by loading the corresponding module: 
`% module load tools/julia`
- or specify the version:


`% module load tools/julia/1.6.3`


etc...


- Check with 
`% module whatis tools/julia`


`% module help tools/julia`


`% man julia`


and documentation at [julialang.org](http://julialang.org/) & [juliaplots.org](http://juliaplots.org)



## Matlab

- Full fledged MATLAB is not available on `Hydra`
    - we would need to purchase licenses for Hydra,
    - Hydra users can use compiled MATLAB, since we installed the MATLAB run-time environment,
    - SAO users can use the ITS supported `MATLAB` compiler to produce run-time version of their MATLAB code.
- The `MATLAB` run-time environment is available on `Hydra`
    - to access it, load the right module:


| Modules | Description |
| --- | --- |
| `matlab/R2014a` | 2014 first release |
| `matlab/R2017b0` | 2017 second release (SAO/CF equivalent) |
| `matlab/R2017b` | 2017 second release, with (latest) update (# 9) |
| `matlab/R2019a` | 2019 first release |
| `matlab/R2019b` | 2019 second release |
| `matlab/R2020a` | 2020 first release |
| `matlab/R2020b` | 2020 second release |
| `matlab/R2021a` | 2021 first release |
| `matlab/R2021b` | 2021 second release |
| `matlab/R2022a` | 2022 first release |
| `matlab/R2022b` | 2022 second release |
| `matlab/R2023a` | 2023 first release |
| `matlab/R2023b` | 2023 second release |
| `matlab/rt → R2021b` | default run-time is set to use R2021b, latest version avail at SAO on ITS-managed machines |
| matlab/R2024a | 2024 first release |
| matlab/R2024b | 2024 second release |
| matlab/R2025a | 2025 first release |
| matlab/R2025b | 2025 second release |


**NOTES**
        - You must compile your `MATLAB` application (elsewhere) to run it on Hydra,
        - SAO has a single (concurrent) seat license for the `MATLAB` compiler, available on all ITS-managed machines.
        - Look at the README file under `~/hpc/examples/matlab` on Hydra.


