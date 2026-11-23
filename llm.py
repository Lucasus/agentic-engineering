from os import environ
from pathlib import Path

from huggingface_hub import hf_hub_download, snapshot_download
from llama_cpp import Llama, llama_perf_context, llama_supports_gpu_offload

gpu_layers = int(environ.get("LLAMA_GPU_LAYERS", "0"))
if gpu_layers and not llama_supports_gpu_offload():
    raise RuntimeError("GPU offload is unavailable. Check that the Dev Container can access NVIDIA CUDA.")

models_dir = Path(__file__).resolve().parent / ".models"
model_name = environ.get("LLAMA_MODEL", "qwen2.5-7b")
if model_name == "qwen2.5-7b":
    folder = snapshot_download(
        "Qwen/Qwen2.5-7B-Instruct-GGUF",
        local_dir=models_dir / "qwen2.5-7b-instruct",
        allow_patterns="*q4_k_m*.gguf",
    )
    model_path = f"{folder}/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf"
elif model_name == "gemma-4-12b":
    model_path = hf_hub_download(
        "ggml-org/gemma-4-12B-it-GGUF",
        "gemma-4-12B-it-Q4_0.gguf",
        local_dir=models_dir / "gemma-4-12b-it",
    )
else:
    raise ValueError(f"Unknown LLAMA_MODEL {model_name!r}. Use qwen2.5-7b or gemma-4-12b.")

model = Llama(
    model_path=model_path,
    n_ctx=4096, n_gpu_layers=gpu_layers, verbose=False,
)


def llm(context):
    stop = [" THOUGHT:", " TOOL:", " TOOL_OUTPUT:", " RESPONSE:", " OUTPUT:", " USER:"]
    if model_name == "gemma-4-12b":
        result = model.create_chat_completion(
            messages=[
                {"role": "system", "content": context[0]},
                {"role": "user", "content": "\n".join(context[1:])},
            ],
            temperature=0,
            max_tokens=128,
            stop=stop,
        )
        text = result["choices"][0]["message"]["content"] or ""
    else:
        prompt = "\n".join(context) + "\n"
        result = model.create_completion(prompt, temperature=0, max_tokens=128, stop=stop)
        text = result["choices"][0]["text"]
    return text.strip().partition("\n")[0]


def print_generation_speed():
    timing = llama_perf_context(model.ctx)
    if timing.t_eval_ms > 0:
        tokens_per_second = 1000 * timing.n_eval / timing.t_eval_ms
        print(f"Generation speed: {tokens_per_second:.1f} tokens/s")
    else:
        print("Generation speed: unavailable")
