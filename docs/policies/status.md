# Cluster status

The status page at <https://hydra.si.edu/tools/status/> shows what the cluster is doing now and over the past 30 days. It opens only from the SI network or the SI VPN. The page reloads itself every hour, and links at the top switch it to a 5 or 20 minute refresh.

| Tab | Shows |
|---|---|
| Usage | CPU and memory in use on every node; jobs running, queued and available over time; who has jobs running and queued |
| Warnings | jobs and nodes that need attention |
| Breakdown by Queue | slots used and free per queue |
| Avail Slots/Wait Job(s) | where a new job could start, and why waiting jobs wait |
| Memory Usage | memory reserved and used per node |
| Resource Limits | the per-user limits and how much of each is in use |
| Disk Usage & Quota | space and file counts on every filesystem |

Two menus under the Usage plots select the snapshot's sort order (name, number of CPUs, usage, load, memory) and the time plot's length (7, 15 or 30 days) and highlight one user's jobs. The same choices go in the URL for bookmarking:

```text
https://hydra.si.edu/tools/status/?sortby=nCPU&len=15d&user=USERNAME
```

Click a plot to open it at full size. The page also links the list of every installed module, as HTML and as plain text.

The same numbers are available on a login node with `qstat -g c`, `qstat+ -gc` and `qhost`; see [Monitor and manage jobs](../jobs/monitoring.md#check-the-state-of-the-cluster). Planned maintenance and outages are announced in the banner at the top of every page of this site and under [News](../news/index.md).
