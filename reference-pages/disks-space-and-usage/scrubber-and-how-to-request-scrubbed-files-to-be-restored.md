---
title: "Scrubber and How to Request Scrubbed Files to be Restored"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152322/Scrubber+and+How+to+Request+Scrubbed+Files+to+be+Restored"
date-modified: "2025-10-06"
author: "SGK/MK/PBF"
---

1. [Introduction - What is Scrubbing](scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)
2. [What Disks Are Scrubbed](scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)
3. [How to Access the Scrubber Tools](scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)
4. [How to Check what Will be Scrubbed](scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)
5. [How to Find out what Was Scrubbed](scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)
6. [How to Request Scrubbed Files to be Restored](scrubber-and-how-to-request-scrubbed-files-to-be-restored.md)


## 1.Introduction - What is Scrubbing?


In order to maintain free disk space on the public disks, we use a disk scrubber to remove old files and old empty directories.


The scrubber is run on a weekly basis, it deletes old empty directories, but old files are, at first, moved away in a staging location, then *permanent*ly deleted some 10 days later.


::: {.note title="Please Note"}
Since the scrubber moves old files away at first, and delete them later,


- there is a grace period between the scrubbing (move) and the *permanent* deletion to allow users to request for some scrubbed files to be restored;
- reasonable requests to restore scrubbed files must be be sent no later than the Friday following the scrubbing, by 5pm;
- scrubbed files still "count" against the user quota until they are *permanent*ly deleted;
- one *permanent*ly deleted (aka zapped) the files can no longer be restored.


Requests to restore scrubbed file should be


- rare,
- reasonable (*i.e.* no blanket request), and,
- can only be granted while the scrubbed files are not yet *permanently* deleted.


Past the grace period, the files are no longer available, hence users who want their scrubbed files restore have to act *promptly*.
:::


## 2. What Disks Are Scrubbed


The disks that are scrubbed are:


- `/scratch/public/{biology|genomics|nasm|sao}- 180 days old files/empty directories`
    - `/scratch/genomics` is the same as `/scratch/public/genomics`, etc.


## 3. How to Access the Scrubber's Tools


To access the scrubber tools, you need to load the module:


`module load tools/scrubber`


- to get the list of tools, use:


`module help tools/scrubber`


- to get the man page, accessible after loading the module, use:


`man <tool-name>`


## 4. How to Check what Will Be Scrubbed


- To check what files will be scrubbed, use: 
 
`find-scrub [-in <dir>] [-age <age>]` 

this will look for files older than <age> days in <dir>, by default dir=current working directory, and age=173 or 83 days.
- This search taxes the file system (aka disk server), especially if you have a lot of files, so use as needed only.


## 5. How to Find Out what Was Scrubbed


You will receive an email if any of your files were scrubbed.


- To look at the report for what was scrubbed on Sunday Jun 16 2024 under `/scratch/public/genomics/kweskinm`:


`show-scrubber-report /scratch/public/genomics/kweskinm 240616`


- To find out which old empty directories where scrubbed:


`list-scrubbed-dirs [-long|-all] /scratch/public/genomics/kweskinm 240616 [<RE>|-n]`


where the <RE> is an optional regular-expression to limit the printout, w/o an RE your get the complete list, unless you specify -n and you get the number of scrubbed directories.


The -long or -all option allows you to get more info (like age, size and owner)


- To find out which old files where scrubbed:


`list-scrubbed-files [-long|-all] /scratch``/public/genomics/kweskinm 240616 [<RE>|-n]`


where again the <RE> is an optional regular-expression to limit the printout, w/o an RE your get the complete list, unless you specify -n and you get the number of scrubbed files;


the `-long` option will produce a list that includes the files' age and size, -all will list age, size and owner.


- ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) The <RE> (regular expressions) are PERL-style RE:
    - `.` means any char,
    - `.*` means any set of chars,
    - `[a-z]` means any single character between `a` and `z,`
    - `^` means start of match,
    - `$` means end of match, etc ([see gory details here](http://perldoc.perl.org/perlre.html#Regular-Expressions)).
- for example:


`'^/scratch/public/genomics/blah/project/.*\.log$'`


means all the files that end in`'.log'`under `'/scratch/public/genomics/blah/project/'`


## 6. How to Request Scrubbed Files to be Restored


In order to request that some of your scrubbed files be restored, you need to create a list of files, *trimmed it down to what you really need,* and verify that list.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) We do not accept bulk restore requests.


To produce the list of files to restore (that in this example were under `/scratch/public/genomics/kweskinm/big-project`), follow these steps:


1. Load the scrubber module (under tools): 
`module load tools/scrubber`
2. Create a list (use the appropriate path): 
`list-scrubbed-files /scratch/public/genomics/kweskinm 240721 > restore.list` to get a list of all the files scrubbed on Sunday Jul 21 2024, or for example: 
`list-scrubbed-files /scratch/public/genomics/kweskinm 240721 /scratch/public/genomics/kweskinm/big-project/ > restore.list` 
 to get a list all the scrubbed files under `'big-project/`' and in both cases save the list in the file 'r`estore.list' (`in the current working directory). 
 
![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Note that `/scratch/public/genomics/kweskinm/big-project` means `/scratch/public/genomics/kweskinm/big-project*`, not `/scratch/public/genomics/kweskinm/big-project/`
3. Edit the file '`restore.lis`t' to trim it down to what you really need, with any text editor (like `vi, nano, emacs`, etc);
4. Verify the '`restore.list`' file: 
`verify-restore-list /scratch/public/genomics/kweskinm 240721 restore.list` 
 or, to get more info 
`verify-restore-list -d /scratch/public/genomics/kweskinm 240721 restore.list` 
if the verification produced an error, edit the file accordingly.
    - You need a separate restore file per scrubbed date and per disk (i.e., `/scratch`vs `/scratch`)
5. Only then, and if the verification produced no error, submit your scrubbed file restoration request as follow:
    - SAO users: email the location of the list file(s) to [hpc\@cfa.harvard.edu](mailto:hpc@cfa.harvard.edu)
    - non-SAO users: email the location of the list file(s) to [SI-HPC\@si.edu](mailto:SI-HPC@si.edu)
        - While you can email the list file(s) themselves, it is more a lots more convenient for us if these list files are already somewhere on Hydra.


You can also consult the man pages for the `list-scrubbed-files` and `verify-restore-list` commands, as follows:


`module load tools/scrubber`


`man list-scrubbed-files`


`man verify-restore-list`


The restored files will not be scrubbed for another 180 days:


- 
    - check with `ls -lc filename` or `stat filename` on a restored file, it is the `ctime` (change time) that matters.
