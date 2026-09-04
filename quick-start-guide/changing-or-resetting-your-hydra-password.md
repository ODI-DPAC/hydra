---
title: "Changing or Resetting your Hydra Password"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152226/Changing+or+Resetting+your+Hydra+Password"
date-modified: "2025-03-05"
author: "SGK/MK"
categories: ["hydra7"]
---

You can change your password either:


- [Logging in into hydra and using CLI](changing-or-resetting-your-hydra-password.md) (command line interface), *before it expires;*
- [Using the Self-Serve Web Page](changing-or-resetting-your-hydra-password.md) (*up to 14-days after it expired*).


You can reset your password as follows:


- [Using the Self-Serve Web Page](changing-or-resetting-your-hydra-password.md) (*up to 14-days after it expired*).


Past the 14 days grace period:


- You need to email to [si-hpc-admin\@si.edu](mailto:si=hpc-admin@si.edu) to request a password reset. Once your password is reset, you will receive an email with instructions.


Emails are sent to your work/canonical email account.


::: {.note title="Note:"}
The material on this page is part of the Quick Start Guide and is not exhaustive. For more details, please see the [Reference Pages](../reference-pages.md).
:::


**Passwords must be changed when your account is created and every 180 days thereafter.**


::: {.note title="Note"}
- You will receive an email notification to change your password before it expires.
- Please change it before it expires. See below how to change or reset it *yourself*, see below.
- *Do not send us an email requesting to have it reset, use the Self-Serve web page*.
:::


## Changing your Password using CLI (command line interface)


1. Log into `hydra-login01.si.edu` or `hydra-login02.si.edu` (using `ssh`or an ssh client).
2. At the command prompt use the `passwd` command, as follows:


```
[username@login-30-1 ~]$ passwd
Changing password for user username.
(current) LDAP password:
New password:
Retype new password:
```


Since we use LDAP, this is it!


::: {.note title="Note the following restrictions:"}
Passwords must conform to SI password policies and meet the following requirements:


1. at least 12 characters in length, and include at least:
 1. one digit,
 2. one upper case,
 3. one lower case, and
 4. one special character.
2. moreover, new passwords cannot be too similar to old passwords.
:::


## Resetting or Changing your Password via the Self-Serve Web Page


- If you need your password to be reset go to the Self-Serve Password Page either
    - directly at this URL: [https://hydra.si.edu/ssp/?action=sendtoken](https://hydra.si.edu/ssp/?action=sendtoken) (VPN or trusted computers), or
    - via the [telework.si.edu](https://telework.si.edu) site:
        - click on the "Hydra" button under IT Tools (you can type hydra in the search bar to find it)
        - and then choose
            - "Change Password on Hydra-7"


or


- 
    - 
        - 
            - "Reset Password on Hydra-7"


- Type in your username on Hydra and click "Send"
    - you will receive a link via email (to your *canonical*email, the one ending in `.edu` in most cases).


- If you are on an office network or on VPN:
    - follow that link to enter your new password;
- If you are using telework:
    - return to the main [telework.si.edu](https://telework.si.edu) page and paste the link in the email in the "Enter internal resource" text box, i.e.: 
![](../assets/Screenshot_2024-05-24_at_9.54.56_AM.png)


1. [That same page](https://hydra-7.si.edu/ssp/index.php) also allows you to change your password, by entering your current one and the new one.
    1. Note that there is a 14-day grace period to allow you to change your password *after it expires* before your account gets locked.
