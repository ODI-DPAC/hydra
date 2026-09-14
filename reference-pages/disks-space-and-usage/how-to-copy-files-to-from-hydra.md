---
title: "How to Copy Files to/from Hydra"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152307/How+to+Copy+Files+to+from+Hydra"
date-modified: "2021-10-08"
author: "SGK/PBF"
---

1. [From a Computer Running Linux](how-to-copy-files-to-from-hydra.md)
2. [From a Computer Running MacOS](how-to-copy-files-to-from-hydra.md)
3. [From a Computer Running Windows](how-to-copy-files-to-from-hydra.md)
4. Using Other Tools
    1. [Using Dropbox](how-to-copy-files-to-from-hydra/using-dropbox.md)
    2. [Using Firefox Send](how-to-copy-files-to-from-hydra/using-firefox-send.md)
    3. [Using rclone](how-to-copy-files-to-from-hydra/using-rclone.md)


## Remember


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) When copying to Hydra, especially large files, be sure to do it to the appropriate disk (and not `/home` or `/tmp`).


## 1. From a Computer running Linux


- You can copy files to/from `hydra` using `scp`, `sftp or rsync:`
    - to `Hydra` you can only copy from *trusted* hosts (computers on SI trusted network, or VPN'ed),
    - from `Hydra` to any host that allows external `ssh` connections (if you can `ssh` from Hydra to it, you can `scp`, `sftp and rsync` to it).
- For large transfers (over 70GB, sustained), we ask users to use `rsync`, and limit the bandwidth to 20 MB/s (70 GB/h), with the "`--bwlimit="` option:
    - `rsync --bwlimit=20000 ...` 
If this pose a problem, contact us.
    - Baseline transfer rate from SAO to HDC (Herndon data center) is around 600 Mbps, single thread, or ~72 MB/s or ~252 GB/h 
The link saturates near 500 Mbps (50% of Gbps) or 62 MB/s or 220 GB/h
- Remember that `rm`, `mv` and `cp` can also create high I/O load, so consider to
    - limit your concurrent I/Os: do not start a slew of I/Os at the same time, and
    - serialize your I/Os as much as possible: run one *after* the other.


### **NOTE** for SAO Users:


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Access from the "*outside*" to SAO/CfA hosts (computers) is limited to the*border control hosts* (l`ogin.cfa.harvard.edu` and `pogoN.cfa.harvard.edu`), instructions for tunneling via these hosts is explained on


- the CF's [SSH Remote Access](http://www.cfa.harvard.edu/cf/services/remote/ssh.html) page, or
- the HEAD Systems Group's [SSH FAQ](http://ihea-www.cfa.harvard.edu/HEAD-info/syshelp/web/ssh-faq.htm) page.


## 2.From a Computer Running MacOS


A trusted or VPN'd computer running MacOS can use `scp`, `sftp or rsync`:


- Open the `Terminal` application by going to `/Applications/Utilities` and finding `Terminal`. ![Terminal.app](../../assets/terminal.png)
- At the prompt, use `scp`, `sftp or rsync, after cd'ing to the right place.`
- For large transfers limit the bandwidth and use "`rsync --bwlimit=4000"`.


Alternatively you can use a GUI based `ssh/scp` compatible tool like [FileZilla](https://filezilla-project.org/). Note, `Cyberduck`is not recommended because it uses a lot of CPU cycles on Hydra.


You will still most likely need to run VPN.


## 3. From a Computer Running Windows


![(grey lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb.svg) You can use `scp`, `sftp or rsync` if you install [Cygwin](http://www.cygwin.org)- Note that Cygwin includes a X11 server.


Alternatively you can use a GUI based `ssh/scp` compatible tool like [FileZilla](https://filezilla-project.org/) or [WinSCP](https://winscp.net/eng/index.php). Note, `Cyberduck` is not recommended because it uses a lot of CPU cycles on Hydra.


You will still most likely need to run VPN.
