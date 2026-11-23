# Calculator agent

## In the Dev Container

In VS Code, open this repository and select **Dev Containers: Reopen in Container**.
The container installs the Python packages automatically. Skip straight to the
sample commands below.

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

The first run downloads a 4.7 GB model into `.models/` and runs it on your CPU.

The examples add tool calls, thoughts, and follow-up questions in that order.
For the third example, enter `3` when asked for a multiplier. All three should
return `126`.
