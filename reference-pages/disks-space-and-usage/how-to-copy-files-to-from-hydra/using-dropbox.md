---
title: "Using Dropbox"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152309/Using+Dropbox"
date-modified: "2024-06-06"
author: "SGK/PBF"
categories: ["hydra7"]
---

- The `dropbox_uploader` module was removed: neither versions we tried are working any longer.
    - we recommend users switch to `rclone.`


We will re-install `dropbox_loader` if we figure out how to make it work again.


- Files can be exchanged with Dropbox using the script [Dropbox-Uploader](https://github.com/andreafabrizi/Dropbox-Uploader), which can be loaded using the `tools/dropbox_uploader` module and running the `dropbox` or `dropbox_uploader.sh` script.
- Running this for script for the first time will give instructions on how to configure your Dropbox account and create a `~/.dropbox_uploader` configuration file with authentication information.
- Using this method will not sync your Dropbox, but will allow you to upload/download specific files.
