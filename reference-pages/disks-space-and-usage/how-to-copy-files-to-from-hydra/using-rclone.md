---
title: "Using rclone"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152313/Using+rclone"
---

- [rclone](https://rclone.org/) is utility that can be configured to work with many online file storage systems including Dropbox, Microsoft OneDrive or Google Drive (see the full list [here](https://rclone.org/#providers)).
- You can use rclone on Hydra with `module load tools/rclone`
- When authorizing rclone access to your Dropbox, OneDrive or GoogleDrive you can use the rclone AppID created by the program developers or create your own.
    - These instructions are for using the already created rclone App ID.
    - The rclone documentation suggests creating your own app if you experience throttling using the shared App ID.
    - See the rclone documentation links for Dropbox and OneDrive for more information.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)By default the rclone configuration file is `~/.config/rclone/rclone.conf`


### Configuring rclone for use with Dropbox


Full documentation is available here: [https://rclone.org/dropbox/](https://rclone.org/dropbox/)


To authorize rclone's access to your Dropbox account, start the configuration on Hydra, then move to a workstation with a graphical interface and finally finish on Hydra.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)If you need to deauthorize rclone's access, log in to your Dropbox account via a browser, go to Settings and then the Connected apps tab and remove rclone.


#### ***Part 1 (on Hydra)***


We are naming this connection to dropbox "db". That name will be used in the rclone commands to identify the configuration to be used for the file transfer.


```{.text title="on Hydra"}
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
 * Say Y if the machine running rclone has a web browser you can use
 * Say N if running rclone on a (remote) machine without web browser access
If not sure try Y. If Y failed, try N.
y/n> n
...
config_token>
```


#### ***Part 2 (on your workstation)***


**Leave rclone on Hydra running with the `config_token>` prompt up.**


Download and unzip the pre-compiled rclone version for your workstation OS: [https://rclone.org/downloads/](https://rclone.org/downloads/)


*On Mac or Linux systems:*


Open a new terminal window and navigate to the directory with the unzipped copy of rclone and enter this command:


```{.text title="on your Mac or Linux system"}
$ ./rclone authorize "dropbox"
```


*On Windows workstations:*


Open a new Command Prompt and navigate to the rclone directory


```{.text title="on your Windows PC"}
C:\> rclone authorize "dropbox"
```


A browser window will open where you should log in to your Dropbox account and authorize rclone's access to your account.


In the Terminal window, you will get an access token that you should then enter into the `config_token>` prompt on Hydra (the text to copy is about 150 characters).


```{.text title="on Hydra"}
config_token> {"access_token":"...","token_type":"bearer","expiry":"..."}

Configuration complete.

Keep this "db" remote?
y) Yes this is OK (default)
y/e/d> y

Current remotes:
Name                 Type
====                 ====
db                   dropbox

...
q) Quit config
e/n/d/r/c/s/q> q
```


### Configuring rclone for use with OneDrive


***rclone is currently not working with the Smithsonian's OneDrive because it needs to be authorized as an allowed app by the OneDrive administrators. A request to allow access has been requested. (2024-12-13)***


Like with the Dropbox configuration, this is done in two parts, first on Hydra with the `rclone config` command and then on your workstation by downloading and running a local copy of rclone and authorizing rclone's access to your cloud account.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)If you need to deauthorize rclone's access, open this page: [https://portal.office.com/account](https://portal.office.com/account) Select “App permissions” and then revoke "rclone".


#### ***Part 1 (on Hydra)***


Follow the steps shown above for the Dropbox setup, but choose the `Microsoft OneDrive` option. and choose a short name for the configuration like `od`.


Like with Dropbox, leave `client_id>` and `client_secret>` blank.


When prompted for the OneDrive close region, choose: `Microsoft Cloud Global`. There is an option `Microsoft Cloud for US Government`, but the Smithsonian does not use this system.


When you get to the `config_token>` prompt for authenticating with OneDrive on your workstation, continue to the section on your workstation, keeping rclone running on Hydra.


#### ***Part 2 (on your workstation)***


Follow the steps shown above for the Dropbox setup, but enter `rclone authorize "onedrive"` in your workstation's command prompt or terminal.


Paste the token result into Hydra (the text to copy is about **3500 characters**):


```{.text title="on Hydra"}
config_token> {"access_token":"...","token_type":"bearer","expiry":"..."}

Option config_type.
Type of connection
Choose a number from below, or type in an existing string value.
 1 / OneDrive Personal or Business
   \ (onedrive)
...
config_type> 1

y) Yes this is OK (default)
y/e/d> y
Choose a number from below, or type in an existing value
 1 / OneDrive Personal or Business
   \ "onedrive"
...
Your choice> 1

Option config_driveid.
Choose a number from below, or type in your own string value.
 1 / OneDrive (business)
   \ (...)
 2 / OneDrive (business)
   \ (...)

config_driveid> 1
Drive OK?
Found drive "root" of type "business"
URL: https://.../Documents
y) Yes (default)
n) No
y/n>y

Configuration complete.
Keep this "od" remote?
y) Yes this is OK (default)
e) Edit this remote
d) Delete this remote
y/e/d> y

Current remotes:
Name                 Type
====                 ====
od                   onedrive

q) Quit config
e/n/d/r/c/s/q> q
```


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) The URL returned at the choice of drive should end with `Documents`. If it ends with `PreservationHoldLibrary` , enter `n` and restart the rclone configuration choosing the other option.


### **Transferring files with rclone**


After you configured rclone with a cloud service you can use the rclone commands listed in the [online documentation](https://rclone.org/commands/).


#### ***Example 1: Copying to or from Hydra with [rclone copy](https://rclone.org/commands/rclone_copy/)***


```{.text title="rclone copy"}
# A single file from Hydra to a directory "hydra_backup" on a remote system
rclone copy /path/to/hydra/file db:hydra_backup

# An entire directory from Hydra to 'dest' on remote system
rclone copy /path/to/hydra/dir/ db:hydra_backup/dest

# From the remote directory to your Hydra home directory
rclone db:hydra_backup/file ~
```


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Replace `db` with the name of you used for your rclone configuration


#### ***Example 2: Syncing contents of a directory with [rclone sync](https://rclone.org/commands/rclone_sync/)***


```{.text title="rclone copy"}
# -i will prompt for each file to be copied or deleted
rclone -i sync /path/to/hydra/dir db:hydra_backup/dest
```


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Replace `db` with the name of you used for your rclone configuration
