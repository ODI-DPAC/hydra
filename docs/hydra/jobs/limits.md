# Resource limits

Each queue limits what one job may use; these cluster-wide limits cap how much of the cluster one user may hold at once. A job that would exceed one waits in the queue until your other jobs finish. The values are from `qconf -srqs` in May 2024; the commands at the end print the current ones.

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
| `sThC.q`, `mThC.q` | 840 |
| `lThC.q` | 417 |
| `uThC.q` | 139 |
| `sThM.q` | 840 |
| `mThM.q` | 569 |
| `lThM.q` | 379 |
| `uThM.q` | 71 |
| `uTxlM.rq` | 480 |
| `qrsh.iq` | 16 |
| `lTIO.sq` | 8 |
| `lTWFM.sq` | 2 |

## Concurrent jobs per user

| Queue | Jobs |
|---|---|
| `qrsh.iq` | 1 |
| `qgpu.iq` | 1 |
| `lTIO.sq` | 2 |
| `uTxlM.rq` | 3 |
| `lTWFM.sq` | 1 |

## GPUs

| Queue | Per user | All users |
|---|---|---|
| `qgpu.iq` | 1 | 4 |
| `sTgpu.q` | 4 | 4 |
| `mTgpu.q` | 3 | 4 |
| `lTgpu.q` | 2 | 4 |
| `uTgpu.q` | 1 | 4 |

## Other limits

| Resource | Per user |
|---|---|
| `big_tmp` units (see [bigtmp](../storage/special.md)) | 25 |
| IDL runtime licenses | 102 |
| reserved memory in `lThM.q` | 2.6 TB |

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
