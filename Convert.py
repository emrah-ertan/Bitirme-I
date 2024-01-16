from PIL import Image
import potrace
import Scale




def to_svg_openPotrace(path,blackLevel):

    image = Image.open(path)

    bm = potrace.Bitmap(image, blacklevel=float(blackLevel))
    # bm.invert()
    plist = bm.trace()
    with open(f"GeneratedImages/vector_graphic{path[21:-4]}.svg", "w") as fp:
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

    print("SVG Dosyası oluşturuldu")