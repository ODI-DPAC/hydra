---
title: "Network: Ethernet and InfiniBand"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152286/Network+Ethernet+and+InfiniBand"
date-modified: "2021-10-08"
author: "SGK"
---

All the nodes (i.e., the compute nodes, the login nodes, and the head node) are interconnected using not only the regular 10GbE network (Ethernet), but also via a high-speed, low latency, communication fabric, known as the InfiniBand (IB):


- The IB switch is capable of a 100Gbps transfer rate, although the older nodes have IB card capable of 40Gbps only.
- The GPFS storage use the Infiniband fabric for for its I/O.
- To use the IB for message passing (MPI) you must
    - build the executable the right way, and
    - specify that you want to use the IB in your job script.
    - We have modules to do precisely that.
- A MPI program will not use *by default* the IB for message passing - you need to build it *right* to make it use the IB.
