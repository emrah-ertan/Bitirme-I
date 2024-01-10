from PIL import Image
import potrace
import Scale
from main import olcek
def to_svg_openPotrace(path,blackLevel):

    image = Image.open(path)

    bm = potrace.Bitmap(image, blacklevel=blackLevel)
    # bm.invert()
    plist = bm.trace()
    if(path == "GenerateImages/imageStablev15.png"):
        with open(f"vector_graphic_imageStablev15.svg", "w") as fp:
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
        Scale.svg("GenerateImages/imageStablev15.svg",olcek)
    elif(path == "GenerateImages/imageStablev14.png"):
        with open(f"vector_graphic_imageStablev14.svg", "w") as fp:
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
        Scale.svg("GenerateImages/imageStablev14.svg", olcek)
    elif (path == "GenerateImages/imageStability.png"):
        with open(f"vector_graphic_imageStability.svg", "w") as fp:
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
        Scale.svg("GenerateImages/imageStability.svg", olcek)
    elif (path == "GenerateImages/imageCLIP.png"):
        with open(f"vector_graphic_imageCLIP.svg", "w") as fp:
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
        Scale.svg("GenerateImages/imageCLIP.svg", olcek)
    elif (path =="GenerateImages/imageStablev15ClipSkip.png"):
        with open(f"vector_graphic_imageStablev15ClipSkip.svg", "w") as fp:
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
        Scale.svg("GenerateImages/imageStablev15ClipSkip.svg",olcek)

    print("SVG Dosyası oluşturuldu")