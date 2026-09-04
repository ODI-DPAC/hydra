---
title: "Hydra Policies"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152216/Hydra+Policies"
categories: ["hydra7"]
---

**Existing Smithsonian General Policies and SI Computer and Network Usage Policies**


The Smithsonian Institution High Performance Computing resources (i.e., SI/HPC: the `Hydra` cluster and its associated resources) is an official SI asset and, as such, is subject to all of the regulations and policies outlined in SI's official directives, such as SD-931.


Since all SI/HPC users must have a Smithsonian network account before being granted an account, they have already agreed to the policies described in [SD-931](https://sinet.sharepoint.com/:b:/r/sites/PRISM2/SIOrganization/OCFO/opmb/SD/SD931.pdf?csf=1&web=1&e=48KSeY).


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) New SI/HPC account holders should consider reacquainting themselves with [SD-931](https://sinet.sharepoint.com/:b:/r/sites/PRISM2/SIOrganization/OCFO/opmb/SD/SD931.pdf?csf=1&web=1&e=48KSeY). In addition, it is expected that SI/HPC users' computer security awareness training (CSAT) is up to date.







## **User accounts**


Individuals who have been granted a Smithsonian network account are eligible for a `Hydra` account.


In addition, it is expected that each SI/HPC user will provide and keep up to date the following, which will be gathered through an [online form](https://smithsonianprod.servicenowservices.com/si?id=sc_cat_item&sys_id=962e05331b96e05078932f41f54bcb3b&sysparm_category=8b5b9d421b601410520ba82eac4bcb65):


- Name
- Unit/Department
- Supervisor name
- Supervisor approval via online interface
- 1-2 sentence description of the work they plan to conduct on Hydra.


SAO/CfA affiliates should the account request [form](https://lweb.cfa.harvard.edu/cf/services/cluster/request-account.html) hosted at the [SAO/CfA ITS/HPC info page](https://lweb.cfa.harvard.edu/cf/services/cluster/), managed by the SAO HPC analysist (currently: Sylvain Korzennik).


Introduction to Hydra workshops are held quarterly; contact [SI-HPC\@si.edu](mailto:SI-HPC@si.edu) for more information.


#### Note:


- The sharing of credentials on SI/HPC assets (like `Hydra`) is strictly prohibited.
- *Borrowing* disk space from other users to bypass quota is also prohibited. While it is, of course, OK to share data with collaborators, users should not try to bypass quota limit by having their data stored by others.
    - Either policy violation may/will result in suspension/cancellation of the user's account. Users should contact us if they need more resources to complete some specific task.
- Users who have temporary appointments (students, postdocs, fellows, contractors, etc.) will need to renew their accounts annually (including SAO's postdocs/fellows).
- Users and their supervisors will be contacted upon account expiration (via the email in their `~/.forward` file). If there is no response for the user or their supervisor within 30 days, the data will be subject to deletion. 
![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) If someone else should be contacted regarding a user's account/data, or the user's supervisor has changed or left, it is the user's responsibility to notify their SI/HPC contact person.







## **Hydra Use**


As with all assets on the Smithsonian network, `Hydra` users should have no expectation of privacy concerning their use of `Hydra`. Users should adhere to "*Rule 5*" of SD-931 regarding appropriate computer and network use.


`Hydra`'s administrators reserve the right to suspend, cancel, or modify user accounts, quotas on the public disks, queue configuration, and other configuration settings, without warning and as needed to maintain the cluster integrity and optimal use as a *shared resource*.


Users should keep in mind that `Hydra` is a *shared resource*. As such, users should avoid conducting analyses on the login nodes or the head node, be mindful that others are using the cluster, and understand that others' work is no less important than yours.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) If you are wondering whether your behavior is in violation of "the spirit" of shared-use, consider whether dozens of people doing the same thing as you would adversely affect the functioning of the cluster.


![(tick)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/check.svg) Users are responsible for monitoring the status and the progress of their jobs. Users who plan to conduct many similar operations should start with a small (set of) test job(s) before scaling up their use. Users who have jobs running on `Hydra` should be able to access the cluster while their jobs are running, so they can adjust their use if need be.


![(tick)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/check.svg) Since the SI/HPC resources are a shared resource, users are expected to do a best effort to estimate their needs (CPU time, memory, disk space) and have a handle on how it scales with the size of their analysis.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) Users are subject to suspension or cancellation of their accounts if they systematically abuse a scarce or depleted resource (memory -aka RAM- disk space, especially high throughput disks like SSDs, etc.) or bypass the resource limits in place.







## **Disk Use on Hydra**


Disk storage on `Hydra` is not to be used for archival storage. Users should have no expectation of the long-term viability of their files stored on `Hydra`. While the disk system on `Hydra` is highly reliable, the Smithsonian is not responsible for any data that are lost on `Hydra`.


Data on disks on Hydra are not backed up, except for the `/home` and `/data` disks, and old data on the public disks will be regularly removed (scrubbed) according to the following model:


- Files and directories on `/scratch/public` (aka `/scratch`/`{biology|genomics|nasm|sao})` will be scrubbed after 180 days.
- Files and directories on `/pool/public` (aka `/pool/{biology|genomics|nasm|sao})`will be scrubbed after 180 days.
- The backups of `/home` and `/data` are mainly for disaster recovery, since we have snapshots enabled on these disks.


Remember:


- All public disks have quotas and are scrubbed.
- Analyses on large files and data-sets should be conducted using the `/scratch` disk.
- The `/home` and `/data` disks should not be used for large files, their low quota will prevent users from storing large files.
- All data associated with an expired account is subject to deletion 30 days after the account expires, unless agreed otherwise.
- It is the responsibility of the user leaving SI to either save her/his data or pass on the responsibility of her/his data to her/his supervisor.







## **Oversubscribed and Inefficient Jobs**


We monitor the cluster usage for the following conditions:


- Oversubscribed jobs: scaled CPU usage > 133%;
- Very inefficient or “hosed” jobs: efficiency (CPU/age) < 10% and age > 36hr;
- Inefficient jobs: scaled CPU usage < 33%;
- Jobs that over-reserved memory: >2.5x actual RAM use;
- Nodes whose load exceeds 133% of its capacity.


Users with such jobs receive warning emails (sent to the email listed in their `~/.forward` file), while for nodes with excessive load, we will identify the jobs responsible for the load spike.


- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) These jobs will be promptly terminated and user(s) will be notified. We will help finding the right configuration, as some programs end up creating an excessive number of threads, hence despite a nominal CPU usage, the load becomes excessively high.


**User responsibility to respond to warnings:**


![(tick)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/check.svg) For “hosed” and oversubscribed jobs, users should respond to warnings by emailing si-hpc-admin\@si.edu within 24 hours of receiving the warnings, whenever possible, to help determine whether jobs should be killed. Oversubscribed jobs that are expected to run for over 24 hours after receiving the first warning should be killed and resubmitted with the correct parameters.


![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) When Hydra’s usage is high, or when the over-subscription is excessive, jobs may get killed promptly by the system administrator team at their discretion. When the cluster load is very high, users with a lot of inefficient jobs will have some of their jobs automatically killed and will receive a warning. Currently the load threshold for this is 70% and users will have their inefficient jobs trimmed down to have on only 100 'unused' slots per user.


![(tick)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/check.svg) For inefficient and memory over-reserved jobs, users should monitor their jobs, not ignore the warnings and contact the support staff if they do not know or understand why the warnings are occurring and/or how to fix the problem for future jobs.


Our overarching goal is to support all users: to get all jobs through the queue and help users learn how to best make use of a shared resource. Remember that oversubscribed jobs are likely to slow down someone else’s job(s) running on the same compute node(s), while inefficient or memory over-reserved jobs are clobbering the system and preventing the scheduler from starting the jobs waiting in the queue.


![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg)As a reminder, all users are expected to read messages sent to the email address listed in their ~/.forward file.


**Communication**


All users are expected to check **and** read their email regularly, including those from the HPCC-L mail group (hpcc-l\@cfa.harvard.edu) . Users will be added to the HPCC-L mail group when they are granted an account.


The SI/HPC admins use email to:


1. announce new features (e.g. on `Hydra`),
2. warn users when their jobs are improperly using resources,
3. warn users when their files will be scrubbed,
4. warn users whose accounts are expiring,
5. announce configuration changes, and
6. announce new policies or changes to existing policies.


Users should be sure that the file `~/.forward` (in their home directory on `Hydra`) contains a working email address that is regularly checked.


A `~/.forward` file is created for each new account, using the user *canonical* email. See [here](https://kb.iu.edu/d/ablm) about creating a `~/.forward` file.







## **Whom to Contact**


- All questions should be send to [si-hpc\@si.edu](mailto:si-hpc@si.edu)
- SAO users: Sylvain Korzennik & Babin Sunar at [hpc\@cfa.harvard.edu](mailto:hpc@cfa.harvard.edu)
- Non-SAO users: Alex E. White, Matthew Kweskin, Vanessa Gonzalez, Mike Trizna and Kenneth (Tripp) Macdonald at [si-hpc\@si.edu](mailto:si-hpc@si.edu)
