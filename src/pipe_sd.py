import torch
from diffusers import StableDiffusion3Pipeline

pipe = StableDiffusion3Pipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium-diffusers",
    text_encoder_3=None,
    tokenizer_3=None,
    torch_dtype=torch.float16,
)

#pipe.load_lora_weights("/home/server/sd3_trained_models/anime_boobs_300/checkpoint-300")
pipe = pipe.to("cuda")
