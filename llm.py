from os import environ
from pathlib import Path

from huggingface_hub import snapshot_download
from llama_cpp import Llama, llama_supports_gpu_offload

gpu_layers = int(environ.get("LLAMA_GPU_LAYERS", "0"))
if gpu_layers and not llama_supports_gpu_offload():
    raise RuntimeError("GPU offload is unavailable. Check that the Dev Container can access NVIDIA CUDA.")

folder = snapshot_download("Qwen/Qwen2.5-7B-Instruct-GGUF",
                           local_dir=Path(__file__).resolve().parent / ".models" / "qwen2.5-7b-instruct",
                           allow_patterns="*q4_k_m*.gguf")
model = Llama(
    model_path=f"{folder}/qwen2.5-7b-instruct-q4_k_m-00001-of-00002.gguf",
    n_ctx=4096, n_gpu_layers=gpu_layers, verbose=bool(gpu_layers),
)


def llm(context):
    prompt = "\n".join(context) + "\n"
    result = model.create_completion(prompt, temperature=0, max_tokens=128,
        stop=[" THOUGHT:", " TOOL:", " TOOL_OUTPUT:", " RESPONSE:", " OUTPUT:", " USER:"])
    return result["choices"][0]["text"].strip().splitlines()[0]
