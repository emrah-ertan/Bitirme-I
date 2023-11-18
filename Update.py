import cv2
import numpy as np
import xml.etree.ElementTree as ET



def _renkBelirle(r,g,b):
    renk_kodu = "#{:02x}{:02x}{:02x}".format(r, g, b)
    return renk_kodu

def _nothing(x):
    pass


def renklendir(svg_path):
    img = np.zeros((512, 680, 3), np.uint8)
    cv2.namedWindow("resim")
    cv2.createTrackbar("R", "resim", 0, 255, _nothing)
    cv2.createTrackbar("G", "resim", 0, 255, _nothing)
    cv2.createTrackbar("B", "resim", 0, 255, _nothing)
    while (1):
        cv2.imshow("resim", img)
        r = cv2.getTrackbarPos("R", "resim")
        g = cv2.getTrackbarPos("G", "resim")
        b = cv2.getTrackbarPos("B", "resim")
        img[:] = [b, g, r]
        if (cv2.waitKey(1) & 0xFF == ord("q")):
            # SVG dosyasını aç
            tree = ET.parse(svg_path)
            root = tree.getroot()
            # Tüm "path" öğelerini bul
            paths = root.findall('.//{http://www.w3.org/2000/svg}path')  # path öğelerini SVG dosyasına göre bul
            for path in paths:
                path.set('fill', _renkBelirle(r,g,b))
                #print(_renkBelirle(r,g,b))
            # Değiştirilmiş SVG dosyasını kaydet
            tree.write('colored_converted_image.svg')
            break
    cv2.destroyAllWindows()