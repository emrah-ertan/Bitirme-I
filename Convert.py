import subprocess
from PIL import Image
import cv2
import numpy as np
import OpenPotrace


def to_bitmap(path,bitmapThresh):
    image = cv2.imread(path)
    array_image = np.array(image)

    # Split the three channels
    r, g, b = np.split(array_image, 3, axis=2)
    r = r.reshape(-1)
    g = r.reshape(-1)
    b = r.reshape(-1)

    # Standard RGB to grayscale
    bitmap = list(map(lambda x: 0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2], zip(r, g, b)))
    bitmap = np.array(bitmap).reshape([array_image.shape[0], array_image.shape[1]])

    bitmap = np.dot((bitmap > bitmapThresh).astype(float), 255)
    im = Image.fromarray(bitmap.astype(np.uint8))
    im.save('output.bmp')
    print("Bitmap dosyası 'image.bmp' oluşturuldu")
    return im



def to_svg_potrace_exe(bitmap_path):
    parametreler = ["potrace.exe", bitmap_path, "-b", "svg"]
    subprocess.run(parametreler)
    print("Bitmap dosyası svg formatına dönüştürüldü")





def to_svg_openPotrace(path,bitmapThresh=125):
    data = to_bitmap(path,bitmapThresh)
    bitmap = OpenPotrace.Bitmap(data,0.5)
    path = bitmap.trace()
    #print(path)

    with open('output.svg', 'w') as file:
        file.write('<svg width="512" height="512" xmlns="http://www.w3.org/2000/svg">\n')
        for i in path:
            file.write(f'<path d="{i}" />\n')
        file.write('</svg>')





















"""""
def to_svg(image_path):

    image = Image.open(image_path)

    with open("converted_to_vector_graphic.svg", "w") as svg_file:

        svg_file.write('<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n')
        svg_file.write('<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" ')
        svg_file.write('"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n')
        svg_file.write('<svg width="{}" height="{}" xmlns="http://www.w3.org/2000/svg">\n'.format(image.width,
                                                                                                  image.height))
        # Her pikseli dönerek SVG çıktısını oluştur
        for y in range(image.height):
            for x in range(image.width):
                r, g, b = image.getpixel((x, y))
                svg_file.write(
                    '<rect x="{}" y="{}" width="1" height="1" fill="rgb({},{},{})" />\n'.format(x, y, r, g, b))
        # SVG kapanış etiketini yaz
        svg_file.write('</svg>\n')

    print("JPG dosyası başarıyla SVG dosyasına dönüştürüldü.")
"""""

"""""
def svg2png(bytestring=None, *, file_obj=None, url=None, dpi=300,
            parent_width=None, parent_height=None, scale=1, unsafe=False,
            background_color=None, negate_colors=False, invert_images=False,
            write_to=None, output_width=None, output_height=None):
    return surface.PNGSurface.convert(
        bytestring=bytestring, file_obj=file_obj, url=url, dpi=dpi,
        parent_width=parent_width, parent_height=parent_height, scale=scale,
        background_color=background_color, negate_colors=negate_colors,
        invert_images=invert_images, unsafe=unsafe, write_to=write_to,
        output_width=output_width, output_height=output_height)
"""""