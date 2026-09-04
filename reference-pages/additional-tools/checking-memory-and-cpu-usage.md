---
title: "Checking Memory and CPU Usage"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/374604074/Checking+Memory+and+CPU+Usage"
date-modified: "2025-10-23"
author: "SGK"
categories: ["hydra7"]
---

- `plot-qmemuse:`a tool to plot the memory and CPU usage of jobs that ran recently or are running in the high memory queues.
- We monitor the jobs running in the high-memory queue, taking a usage snapshot every five minutes. This tool only applies to jobs in the high-memory queues
- The resulting statistics can be used to visualize the resources usage of a given job with the command `plot-qmemuse`, using


`% plot-qmemuse <jobid>`


``or


`% plot-qmemuse <jobid>.<taskid>`


For that command to run, you must load the `gnuplot module` first. By default this tool produces a plot in a 850x850 pixels `png` file.


You can specify the following options:


| `-l <label>` | to add your own label on the plot |
| --- | --- |
| `-s <size>` | to specify the plot size, in pixel (-s 1200 for a 1200x1200 plot) |
| `-o <filename>` | to specify the name of the `png` file |
| `-x` | to plot on the screen (using `X11`, assuming your connection to hydra allows `X11`) |


You can view the plot in the `png` file with the command `display <filename>`, assuming that your connection to hydra allows `X11`, or


you can copy that file to your local machine and view it with your browser or a png-compatible image viewer (like `xv`).
