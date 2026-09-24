# Blast2GO

Hydra has a license for [Blast2GO Command Line](https://www.biobam.com/blast2go-command-line-tools/) ([manual](https://help.biobam.com/space/BCD/2239692845/User+Manual+v.1.5)) with a local copy of the mapping database, so mapping and annotation run without the network round trips of the desktop version. The module is `bio/blast2go`.

## License

The license allows one execution of the command-line program at a time, on one node. Jobs run in the queue `lTb2g.q`, which keeps one slot on that node free for Blast2GO; a second Blast2GO job waits until the first finishes.

!!! warning "Use Blast2GO for mapping and annotation only"

    Because one job runs at a time, do not run the BLAST step inside Blast2GO. Run BLAST separately (see [BLAST](blast.md)), split across many jobs if the input is large, with `-outfmt 5`; Blast2GO reads the XML with `-loadblast31` or `-loadblast`.

## Job file

Request the queue and the `b2g` resource. The queue allows 36 GB of memory and two slots per job, with the time limits of the long queues (30 days of CPU, 60 days elapsed). The module defines two commands. `runblast2go` starts Blast2GO with the Java options set. `hydracliprop` copies a `cli.prop` template configured for the local database into the current directory; it overwrites an existing one, so run it once.

```sh title="b2g.job"
#$ -S /bin/sh
#$ -N b2g -cwd -j y -o b2g.log
#$ -q lTb2g.q
#$ -l b2g,mres=32G,h_data=32G,h_vmem=32G
#
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
module load bio/blast2go
hydracliprop
runblast2go \
  -properties cli.prop \
  -loadfasta /share/apps/bioinformatics/blast2go/1.5.1/example_data/plant_nucleotide.fasta \
  -loadblast31 /share/apps/bioinformatics/blast2go/1.5.1/example_data/plant_blast_31.zip \
  -useobo $BLAST2GO_OBO \
  -mapping \
  -annotation \
  -savebox example.box \
  -savereport example.pdf
echo = `date` job $JOB_NAME done
```

| Variable | Default | Effect |
|---|---|---|
| `BLAST2GO_HEAP_SIZE` | `1024m` | Java maximum heap for `runblast2go` |
| `BLAST2GO_TEMP` | the directory you are in when the module loads | `-tempfolder`, where logs and temporary files go; in a job with `-cwd` that is the job's directory |
| `BLAST2GO_OBO` | set by the module | the OBO file matching the local mapping database, from [biobam](http://resources.biobam.com/b2g_res/obo_files/index.html) |

The mapping database is large and the HPC team keeps only the current version; an update removes the previous one.

## Graphs and statistics

`-statistics all` writes every available statistic as PNG images, CSV and `.b2g` files. The manual lists the individual statistics and the report options.
