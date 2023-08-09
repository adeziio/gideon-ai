import torch
from diffusers import StableDiffusionPipeline


def run(input):
    try:
        input = input.lower()
        response = ""

        # print("Torch version:", torch.__version__)

        # print("Is CUDA enabled?", torch.cuda.is_available())

        pipe = StableDiffusionPipeline.from_pretrained(
            "stable-diffusion-v1-5")
        pipe = pipe.to("cuda")

        with torch.autocast('cuda'):
            image = pipe(input).images[0]

        image.save("generated_image.png")

        return response
    except Exception as e:
        return str(e)
