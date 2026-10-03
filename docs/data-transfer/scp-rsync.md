# scp, sftp and rsync

**scp**, **sftp** and **rsync** are the standard Unix tools for copying files over an ssh connection. `scp` copies files with a single command. `sftp` opens a session in which you move around and copy files one at a time. `rsync` copies whole directories and, on a second run, only what has changed. Hydra's login nodes accept all three from any computer on the Smithsonian network or the SI VPN. Graphical clients such as WinSCP and FileZilla use the same protocol and work the same way. From Hydra outward, the same tools reach any host that accepts an ssh connection from the login nodes.

The three tools are installed by default on macOS and Linux. Windows 10 (version 1803 and later) and Windows 11 include `scp` and `sftp`. `rsync` is not part of Windows. Use it through the Windows Subsystem for Linux (WSL), or use a graphical client instead.

!!! tip "Use rsync for anything over about 70 GB"

    `rsync` can resume an interrupted copy and limit its own speed. For large transfers we ask you to cap the rate at 20 MB/s (about 70 GB per hour) with `--bwlimit=20000`, so that one transfer does not fill the link for everyone. If that limit is a problem for your work, email [SI-HPC@si.edu](mailto:SI-HPC@si.edu).

Give every transfer a destination under `/scratch` or `/data`. The home directory has a small quota, and `/tmp` is small and shared.

## Copy files with scp

Open a terminal. On macOS that is Terminal, in `/Applications/Utilities`. On Windows it is Command Prompt or PowerShell. Use `cd` to go to the directory the files are in.

Copy one file to a directory on Hydra:

```console
$ scp -p results.tar USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/
```

Copy several files at once, with a wildcard:

```console
$ scp -p reads_*.fastq.gz USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/
```

Copy a file from Hydra to the current directory on your computer:

```console
$ scp -p USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/results.tar .
```

Copy several files from Hydra with a wildcard. The quotes make Hydra expand the wildcard rather than your own shell.

```console
$ scp -p 'USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/*.log' .
```

The destination directory must exist. `-p` keeps the files' modification times, which is useful when you later want to know which copy is newer. `man scp` lists the other options.

## Copy or synchronise with rsync

`rsync` copies only the files that are new or have changed since the last run. A second run after an interruption finishes the job rather than starting over, and a run over a directory you have already copied moves only what you changed.

Copy a directory to Hydra, at a limited rate:

```console
$ rsync -avz --bwlimit=20000 project/ USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/
```

Copy results back from Hydra:

```console
$ rsync -avz USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/results/ results/
```

See what a run would copy without copying anything:

```console
$ rsync -avzn project/ USERNAME@hydra-login01.si.edu:/scratch/genomics/USERNAME/project/
```

The options mean the following. `-a` copies directories recursively and keeps permissions and times. `-v` lists each file as it goes. `-z` compresses in transit. `-n` is the dry run. A trailing slash on the source copies the directory's contents. Without it, `rsync` copies the directory itself into the destination. `man rsync` covers the rest.

## Use sftp

`sftp` opens a session on Hydra and takes commands, which suits a few files here and there.

```console
$ sftp USERNAME@hydra-login01.si.edu
sftp> cd /scratch/genomics/USERNAME/project
sftp> put results.tar
sftp> get summary.csv
sftp> exit
```

You will use four commands most. `cd` changes the directory on Hydra. `lcd` changes the directory on your computer. `put` uploads a file and `get` downloads one. `man sftp` lists the rest.

## Use WinSCP on Windows

[WinSCP](https://winscp.net/) is a free Windows program that copies files by drag and drop over sftp.

1. In the Login window, set the file protocol to SFTP, the host name to `hydra-login01.si.edu`, the port to 22, and your Hydra username. Leave the password blank and click **Login**:

    ![WinSCP session settings with the host, port and username filled in](../assets/winscp00.jpg)

2. Accept the host key the first time. Then enter your Hydra password when the login dialog asks for it:

    ![WinSCP asking for the password while connecting](../assets/winscp0.jpg)

3. Your computer is in the left pane and your Hydra home directory in the right. Navigate the right pane to a directory under `/scratch` or `/data` before copying anything:

    ![WinSCP with a local directory on the left and a Hydra home directory on the right](../assets/winscp1.jpg)

4. Drag files between the panes to copy them. The Transfer Settings bar shows progress:

    ![WinSCP after a transfer, both panes listed](../assets/winscp2.jpg)

WinSCP can also show only the Hydra side ("Explorer" mode), in which case you drag files from Windows File Explorer. Its Preferences say which.

## Use FileZilla on any system

[FileZilla](https://filezilla-project.org/) is a free client for macOS, Windows and Linux. The screenshots are from a Mac. The other systems look the same.

1. In the Quickconnect bar, enter the host `hydra-login01.si.edu`, your Hydra username, your password and port 22, then click **Quickconnect**:

    ![The FileZilla Quickconnect bar with the host, username, password and port filled in](../assets/Screen_Shot_2018-02-21_at_9.54.56_AM.png)

2. The first time, FileZilla asks whether to save passwords. Choose **Do not save passwords**:

    ![The FileZilla dialog asking whether to remember passwords](../assets/Screen_Shot_2018-02-21_at_9.49.14_AM.png)

3. Accept the host key when FileZilla shows it. Tick **Always trust this host** so it does not ask again:

    ![The FileZilla unknown host key dialog](../assets/Screen_Shot_2018-02-21_at_9.49.32_AM.png)

4. Your computer is on the left and Hydra on the right. Navigate the right side to a directory under `/scratch` or `/data`, or type the path into the **Remote site** box, then drag files between the two sides:

    ![FileZilla with a local directory on the left and a Hydra directory on the right](../assets/Screen_Shot_2018-02-21_at_9.50.53_AM.png)

We do not recommend Cyberduck. It keeps a process busy on the login node, and the login-node limits then kill it.

## Keep the load down

`rm`, `mv` and `cp` on thousands of files load the file servers as much as a transfer does. Run large file operations one after another rather than several at once. Anything that takes more than a few minutes on a login node should run under `qrsh` or as a job instead. See [Start an interactive session](../interactive/qrsh.md).

## Further reading

- [Filesystems](../storage/filesystems.md) for the partitions and their quotas
- [Globus](globus.md) for transfers too large or too long for `rsync`
- [Logging in and passwords](../getting-started/login.md) for ssh keys, which let `scp` and `rsync` run without a password
