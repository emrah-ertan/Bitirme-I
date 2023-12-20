import torch
from diffusers import StableDiffusionPipeline


hugging_face_key = open("HUGGING_FACE_KEY", "r").read()

class CFG:
    if(torch.cuda.is_available()):
        device ="cuda"
    else:
        print("CUDA Bulunamadı! CPU Kullanılıyor...")
        device = "cpu"

    seed = 7
    generator = torch.Generator(device).manual_seed(seed)
    image_gen_steps = 5
    #image_gen_model_id = "ChineseLandscapeArt_v10"
    #image_gen_model_id = "CompVis/stable-diffusion-v1-4"
    #image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size =(256,256)
    image_gen_guidance_scale = 9
    prompt_gen_model_id = "gpt2"
    prompt_dataset_size = 6
    prompt_max_length = 27

image_gen_model = StableDiffusionPipeline.from_pretrained(CFG.image_gen_model_id,torch_dtype=torch.float16,
                    revision="fp16",use_auth_token=hugging_face_key, safety_checker=None, guidance_scale=9)
image_gen_model = image_gen_model.to(CFG.device)


def generateImage(prompt,model):
    image = model(
        prompt, num_inference_steps = CFG.image_gen_steps,
        generator =CFG.generator,
        guidance_scale=CFG.image_gen_guidance_scale
    ).images[0]

    image = image.resize(CFG.image_gen_size)
    return image
