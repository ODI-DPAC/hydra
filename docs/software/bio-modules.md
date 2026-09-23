# Bioinformatics modules

- As of May 2024, about 100 bioinformatics software packages have been installed on Hydra-7 , a list we had to prune down from the 200+ that were over the years installed on Hydra-6, and 8 new packages were added,
- As we reorganized things, we also moved some general use packages from `bio/` to `tools/`
- The list of packages that we pruned is also down this page, here.


Job files will need to be adjusted to reflect these changes.


- Users looking for software not on this list can compile/install in their own space or request installation by emailing [SI-HPC\@si.edu.](mailto:SI-HPC@si.edu.)
- Note that with our limited time, we prioritize installing software that many users need and is well-documented.
- Please contact [SI-HPC\@si.edu](mailto:SI-HPC@si.edu) if you notice any issues with bioinformatics software and modules.


### General Packages Moved from bio/ to tools/


- The following packages had their modules under bio/ and have been moved to tools/:


`awscli, ffsend, julia, rclone, ruby`


### New Packages in bio/


- The following packages are now available on Hydra-7, they were not available on Hydra-6:


`admixtools, basespace, blobtoolkit, mitos, paup, quast, raxml-ng, rsem`


### Pruned Packages


- The following packages, that were available on hydra-6, *are no longer*available on Hydra-7:


`anuga, aster, atram, autoparts, bayesass, beagle_5.1, blasr, blast_taxa_backfill, blat, centrifuge, comp_popgen_sjsw, delimitr, discovista, dna-algorithm, dotnet-core, edirect, edta, eems, ervin, ete3, exabayes, fatotwobit, fsct, gadma, gatb-minia-pipeline, gblocks, genomescope, gnuparallel, goleft, gsutil, haystac, hifiadapterfilt, hmmer, hybphylomaker, hyde, hyphy, ibpp, imagemagick, insector, ivis, jags, jbrowse, kakapo, makehub, manta, mauve, mcscanx, megadetector, metamaps, metamorpheus, metapop2, mitogeneextractor, mitohifi, ml_derkarabetian, mpboot, mptp, msmc2, multiqc, ngsadmix, ngstools, opt-sne, orthomcl, paml, partitionfinder, patchwork, pbsuite, pcangsd, phast, phrapl, phylobayes, phylobayes-mpi, phyloflash, phylomad, phylonet, phyparts, phyx, pilon, prokka, proteinortho, pyrad, ragout, relernn, rjags, rsem-eval, salmon, salsa, seq-seq-pan, shapeit, sharkmer, smc++, spruceup, sspace, stampy, star, strauto, stringtie, supernova, tabix, transrate_1.0.3, trinotate, vcflib, velvet, viridal, w2rap-contigger, wgd`


- If you need one of these tools, contact us at `si-hpc@si.edu`


## Complete List of `bio/` Packages


- Here is the full list of `bio` packages available on Hydra-7 as we migrated to Rocky 8 (May 2024):


For many packages the default version has changed. In some cases. Please review your job files to ensure that the intended version is being used. | **Module** | **Version(s) on Hydra-7***"(def)" denotes default version***** | **Version(s) on Hydra-6***"(def)" denotes default version***** | **Change in default version?** | **Note** |
| --- | --- | --- | --- | --- |
| ```
abyss
``` | 2.3.7(def) | 2.2.4(def) | yes |  |
| ```
admixtools
``` | 7.0.2(def) |  |  |  |
| ```
admixture
``` | 1.3.0(def) | 1.3.0(def) |  |  |
| ```
angsd
``` | 0.941(def) | 0.921, 0.931, 0.937(def), 0.94 | yes |  |
| ```
assembly_stats
``` | 0.1.4(def) | 0_1_3(def) | yes |  |
| ```
astral
``` | 5.7.8(def), 5.15.5-MP | 5.7.8(def), mp-5.15.5 |  |  |
| ```
augustus
``` | 3.5.0(def) | 3.3.2(def) | yes |  |
| ```
basespace
``` | 1.5.4(def) |  |  |  |
| ```
bayescan
``` | 2.1(def) | 2.1(def) |  |  |
| ```
bbmap
``` | 39.06(def) | 38.67(def) | yes |  |
| ```
bcftools
``` | 1.19(def) | 1.9(def) | yes |  |
| ```
beagle
``` | 4.0.1(def) | 3.2(def), 4.0.1 | yes |  |
| ```
beast
``` | 2.6.7, 2.7.6(def) | 1.10.4, 2.6.0, 2.6.0-no-beagle, 2.6.1, 2.6.3, 2.6.6, 2.6.7(def), 2.7.5-no-beagle, 2.7.6-beagle | yes |  |
| ```
bedtools
``` | 2.31.1(def) | 2.28.0(def) | yes |  |
| ```
bioawk
``` | 1.0(def) | 1.0(def) |  |  |
| ```
bioperl
``` | 1.7.8(def) | 1.7.2(def) | yes |  |
| ```
biopython
``` | 1.83(def) | 1.74(def), 1.74_python2.7 | yes |  |
| ```
blast
``` | 2.15.0(def) | 2.6.0, 2.6.0_old_db, 2.8.1, 2.8.1-precompiled, 2.9.0, 2.9.0_v5, 2.10.1(def), 2.13.0 | yes |  |
| ```
blast2go
``` | To be installed | 1.4.4, 1.5.1(def) |  | This will be installed after the deployment of Hydra77 |
| ```
blobtoolkit
``` | 3.3.10(def) |  |  |  |
| ```
blobtools
``` | 1.1.1(def) | 1.0.1(def), 2, 2.6.3 | yes | This is for blobtools 1.x, later versions are in the module bio/blobtoolkit |
| ```
bowtie2
``` | 2.5.3(def) | 2.3.5(def), 2.5.1 | yes |  |
| ```
bpp
``` | 4.7.0(def) | 1, 4.6.1(def) | yes |  |
| ```
busco
``` | 5.7.0(def) | 3.0.2(def), 4.0.2, 5.1.3, 5.2.2, 5.3.2, 5.4.3 | yes |  |
| ```
bwa
``` | 0.7.17(def) | 0.7.17(def) |  |  |
| ```
cactus
``` | 2.8.0(def) | 2019.03.01, 2020(def), cactus_test | yes |  |
| ```
canu
``` | 2.2(def) | 1.8(def), 2.1.1 | yes |  |
| ```
cd-hit
``` | 4.8.1(def) | 4.8.1 | yes |  |
| ```
cutadapt
``` | 4.7(def) | 2.4(def) | yes |  |
| ```
dates
``` | 753(def) | 753(def) |  |  |
| ```
diamond
``` | 2.1.9(def) | 1.0(def) | yes |  |
| ```
exonerate
``` | 2.4.0(def) | 2.4.0(def) |  |  |
| ```
fastp
``` | 0.23.4(def) | 0.23.4 | yes |  |
| ```
fastqc
``` | 0.12.1(def) | 0.11.8(def) | yes |  |
| ```
faststructure
``` | 1.0(def) | 1.0(def) |  |  |
| ```
fasttree
``` | 2.1.11(def) | 2.1.11(def) |  |  |
| ```
gatk
``` | 3.8.1.0, 4.5.0.0(def) | 3.8.1.0(def), 4.1.3.0 | yes |  |
| ```
gemoma
``` | 1.9(def) | 1.0(def), 1.7.1, 1.9 | yes |  |
| ```
getorganelle
``` | 1.7.7.0(def) | 1.6.2d(def), 1.7.5 | yes |  |
| ```
guppy
``` | 6.5.7(def) | 5.0.16(def) | yes |  |
| ```
hifiasm
``` | 0.19.8(def) | 0.14.2(def), 0.16.1 | yes |  |
| ```
hisat2
``` | 2.2.1(def) | 2.2.1(def) |  |  |
| ```
htslib
``` | 1.19.1(def) | 1.9(def) | yes |  |
| ```
hybpiper
``` | 1.3.1_final, 2.1.6(def) | 1.3.1(def), 2.0.1, 2.1.6 | yes |  |
| ```
illumiprocessor
``` | 2.10(def) | 2.0.9_trimgalore, 2.10_trimgalore, 2.10_trimgalore_2023-02-17(def) | yes |  |
| ```
ipyrad
``` | 0.9.94(def) | 0.7.30(def), 0.9, 0.9.74 | yes |  |
| ```
iqtree
``` | 1.6.12, 2.3.1(def) | 1.6.12, 2.0.4, 2.0.6, 2.1.1, 2.1.2, 2.1.3(def), 2.rc.1 | yes |  |
| ```
jellyfish
``` | 2.3.1(def) | 2.3.0(def) | yes |  |
| ```
kraken
``` | 2.1.3(def) | 2.0(def), 2.1.2 | yes |  |
| ```
krakenuniq
``` | 1.0.4(def) | 1.0.1(def) | yes |  |
| ```
mafft
``` | 7.525(def) | 7.407(def) | yes |  |
| ```
maker
``` | 3.01.03(def) | 2.31.10(def) | yes |  |
| ```
mapdamage2
``` | 2.2.2(def) | 2.2.1(def) | yes |  |
| ```
masurca
``` | 4.1.1(def) | 3.2.2, 3.3.3, 3.3.3_test, 3.3.8(def), 3.3.9, 4.0.0, 4.0.9, 4.1.0 | yes |  |
| ```
merqury
``` | 1.3(def) | 1.3(def) |  |  |
| ```
migrate
``` | 3.7.2, 5.0.6(def) | 3.6.11, 3.7.2, 4.4.4 |  |  |
| ```
minimap2
``` | 2.28(def) | 2.24(def) | yes |  |
| ```
mitofinder
``` | 1.4.1(def) | 1.2(def), 1.4 | yes |  |
| ```
mitos
``` | 2.1.8(def) |  |  |  |
| ```
mitoz
``` | 3.6(def) | 3.5(def) | yes |  |
| ```
mrbayes
``` | 3.2.7a(def) | 3.2.7_beagle, 3.2.7a(def) | yes |  |
| ```
nucmer
``` | 3.2.3, 4.0.0rc1(def) | 3.23(def) | yes |  |
| ```
oma
``` | 2.6.0(def) | 2.3.1, 2.4.1, 2.4.2 |  |  |
| ```
orthofinder
``` | 2.5.5(def) | 2.0.9, 2.5.4 |  |  |
| ```
paup
``` | 4a168(def) |  |  |  |
| ```
phyluce
``` | 1.6.8, 1.7.3(def) | 1.5_tg, 1.6.7(def), 1.7.0, 1.7.1 | yes |  |
| ```
picard-tools
``` | 2.20.6, 3.1.1(def) | 2.20.6(def) | yes |  |
| ```
plink
``` | 1.90b7.2(def) | 1.90b4(def) | yes |  |
| ```
psmc
``` | 0.6.5(def) | 0.6.5(def) |  |  |
| ```
purge_dups
``` | 1.2.6(def) | 1.0(def) | yes |  |
| ```
qiime2
``` | 2024.2-amplicon(def), 2024.2-shotgun | 2019.7, 2019.1, 2020.8, 2021.11(def) | yes | qiime2 now has separate amplicon and shotgun sequencing packages |
| ```
quast
``` | 5.2.0(def) |  |  |  |
| ```
R
``` | 4.3.3(def) | 3.5.2_rgdal, 3.6.0_conda, 3.6.1(def) | yes |  |
| ```
raxml
``` | 8.2.13(def) | 8.2.12(def), 8.2.12-mpi, ng-0.9.0 | yes |  |
| ```
raxml-ng
``` | 1.2.1(def) |  |  |  |
| ```
repeatmasker
``` | 4.1.5, 4.1.6(def) | 4.0.9(def) | yes |  |
| ```
repeatmodeler
``` | 2.0.5(def) | 1.74(def) | yes |  |
| ```
revbayes
``` | 1.2.2(def) | 1.0.11(def), 1.0.13 | yes |  |
| ```
rohan
``` | 1.0.1(def) | 1.0.1(def) |  |  |
| ```
rsem
``` | 1.3.3(def) |  |  |  |
| ```
samtools
``` | 1.19.2(def) | 1.9, 1.17(def) | yes |  |
| ```
seqkit
``` | 2.8.1(def) | 0.13.2, 2.3.1(def) | yes |  |
| ```
seqtk
``` | 1.4(def) | 1.0(def) | yes |  |
| ```
spades
``` | 3.15.5(def) | 3.11.1, 3.12.0, 3.14.0(def), 3.15.5 | yes |  |
| ```
sratoolkit
``` | 3.1.0(def) | 2.9.6, 2.11.0(def) | yes |  |
| ```
stacks
``` | 2.66(def) | 1.48, 2.6.5, 2.41(def) | yes |  |
| ```
structure
``` | 2.3.4(def) | 2.3.4(def) |  |  |
| ```
transabyss
``` | 2.0.1(def) | 2.0.1(def) |  |  |
| ```
transdecoder
``` | 5.7.1(def) | 5.5.0(def) | yes |  |
| ```
transrate
``` | 1.0.3 | 1.0.3, 1.0.3.2, 1.0.3_mamba, 1.0.3_orp |  |  |
| ```
trim_galore
``` | 0.6.10(def) | 0.6.4(def) | yes |  |
| ```
trimmomatic
``` | 0.39(def) | 0.39(def) |  |  |
| ```
trinity
``` | 2.15.1(def) | 2.8.5(def), 2.9.0, 2.9.1, 2.13.2, r2013_2_25 | yes |  |
| ```
vcftools
``` | 0.1.16(def) | 0.1.16(def) |  |  |
| ```
wtdbg2
``` | 2.5(def) | 2.5(def) |  |  |
