#import GenerateCivitai
#import Generate
import cv2
import numpy as np


"""""
#MENU
user_input = input("Enter input:")

image = Generate.generateImage(user_input,Generate.image_gen_model)
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)


cv2.imshow("Generated Image",image)
user_input = user_input.replace(" ","")
cv2.imwrite("GeneratedImages/"+user_input+".jpg",image)

Convert.to_bitmap("GeneratedImages/"+user_input+".jpg")
Convert.to_svg_potrace_exe("image.bmp")
Update.renklendir(image.svg)


cv2.waitKey(0)
cv2.destroyAllWindows()
"""""