import xml.etree.ElementTree as ET

olcek =open("olcek", "r").read()
olcek = float(olcek)

def svg(svg_path):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    for element in root.iter():
        if 'x' in element.attrib and 'y' in element.attrib:
            element.set('x', str(float(element.get('x')[:3]) * olcek))
            element.set('y', str(float(element.get('y')[:3]) * olcek))
        if 'width' in element.attrib:
            element.set('width', str(float(element.get('width')[:3]) * olcek))
        if 'height' in element.attrib:
            element.set('height', str(float(element.get('height')[:3]) * olcek))

    # Ölçeklendirilmiş SVG dosyasını kaydet
    tree.write(f"GeneratedImages/vector_graphic_scaled{svg_path[30:-4]}.svg")
    print("SVG dosyası yeniden ölçeklendirildi")