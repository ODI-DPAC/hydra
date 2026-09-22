# MaSuRCA

MaSuRCA is an assembly algorithm that relies on creating "super-reads" then assembling them with other assemblers such as Celera (an overlap, layout, consensus assembler). It also has the ability to create "hybrid" assemblies using both PacBio and Illumina data.


This is meant to be a cookbook example of how to run MaSuRCA on Hydra, not a comprehensive guide.


To generate a MaSuRCA assembly, you will need to follow several steps.


1. Load your data (FASTQ files for Illumina, FASTA for PacBio) into your `/scratch` directory (see Transferring files to or from Hydra for more info).
2. Generate a sample MaSuRCA config file. You can do this by entering the following commands into your terminal: 
`module load bioinformatics/masurca` 
`masurca -g masurca.config`
3. Now you will edit the `masurca.config` so that it includes the paths to your sequence files and values for the program parameters.
    1. DATA:
        1. You need to enter data for the different options given in the config file. E.g. 'PE' stands for 'Paired-end' and 'JUMP' stands for mate-pairs or jumping libraries. You'll see below that the PacBio line is commented out. If you have PacBio data, remove the #. Likewise, if you don't have Jumping libraries, add a # to the start of those lines. Make sure that you use full file paths for your read locations. A good way to get this right is to navigate to the directory that holds your files, use the command `pwd`, copy and paste the path, then add a `/` and copy and paste the filename. If your paths are complicated, this is a good way to avoid typos.
        2. When you give names to the paired-end or mate pair libraries, make sure that you use a unique two letter code for each separate library. It also asks for both the average read length and the standard deviation for each library. Keep in mind that Illumina reads should be in FASTQ format and PacBio reads should be in FASTA format. Here is an example of how that might look:


```{.text title="Example library config"}
DATA

#Illumina paired end reads supplied as <two-character prefix> <fragment mean> <fragment stdev> <forward_reads> <reverse_reads>
#if single-end, do not specify <reverse_reads>
#MUST HAVE Illumina paired end reads to use MaSuRCA
PE= pe 500 50 /FULL_PATH/frag_1.fastq /FULL_PATH/frag_2.fastq
#Illumina mate pair reads supplied as <two-character prefix> <fragment mean> <fragment stdev> <forward_reads> <reverse_reads>
JUMP= sh 3600 200 /FULL_PATH/short_1.fastq /FULL_PATH/short_2.fastq
#pacbio OR nanopore reads must be in a single fasta or fastq file with absolute path, can be gzipped
#if you have both types of reads supply them both as NANOPORE type
#PACBIO=/FULL_PATH/pacbio.fa
#NANOPORE=/FULL_PATH/nanopore.fa
#Other reads (Sanger, 454, etc) one frg file, concatenate your frg files into one if you have many
#OTHER=/FULL_PATH/file.frg
END
```
    2. PARAMATERS
        1. Most parameters have comments (lines that start with '#') that will guide you in selecting the appropriate values for each. Do not change the USE_GRID option - we do not have MaSuRCA set up to run with that option on Hydra. Make sure that the number of threads you put for the NUM_THREADS option is reflected in your job file.


```
PARAMETERS
#set this to 1 if your Illumina jumping library reads are shorter than 100bp
EXTEND_JUMP_READS=0
#this is k-mer size for deBruijn graph values between 25 and 127 are supported, auto will compute the optimal size based on the read data and GC content
GRAPH_KMER_SIZE = auto
#set this to 1 for all Illumina-only assemblies
#set this to 0 if you have more than 15x coverage by long reads (Pacbio or Nanopore) or any other long reads/mate pairs (Illumina MP, Sanger, 454, etc)
USE_LINKING_MATES = 0
#specifies whether to run mega-reads correction on the grid
USE_GRID=0
#specifies queue to use when running on the grid MANDATORY
GRID_QUEUE=all.q
#batch size in the amount of long read sequence for each batch on the grid
GRID_BATCH_SIZE=300000000
#use at most this much coverage by the longest Pacbio or Nanopore reads, discard the rest of the reads
LHE_COVERAGE=25
#set to 1 to only do one pass of mega-reads, for faster but worse quality assembly
MEGA_READS_ONE_PASS=0
#this parameter is useful if you have too many Illumina jumping library mates. Typically set it to 60 for bacteria and 300 for the other organisms 
LIMIT_JUMP_COVERAGE = 300
#these are the additional parameters to Celera Assembler.  do not worry about performance, number or processors or batch sizes -- these are computed automatically. 
#set cgwErrorRate=0.25 for bacteria and 0.1<=cgwErrorRate<=0.15 for other organisms.
CA_PARAMETERS =  cgwErrorRate=0.15
#minimum count k-mers used in error correction 1 means all k-mers are used.  one can increase to 2 if Illumina coverage >100
KMER_COUNT_THRESHOLD = 1
#whether to attempt to close gaps in scaffolds with Illumina data
CLOSE_GAPS=1
#auto-detected number of cpus to use
NUM_THREADS = 16
#this is mandatory jellyfish hash size -- a safe value is estimated_genome_size*estimated_coverage
JF_SIZE = 200000000
#set this to 1 to use SOAPdenovo contigging/scaffolding module.  Assembly will be worse but will run faster. Useful for very large (>5Gbp) genomes from Illumina-only data
SOAP_ASSEMBLY=0}
```


MaSuRCA runs with 2 job files. The first uses your .config file to generate an sh script called assemble.sh. Then you just execute the sh script to complete the actual assembly.


- Sample parameters for a job file for the first part of MaSuRCA.
    - Queue: sThC.q
    - Threads & RAM: single thread, 2GB RAM
    - Module: `module load bioinformatics/masurca`
    - Commands: `masurca <CONFIG_FILE>`
- This job should complete in a few seconds and result in a file called assemble.sh
- Create a second job file for the second part of MaSuRCA.
    - Queue: lThM.q or uTxlM.rq (the latter is restricted to users that request access from [SI-HPC\@si.edu](mailto:SI-HPC@si.edu))
    - Threads & RAM: 16 threads, 30GB RAM each (RAM usage will depend on the genome size - you are able to select up to 512GB on the lThM.q. If you need more than that, please request access to uTxlM.rq)
    - Module:`module load gcc/4.9.2`
    - Command: `./assemble.sh`
- Submit this second job. It can take a very long time depending on genome size and coverage.
