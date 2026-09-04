---
title: "Using a Jupyter Notebook on Hydra"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/170987181/Using+a+Jupyter+Notebook+on+Hydra"
date-modified: "2024-07-05"
author: "MK/SGK"
categories: ["hydra7"]
---

## Introduction


- Jupyter notebooks deliver a "literate programming" interface with Python that combines MarkDown-based documentation with code cells.
- Using Jupyter on Hydra is especially helpful for:
    - Keeping a record of a your analysis in notebook format, that can be accessed later
    - Working with images or visualizations that cannot be viewed through the command line interface.
- While you can use a login node as Jupyter server
    - we strongly recommend that you use a compute node and connect to one via the interactive queue.
- To use a Jupyter nootebook you will need to do the following on Hydra
    1. access a compute node via the interactive queue,
    2. load a `python` module or use `conda`
    3. start a Jupyter lab server
- on your local machine
    1. start a `ssh` tunnel
    2. connect via that tunnel to the Jupyter server from a browser


## How To Start a Jupyter lab Server


### 1- Start an interactive session on Hydra


From a login node, start an access the interactive session as follows:


`qrsh`


or


`qrsh -pe mthread N`


or


`qrsh -l gpu`


where N is the number of threads you would like to request more than one and use `-l gpu` if you want to use a GPU


Your prompt will change from something like`[user@hydra-login01]` to `[user@compute-XX-XX]` where *compute-**XX-XX* is the name of the compute node the schedule started your interactive session on.


### 2- Load a `python` module or use `conda`


To access Jupyter, either load


- a python module, like in


`module load tools/python`


or


- a conda module, and activate a specific module, like jupyter, if necessary.


`module load tools/conda`


`conda activate jupyter`


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) If you request a GPU, you will also need to*load the CUDA libraries. with*


`module load nvidia/24/cuda`


*You can test that it worked with the command* `nvidia-smi`.


### 3- Launch a jupyter lab server


Since the server will run from the directory you start it from, so make sure you are "above" the directory where you want your notebooks to live.


The interactive queue puts you into your `/home/<user>` directory by default, use `cd` to navigate to the right directory first.


#### 3.a Using a provided script


- Load the `tools/jupyter` module, run the jupyter lab server script and follow the instructions:


`module load tools/jupyter`


`start-jupyter-lab-server --port=N`


where `--port=N` is optional and N is the port number to use (a number between 8000 and 9999, default value is 8888).


- You can use `start-jupyter-lab-server -help`to see all the available options.


*alternatively:*


#### 3.b Explicit instructions


#### 1- Use:


`jupyter lab --no-browser --ip=`hostname` --port=8888`


This will launch the Jupyter lab server, using port 8888, and will produce output looking something like this:


`[I 14:38:44.628 NotebookApp] Serving notebooks from local directory: /scratch/genomics/triznam`


`[I 14:38:44.628 NotebookApp] The Jupyter Notebook is running at:`


`[I 14:38:44.628 NotebookApp] http://compute-08-31.local:8888/?token=e54bd4f1469387555c114697278fe2ff10089cbf723c595b`


`[I 14:38:44.628 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).`


`[C 14:38:44.636 NotebookApp]`


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Note that you can use any port between 8000 and 9999, port 8888 is the default one.


*Now back to your local computer*


#### 2- Start the ssh tunnel


- open up a terminal
- in that terminal, run the following command:


`ssh -N -L 8888:compute-XX-XX:8888 USERNAME@hydra-login01.si.edu`


where:


- *XX-XX* corresponds to the compute node that the `qrsh` command placed you on.
- the first 8888 is the port of your local computer. If you are already running a local Jupyter notebook, then simply change this to a free port,
- the second 8888 is the port of the Jupyter lab server is listening to, the number you used with --port= when you launchd the jupyter lab server (see 3- above),
- USERNAME is your username on hydra.
    - Use instead `USERNAME@hydra-login02.si.edu` if you've accessed Hydra via `ssh USERNAME@hydra-login02.si.edu`


This will prompt you for your Hydra password, so type it in, and it will just 'hang' there (i.e., the tunnel is running).


#### 3- Connect to the Jupyter server from a browser


- Open a browser on your local machine
- Go to [http://localhost:8888](http://localhost:8888/).
    - This should start a Jupyter notebook window,
    - it will ask for a token or password, so copy and paste the long token from the end of the URL that was printed out when you launched Jupyter above.
    - You can also type in `http://localhost:8888/lab?token=XXXX`
        - where XXXX is that long token*.*


## Shutting Down


- On your browser, under "file", use "shut down", this will terminate your notebook and the Jupyter lab server on Hydra
- In the terminal were the ssh tunnel is running, use control+c to kill it,
- then exit from your interactive session on Hydra and from the local terminal.


## Setting up a Jupyter Server password


To avoid having to paste that long token every time, you can create a password for yourself.


```
jupyter server password
```


(and then enter a memorable password)


Now next time you launch Jupyter, you will be prompted to enter a password instead of that unique token.


## Creating conda environment specific kernels


To create a Jupyter *kernel* that is pre-built with all of the conda packages from your conda environment, do the following.


```
conda activate env_name
python -m ipykernel install --user --name="env_name"
```


Then you should see that kernel as a dropdown in Jupyter notebook or as a notebook option in Jupyter Lab.


Having kernels is also useful for running notebooks as a job using [PaperMill](https://papermill.readthedocs.io/en/latest/).
