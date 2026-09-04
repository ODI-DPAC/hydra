---
title: "FAQs"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152356/FAQs"
categories: ["hydra7"]
---

::: {.callout-note collapse="true" title="Details"}
The list of installed packages is on our [software](reference-pages/software.md) page. You can also view the available modules with `module avail`, which will list the software that have modules.
:::


::: {.callout-note collapse="true" title="Details"}
Login to Hydra and issue the command `module avail,`


or go to the status page(s) ([\@si.edu](https://hydra-7.si.edu/tools/status/) or [\@cfa.harvard.edu](https://lweb.cfa.harvard.edu/~sylvain/hydra/)), or the [Hydra-7 tools](https://hydra-7.si.edu/tools/) page and click on link to display the list of available modules
:::


::: {.callout-note collapse="true" title="Details"}
Did you use the `-cwd` flag in your qsub script/embedded directives?


If you do not use the `-cwd` flag, which tells the scheduler to use your 'current working directory',


your job will run from your home folder and all log files will be written there.
:::


::: {.callout-note collapse="true" title="Details"}
Yes, a couple of nodes offer interactive access to compute nodes on Hydra.


- Use the command `qrsh` instead of `qsub` (not `ssh`);
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) like all queues, the interactive queue has limits (CPU time, elapsed time, memory and number of CPUs/threads/cores/slots);
- ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) Read the documentation under [Available Queues](reference-pages/submitting-jobs/available-queues.md).
:::
