---
title: "Installing Miniconda on Hydra"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152341/Installing+Miniconda+on+Hydra"
date-modified: "2021-11-19"
author: "MPK/SGK"
---

Although using the pre-installed Anaconda with the `tools/conda` module requires the least efforts from the user, there may be cases where you want full control of the installation such as modifying the "base" environment. If that is the case, installing your own copy of Miniconda in your user space is an option.


### Installing


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


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) If you don't see `(base)`, and your shell is `bash` (true for biology users) there may be an issue with a config file in your home directory.


You can fix this with: `nano ~/.bash_profile`and then append this text to the bottom of the file:


| `# Get the aliases and functions` 
`if [ -f ~/.bashrc ]; then` 
```. ~/.bashrc` 
`fi` |
| --- |


Log out and back in again to see if `(base)` is now at the beginning of your command prompt.


### What did the installer do?


- `~/miniconda3/`: where all the conda programs are installed
- `~/.bashrc` (for `bash` users, this file is run when you start a new `bash` shell): a command has been appended to enable conda (modifying your `$PATH`) and changing your prompt.
- `~/.conda/` and `~/.condarc`: hidden directory and file with settings
