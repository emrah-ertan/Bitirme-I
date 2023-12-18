import openai
from base64 import b64decode

openai_key = open("OPENAI_KEY", "r").read()

prompt = "Tulip Pattern"
size = "512x512"
n = 1
response_format = "b64_json"

response = openai.Image.create(prompt,n,size,response_format = response_format)



#RESİM KAYDETME
images = []
for image in response['data']:
    images.append(image.b64_json)

prompt = prompt.replace(" ","").lower()
for index,image in enumerate(images):
    with open(f"{prompt}{index}.png","wb") as file:
        file.write(b64decode(image))




"""""
#IMAGE DEĞİL URL DÖNDÜRME

imageUrl = response['data'][0]['url']
print(imageUrl)
"""""