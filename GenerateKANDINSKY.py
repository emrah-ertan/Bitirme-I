

from diffusers import AutoPipelineForText2Image
import torch

userPrompt= open("userprompt", "r").read()
mainSeed = open("seed", "r").read()
mainSeed= int(mainSeed)
adimSayisi = open("useradimsayisi", "r").read()


pipe = AutoPipelineForText2Image.from_pretrained("kandinsky-community/kandinsky-2-1", torch_dtype=torch.float16)
pipe.enable_model_cpu_offload()

prompt = userPrompt
negative_prompt = ""

image = pipe(prompt=prompt, negative_prompt=negative_prompt, prior_guidance_scale =1.0, height=512, width=512,num_inference_steps=int(adimSayisi)).images[0]
image.save("GeneratedImages/imageKANDINSKY.png")
