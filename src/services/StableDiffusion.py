def run(model, input):
    try:
        import base64
        import torch
        from diffusers import StableDiffusionPipeline

        input = input.lower()
        response = ""

        pipe = StableDiffusionPipeline.from_single_file(
            f"src/models/{model}.ckpt",
            torch_dtype=torch.float16
        )
        pipe = pipe.to("cuda")
        image = pipe(input).images[0]
        with torch.autocast('cuda'):
            image = pipe(input).images[0]

        image.save("temp/image.png")

        with open("temp/image.png", "rb") as image_file:
            encoded_string = base64.b64encode(
                image_file.read()).decode('utf-8')
        response = encoded_string
        return response
    except Exception as e:
        return str(e)
