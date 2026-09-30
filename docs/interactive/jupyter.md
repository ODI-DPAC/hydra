# Jupyter

Jupyter Lab runs on a compute node, and an ssh tunnel brings it to a browser on your machine. It keeps a record of an analysis in notebook form and shows images and plots that a terminal cannot.

## Start a Jupyter Lab server

1. Start an [interactive session](qrsh.md), with slots and a GPU if the notebook needs them:

    ```console
    $ qrsh -pe mthread 4
    ```

2. On the compute node, change to the directory the notebooks live in, or above it, because the server serves that tree.

3. Load a Python. Either the Python module:

    ```console
    $ module load tools/python
    ```

    or a conda environment that has Jupyter installed (see [Python and conda](../software/python.md)):

    ```console
    $ module load tools/conda
    $ start-conda
    $ source activate ENVIRONMENT
    ```

    With a GPU, also load the CUDA libraries: `module load nvidia/24/cuda`. `nvidia-smi` then lists the card.

4. Start the server with the script in `tools/jupyter`, which picks a port and prints the tunnel command:

    ```console
    $ module load tools/jupyter
    $ start-jupyter-lab-server
    ```

    `start-jupyter-lab-server --port=N` chooses the port (8000 to 9999; 8888 is the default); `-help` lists the options. Without the script, the command is `jupyter lab --no-browser --ip=$(hostname) --port=8888`, and the output ends with a URL of the form `http://compute-XX-XX.local:8888/?token=…`.

5. On your own machine, open the tunnel the script printed, in a terminal you then leave alone:

    ```console
    $ ssh -N -L 8888:compute-XX-XX:8888 USERNAME@hydra-login01.si.edu
    ```

6. Open <http://localhost:8888> in a browser and paste the token from the server's output when asked, or open `http://localhost:8888/lab?token=TOKEN` directly.

## Stop the server

1. In the browser, choose **File** and then **Shut Down**. This stops the notebook and the server on the node.
2. `Ctrl-C` in the tunnel's terminal.
3. `exit` in the interactive session.

## Use a password instead of the token

Once, on a compute node with the same Python loaded:

```console
$ jupyter server password
```

Later servers ask for that password in place of the token.

## Use a conda environment as a kernel

To run notebooks against the packages of a conda environment, register it as a kernel once:

```console
$ source activate ENVIRONMENT
$ python -m ipykernel install --user --name=ENVIRONMENT
```

The environment then appears in Jupyter's kernel list. A registered kernel also lets a notebook run as a batch job with [Papermill](https://papermill.readthedocs.io/en/latest/).

## Further reading

- [Python and conda](../software/python.md) for installing packages and kernels in your own environment
- [Start an interactive session](qrsh.md) for the session and tunnel this page builds on
