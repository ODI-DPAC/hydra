# Resource limits

Each queue limits what one job may use. These cluster-wide limits cap how much of the cluster one user may hold at once. If a job would push you over one of these limits, it waits in the queue until your other jobs finish. The commands at the end of the page print the current values.

## Queued jobs

| Limit | Value |
|---|---|
| jobs queued on the cluster, all users | 25,000 |
| jobs queued by one user | 2,500 |
| tasks in one job array | 10,000 |

A job array counts as one job. `q-wait` and a counting loop for scripts that submit many jobs are under [Submit many jobs without exceeding the limit](submit.md#submit-many-jobs-without-exceeding-the-limit).

## Slots per user

| Queue | Slots |
|---|---|
| all queues together | 840 |
| `sThC.q` | 840 |
| `mThC.q` | 640 |
| `lThC.q` | 431 |
| `uThC.q` | 143 |
| `sThM.q` | 840 |
| `mThM.q` | 640 |
| `lThM.q` | 390 |
| `uThM.q` | 73 |
| `uTxlM.rq` | 536 |
| `qrsh.iq` | 64 |
| `lTIO.sq` | 8 |
| `lTWFM.sq` | 2 |

## Concurrent jobs per user

| Queue | Jobs |
|---|---|
| `qrsh.iq` | 12 |
| `qgpu.iq` | 1 |
| `lTIO.sq` | 8 |
| `uTxlM.rq` | 3 |
| `lTWFM.sq` | 1 |

## Reserved memory per user

| Queues | Reserved memory (`mres`) |
|---|---|
| `sThC.q` `mThC.q` `lThC.q` `uThC.q` together | 10 TB |
| `sThM.q` `mThM.q` `lThM.q` `uThM.q` together | 9 TB |
| `uTxlM.rq` | 8 TB |

## GPUs per user

| Queue | GPUs |
|---|---|
| all GPU queues together | 4 |
| `sTgpu.q` | 4 |
| `mTgpu.q` | 3 |
| `lTgpu.q` | 2 |
| `qgpu.iq` | 1 |

The cluster has 8 GPUs. A group of approved users has higher GPU limits.

## Other limits

| Resource | Per user |
|---|---|
| IDL runtime licenses | 102 |

## All users together

| Resource | Limit |
|---|---|
| slots, all queues | 5,960 |
| slots in the high-CPU queues | 5,176 |
| slots in the high-memory queues | 4,680 |
| slots in `uTxlM.rq` | 536 |
| slots in the GPU queues | 104 |
| reserved memory, high-CPU queues | 40 TB |
| reserved memory, high-memory queues | 36 TB |
| reserved memory, `uTxlM.rq` | 8 TB |

## Print the current limits

```console
$ qconf -srqs                        # every resource quota set
$ qconf -srqs max_hC_slots_per_user  # one set
$ qconf -sconf global | grep max     # cluster-wide job limits
$ qquota -u $USER                    # your usage against the limits
$ qquota -u $USER -l mem_res         # one resource
$ module load tools/local; qquota+ +% -l slots -u $USER   # with percentages
$ check-qwait                        # your waiting jobs and the quota holding each
```

`man 5 sge_resource_quota` and `man 5 sge_conf` explain the output.
