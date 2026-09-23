# Logging in and passwords

You reach Hydra with an ssh client from a computer on the Smithsonian network or the SI VPN, or through a web terminal on telework.si.edu. This page covers both, and how to change or reset your password.

## Where you can connect from

The login nodes are `hydra-login01.si.edu` and `hydra-login02.si.edu`; either can be used. They accept connections only from:

- a computer on the Smithsonian network,
- a computer connected to the SI VPN ([VPN authentication instructions](https://smithsonianprod.servicenowservices.com/si?sys_kb_id=e2996a031b79ae50e5c0657ae54bcb5d&id=kb_article_view&sysparm_rank=1&sysparm_tsqueryId=b8c7ecb2cf9f43500b16fb152f851cc6)), or
- the web terminal on [telework.si.edu](https://telework.si.edu/), which works from anywhere.

!!! warning "Three failed logins lock the account for 15 minutes"

    Wait 15 minutes before trying again. Retrying during the lockout restarts it.

## Log in

Replace `USERNAME` with your Hydra username from your welcome email, in lower case.

=== "macOS and Linux"

    Open a terminal (on macOS, Terminal is in `/Applications/Utilities`) and run:

    ```bash
    ssh USERNAME@hydra-login01.si.edu
    ```

    The first time you connect, ssh asks you to confirm the host key. Type `yes`.

    ```text
    The authenticity of host 'hydra-login01.si.edu' can't be established.
    RSA key fingerprint is ...
    Are you sure you want to continue connecting (yes/no)? yes
    ```

    At the `Password:` prompt, type your password. Nothing is echoed while you type.

=== "Windows"

    Windows 10 (1803 and later) and Windows 11 include ssh. Open Command Prompt or PowerShell from the Start menu and run:

    ```bash
    ssh USERNAME@hydra-login01.si.edu
    ```

    The first time you connect, ssh asks you to confirm the host key. Type `yes`.

    ```text
    The authenticity of host 'hydra-login01.si.edu' can't be established.
    RSA key fingerprint is ...
    Are you sure you want to continue connecting (yes/no)? yes
    ```

    At the `Password:` prompt, type your password. Nothing is echoed while you type.

    If you see `'ssh' is not recognized as an internal or external command`, use [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) instead: download `putty.exe` (no installer needed), start it, enter `USERNAME@hydra-login01.si.edu` as the Host Name, and click Open. Accept the host key warning the first time.

    ![PuTTY configuration window with the host name filled in](../assets/putty-config.png)

=== "Web browser (telework)"

    1. Sign in at [telework.si.edu](https://telework.si.edu/).
    2. Expand **IT Tools** and choose **Hydra** (type `hydra` in the search box to find it).
    3. Choose one of the **Web SSH terminal (WeTTY)** links.
    4. Enter your Hydra username at the `login:` prompt and your password at the `password:` prompt.

    ![WeTTY web terminal on telework.si.edu](../assets/wetty.png)

You are logged in when the prompt changes to:

```text
[USERNAME@hydra-login01 ~]$
```

## Log in without a password

On macOS and Linux you can use an ssh key pair instead of a password. Generate a key with `ssh-keygen`, then copy the public key to Hydra:

```bash
ssh-copy-id USERNAME@hydra-login01.si.edu
```

Do the same for `hydra-login02.si.edu`, or add both nodes to `~/.ssh/config` on your computer.

## Passwords

The initial password must be changed when the account is created, and every 180 days after that. An email notification is sent before a password expires. Change it before then, using either method below; email requests for a reset are handled only after the self-service grace period has passed.

!!! note "Password requirements"

    At least 12 characters, with at least one digit, one upper-case letter, one lower-case letter and one special character. A new password must not be similar to a previous one.

### Change your password from the command line

While your password is still valid, log in and run `passwd`:

```console
$ passwd
Changing password for user USERNAME.
(current) LDAP password:
New password:
Retype new password:
```

The change applies to both login nodes immediately.

### Change or reset your password on the self-service page

The self-service page handles both a change (you know the current password) and a reset (you don't), including up to 14 days after the password has expired.

1. Open the page. From the SI network or VPN, go directly to <https://hydra.si.edu/ssp/>. From telework.si.edu, choose **Hydra** under IT Tools, then **Change Password on Hydra-7** or **Reset Password on Hydra-7**.
2. To reset, enter your Hydra username and click **Send**. A link is emailed to your canonical address, usually the one ending in `.edu`.
3. Follow the link. From telework, paste it into the **Enter internal resource** box on the telework home page instead of opening it directly.

    ![The internal resource box on the telework home page](../assets/Screenshot_2024-05-24_at_9.54.56_AM.png)

4. Enter your new password.

### After the 14-day grace period

Once a password has been expired for more than 14 days the account is locked. Email [SI-HPC-Admin@si.edu](mailto:SI-HPC-Admin@si.edu) to request a reset; you will receive instructions at your work email address.
