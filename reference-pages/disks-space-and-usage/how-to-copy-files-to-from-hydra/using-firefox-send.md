---
title: "Using Firefox Send"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152311/Using+Firefox+Send"
date-modified: "2021-10-11"
author: "SGK/PBF"
---

- [Firefox Send](https://send.firefox.com/) is was a free online file-sending service (or a file exchange mechanism).
- Using this system along with the command [ffsend](https://gitlab.com/timvisee/ffsend) available on Hydra (`module load tools/ffsend`), you can transfer files to/from Hydra *without needing VPN*.
- Firefox Send is a two-step process,
    1. you first upload a file (or a set of files packed in an archive) to the Firefox Send server which will generate a unique URL for the upload, and
    2. you download the file using that URL and recover the file's original name.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) While Firefox discontinued this service, you can still use it, using Tim Visée replacement, at [https://send.vi.ee](https://send.vi.ee) ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg)


You can upload up to 1GB at a time, and if you sign up for a Firefox account, that limit increases to 2.5GB.


Optional: `ffsend` has options for setting a password and expiration. See `ffsend help` for more information.


## Example 1: Sending *to* Hydra


### a. Uploading files from your local machine (workstation/laptop) using the Send website:


1. Open the [Firefox Send website](http://send.firefox.com/) (`send.vis.ee`) from any browser.
2. Choose a file to upload, and optionally:
    1. use `tar`, `zip` etc. to upload an archive of several files.
    2. modify the expiration of the file (number of downloads or number of days), the default is to allow only one download and it expires within one day.
    3. add a password that's needed to download the file.
3. Copy the URL generated for your upload.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) You need to save that unique URL to get that file later. Unlike Dropbox or Google Drive, Firefox Send will not show you what you uploaded.


### b. Downloading on Hydra from Firefox Send using `ffsend`


```{.text title="on Hydra"}
$ module load tools/ffsend
$ ffsend download https://send.vis.ee/download/7800f8272ba5ef7b/#cNSwgMaNqmdsdwG6RxM71A
Download complete
```


## Example 2: Sending *from* Hydra


### a. Uploading from Hydra using `ffsend`


```{.text title="on Hydra"}
$ module load tools/ffsend
$ ffsend upload test.tar.gz                                                                         
Upload complete                                                                                                               
https://send.vis.ee/download/0324d02485dc9a02/#cxER28yNyf2dcwzwfIla6g
```


### b. Downloading to your local machine (workstation/laptop)


Open the URL created on Hydra in a web browser to download the file to your local machine.


## Notes


- while `send.firefox.com` was discontinued, a workaround is to use `--host``https://send.vis.ee` (see [https://gitlab.com/timvisee/ffsend/-/issues/101](https://gitlab.com/timvisee/ffsend/-/issues/101).)
- as of version 0.2.65, `ffsend` will use `send.vis.ee` instead of the defunct `send.firefox.com`
- We have modified the module `bioinformatics/``ffsend` to include two aliases:
    - `ffupload`, aliased to "`ffsend upload`", and
    - `ffdownload`, aliased to "`ffsend``download`".
- We will not change the `ffupload` alias to revert to using `moz://a` since they discontinued the service.
