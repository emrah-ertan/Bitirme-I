import numpy as np
import Convert
import Scale
import os
import time

userPrompt = "Portal of glory"
adimSayisi = 10

blackLevel = 0.5
olcek = 0.5
dosya = open("olcek", "w").write(str(olcek))

mainSeed = np.random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])



def run():
    startTime1 = time.time()
    import GenerateCivitai
    while True:
        if os.path.exists("GeneratedImages/imageStablev15.png"):
            break
        else:
            continue
    endTime1 = time.time()
    elapsedTime1 = endTime1 - startTime1

    startTime2 = time.time()
    import GenerateCivitaiClipSkip
    while True:
        if os.path.exists("GeneratedImages/imageStablev15ClipSkip.png"):
            break
        else:
            continue
    endTime2 = time.time()
    elapsedTime2 = endTime2 - startTime2
    startTime3 = time.time()
    import GenerateHuggingF
    while True:
        if os.path.exists("GeneratedImages/imageStablev14.png"):
            break
        else:
            continue
    endTime3 = time.time()
    elapsedTime3= endTime3 - startTime3
    """""startTime4 = time.time()
    import GenerateStabilityai"
    while True:
        if os.path.exists("GeneratedImages/imageStability.png"):
            break
        else:
            continue
    endTime4= time.time()
    elapsedTime= endTime4-startTime4"""""
    startTime5 = time.time()
    import GenerateKANDINSKY
    while True:
        if os.path.exists("GeneratedImages/imageKANDINSKY.png"):
            break
        else:
            continue
    endTime5 =time.time()
    elapsedTime5 = endTime5 - startTime5
    startTime6 = time.time()
    import GenerateMiniDalle2
    while True:
        if os.path.exists("GeneratedImages/imageMiniDalle2.png"):
            break
        else:
            continue
    endTime6 =time.time()
    elapsedTime6 = endTime6 - startTime6


    print(f"Elapsed Time1: {elapsedTime1}")
    print(f"Elapsed Time2: {elapsedTime2}")
    print(f"Elapsed Time3: {elapsedTime3}")
    #print(f"Elapsed Time4: {elapsedTime4}")
    print(f"Elapsed Time5: {elapsedTime5}")
    print(f"Elapsed Time6: {elapsedTime6}")


def indir():
    Convert.to_svg_openPotrace("GeneratedImages/imageStablev15.png", blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageStablev15ClipSkip.png",blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageStablev14.png", blackLevel)
    # Convert.to_svg_openPotrace("GeneratedImages/imageStability.png", blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageKANDINSKY.png",blackLevel)
    Convert.to_svg_openPotrace("GeneratedImages/imageMiniDalle2.png",blackLevel)

    Scale.svg("GeneratedImages/vector_graphicStablev15.svg")
    Scale.svg("GeneratedImages/imageStablev15ClipSkip.svg")
    Scale.svg("GeneratedImages/vector_graphicStablev14.svg")
    #Scale.svg("GeneratedImages/imageStability.svg")
    Scale.svg("GeneratedImages/imageKANDINSKY.svg")
    Scale.svg("GeneratedImages/imageMiniDalle2.svg")