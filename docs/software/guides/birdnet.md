# BirdNET

[BirdNET-Analyzer](https://birdnet-team.github.io/BirdNET-Analyzer/) identifies bird species in audio recordings with a deep-learning model covering more than 6,000 species. Two modules provide version 2.4.0: `bio/birdnet` (the default) for analysis, on CPUs, and `bio/birdnet/2.4.0-gpu` for training custom classifiers on a GPU. Both provide `birdnet-analyze`, `birdnet-segments`, `birdnet-species`, `birdnet-train`, `birdnet-evaluate`, `birdnet-embeddings`, `birdnet-search` and `ffprobe`; the model is installed with them, so jobs need no network access.

The models are licensed CC BY-NC-SA 4.0, for non-commercial use. Cite Kahl, Wood, Eibl and Klinck (2021), *Ecological Informatics* 61:101236.

## Size the dataset

Analysis processes 30 to 60 hours of audio per CPU-hour, so the hours of audio divided by the slots requested gives the expected run time; the number of files matters only as the upper bound on useful slots. Count the hours with the module's `ffprobe`:

```console
$ module load bio/birdnet
$ for f in /scratch/genomics/USERNAME/audio/*; do ffprobe -v error -show_entries format=duration -of csv=p=0 "$f"; done \
    | awk '{s+=$1} END {printf "%.1f hours in %d files\n", s/3600, NR}'
```

## Analyse recordings

Analysis runs on CPUs; do not request a GPU. `--threads` parallelises across files, one file per thread, so request no more slots than the directory has files. TensorFlow needs about 6 GB of virtual memory even for one file: keep slots × `h_data` at 8 GB or more (for one slot, `-l mres=8G,h_data=8G,h_vmem=8G`).

```sh title="birdnet.job"
#$ -S /bin/sh
#$ -N birdnet -cwd -j y -o birdnet.log
#$ -q sThC.q
#$ -pe mthread 8
#$ -l mres=16G,h_data=2G,h_vmem=2G
#
set -e
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + NSLOTS = $NSLOTS
module load bio/birdnet
birdnet-analyze /scratch/genomics/USERNAME/audio \
    -o /scratch/genomics/USERNAME/birdnet_out \
    --threads $NSLOTS \
    --min_conf 0.25
echo = `date` job $JOB_NAME done
```

`set -e` stops the job at the first failed command, so the final `done` line prints only on success. The example is at `/share/apps/bioinformatics/birdnet/2.4.0/examples/birdnet.job`.

For more than about 200 hours of audio, split the recordings into directories and run one [array task](../../jobs/arrays.md) per directory rather than one large job; each recording is analysed independently.

## Train a custom classifier

Training runs on a GPU with the `2.4.0-gpu` module, as a job or under `qrsh -l gpu,ngpus=1`, never on a login node. Training data is one subdirectory per class, each holding 3-second clips.

```sh title="birdnet-train.job"
#$ -S /bin/sh
#$ -N birdnet-train -cwd -j y -o birdnet-train.log
#$ -q sTgpu.q
#$ -l gpu,ngpus=1,gpuarch=L40S
#$ -l mres=16G,h_data=16G,h_vmem=64G
#
set -e
echo + `date` job $JOB_NAME started in $QUEUE with jobID=$JOB_ID on $HOSTNAME
echo + CUDA_VISIBLE_DEVICES = $CUDA_VISIBLE_DEVICES
module load bio/birdnet/2.4.0-gpu
export OMP_NUM_THREADS=1
export TF_NUM_INTEROP_THREADS=1
export TF_NUM_INTRAOP_THREADS=1
birdnet-train /scratch/genomics/USERNAME/train_data \
    -o /scratch/genomics/USERNAME/custom_classifier
echo = `date` job $JOB_NAME done
```

!!! warning "`h_vmem` below 64 GB crashes training with a misleading message"

    TensorFlow and CUDA map about 40 GB of virtual memory for the smallest training run. With a smaller `h_vmem` the job fails at start with `cudaSetDevice ... out of memory`, which refers to the job's virtual-memory limit, not to GPU memory, and exits with status 0. `set -e` is what makes the job report the failure.

Give `-o` an absolute path; a relative path crashes when the classifier is saved. The three `export` lines keep TensorFlow's CPU thread pools inside the one slot the job requested. Training has been run on the L40S node, which the `gpuarch=L40S` request selects; CPU slots can be added with `-pe mthread Z` (see [GPUs](../gpus.md)), but training is GPU-bound and gains little from them. The example is at `/share/apps/bioinformatics/birdnet/2.4.0-gpu/examples/birdnet-train.job`.

To analyse recordings with the trained classifier, run `birdnet-analyze` from the CPU module, as above, with `--classifier` pointing at the saved model.

## Errors

BirdNET writes its error log to `~/birdnet_error_log.txt`; read it when a run fails without a clear message in the job log. `BUILD_INFO.txt` in each installation directory records the patches applied to the upstream package on Hydra.
