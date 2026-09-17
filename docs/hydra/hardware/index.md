# Cluster hardware

Hydra-7 (2024) runs Rocky Linux 8 with the Altair Grid Engine. Roughly 78 compute nodes, about 5,900 CPU cores and 50 TB of memory, plus GPU nodes, connected by 10 GbE and InfiniBand.

- [Login, head and compute nodes; network](nodes.md)
- [Hardware limits table](limits.md): nodes, slots and memory per queue

Run `qhost+` or `qstat -g c` on a login node for live numbers.
