import numpy as np
import Convert
import Scale
import os
import time

userPrompt = "Blank Canvas"
adimSayisi = 10

blackLevel = 0.5
olcek = 0.5
dosya = open("olcek", "w").write(str(olcek))

mainSeed = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])



def run():
    #Mevcut Dosyaların Silinmesi

    #png dosyalarını sil
    if os.path.exists("GeneratedImages/imageStablev15.png"):
        os.remove("GeneratedImages/imageStablev15.png")
    if os.path.exists("GeneratedImages/imageStablev15ClipSkip.png"):
        os.remove("GeneratedImages/imageStablev15ClipSkip.png")
    if os.path.exists("GeneratedImages/imageStablev14.png"):
        os.remove("GeneratedImages/imageStablev14.png")
    if os.path.exists("GeneratedImages/imageStability.png"):
        os.remove("GeneratedImages/imageStability.png")
    if os.path.exists("GeneratedImages/imageKANDINSKY.png"):
        os.remove("GeneratedImages/imageKANDINSKY.png")
    if os.path.exists("GeneratedImages/imageMiniDalle2.png"):
        os.remove("GeneratedImages/imageMiniDalle2.png")

    #svg dosyalarını sil
    if os.path.exists("GeneratedImages/vector_graphicStablev15.svg"):
        os.remove("GeneratedImages/vector_graphicStablev15.svg")
    if os.path.exists("GeneratedImages/vector_graphicStablev15ClipSkip.svg"):
        os.remove("GeneratedImages/vector_graphicStablev15ClipSkip.svg")
    if os.path.exists("GeneratedImages/vector_graphicStablev14.svg"):
        os.remove("GeneratedImages/vector_graphicStablev14.svg")
    if os.path.exists("GeneratedImages/vector_graphicStability.svg"):
        os.remove("GeneratedImages/vector_graphicStability.svg")
    if os.path.exists("GeneratedImages/vector_graphicKANDINSKY.svg"):
        os.remove("GeneratedImages/vector_graphicKANDINSKY.svg")
    if os.path.exists("GeneratedImages/vector_graphicMiniDalle2.svg"):
        os.remove("GeneratedImages/vector_graphicMiniDalle2.svg")

    #scaled svg dosyalarını sil
    if os.path.exists("GeneratedImages/vector_graphic_scaledStablev15.svg"):
        os.remove("GeneratedImages/vector_graphic_scaledStablev15.svg")
    if os.path.exists("GeneratedImages/vector_graphic_scaledStablev15ClipSkip.svg"):
        os.remove("GeneratedImages/vector_graphic_scaledStablev15ClipSkip.svg")
    if os.path.exists("GeneratedImages/vector_graphic_scaledStablev14.svg"):
        os.remove("GeneratedImages/vector_graphic_scaledStablev14.svg")
    if os.path.exists("GeneratedImages/vector_graphic_scaledStability.svg"):
        os.remove("GeneratedImages/vector_graphic_scaledStability.svg")
    if os.path.exists("GeneratedImages/vector_graphic_scaledKANDINSKY.svg"):
        os.remove("GeneratedImages/vector_graphic_scaledKANDINSKY.svg")
    if os.path.exists("GeneratedImages/vector_graphic_scaledMiniDalle2.svg"):
        os.remove("GeneratedImages/vector_graphic_scaledMiniDalle2.svg")


    #Mevcut dosyalar silindikten sonra yeni dosyaların oluşturulması
    import GenerateCivitai
    while True:
        if os.path.exists("GeneratedImages/imageStablev15.png"):
            break
        else:
            continue
    import GenerateCivitaiClipSkip
    while True:
        if os.path.exists("GeneratedImages/imageStablev15ClipSkip.png"):
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
            break
        else:
            continue
    import GenerateKANDINSKY
    while True:
        if os.path.exists("GeneratedImages/imageKANDINSKY.png"):
            break
        else:
            continue
    import GenerateMiniDalle2
    while True:
        if os.path.exists("GeneratedImages/imageMiniDalle2.png"):
            break
        else:
            continue
    print(f"Main.py run() fonksiyonu çalıştı. Gelen prompt: {userPrompt}")
    print(f"Main.py run() fonksiyonu çalıştı. Gelen adım sayısı: {adimSayisi}")
    print(f"Dönüş değeri 1 olarak belirlendi ve döndürülüyor")
    return 1


def indir():
    if os.path.exists("GeneratedImages/imageStablev15.png"):
        Convert.to_svg_openPotrace("GeneratedImages/imageStablev15.png", blackLevel)
    if os.path.exists("GeneratedImages/imageStablev15ClipSkip.png"):
        Convert.to_svg_openPotrace("GeneratedImages/imageStablev15ClipSkip.png",blackLevel)
    if os.path.exists("GeneratedImages/imageStablev14.png"):
        Convert.to_svg_openPotrace("GeneratedImages/imageStablev14.png", blackLevel)
    #if os.path.exists("GeneratedImages/imageStability.png"):
        # Convert.to_svg_openPotrace("GeneratedImages/imageStability.png", blackLevel)
    if os.path.exists("GeneratedImages/imageKANDINSKY.png"):
        Convert.to_svg_openPotrace("GeneratedImages/imageKANDINSKY.png",blackLevel)
    if os.path.exists("GeneratedImages/imageMiniDalle2.png"):
        Convert.to_svg_openPotrace("GeneratedImages/imageMiniDalle2.png",blackLevel)


    if os.path.exists("GeneratedImages/vector_graphicStablev15.svg"):
        Scale.svg("GeneratedImages/vector_graphicStablev15.svg")
    if os.path.exists("GeneratedImages/vector_graphicStablev15ClipSkip.svg"):
        Scale.svg("GeneratedImages/vector_graphicStablev15ClipSkip.svg")
    if os.path.exists("GeneratedImages/vector_graphicStablev14.svg"):
        Scale.svg("GeneratedImages/vector_graphicStablev14.svg")
    #if os.path.exists("GeneratedImages/vector_graphicStability.svg"):
        #Scale.svg("GeneratedImages/vector_graphicStability.svg")
    if os.path.exists("GeneratedImages/vector_graphicKANDINSKY.svg"):
        Scale.svg("GeneratedImages/vector_graphicKANDINSKY.svg")
    if os.path.exists("GeneratedImages/vector_graphicMiniDalle2.svg"):
        Scale.svg("GeneratedImages/vector_graphicMiniDalle2.svg")

    print(f"Main.py indir() fonksiyonu çalıştı. Gelen blackLevel: {blackLevel}")
    print(f"Main.py indir() fonksiyonu çalıştı. Gelen ölçek: {olcek}")
    return 1