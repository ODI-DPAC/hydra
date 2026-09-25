# rclone and cloud storage

[rclone](https://rclone.org/) is a command-line program that copies files between a computer and cloud storage such as Dropbox, OneDrive, Google Drive, Amazon S3 and [many other services](https://rclone.org/#providers). On Hydra it is the module `tools/rclone`. It is the way to reach a cloud account from Hydra, and the way to get data onto Hydra from a computer that cannot connect to the login nodes, such as one on telework.si.edu.

Setting up a cloud account takes two places. rclone has to be authorized with the cloud service through a web browser, and the login nodes have none, so you run `rclone config` on Hydra, run `rclone authorize` on your own computer, and paste the result back into the Hydra session. The Dropbox walkthrough below shows every prompt. OneDrive differs in three answers, listed after it.

## Set up Dropbox

### On Hydra

Load the module and start the configuration. Answer the prompts as shown; `...` marks lines left out.

```text title="on Hydra"
$ module load tools/rclone
$ rclone config
n) New remote
n/s/q> n
name> db
Type of storage to configure.
...
12 / Dropbox
   \ (dropbox)
...
Storage> 12

OAuth Client Id
client_id> [leave blank]
OAuth Client Secret
client_secret> [leave blank]

Edit advanced config? (y/n)
y/n> n

Use web browser to automatically authenticate rclone with remote?
y/n> n
...
config_token>
```

Leave this session at the `config_token>` prompt and go to your own computer.

### On your own computer

Download rclone for your operating system from <https://rclone.org/downloads/> and unzip it. In a terminal (Terminal on macOS or Linux, Command Prompt on Windows), change to the unzipped directory and run:

```text title="on your computer"
$ ./rclone authorize "dropbox"
```

On Windows the command is `rclone authorize "dropbox"`, without the `./`.

A browser window opens on Dropbox's sign-in page. Sign in and allow rclone to access the account. The terminal then prints a token of about 150 characters, starting `{"access_token":`. Copy the whole of it.

### Back on Hydra

Paste the token at the waiting prompt and keep the remote:

```text title="on Hydra"
config_token> {"access_token":"...","token_type":"bearer","expiry":"..."}

Configuration complete.
Keep this "db" remote?
y/e/d> y

Current remotes:
Name                 Type
====                 ====
db                   dropbox

e/n/d/r/c/s/q> q
```

rclone saves the remote in `~/.config/rclone/rclone.conf`. If you later want to withdraw rclone's access, open Dropbox's [connected apps](https://www.dropbox.com/account/connected_apps) settings and remove it.

## Set up OneDrive

!!! warning "OneDrive at the Smithsonian requires an administrator to allow rclone"

    Since December 2024, rclone cannot connect to a Smithsonian OneDrive account until the OneDrive administrators add it as an allowed app. A request is open. Until it is granted, the steps below end with an authorization error.

The procedure is the Dropbox one with three differences.

1. In `rclone config`, choose the `Microsoft OneDrive` storage type and a short name such as `od`. Leave `client_id>` and `client_secret>` blank, as for Dropbox.

2. When rclone asks for the region, choose `Microsoft Cloud Global`. There is an option for `Microsoft Cloud for US Government`, but the Smithsonian does not use that system.

3. On your computer, run `rclone authorize "onedrive"` and sign in with your Smithsonian account. The token is longer, about 3,500 characters. After you paste it on Hydra, rclone asks which drive to use:

    ```text title="on Hydra"
    config_token> {"access_token":"...","token_type":"bearer","expiry":"..."}

    Option config_type.
    Type of connection
     1 / OneDrive Personal or Business
       \ (onedrive)
    ...
    config_type> 1

    Option config_driveid.
     1 / OneDrive (business)
       \ (...)
    config_driveid> 1
    Drive OK?
    Found drive "root" of type "business"
    URL: https://.../Documents
    y/n> y

    Configuration complete.
    Keep this "od" remote?
    y/e/d> y
    ```

To withdraw rclone's access, open <https://portal.office.com/account>, choose **App permissions**, and revoke rclone.

## Other services

Google Drive, Amazon S3 and the rest follow the same two-place pattern. rclone's page for each service shows its prompts, for example [Google Drive](https://rclone.org/drive/) and [S3](https://rclone.org/s3/). rclone's shared app ID works for most people. If the shared one is throttled, the page for the service says how to register your own.

## Copy and sync

List what is in the remote:

```console
$ rclone ls db:
```

Copy one file, or a directory, to the cloud:

```console
$ rclone copy results.tar db:hydra_backup/
$ rclone copy /scratch/genomics/USERNAME/project db:project/
```

Copy from the cloud to Hydra:

```console
$ rclone copy db:raw/ /scratch/genomics/USERNAME/raw/
```

Make the cloud copy match a directory on Hydra. `-i` asks before each change, which is worth keeping on until you trust the command:

```console
$ rclone sync -i /scratch/genomics/USERNAME/project db:project/
```

`--dry-run` on any command shows what it would do and does nothing. rclone runs on the login nodes, because they are the nodes with a route to the internet. A large copy can trip the login-node limits, so cap the rate with `--bwlimit 20M`, and run the copy inside `screen` or `tmux` so that it survives a dropped connection.

## Further reading

- [rclone documentation](https://rclone.org/docs/), for every command and option
- [Filesystems](../storage/filesystems.md), for where to put the data on Hydra
- [Warning emails](../jobs/efficiency.md#high-cpu-use-on-a-login-node), for the login-node limits
