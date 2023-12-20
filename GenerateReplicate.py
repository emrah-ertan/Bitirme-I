import replicate


replicate_key = open("REPLICATE_KEY", "r").read()


#Drawer Types:
    #vqgan
    #vdiff
    #pixel


output = replicate.run(
  "pixray/text2image:5c347a4bfa1d4523a58ae614c2194e15f2ae682b57e3797a5bb468920aa70ebf",
  input={
    "drawer": "vqgan",
    "prompts": "Tulip Pattern",
    "settings": "\n"
  }
)
print(output)