---
title: "How to Use GPUs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152354/How+to+Use+GPUs"
date-modified: "2025-10-13"
author: "SGK"
categories: ["hydra7"]
---

1. [Introduction](how-to-use-gpus.md)
2. [GPU Configuration](how-to-use-gpus.md)
3. [Available Queues](how-to-use-gpus.md)
4. [Limits](how-to-use-gpus.md)
5. [Examples](how-to-use-gpus.md)
6. [Local Tools](how-to-use-gpus.md)
    1. `check-gpu-usage`
    2. `get-gpu-info`
7. [Other Tools](how-to-use-gpus.md)
    1. CUDA
    2. NVIDIA OpenACC/CUF
    3. NVSMI


# 1. Introduction


A total of 8 GPUs are available on Hydra on 3 nodes.


- One node has four GPU cards (NVIDIA L40S)
- Two nodes have two GPU cards (NVIDIA GV100)


| Type | CUDA Cores | Memory | Mem b/w | #GPUs/#nodes | Total(GPUS) |
| --- | --- | --- | --- | --- | --- |
| L40S | 18,176 | 48GB | 864 GB/s | 4/1 | 4 |
| GV100 | 5,120 | 32GB | 870 GB/s | 2/2 | 4 |


CUDA cores are not equivalent to CPU cores.


# 2. GPU Configuration


- The GPUs are configured as follow:
    - The CUDA driver is version 12.4 (Driver Version 550.54.15)
    - compute mode is set to EXCLUSIVE_PROCESS
        - only one context is allowed per device, usable from multiple threads at a time
    - persistence is ENABLED
        - NVIDIA driver remains loaded even when there are no active clients
    - accounting is ENABLED
        - see `man nvidia-smi`


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) This means that GPU applications will


- start faster (no need to re-load the driver), and
- only one process can use a GPU at a time (exclusive use.)
- accounting is on.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Only one process per GPU can run at the same time, each process gets a different GPU.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Starting one more process than available GPUs will fail with the following error message:


`Error: all CUDA-capable devices are busy or unavailable` 
`in file XXX.cu at line no NNN`


# 3. Available Queues


- Four queues are available to access the GPUs:
    - an interactive queue, `qgpu.iq`, that has a 24hr elapsed time limit, and
    - three batch queues `sTgpu.q, mTgpu.q` and `lTgpu.q`, corresponding to a short, medium and long time limit.
- There are also limits on memory usage (CPU's memory) and how many concurrent GPUs can be used, see the [Available Queues page](submitting-jobs/available-queues.md).


To run a GPU job or get a GPU in an interactive queue:


- You must request to run in one of these queues, and specify how many GPUs will will use, as follows (*both are needed*):


`% qsub -l gpu,ngpus=1 -q sTgpu.q`


or


`% qrsh -l gpu,ngpus=1`


- If your job will use two GPUs, use:


`% qsub -l gpu,ngpus=2 -q lTgpu.q`


- You can specify what type of GPU to use with `gpuarch` , i.e.:


`-l gpu,ngpus=1,gpuarch=L40S`


or


`-l gpu,ngpus=1,gpuarch=GV100`


Specifying the queue name is optional, unless your jobs will need more time to complete.


- The `ngpus=` specification is a RSMAP (aka a resource map) and can be more complex, like `ngpus='2[affinity=true]'`


::: {.note title="NOTE"}
- If you only use `-l gpu` your job will run but will end up in error mode (`Eqw)`
 - The job output will look like this:


```
prolog: Error submitting job 'test-gpu' (10264023) while using a GPU queue (sTgpu.q): '-l ngpus=N' is missing.
prolog: The job will not run and will be in 'Eqw' mode.
prolog: Delete it with 'qdel 10264023', and resubmit accordingly.
```


- The jobs scheduler (i.e., the Grid Engine) will assign which GPUs to use by setting the env. variables `$CUDA_VISIBLE_DEVICES`, as well as `$SGE_HGR_GPUS`
 - make sure your application uses these GPUs.
- ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Advanced users, read the following man pages
 - `man sge_resource_map`
 - `man sge_nvidia`
 - `man sge_config`
:::


# 4. Limits


- GPU usage limits are:
    - Time and memory queue limits: how much a job or a interactive session can use;
    - Queue resource quotas: how many GPUs a user can use at the same time.


## 4a. Time and memory queue limits


- Like all other queues, the GPU queues have elapsed and CPU time limits, as well as resident and virtual memory limits.
- These are currently:


<table class="wrapped confluenceTable" style="margin-left: 40.0px;"><colgroup><col/><col/><col/><col/><col/></colgroup><tbody style="margin-left: 40.0px;"><tr style="margin-left: 40.0px;"><th class="confluenceTh" scope="col" style="margin-left: 160.0px;">queue</th><th class="confluenceTh" scope="col" style="margin-left: 40.0px;">elapsed</th><th class="confluenceTh" scope="col" style="margin-left: 40.0px;">CPU</th><th class="confluenceTh" scope="col" style="margin-left: 40.0px;">resident</th><th class="confluenceTh" scope="col" style="margin-left: 40.0px;">virtual</th></tr><tr style="margin-left: 40.0px;"><th class="confluenceTh" scope="col" style="margin-left: 40.0px;">name</th><th class="confluenceTh" colspan="2" scope="colgroup" style="text-align: center;margin-left: 40.0px;">time</th><th class="confluenceTh" colspan="2" scope="colgroup" style="text-align: center;margin-left: 40.0px;">memory</th></tr><tr style="margin-left: 40.0px;"><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6" style="margin-left: 40.0px;" title="Background color : Light yellow 35%"><code title=""><span style="color:var(--ds-text-accent-blue,#0055cc);">qgpu.iq</span></code></td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">24:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">12:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">64G</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">128G</td></tr><tr style="margin-left: 40.0px;"><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6" style="margin-left: 40.0px;" title="Background color : Light yellow 35%"><code title=""><span style="color:var(--ds-text-accent-blue,#0055cc);">sTgpu.q</span></code></td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">14:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">7:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">64G</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">128G</td></tr><tr style="margin-left: 40.0px;"><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6" style="margin-left: 40.0px;" title="Background color : Light yellow 35%"><code title=""><span style="color:var(--ds-text-accent-blue,#0055cc);">mTgpu.q</span></code></td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">288:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">144:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">64G</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">128G</td></tr><tr style="margin-left: 40.0px;"><td class="highlight-#fffae6 confluenceTd" data-highlight-colour="#fffae6" style="margin-left: 40.0px;" title="Background color : Light yellow 35%"><code title=""><span style="color:var(--ds-text-accent-blue,#0055cc);">lTgpu.q</span></code></td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">1440:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">720:15:00</td><td class="confluenceTd" style="text-align: right;margin-left: 40.0px;">64G</td><td class="confluenceTd" style="text-align: right;margin-left: 240.0px;">128G</td></tr></tbody></table>


- The command `qconf -sq <qname>` will list these values.
- The CPU time, resident and virtual memory limits scale up with the number of CPU slots,
    - hence you can increase these by requesting more slots with `-pe mthread N`


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) These apply to the CPU, not the GPU.


## 4b. Queue resource quotas


- Like all other resources, users are limited to how much GPUs they can use concurrently.
- These are currently:


| queue | #GPU |
| --- | --- |
| name | limit |
| `qgpu.iq` | 1 |
| `sTgpu.q` | 4 |
| `mTgpu.q` | 3 |
| `lTgpu.q` | 2 |
| <in total> | 4 |


- The command `qconf -srqs`will list these values.
- The command `qquota` (or `qquota+`) will show the current queue resources usage per quota (if used).


# 5. Examples


## Trivial Examples


I wrote a trivial test case: computing a Julia set (fractals) and saving the corresponding image. It is derived from NVIDIA's own example.


You can find that example, and equivalent codes, under `/home/hpc/examples/gpu`


<table class="wrapped confluenceTable"><colgroup class=""><col class=""/><col class=""/></colgroup><tbody class=""><tr class=""><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">cuda/</span></code></td><td class="confluenceTd">CUDA and C++ code (.cu .cpp Makefile)</td></tr><tr class=""><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">cuda/gpu</span></code></td><td class="confluenceTd">GPU example</td></tr><tr class=""><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">cuda/cpu</span></code></td><td class="confluenceTd">CPU equivalent</td></tr><tr class=""><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">matlab</span>/</code></td><td class="confluenceTd" colspan="1">MATLAB, using standalone compiled code (available for now only at SAO)</td></tr><tr class=""><td class="confluenceTd"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">matlab/gpu</span></code></td><td class="confluenceTd">GPU example</td></tr><tr class=""><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">matlab/cpu</span></code></td><td class="confluenceTd" colspan="1">CPU equivalent</td></tr><tr class=""><td class="confluenceTd" colspan="1"><code><span style="color:var(--ds-text-accent-blue,#0055cc);">idl/</span></code></td><td class="confluenceTd" colspan="1">IDL CPU-only equivalent (for comparison)</td></tr></tbody></table>


### Note:


I wrote more sophisticated alternative to that example, to achieve a 500:1 speed up compared to the equivalent computation running a single CPU.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) That's reducing a 7.5 hour long computation to less than 1 minute, in a case that is intrinsically fully "parallelizable."


It illustrates the potential gain, compared to the cost of coding using CUDA (an extension of C++)


# 6.Local Tools


- We provide two local GPU related tools:
    - `check-gpu-usage`: checks current usage in the GPU queues.
    - `get-gpu-info`: queries whether a node has a GPU, returns the GPU(s) properties and which process(es) use(s) the GPUs.
    - `qacct+` now support GPU accounting (`man qacct+` or check [Additional Tools](additional-tools.md))
    - You can also query the GE GPU info and assignment with `qstat -s r -F mgpu,gpuarch,ngpus -q '*gpu*'`


## 6a. check-gpu-usage


Perl script to checks current usage in the GPU queues according to the job scheduler (i.e., the Grid Engine)


```
hpc@hydra-login% check-gpu-usage
hostgroup: @gpu-hosts (3 hosts)
                - --- memory (GB) ----  -  #GPU - --------- slots/CPUs --------- 
hostname        -   total   used   resd -  a/u  - nCPU used   load - free unused 
compute-50-01   -   503.3   19.6  483.7 -  4/0  -   64    0    0.0 -   64   64.0
compute-79-01   -   125.4   18.1  107.3 -  2/0  -   20    0    0.0 -   20   20.0
compute-79-02   -   125.5   46.2   79.3 -  2/1  -   20    1    2.1 -   19   17.9

Total #GPU=8 used=1 (12.5%)
```


## 6b. get-gpu-info


C-shell script to query whether a node has a GPU, returns the GPU(s) properties and which process(es) use(s) the GPUs.


Wrapper that runs the python script `get-gpu-info.py`, that python script uses the pyNVML (python bindings to NVML).


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) the `get-gpu-info` wrapper checks if the first argument is in the form `NN-MM`, and if it is will run `get-gpu-info.py` on `compute-NN-MM`


```{.text title="Here is how to use it:"}
usage: get-gpu-info.py [-h] [-i] [-d] [-l [LOOP]] [-c COUNTS] [--ntstamp NTSTAMP] [id]

get-gpu-info.py: show info about GPU(s)

positional arguments:
  id                    specify the GPU id, implies --info

optional arguments:
  -h, --help            show this help message and exit
  -i, --info            show info for each GPU
  -d, --details         show details of running process, implies --info
  -l [LOOP], --loop [LOOP]
                        repeat every LOOP [in sec: 10 to 3600], default is 30,
                        implies --info
  -c COUNTS, --counts COUNTS
                        limits the no. of times to loop, implies --info
  --ntstamp NTSTAMP     specify how often to put a time stamp, by default puts
                        one every 10 readings

Ver 1.1/0 Oct 2021/SGK
```


### Examples


- on login node, no 'NN-MM' given


```
login01% get-gpu-info
get-gpu-info.py: 0 GPU on login01
```


- on login node, checking 50-01


```
login01% get-gpu-info 50-01 -d
4 GPUs on 50-01
Thu May 16 15:30:06 2024
id               ------ memory ------  ------ bar1 --------  ---- usage ----
   --- name ---    used/total            used/total           gpu  mem #proc
0  NVIDIA_L40S   479.1M/44.99G   1.0%  1.688M/64.00G   0.0%    0%   0% 0
1  NVIDIA_L40S   479.1M/44.99G   1.0%  1.688M/64.00G   0.0%    0%   0% 0
2  NVIDIA_L40S   479.1M/44.99G   1.0%  1.688M/64.00G   0.0%    0%   0% 0
3  NVIDIA_L40S   479.1M/44.99G   1.0%  1.688M/64.00G   0.0%    0%   0% 0
```


- on login node, checking 79-01


```
login01% get-gpu-info 79-01 -d
2 GPUs on 79-01
Thu May 16 15:30:12 2024
id               ------ memory ------  ------ bar1 --------  ---- usage ----
   --- name ---    used/total            used/total           gpu  mem #proc
0  Quadro_GV100  276.5M/32.00G   0.8%  2.688M/256.0M   1.0%    0%   0% 0
1  Quadro_GV100  276.5M/32.00G   0.8%  2.688M/256.0M   1.0%    0%   0% 0
```


- on login node, checking gpu0 on 79-02, that has a job attached to it


```
login01% get-gpu-info 79-02 -d 0
2 GPUs on 79-02
Thu May 16 15:30:19 2024
id               ------ memory ------  ------ bar1 --------  ---- usage ----
   --- name ---    used/total            used/total           gpu  mem #proc
0  Quadro_GV100  6.212G/32.00G  19.4%  5.188M/256.0M   2.0%    0%   0% 1
    pid=494189 name=b'python3' used_memory=5.939G
```


# 7. Other Tools


## CUDA


- The CUDA compiler is now part of the NVIDIA compilers, and is accessible loading the NVIDIA module


`% module load nvidia`


that loads by default NVIDIA 23.9 and CUDA 12.2.


- Other version are available, check with


`% module whatis nvidia`


NVIDIA OpenACC/CUF


- The NVIDIA compilers support [OpenACC](http://www.openacc.org/).
- OpenACC, similarly to OpenMP, instructs a compiler to produce code that will run on the GPU
- It uses `pragmas`, i.e., instructions to the compilers that look otherwise like comments, to specify what part of the computation should be offset to the GPU.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) A single pair of such `pragmas` produced a >300x speed up of the Julia set test case.


- This requires an additional license that is available on `Hydra` (not at SAO, tho).
- The NVIDIA compilers also support CUDA FORTRAN (aka CUF).
- You can write or modify existing FORTRAN code to use the GPU like you can using C/C++ & CUDA.
- Simple examples are available in `/home/hpc/examples/gpu/cuda`


## NVSMI: The NVIDIA System Management Interface


- NVSMI v550.54.15 and dcgm v 3.35 are available on the GPU nodes.
- The following tools are available *only on nodes with GPUs*
    - `nvidia-smi`: NVIDIA System Management Interface program
    - `dcgmi`: NVIDIA Datacenter GPU Management Interface
        - must load the `cuda-dcgm` module.


#### NVIDIA-SMI


- `nvidia-smi`allows you to query & monitor the status of the GPU card(s):


```{.text title="Try one of the following commands:"}
hpc@compute-79-01% nvidia-smi
hpc@compute-79-01% nvidia-smi dmon -d 30 -s pucm -o DT
hpc@compute-79-01% nvidia-smi pmon -d 10 -s um -o DT
hpc@compute-79-01% nvidia-smi \
         --query-compute-apps=timestamp,gpu_uuid,pid,name,used_memory \
         --format=csv,nounits -l 15
hpc@compute-79-01% nvidia-smi \
         --query-gpu=name,serial,index,memory.used,utilization.gpu,utilization.memory \
         --format=csv,nounits -l 15
hpc@compute-79-01% nvidia-smi -q -i 0 --display=MEMORY,UTILIZATION,PIDS
```


- The man page for `nvidia-smi` is available on the login nodes (`man nvidia-smi`)


### NVML/pynvml


The NVIDIA Management Library ([NVML](https://developer.nvidia.com/nvidia-management-library-nvml)) and the python bindings to NVML (`pyNVML`) are available.


- the [NVML documentation](http://docs.nvidia.com/deploy/nvml-api/index.html) is available at NVIDIA's web site
- `pyNVML` 7.352.0 is available via the `nvidia/pynvlm` module, and the [documentation is on-line](http://pythonhosted.org/nvidia-ml-py/).
