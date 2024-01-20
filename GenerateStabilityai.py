import os
import io
import warnings

import numpy as np
import torch
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
userPrompt= open("userprompt", "r").read()
mainSeed = open("seed", "r").read()
mainSeed= int(mainSeed)
adimSayisi = open("useradimsayisi", "r").read()



stability_key = open("STABILITY_KEY", "r").read()

os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'
os.environ['STABILITY_KEY'] = stability_key

stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0",
)


stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0",
)




answers = stability_api.generate(
    prompt= str(userPrompt),
    seed=[mainSeed],
    steps=int(adimSayisi),
    cfg_scale=8.0,
    width=512,
    height=512,
    samples=1,
    sampler=generation.SAMPLER_K_DPMPP_2M
)

for resp in answers:
    for artifact in resp.artifacts:
        if artifact.finish_reason == generation.FILTER:
            warnings.warn(
                "Your request activated the API's safety filters and could not be processed."
                "Please modify the prompt and try again.")
        if artifact.type == generation.ARTIFACT_IMAGE:
            img = Image.open(io.BytesIO(artifact.binary))
            img.save("GeneratedImages/imageStability.png")



