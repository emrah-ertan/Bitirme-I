import subprocess
from PIL import Image
import cv2
import numpy as np
import OpenPotrace

def to_svg_openPotrace(path):
    try:
        image = Image.open(path)
    except IOError:
        print("Image (%s) could not be loaded." % path)
        return

    bm = OpenPotrace.Bitmap(image, blacklevel=0.5)
    # bm.invert()
    plist = bm.trace()
    with open(f"{path[:-4]}.svg", "w") as fp:
        fp.write(
            f'''<svg version="1.1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{image.width}" height="{image.height}" viewBox="0 0 {image.width} {image.height}">''')
        parts = []
        for curve in plist:
            fs = curve.start_point
            parts.append(f"M{fs.x},{fs.y}")
            for segment in curve.segments:
                if segment.is_corner:
                    a = segment.c
                    b = segment.end_point
                    parts.append(f"L{a.x},{a.y}L{b.x},{b.y}")
                else:
                    a = segment.c1
                    b = segment.c2
                    c = segment.end_point
                    parts.append(f"C{a.x},{a.y} {b.x},{b.y} {c.x},{c.y}")
            parts.append("z")
        fp.write(f'<path stroke="none" fill="black" fill-rule="evenodd" d="{"".join(parts)}"/>')
        fp.write("</svg>")







def to_bitmap(path,bitmapThresh):
    image = cv2.imread(path)
    array_image = np.array(image)

    r, g, b = np.split(array_image, 3, axis=2)
    r = r.reshape(-1)
    g = r.reshape(-1)
    b = r.reshape(-1)

    bitmap = list(map(lambda x: 0.299 * x[0] + 0.587 * x[1] + 0.114 * x[2], zip(r, g, b)))
    bitmap = np.array(bitmap).reshape([array_image.shape[0], array_image.shape[1]])

    bitmap = np.dot((bitmap > bitmapThresh).astype(float), 255)
    im = Image.fromarray(bitmap.astype(np.uint8))
    #im.save('output.bmp')
    return im



def to_svg_potrace_exe(bitmap_path):
    parametreler = ["potrace.exe", bitmap_path, "-b", "svg"]
    subprocess.run(parametreler)

























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