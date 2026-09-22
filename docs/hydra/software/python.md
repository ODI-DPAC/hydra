# Python and conda

- The default Python with Rocky 8.x is version 3.6.8;
    - so unless you load a specific module, you will run these versions of Python.


- Additional versions of Python are available as follows:


| Module | Version | Comment |
| --- | --- | --- |
| none | 3.6.8 | `python` under Rocky 8.10 |
| none | 2.7.18 | `python2` under Rocky 8.10 |
| `python3` | 3.9.18 | BCM version |
| `python39` | 3.9.18 | BCM version |
| | | |
| `tools/python` | 3.11.4 :: Anaconda, Inc. | current default |
| `tools/python/2.7` | 2.7.16 :: Anaconda, Inc. | |
| `tools/python/3.7` | 3.7.3 :: Anaconda, Inc. | Anaconda built/full support |
| `tools/python/3.8` | 3.8.8 :: Anaconda, Inc. | Anaconda built/full support |
| `tools/python/3.9` | 3.9.8 | Built from source |
| `tools/python/3.9a` | 3.9.13 | Built from source |
| `tools/python/3.10` | 3.10.0 | Built from source |
| `tools/python/3.11` | 3.11.4 :: Anaconda, Inc. | Anaconda built/full support |
| `tools/python/3.11b` | 3.11.7 :: Anaconda, Inc. | Anaconda built/full support |
| `tools/python/3.13` | 3.13.5 :: Anaconda, Inc. | Anaconda built/full support |
| `tools/python/3.14` | 3.14.0 | Built from source |
| | | |
| `intel/python` | 3.9.7 :: Intel Corporation | Intel's version |
| `intel/python/37-21.4` | 3.7.11 :: Intel(R) Corporation | Intel's version w/ 21.4 |
| `intel/python/39` | 3.9.7 :: Intel(R) Corporation | Intel's version |
| `intel/python/39-22.1` | 3.9.7 :: Intel(R) Corporation | Intel's version w/ 22.1 |
| `intel/python/39-23.1` | 3.9.26 :: Intel(R) Corporation | Intel's version w/ 23.1 |
| `intel/python/39-24.0` | 3.9.18 :: Intel(R) Corporation | Intel's version w/24.0 |
| `conda/25.9.1` | 3.11.14 | Intel's version w/ 25.3 |
| `conda/25.9.1` | 3.12.12 | Intel's version w/ 25.3 |
- Intel is now distributing Python via `conda` (see [this page](https://www.intel.com/content/www/us/en/developer/articles/technical/get-started-with-intel-distribution-for-python.html))
    - You can also access it via the `intel_python_311` or `intel_python_312` environments after loading `conda/25.9.1`


If you are looking for the versions with all the usual packages, use the `tools/python`one. This list will vary as we install new versions.


## Package Installation and Management


We have installed a long list of packages with the Anaconda versions.


You can view that list with (after loading the appropriate module)


`% module load tools/python`


`% pip list`


You can install additional packages without elevated (admin/root) privileges with


`% pip install --user <package-name>`


Alternatively you can use `conda` to manage your Python packages and beyond that manage your environment - rather than using module files.


- If you only need a handful of packages that have no incompatibilities with the ones already installed and
- you can use one of the available python version you may chose not to bother with `conda,`and use`pip install --user.`
- For further explanations on Anaconda and Miniconda and instructions on using `conda`, consult the Conda: Anaconda & Miniconda page.


## Python Multi-Threading (NUMPY and others)


- By default, `NUMPY,`as well as other packages, are built to use multi-threading, namely some numerical operations will use all the available CPUs on the node it is running on.
    - This is *NOT* the way to use a shared resource, like Hydra,
    - The symptom is that your job is oversubscribed.
- The solution is to tell `python` how many threads to use, using the respective module:


```{.text title="serial case"}
module load tools/python/use-single-thread
```


or


```{.text title="multi-thread case"}
module load tools/python/use-multi-thread
```


use `module show <module-name>` to see what is done, the multi-thread version will use the value stored in the environment variable NSLOTS to match the requested resource (`-pe mthread`).


If you distribute your python code with mpi, use the single thread version.


You can use


- 
    - `tools/python-single-thread-numpy` or `tools/single-thread-numpy` instead of `tools/python/use-single-thread`


and


- 
    - `tools/python-mthread-numpy` or `tools/mthread-numpy` instead of `tools/python/use-multi-thread`


for backward compatibility.


### Example


```{.text title="demo-mthread-numpy.job"}
#
## this example uses 4 threads
#$ -pe mthread 4
#$ -cwd -j y -o demo-mthread-numpy.log -N demo-mthread-numpy
#
echo + `date` $JOB_NAME started on $HOSTNAME in $QUEUE with id=$JOB_ID
echo NSLOTS = $NSLOTS
#
module load tools/python/3.8
module load tools/python/use-multi-thread
python my-big-data-cruncher.py
#
echo = `date` $JOB_NAME done.
```


Last update 16 May 2024 SGK/MPK

## Conda: Anaconda & Miniconda



### Introduction


Conda is a free & open-source package and environment management system, see [conda.io](https://docs.conda.io/en/latest/):


- It was started by the Python community (hence the snake name reference) to help handling the plethora of Python packages,
    - but it has been extended to support any languages (*Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN*) and to manage the OS environment.
- It is used by a large community in data science and biology.
- It requires no elevated (admin/root) privileges to install software and/or create "environments", if used properly and works under different OSes.
- Conda main development is carried out by a commercial company, Anaconda, that offers free and paid versions; the free version works great.
- There are two free versions:
    1. The full fledge version, [Anaconda](https://anaconda.org/).
    2. A small, bootstrap version of Anaconda, called [Miniconda.](https://docs.conda.io/en/latest/miniconda.html)


### Anaconda, Miniconda, Miniforge?


- Users may find it convenient to use [Anaconda, Miniconda](https://conda.io/docs/) or Miniforge (mambe) to install and manage software in their user space.
- It is acceptable to use these systems, but like compiling and running any software on Hydra, the user should be familiar with how the software functions and uses resources (memory, CPUs, disk) so as not to overutilize cluster resources.
- User can either:
    - install [Miniconda](https://docs.conda.io/en/latest/miniconda.html),
    - Install Miniforge
    - install the full-fledged [Anaconda](https://anaconda.org/),
    - use the pre-installed conda/mamba: full-fledged Anaconda, Miniconda or Miniforge.
- Installing Miniconda or using the pre-installed conda are the preferred options for Hydra, since Miniconda initially installs minimal packages, hence reducing disk usage (required dependencies will be installed by `conda)`.
- Using the pre-installed conda/mamba requires the least efforts from the user, but in some cases might not offer the user full control:
    - users cannot modify or update the "base" installation,
    - instead user should create their own `conda` environment(s) and adjust them as needed.
- If the "base" needs to be updated, please contact us.


#### a. Do NOT Mix and Match


!!! note "WARNING"
    You cannot mix and match Miniconda, Anaconda or pre-installed conda


    If you have installed your own Miniconda or Anaconda, you may have executed:


    `% conda init`


    If you did, you will have stuff like this


    `# >>> conda initialize >>>` 
    `# !! Contents within this block are managed by 'conda init' !!`


    `...`


    `# <<< conda initialize <<<`


    in your `~/.bashrc` file.


    While this is convenient if you always use that same `conda` (your Miniconda, your Anaconda or the pre-installed Anaconda), it does not allow you to *safely* use a different one.


    - If you want to be able to switch to a different `conda` , delete these lines from your `~/.bashrc` file.
    - You can re-execute `conda init` after switching.
    - If you want to be able to switch back and forth, delete these lines and do not execute `conda init` (see below for recommended usage of the pre-installed full-fledged Anaconda).



#### b. Pre-installed conda and mamba


This is the most direct way to start using `conda` on Hydra as it uses a module that is already setup on the system.- You can access the pre-installed conda simply by loading the `tools/conda` module and enabling `conda` with the command `start-conda`
- The recommended procedure to enable `conda` each the time you log on Hydra is to add these two lines


`module load tools/conda`


`start-conda`


to either your `~/.bashrc` or your `~/.cshrc` file (i.e. whether your login shell is `bash` or `csh` respectively).


You don't have to enable `conda` for each time you login, tho.


- We have loaded various versions of conda and mamba available:


| module |  |
| --- | --- |
| `tools/conda/3.8` | Set environment to use the full-fledged conda (Anaconda v3.8) |
| `tools/conda/3.11` | Set environment to use the full-fledged conda (Anaconda v3.11) |
| `tools/conda/3.13` | Set environment to use the full-fledged conda (Anaconda v3.13) |
| `tools/conda/23.1.0` | Set environment to use Miniconda3 conda (v23.1.0) |
| `tools/conda/23.11.0` | Set environment to use Miniconda3 conda (v23.11.0) |
| `tools/conda/25.9.1` | Set environment to use Miniconda3 conda (v25.9.1) |
| `tools/mamba/24.1.2` | Set environment to use mamba, (miniforge3 v24.1.2 |
| `tools/mamba/25.9.1` | Set environment to use mamba, (miniforge3 v25.9.1) |


##### Job files


- To enable `conda` for your jobs that use the Bourne shell (`-S /bin/sh` )
    - either add these two lines in your job file, or
    - add the fist line in a file called `~/.profile`, and the command `start-conda` in the job file.
- To enable `conda` for your jobs that use the C shell (`-S /bin/csh` or no `-S` option passed):
    - either add these two lines in your `~/.cshrc,`or
    - add these two lines in you job file, or
    - the first one in your `~/.cshrc` and the second in the job file


The most flexible method is to type the two lines each time you log in, and adding them to the jobs that need it. ### c. Miniconda


To install Miniconda:


- Download [the latest 64-bit installer.](https://docs.conda.io/en/latest/miniconda.html)
- Follow [these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to install it in your user space (or the Installing Miniconda on Hydra instructions).
    - The default location to unpack the software is your home directory.
    - This works well because `/home` is not scrubbed and the disk space needed by miniconda typically is within the user quotas for `/home`.
- After installation, you can use `conda` to install software and create `conda` environments.


##### Job Files


- To use software installed via `conda` in submitted jobs, you can create a personal module file to add your miniconda `bin` directory to your `PATH`.
    - Follow these instructions.


#### Using the `conda` command


- Instructions on how to use `conda`are in the Using Condapage.


Last update 02 Dec 2025 SGK/MPK

## Installing Miniconda on Hydra

Although using the pre-installed Anaconda with the `tools/conda` module requires the least efforts from the user, there may be cases where you want full control of the installation such as modifying the "base" environment. If that is the case, installing your own copy of Miniconda in your user space is an option.


#### Installing


- Where to install? We suggest your home directory: it's not scrubbed


1. Download: We want the Linux, 64-bit, Python3 installer found on this page: [https://docs.conda.io/en/latest/miniconda.html](https://docs.conda.io/en/latest/miniconda.html) (Note: We recommend getting the Python3 installer even if you need Python2 for some programs. You can setup a separate Python2 environment when needed.)


| `$ wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh` |
| --- |
2. Run installer. Make sure to enter "yes" to "running conda init":


| `$ sh Miniconda3-latest-Linux-x86_64.sh` 
`...` 
`Do you accept the license terms? [yes\|no]` 
`[no] >>> yes` 
`...` 
`[/home/user/miniconda3] >>> [press enter key]` 
`PREFIX=/home/user/miniconda3` 
`...` 
`Do you wish the installer to initialize Miniconda3` 
`by running conda init? [yes\|no]` 
`[no] >>>yes` |
| --- |
3. Log off Hydra and log back in.
4. Look for `(base)` at the beginning of your command prompt.
5. Test with: `which conda`


| `(base) $ which conda` 
`~/miniconda3/bin/conda` |
| --- |


If you don't see `(base)`, and your shell is `bash` (true for biology users) there may be an issue with a config file in your home directory.


You can fix this with: `nano ~/.bash_profile`and then append this text to the bottom of the file:


| `# Get the aliases and functions` 
`if [ -f ~/.bashrc ]; then` 
```. ~/.bashrc` 
`fi` |
| --- |


Log out and back in again to see if `(base)` is now at the beginning of your command prompt.


#### What did the installer do?


- `~/miniconda3/`: where all the conda programs are installed
- `~/.bashrc` (for `bash` users, this file is run when you start a new `bash` shell): a command has been appended to enable conda (modifying your `$PATH`) and changing your prompt.
- `~/.conda/` and `~/.condarc`: hidden directory and file with settings

## Using Conda



#### Packages


- A conda package is the precompiled program and a link to all of the required packages that will also be downloaded and needed.
- A whole pipeline can be defined in a package: all the scripts and dependent software (e.g. qiime2 or phyluce)
- Packages are created by people in the community and shared publicly. Sometimes they’re created by the software developer, but they’re often by users of the software.
- You can create your own packages which a great method for reproducible science and collaboration. We’re not covering that, but we can direct you to resources.


##### `conda` command


We'll be using the `conda` command for managing packages and controlling conda


###### Help with conda


- `conda help`
- `conda install --help`
    - You can consults the ['conda' command reference documentation](https://docs.conda.io/projects/conda/en/latest/commands.html), or
    - the [conda "cheat sheet."](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)


##### Listing installed packages


Some packages come pre-installed with either Anaconda or Miniconda (a lot more if you're using Anaconda), for Minconda:


```
(base)$ conda list
### packages in environment at /home/user/miniconda3:
#
### Name                    Version                   Build  Channel
_libgcc_mutex             0.1                        main
asn1crypto                1.2.0                    py37_0
ca-certificates           2019.10.16                    0
certifi                   2019.9.11                py37_0
cffi                      1.13.0           py37h2e261b9_0
chardet                   3.0.4                 py37_1003
conda                     4.7.12                   py37_0
conda-package-handling    1.6.0            py37h7b6447c_0
cryptography              2.8              py37h1ba5d50_0
...
```


##### How to find `conda` packages


You can search the public package repositories at [https://anaconda.org/](https://anaconda.org/) **What we suggest using**


- Use the anaconda.org search feature.
- Copy the install command from the package's page


Or do a web search: "conda r" or "bioconda mafft"


Or use `conda search "blast"` (finds packages with blast anywhere in their name in your current channels)


- Search for admixtools on [anaconda.org](http://anaconda.org)
    - Only available on bioconda
    - `conda install -c bioconda admixtools`
- Search for mafft on [anaconda.org](http://anaconda.org)
    - Available on multiple channels
    - `bioconda`, `conda-forge`, `anaconda`, `r` are reliable channels. You can try other popular ones.


##### Installing a package


`conda install ...` installs a packages and its dependencies


- It doesn’t matter what your current directory is, it will install in your "conda" directory!
- if you use the pre-installed version of Anaconda, you won't be able to install (or update) anything in the base environment,
    - you will need to create and active your own `conda` environment(s) first (see below) and you will see that name in lieu of `(base)` in the following examples.


```
(base)$ conda install -c bioconda mafft

The following packages will be downloaded:
...
The following NEW packages will be INSTALLED:
...
Proceed ([y]/n)? y
Preparing transaction: done
Verifying transaction: done
Executing transaction: done
```


Test it:


```
(base)$ mafft --help
------------------------------------------------------------------------------
  MAFFT v7.471 (2020/Jul/3)
  https://mafft.cbrc.jp/alignment/software/
  MBE 30:772-780 (2013), NAR 30:3059-3066 (2002)
------------------------------------------------------------------------------
```


##### Adding `bioconda` and `conda-forge` to your channels


```
(base)$ conda config --add channels defaults
(base)$ conda config --add channels bioconda
(base)$ conda config --add channels conda-forge
```


`conda config --get channels` shows your current channels


Which channel is the highest and which is the lowest?


```
$ conda config --get channels
--add channels 'defaults'   # lowest priority
--add channels 'bioconda'
--add channels 'conda-forge'   # highest priority
```


`conda-forge` is the highest, `defaults` is the lowest.


Note: the more channels you have, the increased time to "solve" installation.


```
(base)$ conda install iqtree

...
The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    ca-certificates-2020.6.20  |       hecda079_0         145 KB  conda-forge
    certifi-2020.6.20          |   py37hc8dfbb8_0         151 KB  conda-forge
    conda-4.8.3                |   py37hc8dfbb8_1         3.0 MB  conda-forge
    iqtree-2.0.3               |       h176a8bc_0         2.8 MB  bioconda
    openssl-1.1.1g             |       h516909a_0         2.1 MB  conda-forge
    python_abi-3.7             |          1_cp37m           4 KB  conda-forge
    ------------------------------------------------------------
                                           Total:         8.2 MB
...
```


##### `conda` install tricks


- Installing multiple items
    - `conda install mafft gblocks`
    - “It is best to install all packages at once, so that all of the dependencies are installed at the same time.” [https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)
- Specifying program versions
    - Show available versions with: `conda search python`
    - `conda install python=3`
    - `=3` matches the most recent version starting with `3`
    - `==3.7.5` matches exactly the version specified
    - `">3.7"` matches most recent version greather than 3.7 (in quotes because of the `>` which will interfere with the shell's redirection features)
    - `"<3.8"` matches most recent version less than 3.8 (in quotes because of the `<` which will interfere with the shell's redirection features)
    - See the [conda documentation](https://docs.conda.io/projects/conda-build/en/latest/resources/package-spec.html#package-match-specifications) for more information


#### Using conda in submitted jobs


There are a couple steps needed to utilize `conda` in your submitted jobs.


By default the installed programs won't be found.


##### If you want to use your Miniconda installation:


###### Create a module file


There is Hydra documentation about [creating module files here](custom-modules.md).


We'll set one up for your miniconda install. Module files are text files with instructions on how the current environment should be modified.


We suggest creating a directory in your home folder called `modulefiles` and creating a module called miniconda in that directory.


```
(base)$ mkdir ~/modulefiles
(base)$ cd ~/modulefiles
(base)$ nano miniconda
```


and then enter into the new text file:


```
#%Module1.0
prepend-path PATH /home/your_username/miniconda3/bin
```


Make sure to change `your_username` to your Hydra username!


###### Job file using your module file


Use the `module load` command followed by the path and name of your module file to load your module: `module load ~/modulefiles/miniconda`


Example job file using:


```
### /bin/sh
### ----------------Parameters---------------------- #
#$ -S /bin/sh
#$ -q sThC.q
#$ -l mres=2G,h_data=2G,h_vmem=2G
#$ -cwd
#$ -j y
#$ -N minicondatest
#$ -o minicondatest.out
#
### ----------------Modules------------------------- #
module load ~/modulefiles/miniconda
#
### ----------------Your Commands------------------- #
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
#
echo "Conda location:"
which conda

echo
echo "Installed packages:"
conda list

#
echo = `date` job $JOB_NAME done
```


Excerpt of `minicondatest.out`:


```
...
Conda location:
/home/user/miniconda3/bin/conda

Installed packages:
### packages in environment at /home/user/miniconda3:
#
### Name                    Version                   Build  Channel
...
```


##### If you use the pre-installed Anaconda or Miniconda


- No need to create a module
    - but you need to load the `tools/conda` module and run `start-conda`


Simply replace, in the examples above, the line


`module load ~/modulefiles/miniconda`


by the following two lines


`module load tools/conda`


`start-conda`


Even if you have these two lines in your `~/.bashrc` file. You can save typing the first line in your job file if you insert it in a file called `~/.profile`


- To enable `conda` for your jobs that use the C shell (`-S /bin/csh` or no `-S` option passed):
    - either add these two lines in your `~/.cshrc,`or
    - add these two lines in you job file, or
    - the first one in your `~/.cshrc` and the second in the job file.


If you need access to packages installed in an environment (see below) you will need to add the corresponding `conda activate` command, like in


`conda activate iqtree-v1`


#### Wait, there's one more concept to keep things clean... `environments`


So far all installs we've done have done into one set of packages called `(base)`.


What if programs have conflicting dependencies or you need different versions of the same program?


A `conda` Environment is a compartmentalized set of packages, and if you use the pre-installed Anaconda, it allows you to modify it (since you can't modify the pre-installed Anaconda base environment)


Also, the more packages you have, the longer it will take for conda on the "Solving Environment" step.


What if you wanted to have both iqtree1 and iqtree2 installed? Above we showed how to installed iqtree.


It installed the latest version: 2.0.3. If you also need iqtree 1.x installed, the conda command: `conda install iqtree=1` will downgrade your current iqtree from 2.x to 1.x, i*t won't allow you to have more than one version installed.*You can have environments to have access to the two versions. (Using `iqtree=1` will install the latest version of iqtree that starts with a 1).


##### Creating an environment


```
(base)$ conda create -n iqtree-v1
Collecting package metadata (current_repodata.json): done
Solving environment: done
#### Package Plan ##
  environment location: /home/user/miniconda3/envs/iqtree-v1
Proceed ([y]/n)? y

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
#
### To activate this environment, use
#
###     $ conda activate iqtree-v1
#
### To deactivate an active environment, use
#
###     $ conda deactivate
```


##### Adding packages to the environment


Although the output says to use `conda activate...`, we recommend using `source activate...` because it is compatible with job files submitted through `qsub`


```
(base)$ source activate iqtree-v1
(iqtree-v1)$ conda install iqtree=1
```


Note: you can create an environment and add packages do it in one step with: `conda create -n iqtree-v1 iqtree=1`


##### Using an environment in your job file


When submitting a job that uses a specific conda environment, you need to use `source activate ...` *after* you load your miniconda module.


Example script:


```
...
### ----------------Modules------------------------- #
module load ~/modulefiles/miniconda
source activate iqtree-v1
#
### ----------------Your Commands------------------- #
...
```


##### Removing an environment


To remove an environment and all of its packages:


You have to deactivate the environment before removing it


```
(iqtree-v1)$ conda deactivate
(base)$ conda remove -n iqtree-v1 --all

Remove all packages in environment /home/user/miniconda3/envs/iqtree-v1:

#### Package Plan ##

  environment location: /home/user/miniconda3/envs/iqtree-v1

The following packages will be REMOVED:
...
Proceed ([y]/n)? y
```


##### Useful environments: python2 and R


If you need to a use a program written in python2, you can create an environment with that version of Python


```
(base)$ conda create -n python2 python=2
(base)$ source activate python2
```


You can use conda to install R and R packages


```
(base)$ conda create -n tidyverse r r-tidyverse
(base)$ source activate tidyverse
```


##### When there isn't a `conda` package for a pipeline


Some pipelines don't have a conda package with all the requirements. You can use the program's documentation to install dependencies.


For example the [Hybpiper](https://github.com/mossmatters/HybPiper) pipeline doesn't have a conda package (you could create one and contribute it to bioconda...), but The [install instructions](https://github.com/mossmatters/HybPiper/wiki/Installation) list these requirements:


- Python 2.7 or later [We suggest python3 when possible -Hydra team]
- BIOPYTHON 1.59 or later
- EXONERATE
- BLAST command line tools
- SPAdes
- GNU Parallel
- BWA
- samtools


Use `conda` to install the dependencies for HybPiper in your `hybpiper` environment. You may need to look up package names at [anaconda.org](https://anaconda.org) or your favorite search engine. (Hint: pay special attention to GNU Parallel)


```
(base)$ conda create -n hybpiper install python=3 "biopython>1.59" exonerate blast spades parallel bwa samtools

Collecting package metadata (current_repodata.json): done
Solving environment: done

#### Package Plan ##

  environment location: /home/user/miniconda3/envs/hybpiper

  added / updated specs:
  - biopython[version='>1.59']
  - blast
  - bwa
  - exonerate
  - parallel
  - python=3
  - samtools
  - spades

The following packages will be downloaded:
...
The following NEW packages will be INSTALLED:
...
Proceed ([y]/n)? y
...
Downloading and Extracting Packages
...
```


Now that the dependencies are installed, you can download the scripts for HybPiper:


```
cd ~
git clone https://github.com/mossmatters/HybPiper.git
```


When you're done using an environment, you can go back to `(base)` with: `conda deactivate`


#### 4.Troubleshooting


Finding online help:


- Official conda website (it’s good): [https://docs.conda.io](https://docs.conda.io)
    - Specifically this page called [Conda Package Manager](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html)
- Web search with “conda” in it, e.g.: conda remove environment (this usually brings me to [docs.conda.io](http://docs.conda.io))
- [si-hpc\@si.edu](mailto:si-hpc@si.edu) email
- Thursdays Brown Bags (12-1pm, W107 conference room)


Reinstalling


- `mv ~/miniconda3 ~/miniconda3-old` (if you want to keep the old install) or `rm -rf ~/miniconda3` (to delete the old install)
- `rm -rf .condarc .conda`
- Edit ~/.bashrc
    - delete lines from `# >>> conda initialize >>>` to `# <<< conda initialize <<<`
- logout/back in


#### Advanced


- Installing packages using pip if not available on conda
- Exporting environment as environment.yml, and creating a simplified version for working on local computer
    - export: `conda env export > environment.yml`
    - import: `conda env create -f environment.yml`
    - This is how [qiime2 install](https://docs.qiime2.org/2019.10/install/native/) works


#### Appendix


##### Definitions


- conda: open source package management tool
- Anaconda®: commercial company that develops conda
- Anaconda: distribution of conda with many data science tools pre-bundled
- Miniconda: minimal distribution of conda, other packages can be added
- Channel: grouping of packages managed by one group (e.g. bioconda, conda-forge)


##### Channels


Major conda channels:


- `Main`: built and maintained by anaconda (setup by default)
- `R`: R and packages for it (setup by default)
- `Conda-Forge`: community contributions
- `Bioconda`: contributions from biological community, find packages on [https://bioconda.github.io](https://bioconda.github.io)


#### Additional commands


##### Remove packages


To remove a package from the current environment use `conda remove [package]`


##### Update packages


To update a specific package use `conda update [package]`. To update all packages in the current environment use: `conda update --all`


You can prevent `conda update --all` from updating some packages using these [instructions](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-pkgs.html#preventing-packages-from-updating-pinning)
