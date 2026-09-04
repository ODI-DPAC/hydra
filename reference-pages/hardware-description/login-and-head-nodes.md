---
title: "Login and Head Nodes"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152284/Login+and+Head+Nodes"
date-modified: "2024-05-13"
author: "SGK"
categories: ["hydra7"]
---

## The Head Node: hydra-7.si.edu


- manages the cluster;
- runs the job scheduler (the Grid Engine, aka UGE); and
- starts jobs.


It should never be accessed by users, except if directed by support staff for special operations.


## The Login Nodes: hydra-login0[12].si.edu


- These are the computers available to the users to access the cluster:
    - they are currently 48 cores 128GB Dell R730 servers.
    - do not run your computations on the login nodes.


You can use either node, depending on the node load.
