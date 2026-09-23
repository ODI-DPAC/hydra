# Cluster hardware

Hydra runs Rocky Linux 8 with Grid Engine. The nodes are connected by 10 Gb Ethernet and InfiniBand.

- [Login, head and compute nodes; network](nodes.md)
- [Limits table](limits.md): nodes, slots and memory behind each queue

`qstat -g c` and `qhost` on a login node print the current numbers.
