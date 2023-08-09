# import torch
from diffusers import StableDiffusionPipeline


def run(model, input):
    try:
        input = input.lower()
        response = ""

        if (model == "aden"):
            pipe = StableDiffusionPipeline.from_single_file(
                "src/models/aden.ckpt",
                # torch_dtype=torch.float16
            )
            pipe = pipe.to("cuda")
            image = pipe(input).images[0]
            # with torch.autocast('cuda'):
            #     image = pipe(input).images[0]

            image.save("temp/image.png")
            import base64

            with open("temp/image.png", "rb") as image_file:
                encoded_string = base64.b64encode(
                    image_file.read()).decode('utf-8')

            response = encoded_string

        return response
    except Exception as e:
        return str(e)
