# Calculator agent

## In the Dev Container

Select **Dev Containers: Reopen in Container** in VS Code. If the old container
is already open, select **Dev Containers: Rebuild Container** once.

```sh
python 01_basic.py                     # CPU
LLAMA_GPU_LAYERS=-1 python 01_basic.py # GPU
```

The container requires x86-64, an NVIDIA driver with CUDA 12.4 support, and
[Docker GPU access in WSL 2](https://docs.docker.com/desktop/features/gpu/).
On a machine without GPU access, use the local setup below.

## Outside the Dev Container

From the repository root, use Python 3.11 or newer with `venv` support. On
Debian or Ubuntu, `python-is-python3` and `python3-venv` provide these if needed.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

In each new terminal, run `source .venv/bin/activate` before running a sample.

## Run a sample

```sh
python 01_basic.py
python 02_thoughts.py
python 03_response.py
```

The first run downloads a 4.7 GB model into `.models/`.

The examples add tool calls, thoughts, and follow-up questions in that order.
For the third example, enter `3` when asked for a multiplier. All three should
return `126`.
