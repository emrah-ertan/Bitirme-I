import numpy as np
from diffusers import AutoPipelineForText2Image
import torch
import cv2

from main import userPrompt

pipeline = AutoPipelineForText2Image.from_pretrained('dataautogpt3/OpenDalleV1.1', torch_dtype=torch.float16).to('cuda')
image = pipeline(userPrompt).images[0]


image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
cv2.imwrite("GeneratedImages/imageDalle"+".png",image)