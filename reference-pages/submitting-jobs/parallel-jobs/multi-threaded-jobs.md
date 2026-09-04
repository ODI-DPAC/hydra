---
title: "Multi-Threaded Jobs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152293/Multi-Threaded+Jobs"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

1. [Multi-threaded jobs](multi-threaded-jobs.md)
2. [OpenMP jobs](multi-threaded-jobs.md)


## Multi-threaded, or OpenMP, Parallel Jobs


A multi-threaded job is a job that will make use of more than one CPU but needs all the CPUs to be on the same compute node.


## 1. Multi-threaded jobs


The following example shows how to write a multi-threaded job script:


```{.text title="Example of a Multi-threaded job script, using Bourne shell syntax"}
# /bin/sh
#
#$ -S /bin/sh
#$ -cwd -j y -N demo -o demo.log
#$ -pe mthread 32
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
#
# load the demo (fictional) module
module load tools/demo
#
# convert the generic parameter file, gen-params, to a specific file
# where the number of thread are inserted where the string MTHREADS is found
sed "s/MTHREADS/$NSLOTS/" gen-params > all-params
#
# run the demo program specifying all-params as the parameter file
demo -p all-params
#
echo = `date` job $JOB_NAME done
```


This example will run the tool `demo` using 32 CPUs (slots).


The script


- loads the `tools/demo` module,
- parses the file `gen-params` and replaces every occurrence of the string `MTHREAD` by the allocated number of slots (via `$NSLOTS`),
    - using the stream editor `sed` (man sed),
- saves the result to a file called `all-params,`
- runs the tool `demo` and with the parameter file `all-params`.


## 2. OpenMP jobs


The following example shows how to write an OpenMP job script:


```{.text title="Example of a OpenMP job script, using C-shell syntax"}
# /bin/csh
#
#$ -cwd -j y -N hellomp -o hellomp.log
#$ -pe mthread 32
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
#
# load the nvida module
module load nvidia
#
# set the variable OMP_NUM_THREADS to the content of NSLOTS
# this tell OpenMP applications how many threads/slots/CPUs to use
setenv OMP_NUM_THREADS $NSLOTS 
#
# run the hellomp OpenMP program, build w/ NVIDIA
./hellomp
#
echo = `date` job $JOB_NAME done
```


This example will run the program `hellomp`, that was compiled with the NVIDIA compiler, using 32 threads (CPUs/slots). The script


- loads the nvidia module,
- sets `OMP_NUM_THREADS` to the content of `NSLOTS` to specify the number of threads
- runs the program `hellomp`.


## Examples


- You can find examples of OpenMP for all 3 compilers on Hydra under /home/hpc/examples/openmpm check the README file:
    - gcc/ - GNU compilers;
    - intel/ - Intel compilers;
    - nvidia/ - NVIDIA compilers;
    - share/ - source code.
