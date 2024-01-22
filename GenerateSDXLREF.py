import random
import sys
import torch
from diffusers import DiffusionPipeline

# Kullanıcının girdiği prompt'ın okunması
with open("userprompt", 'r') as dosyaPrompt:
    userPrompt = dosyaPrompt.read()

# Kullanıcının belirlediği adım sayısının okunması
with open("useradimsayisi", "r") as dosyaAdimSayisi:
    adimSayisi = int(dosyaAdimSayisi.read())

# Seed değerinin okunması
with open("seed", "r") as dosyaSeed:
    mainSeed = int(dosyaSeed.read())


pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16,
    use_safetensors=True,
    variant="fp16",
    )

use_refiner = True

if use_refiner:
  refiner = DiffusionPipeline.from_pretrained(
      "stabilityai/stable-diffusion-xl-refiner-1.0",
      text_encoder_2=pipe.text_encoder_2,
      vae=pipe.vae,
      torch_dtype=torch.float16,
      use_safetensors=True,
      variant="fp16",
  )

  refiner = refiner.to("cuda")

  pipe.enable_model_cpu_offload()
else:
  pipe = pipe.to("cuda")

#prompt = "a photo of Pikachu fine dining with a view to the Eiffel Tower"
prompt = userPrompt
seed = mainSeed

images = pipe(
    prompt = prompt,
    output_type = "latent" if use_refiner else "pil",
    generator = torch.Generator("cuda").manual_seed(seed),
    ).images

if use_refiner:
  images = refiner(
      prompt = prompt,
      image = images,
      ).images

#print(f"Prompt:\t{prompt}\nSeed:\t{seed}")
images[0].save("GeneratedImages/imageSDXLREF.png")

