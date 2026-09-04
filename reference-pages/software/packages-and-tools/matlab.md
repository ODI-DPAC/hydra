---
title: "Matlab"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152337/Matlab"
categories: ["hydra7"]
---

- Full fledged MATLAB is not available on `Hydra`
    - we would need to purchase licenses for Hydra,
    - Hydra users can use compiled MATLAB, since we installed the MATLAB run-time environment,
    - SAO users can use the ITS supported `MATLAB` compiler to produce run-time version of their MATLAB code.
- The `MATLAB` run-time environment is available on `Hydra`
    - to access it, load the right module:


| Modules | Description |
| --- | --- |
| `matlab/R2014a` | 2014 first release |
| `matlab/R2017b0` | 2017 second release (SAO/CF equivalent) |
| `matlab/R2017b` | 2017 second release, with (latest) update (# 9) |
| `matlab/R2019a` | 2019 first release |
| `matlab/R2019b` | 2019 second release |
| `matlab/R2020a` | 2020 first release |
| `matlab/R2020b` | 2020 second release |
| `matlab/R2021a` | 2021 first release |
| `matlab/R2021b` | 2021 second release |
| `matlab/R2022a` | 2022 first release |
| `matlab/R2022b` | 2022 second release |
| `matlab/R2023a` | 2023 first release |
| `matlab/R2023b` | 2023 second release |
| `matlab/rt → R2021b` | default run-time is set to use R2021b, latest version avail at SAO on ITS-managed machines |
| matlab/R2024a | 2024 first release |
| matlab/R2024b | 2024 second release |
| matlab/R2025a | 2025 first release |
| matlab/R2025b | 2025 second release |


**NOTES**
        - You must compile your `MATLAB` application (elsewhere) to run it on Hydra,
        - SAO has a single (concurrent) seat license for the `MATLAB` compiler, available on all ITS-managed machines.
        - Look at the README file under `~/hpc/examples/matlab` on Hydra.


Last update 02 Dec 2025 SGK/MPK
