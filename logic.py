import torch
from diffusers import StableDiffusionPipeline

device = "cuda" if torch.cuda.is_available() else "cpu"

def load_model():
    print(f"Loading models to {device}")

    pipe_txt2img = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5"
    ).to(device)

    return pipe_txt2img

def generate_image(pipe, prompt, neg_prompt, seed, steps, cfg):

    # Setup Generator (Seed)
    generator = torch.Generator(device).manual_seed(seed)

    # Generate gambar standard
    image = pipe(
        prompt,
        negative_prompt=neg_prompt,
        num_inference_steps=steps,
        guidance_scale=cfg,
        generator=generator,
        height=512, width=512
    ).images[0]

    return [image]