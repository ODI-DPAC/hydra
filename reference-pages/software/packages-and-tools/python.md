---
title: "Python"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152338/Python"
categories: ["hydra7"]
---

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


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)If you are looking for the versions with all the usual packages, use the `tools/python`one. This list will vary as we install new versions.


# Package Installation and Management


We have installed a long list of packages with the Anaconda versions.


You can view that list with (after loading the appropriate module)


`% module load tools/python`


`% pip list`


You can install additional packages without elevated (admin/root) privileges with


`% pip install --user <package-name>`


Alternatively you can use `conda` to manage your Python packages and beyond that manage your environment - rather than using module files.


- If you only need a handful of packages that have no incompatibilities with the ones already installed and
- you can use one of the available python version you may chose not to bother with `conda,`and use`pip install --user.`
- For further explanations on Anaconda and Miniconda and instructions on using `conda`, consult the [Conda: Anaconda & Miniconda page.](conda-anaconda-miniconda.md)


# Python Multi-Threading (NUMPY and others)


- By default, `NUMPY,`as well as other packages, are built to use multi-threading, namely some numerical operations will use all the available CPUs on the node it is running on.
    - ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) This is *NOT* the way to use a shared resource, like Hydra,
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


## Example


```{.text title="demo-mthread-numpy.job"}
#
# this example uses 4 threads
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
