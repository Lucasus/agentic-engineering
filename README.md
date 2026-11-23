# Calculator agent

Three versions of a small calculator agent. The model runs directly inside Python using plain-text completion.

|File|Adds|
|-|-|
|`01\_basic.py`|`TOOL` calls and final `OUTPUT`|
|`02\_thoughts.py`|`THOUGHT` lines|
|`03\_response.py`|`RESPONSE` questions for missing information|
|`llm.py`|Downloads and runs the local model|

## Run

### Dev Container

Open this repository as its own folder in VS Code and choose **Dev Containers:
Reopen in Container**. The image installs the pinned Python packages and puts
its virtual environment on `PATH`. Run the examples below directly in the
container terminal. Rebuild the container after dependency changes.

### Local Python outside the Dev Container

Use Python 3.11 or newer with `venv` support and the `python` command available.
On Debian or Ubuntu, the `python-is-python3` and `python3-venv` packages provide
these if needed. Set up once from the repository root.

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

For local Python, run `source .venv/bin/activate` in each new terminal.

### Examples

```sh
python 01_basic.py
python 02_thoughts.py
python 03_response.py
```

The first run downloads [Qwen2.5 7B Q4_K_M](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct-GGUF), about **4.7 GB**, into the repository's ignored `.models/` directory. The model runs locally on your CPU without a GPU, API key or separate model server.

The first two examples solve the boxes problem from the slides. The third asks for a multiplier: enter `3`. The answer is `126` in all three.

Pass your own task as an argument:

```sh
python 01_basic.py "What is 18 divided by 3?"
```

## How it works

The LLM helper joins the context into one text prompt and generates its continuation. It uses no chat API, role dictionaries, or chat template. Stop strings limit generation before another protocol entry.

The loop calls the LLM, appends its reply, executes a requested tool, and appends `TOOL\_OUTPUT`. `OUTPUT` finishes; `THOUGHT` continues; `RESPONSE` waits for your answer.

Tool requests are plain text, such as `TOOL: add(17, 25)`. Python parses the numbers and calls a function without `eval`. Tool-call errors go back into context.

`THOUGHT` is generated explanation text. These are minimal teaching examples; a model can still get stuck. Press Ctrl+C to stop.
