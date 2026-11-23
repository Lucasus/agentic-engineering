# Calculator agent

## In the Dev Container

In VS Code, open this repository and select **Dev Containers: Reopen in Container**.
Choose **Agentic Engineering (CPU)** for the standard setup, or
**Agentic Engineering (NVIDIA GPU)** on x86-64 Windows with an NVIDIA driver
that supports CUDA 12.4 and [Docker Desktop using WSL 2](https://docs.docker.com/desktop/features/gpu/).
If you already have a container open, use **Dev Containers: Switch Container**.
Both install their Python packages automatically.

The GPU option uses the same sample commands and model files. To offload fewer
layers if GPU memory is tight, run `LLAMA_GPU_LAYERS=16 python 01_basic.py`.

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
