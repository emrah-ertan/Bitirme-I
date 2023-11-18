import Convert
import Update

def son_isleme(image_path):
    Convert.to_bitmap(image_path)
    Convert.to_svg_potrace_exe("converted_image.bmp")
    Update.renklendir("converted_image.svg")

son_isleme("GeneratedImages/kergit.jpg")
"""""
#MENU
user_input = input("Enter input:")

image = GenerateImage.generate_image(user_input,GenerateImage.image_gen_model)
image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)


cv2.imshow("Generated Image",image)
user_input = user_input.replace(" ","")
cv2.imwrite("GeneratedImages/"+user_input+".jpg",image)

#ConvertImage.to_bitmap("GeneratedImages/"+user_input+".jpg")
#ConvertImage.to_svg_potrace_exe("converted_image.bmp")


cv2.waitKey(0)
cv2.destroyAllWindows()
"""""