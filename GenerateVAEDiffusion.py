import numpy as np
import torch
import cv2


with open("userprompt", "r") as dosyaPrompt:
    prompt = dosyaPrompt.read()
with open("userAdimSayisi", "r") as dosyaAdimSayisi:
    adimSayisi= dosyaAdimSayisi.read()
with open("seed", "r") as dosyaSeed:
    mainseed = dosyaSeed.read()

from diffusers import (
    StableDiffusionXLPipeline,
    KDPM2AncestralDiscreteScheduler,
    AutoencoderKL
)

# Load VAE component
vae = AutoencoderKL.from_pretrained(
    "madebyollin/sdxl-vae-fp16-fix",
    torch_dtype=torch.float16
)

# Configure the pipeline
pipe = StableDiffusionXLPipeline.from_pretrained(
    "dataautogpt3/ProteusV0.2",
    vae=vae,
    torch_dtype=torch.float16,
    seed = mainseed
)
pipe.scheduler = KDPM2AncestralDiscreteScheduler.from_config(pipe.scheduler.config)
pipe.to('cuda')

# Define prompts and generate image
negative_prompt = ""

image = pipe(
    prompt,
    negative_prompt=negative_prompt,
    width=512,
    height=512,
    guidance_scale=9,
    num_inference_steps=adimSayisi,
).images[0]

image2 = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

cv2.imwrite("GeneratedImages/imageVAEDiffusion.png")
cv2.imwrite("GeneratedImages/imageVAEDiffusionBGR.png")