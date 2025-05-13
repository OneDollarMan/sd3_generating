from typing import Optional
import torch
from PIL import Image
from src.pipe_sd import pipe


def generate_image(prompt: str) -> Optional[Image]:
    if not torch.cuda.is_available():
        print('Cuda is not available')
        return None

    image = pipe(
        prompt,
        num_inference_steps=30,
        guidance_scale=7.0,
        #generator=torch.Generator().manual_seed(0)
    ).images[0]
    return image
