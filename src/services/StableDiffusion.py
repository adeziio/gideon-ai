# import torch
# from diffusers import StableDiffusionPipeline


# def run(model, input):
#     try:
#         input = input.lower()
#         response = ""

#         if (model == "aden"):
#             pipe = StableDiffusionPipeline.from_single_file(
#                 "src/models/aden.ckpt", torch_dtype=torch.float16,)
#             pipe = pipe.to("cuda")

#             with torch.autocast('cuda'):
#                 image = pipe(input).images[0]

#             image.save("generated_image.png")

#         return response
#     except Exception as e:
#         return str(e)
