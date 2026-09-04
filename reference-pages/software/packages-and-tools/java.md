---
title: "Java"
confluence_url: "https://confluence.si.edu/spaces/HPC/pages/163152335/Java"
categories: ["hydra7"]
---

- Java versions 17, 18 & 21 are available on Hydra by loading the appropriate module: 
`% module load tools/java`


or


`% module load tools/java/18`


or


`% module load tools/java/21`


- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) java is now under tools/
- ![(warning)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/warning.svg) java 18 does not play nice with the GridEngine:
    - Java, by default, wants to starts as many threads and grab as much memory as possible.
    - By not specifying some memory related parameters, java fails in every submitted job, with the following message:


```
Error occurred during initialization of VM
Could not reserve enough space for object heap
```
    - ![(lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb_on.svg) You should always start java with the following options:


```
java -d64 -server -XX:MaxHeapSize=1g
```


where the value "`1g`" should be adjusted to the memory needed by the application and for the job to fit within the queue and the requested resources memory constraints.


The total amount of memory used by java is not just the maximum heap size.
    - If you need more memory, be sure to adjust the memory resource request accordingly (`-l memres=X,h_data=X,h_vmem=X`), see the section about memory reservation in the [Available Queues](https://confluence.si.edu/display/HPC/Available+Queues) page.


![(grey lightbulb)](https://confluence.si.edu/s/74ffi/9116/n2r6gc/_/images/icons/emoticons/lightbulb.svg) The complete documentation for all of `java` options (all versions) is posted [at Oracle's web site.](https://docs.oracle.com/en/java/javase/).


Last update 16 May 2024 SGK/MPK
