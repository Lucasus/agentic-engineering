# Calculator agent

In VS Code, open this repository and select **Dev Containers: Reopen in Container**.
Then run any example in the container terminal:

```sh
python 01_basic.py
python 02_thoughts.py
python 03_response.py
```

The container installs the Python packages automatically. The first run downloads
a 4.7 GB model into `.models/` and runs it on your CPU.

The examples add tool calls, thoughts, and follow-up questions in that order.
For the third example, enter `3` when asked for a multiplier. All three should
return `126`.
