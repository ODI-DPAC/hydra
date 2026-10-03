# Find scrubbed files and request a restore

Every week the scrubber removes files older than 180 days, and old empty directories, from `/scratch/public`. It moves the files to a staging area and deletes them permanently about ten days later. The rules are under [Filesystems](filesystems.md#scrubbing). You receive an email when any of your files are scrubbed. You can check beforehand what the scrubber will remove, find out afterwards what it removed, and ask for some of it back.

The scrubber tools are in the `tools/scrubber` module. `module help tools/scrubber` lists them. Each has a man page.

## Check what will be scrubbed

1. Load the module and search a directory for files near the age limit:

    ```console
    $ module load tools/scrubber
    $ find-scrub -in /scratch/genomics/USERNAME/project-a -age 173
    ```

    `-in` defaults to the current directory. `-age` defaults to 173 days, a week before the limit.

2. Move anything you still need to `/data`, or off Hydra, before the next Sunday.

`find-scrub` reads every file in the tree, which loads the file server. Run it only on the directories you care about.

## Find out what was scrubbed

1. Note the date in the email. The report is keyed by it as `YYMMDD`.

2. Print the report for your directory and that date:

    ```console
    $ module load tools/scrubber
    $ show-scrubber-report /scratch/public/genomics/USERNAME 260920
    ```

3. List the scrubbed files, or the scrubbed empty directories:

    ```console
    $ list-scrubbed-files -long /scratch/public/genomics/USERNAME 260920
    $ list-scrubbed-dirs -long /scratch/public/genomics/USERNAME 260920
    ```

    `-long` adds age and size. `-all` adds the owner. `-n` prints only the count. A Perl regular expression as a last argument limits the list, for example `'^/scratch/public/genomics/USERNAME/project-a/.*\.log$'` for the `.log` files under `project-a`.

## Request a restore

We restore files only while they are in the staging area, and only for a list you have trimmed to what you need.

1. Write the list of scrubbed files under the directory you want back:

    ```console
    $ module load tools/scrubber
    $ list-scrubbed-files /scratch/public/genomics/USERNAME 260920 /scratch/public/genomics/USERNAME/project-a > restore.list
    ```

    The path argument matches as a prefix, so `project-a` also matches `project-a2`.

2. Edit `restore.list` down to the files you need.

3. Verify the list:

    ```console
    $ verify-restore-list -d /scratch/public/genomics/USERNAME 260920 restore.list
    ```

    Fix anything it reports and verify again. One list per scrubbing date and per partition.

4. Email the full path of the list file to [SI-HPC@si.edu](mailto:SI-HPC@si.edu) before 5 pm on the Friday after the scrubbing. Send the path. Do not attach the file.

!!! danger "Scrubbed files are permanently deleted about ten days after the scrubbing"

    After that no restore is possible. Files in the staging area still count against your quota until then.

A restored file gets a new change time (`ctime`), which is what the scrubber measures, so it is safe for another 180 days. `stat FILE` shows it.

## Further reading

- [Filesystems](filesystems.md#scrubbing) for the scrubbing rules
- [Backups](backups.md) for what is and is not protected
