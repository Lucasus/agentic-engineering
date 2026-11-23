FROM python:3.11.18-slim-bookworm@sha256:a83ba18aef0f865b1a4a611c2cf460fe446f2795673bbb9fe43be570439e3b39

RUN apt-get update \
    && apt-get install -y --no-install-recommends git libstdc++6 \
    && rm -r /var/lib/apt/lists/* \
    && useradd --create-home --shell /bin/bash vscode

COPY requirements*.txt /tmp/
COPY --chmod=755 .devcontainer/gpu /usr/local/bin/gpu
USER vscode
ENV PATH="/home/vscode/.venv/bin:${PATH}"
RUN python -m venv /home/vscode/.venv \
    && python -m pip install --no-cache-dir -r /tmp/requirements.txt
