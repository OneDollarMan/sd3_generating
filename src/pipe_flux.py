import torch
from diffusers import FluxPipeline

pipe = FluxPipeline.from_pretrained("black-forest-labs/FLUX.1-schnell", torch_dtype=torch.bfloat16)
print("[x] FluxPipeline loaded")
pipe.transformer.to("cuda")
print("[x] Transferred to cuda")
pipe.enable_model_cpu_offload()
print("[x] Ready")
