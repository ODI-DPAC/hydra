---
title: "Conda: Anaconda & Miniconda"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152340/Conda+Anaconda+Miniconda"
---

1. [Introduction](conda-anaconda-miniconda.md)
2. [Anaconda, Miniconda, Miniforge/mamba](conda-anaconda-miniconda.md)?
    1. [Do NOT Mix and Match](conda-anaconda-miniconda.md)
    2. [Pre-installed conda or mamba](conda-anaconda-miniconda.md)
    3. [Miniconda](conda-anaconda-miniconda.md)
3. [Conda](conda-anaconda-miniconda.md)


# 1. Introduction


Conda is a free & open-source package and environment management system, see [conda.io](https://docs.conda.io/en/latest/):


- It was started by the Python community (hence the snake name reference) to help handling the plethora of Python packages,
    - but it has been extended to support any languages (*Python, R, Ruby, Lua, Scala, Java, JavaScript, C/ C++, FORTRAN*) and to manage the OS environment.
- It is used by a large community in data science and biology.
- It requires no elevated (admin/root) privileges to install software and/or create "environments", if used properly and works under different OSes.
- Conda main development is carried out by a commercial company, Anaconda, that offers free and paid versions; the free version works great.
- There are two free versions:
    1. The full fledge version, [Anaconda](https://anaconda.org/).
    2. A small, bootstrap version of Anaconda, called [Miniconda.](https://docs.conda.io/en/latest/miniconda.html)


# 2. Anaconda, Miniconda, Miniforge?


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


## a. Do NOT Mix and Match


::: {.note title="WARNING"}
You cannot mix and match Miniconda, Anaconda or pre-installed conda


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) If you have installed your own Miniconda or Anaconda, you may have executed:


`% conda init`


If you did, you will have stuff like this


`# >>> conda initialize >>>` 
`# !! Contents within this block are managed by 'conda init' !!`


`...`


`# <<< conda initialize <<<`


in your `~/.bashrc` file.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) While this is convenient if you always use that same `conda` (your Miniconda, your Anaconda or the pre-installed Anaconda), it does not allow you to *safely* use a different one.


- If you want to be able to switch to a different `conda` , delete these lines from your `~/.bashrc` file.
- You can re-execute `conda init` after switching.
- If you want to be able to switch back and forth, delete these lines and do not execute `conda init` (see below for recommended usage of the pre-installed full-fledged Anaconda).
:::


## b. Pre-installed conda and mamba


![(star)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/star_yellow.svg) This is the most direct way to start using `conda` on Hydra as it uses a module that is already setup on the system.![(star)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/star_yellow.svg)


- You can access the pre-installed conda simply by loading the `tools/conda` module and enabling `conda` with the command `start-conda`
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


### Job files


- To enable `conda` for your jobs that use the Bourne shell (`-S /bin/sh` )
    - either add these two lines in your job file, or
    - add the fist line in a file called `~/.profile`, and the command `start-conda` in the job file.
- To enable `conda` for your jobs that use the C shell (`-S /bin/csh` or no `-S` option passed):
    - either add these two lines in your `~/.cshrc,`or
    - add these two lines in you job file, or
    - the first one in your `~/.cshrc` and the second in the job file


![(star)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/star_yellow.svg) The most flexible method is to type the two lines each time you log in, and adding them to the jobs that need it. ![(star)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/star_yellow.svg)


## c. Miniconda


To install Miniconda:


- Download [the latest 64-bit installer.](https://docs.conda.io/en/latest/miniconda.html)
- Follow [these instructions](https://conda.io/projects/conda/en/latest/user-guide/install/index.html) to install it in your user space (or the [Installing Miniconda on Hydra](conda-anaconda-miniconda/installing-miniconda-on-hydra.md) instructions).
    - The default location to unpack the software is your home directory.
    - This works well because `/home` is not scrubbed and the disk space needed by miniconda typically is within the user quotas for `/home`.
- After installation, you can use `conda` to install software and create `conda` environments.


### Job Files


- To use software installed via `conda` in submitted jobs, you can create a personal module file to add your miniconda `bin` directory to your `PATH`.
    - Follow [these instructions.](https://confluence.si.edu/display/HPC/Using+Conda)


## 3. Using the `conda` command


- Instructions on how to use `conda`are in the [Using Conda](conda-anaconda-miniconda/using-conda.md)page.


Last update 02 Dec 2025 SGK/MPK
