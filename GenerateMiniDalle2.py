import torch
from min_dalle import MinDalle
from torchvision.utils import save_image
from main import userPrompt, mainSeed

def generate_image(
    is_mega: bool,
    text: str,
    seed: int,
    grid_size: int,
    top_k: int,
    image_path: str,
    models_root: str,
    fp16: bool
):
    model = MinDalle(
        is_mega=is_mega,
        models_root=models_root,
        is_reusable=False,
        is_verbose=True,
        dtype=torch.float16 if fp16 else torch.float32,
    )

    image = model.generate_image(
        text,
        seed,
        grid_size,
        top_k=top_k,
        is_verbose=True
    )
    save_image(image, image_path)

generate_image(False,userPrompt,int(mainSeed), 1,1,"GeneratedImages/imageMiniDalle2.png",models_root="./pretrained",fp16=False)