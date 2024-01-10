import Convert
import os

userPrompt = "Tulip Pattern"
adimSayisi = 10
blackLevel = 0.5
olcek = 2


def run():
    import GenerateCivitai
    while True:
        if os.path.exists("GeneratedImages/imageStablev15.png"):
            break
        else:
            continue
    import GenerateHuggingF
    while True:
        if os.path.exists("GeneratedImages/imageStablev14.png"):
            break
        else:
            continue
    import GenerateStabilityai
    while True:
        if os.path.exists("GeneratedImages/imageStability.png"):
            print("Görüntü dosyası mevcut.")
            break
        else:
            continue
    import GenerateCLIP
    while True:
        if os.path.exists("GeneratedImages/imageCLIP.png"):
            print("Görüntü dosyası mevcut.")
            continue
        else:
            pass

def indir():
    Convert.to_svg_openPotrace("GeneratedImages/imageStablev15.png",blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageStablev14.png", blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageStability.png", blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageCLIP.png", blackLevel)