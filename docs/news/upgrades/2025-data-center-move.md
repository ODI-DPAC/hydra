# 2025 data center move

## Status


- Hydra has been successfully moved to the Ashburn Data Center (ADC):
    - Over 125 pieces of equipment have been relocated and re-cabled.
    - The NetApp was upgraded with new disks and disk enclosure; old disks were decommissioned.
    - The new GPFS (bigger and faster) is now in production.


- The cluster's OS had to be upgraded from Rocky Linux 8.9 to 8.10 due to compatibility issues with the ADC network infrastructure.
    - This should not impact any applications - as per our tests.


- The cluster is available for use with a slightly reduced capacity:
    - All storage units are up and running, although *the disk space was reorganized*.
    - The head node and both login nodes are up and running.
    - Some 69 compute nodes are up and running (abt 5300 CPus), although
        - only one of the interactive and I/O node is up and running for now,
        - the GPU nodes are up and running, but not yet available.
    - Some five nodes were down due to h/w failures and are being repaired and put in production.


- Globus services and the R Studio Server are up and running.
- Accessing Hydra remains unchanged, passwords remain valid, etc.


## Disk Space Reorganization


The storage architecture was reorganized to improve performance while maintaining backward compatibility whenever possible:


- `/home` and `/store` remain unchanged.
- `/pool` is deprecated, *you should no longer use it* (see below).
- most of `/scratch` was relocated to the new GPFS for improved performance and capacity (some directories remain on the old GPFS)
- `/data` was expanded and remains on the NetApp, with expanded capacity and (soon) increased user quotas.
- `/fast` will soon be available: a high performance storage that uses NVMe SSD disks in the new GPFS.
- 'bigtmp' will likely be phased out, once `/fast` become available.


### Details on the Disk Space Reorganization


- `/home` remains as it was
    - size: 23 TB
    - user's quota: 384 GB
    - use `/data/public/<group>/<username>` for long term storage
        - <group> stands for biology, genomics, nasm, odi or sao
        - <username> stands for your username on Hydra
    - `/home` is never scrubbed.


- `/data` remains on the NetApp
    - the size of `/data/public` has been increased to 330 TB, and is expected to grow to 450 TB
    - the user's quota will be raised to 10 TB (TBD)
    - `/data/public` is not scrubbed.


- `/scratch` is bigger and faster
    - most of `/scratch` is now on the new GPFS, (namely `/scratch02`)
    - some of it remained on the old GPFS (i.e., `/scratch01`)
    - the size of `/scratch/public` has been increased to 800TB
    - user's quota remains 15 TB, but might be raised later
    - best practice is to use `/scratch`, and not `/scratch01` or `/scratch02`


- `/pool` is deprecated (i.e., you should no longer use it)
    - please stop using `/pool`,
        - although for backward compatibility we created symlinks (aka symbolic links)
        - i.e., paths starting with /pool point to the new locations.
    - the content of `/pool/public` was moved to `/scratch/public/pool`,
        - hence users might have data under two locations now on the same storage unit
            - `/scratch/public/<group>/<username>`
            - `/pool/public/<group>/<username>` that is in reality `/scratch/public/pool/<group>/<username>`
        - you are encouraged to consolidate these two location in one, using `mv -i`
        - as a results, what you store under `/pool/public` and under `/scratch/public` now count against your quota on `/scratch/public`


- `/store` remains as it was
    - near-line storage, split over two NASes


- `/fast` is a new high performance disk space
    - it uses NVMe SSD disks in the new GPFS
        - current size 100 TB
        - uses some 70 TB of NVMe
        - aggregate bandwidth around 300 Gbps
    - will be available soon (TBD)


!!! note
    For this disk space reorganization, files and directories (over 500 million fiies) where copied over and verified, yet


    - special files, like stateless DB, might not have been copied right;
    - something else might have gone wrong;
    - the original copy has been preserved and will not be destroyed for a few months;
     - hence if something was not copied right, please contact us.



## GPU Queues and Nodes


The GPU nodes are up and running, and available as of Tuesday Oct 14 2025.


- Some things have changed, though, see below and the [documentation](../../software/gpus.md).
- What has changed:
    - you must specify `-l gpu,ngpus=1` to use and request 1 GPU (both)
        - `gpu` is an abbreviation for `use_gpu`
        - `ngpus` is equivalent to `GPUS` (notice the 's')
    - If you only use "`-l gpu`", the job will start and promptly end up in `Eqw` mode.
    - `ngpu` or `num_gpu` and `gpu_id` or `gpuid` are no longer available/needed!
    - `ngpus` (or `GPUS`) is an RSMAP, (i.e., equivalent to what `gpu_id` was)
    - `gpuarch` is now an abbreviation for `gpu_arch`
    - The following two environment variables are now set by the job scheduler
        - `SGE_HGR_GPUS`, will be set to something like "`gpu0 gpu1`"
        - `CUDA_VISIBLE_DEVICES`, will be set to something like "`0,1`"
    - Make sure your application uses the GPU(s) assigned to your job via one of these two environment variables.
- What has not changed:
    - names of the queues;
    - queue limits (memory, cpu, elapsed time);
    - sage limit (maximum of concurrent GPU per user).
- Local tools:
    - `get_gpu-info```- same as before
    - c`heck-gpu-usage```- replaces check-gpuse
    - `qacct+```- support GPU accounting


## Globus Services


Globus is available.


- It was moved to a new server and adjusted to accommodate the new storage architecture.


## R Studio Server


The R studio server is up and running.


- It was adjusted to accommodate the new storage architecture.
