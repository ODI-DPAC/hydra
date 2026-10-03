# Usage policies

Hydra is an official Smithsonian asset. Everything on it is subject to the Institution's directives on computer and network use, in particular [SD-931](https://sinet.sharepoint.com/:b:/r/sites/PRISM2/SIOrganization/OCFO/opmb/SD/SD931.pdf?csf=1&web=1&e=48KSeY). You agreed to those directives when you received your Smithsonian network account, and a Hydra account adds the rules on this page. We ask new account holders to reread SD-931, and we expect every Hydra user to keep their computer security awareness training (CSAT) up to date.

## Accounts

Anyone with an active Smithsonian network account can request a Hydra account through the [HPC Account Request](https://smithsonianprod.servicenowservices.com/si?id=sc_cat_item&sys_id=962e05331b96e05078932f41f54bcb3b&sysparm_category=8b5b9d421b601410520ba82eac4bcb65) form. The form collects your name, your unit or department, your supervisor's name and approval, and a sentence or two on the work you plan to do on Hydra. Keep that information current. If your supervisor changes or leaves, or someone else should be contacted about your account and data, tell us.

Accounts for temporary appointments (students, postdocs, fellows, contractors) are renewed once a year. When an account expires we email the user, at the address in their `~/.forward` file, and the supervisor. If neither replies within 30 days, the account's data is subject to deletion.

Two things are prohibited, and either can cost you the account:

- **Sharing credentials.** Your Hydra username and password are yours alone. Nobody else logs in as you, and you log in as nobody else.
- **Borrowing disk space.** Sharing data with collaborators is fine. Storing your data under someone else's account to get around your quota is not. If you need more space or a higher limit for a piece of work, ask us.

We run an introduction to Hydra workshop every quarter. See [Training](../getting-started/training.md).

## Using a shared cluster

As with every system on the Smithsonian network, you have no expectation of privacy in your use of Hydra. Rule 5 of SD-931 on appropriate computer and network use applies.

We reserve the right to suspend, cancel or modify accounts, quotas on the public disks, queue configuration and other settings, without warning, when the integrity of the cluster or its fair use requires it.

Hydra is shared by more than a hundred users, and the cluster works only if each of them treats it that way. In practice that means:

- Do not run analyses on the login nodes or the head node. The login nodes are for editing, compiling, transfers and short tests. The [scheduler](../jobs/concepts.md) is how work reaches the compute nodes. Processes that compute on a login node are slowed, then killed.
- Watch your own jobs. You are responsible for monitoring their state and progress, and you should be reachable while they run, so that you can adjust them if something is wrong.
- Start small. Before submitting many similar jobs, run one or a few, check what they used with `qacct`, and size the rest from that.
- Estimate what you need. CPU time, memory and disk space are all limited, and a request far above what a job uses holds the excess back from everyone else. Know roughly how your needs scale with the size of your analysis.
- Everyone's work matters as much as yours. If you wonder whether something is within the spirit of a shared system, ask whether the cluster would still work if dozens of people did the same thing at once.

Systematic abuse of a scarce resource (memory, disk space, and the local SSDs in particular) or bypassing the resource limits is grounds for suspending or cancelling an account.

## Disks

Hydra's disks are not archival storage. They are reliable, but the Smithsonian is not responsible for data lost on Hydra, and you should have no expectation that files stored there will survive in the long term. Keep a copy of anything you cannot afford to lose somewhere else.

- `/home` and `/data` have snapshots, and a disaster-recovery copy exists so that the partitions can be rebuilt after a storage failure. That copy is not a backup you can restore files from. See [Backups](../storage/backups.md).
- `/scratch/public` is not backed up, and files older than 180 days are removed by the scrubber every week. See [Scrubbed files and restores](../storage/scrubber.md).
- Every public disk has a quota. See [Filesystems](../storage/filesystems.md).
- Put large files and the working data of analyses on `/scratch`.
- When an account expires, its data is subject to deletion 30 days later unless something else has been agreed. A user leaving the Smithsonian either saves their data or hands responsibility for it to their supervisor before they go.

## Oversubscribed and inefficient jobs

We monitor the cluster for jobs that use the compute nodes badly, and email the owner. The conditions, and what the email looks like, are under [Warning emails](../jobs/efficiency.md).

| Condition | Threshold |
|---|---|
| Oversubscribed job | more than 133% of the CPUs it requested in use |
| Hosed job | under 10% efficiency after 36 hours |
| Inefficient job | under 33% of the CPUs it requested in use |
| Memory over-reserved | reserved more than 2.5 times what it uses |
| Overloaded node | load above 133% of the node's capacity |

For an overloaded node we identify the jobs behind the load, end them, and tell their owners. Most of these are programs that start a thread for every CPU on the node regardless of what was requested. We will help you find the right setting.

What we ask of you when a warning arrives:

- For a hosed or oversubscribed job, reply to [SI-HPC-Admin@si.edu](mailto:SI-HPC-Admin@si.edu) within 24 hours where you can, so that we can decide together whether the job should be killed. An oversubscribed job with more than 24 hours still to run should be killed and resubmitted with the right request.
- For an inefficient or memory-over-reserved job, look at what the job is doing, do not ignore the warning, and write to us if you do not understand why it fired or how to fix it for the next job.

When the cluster is busy, or an oversubscription is large, we kill such jobs at our discretion. When the load is above 70%, users with many inefficient jobs have some of them killed automatically, down to 100 unused slots per user, and receive a warning.

Our goal is to get every job through the queue and to help you use a shared system well. An oversubscribed job slows down whoever shares its node. An inefficient or over-reserved job holds CPUs or memory that the scheduler cannot give to the jobs waiting behind it.

## Email

We communicate by email, and we expect you to read it. We use it to announce new features, configuration changes and policy changes, and to warn you about jobs that use resources badly, files about to be scrubbed, and accounts about to expire.

All of that goes to the address in the `~/.forward` file in your Hydra home directory. We create the file when the account is created, with your canonical Smithsonian address. If you would rather receive mail elsewhere, put one address on the first line of that file:

```console
$ echo you@si.edu > ~/.forward
```

## Contact

Questions and requests go to [SI-HPC@si.edu](mailto:SI-HPC@si.edu). Two things go to [SI-HPC-Admin@si.edu](mailto:SI-HPC-Admin@si.edu). One is a reply to a warning email about a hosed or oversubscribed job. The other is a request to unlock an account whose password expired more than 14 days ago. [Getting help](index.md#getting-help) says what to include.
