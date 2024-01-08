import xml.etree.ElementTree as ET



def svg(svg_path,scale_x,scale_y):
    tree = ET.parse(svg_path)
    root = tree.getroot()

    for element in root.iter():
        if 'x' in element.attrib and 'y' in element.attrib:
            element.set('x', str(float(element.get('x')[:3]) * scale_x))
            element.set('y', str(float(element.get('y')[:3]) * scale_y))
        if 'width' in element.attrib:
            element.set('width', str(float(element.get('width')[:3]) * scale_x))
        if 'height' in element.attrib:
            element.set('height', str(float(element.get('height')[:3]) * scale_y))

    # Ölçeklendirilmiş SVG dosyasını kaydet
    tree.write("vector_graphic_scaled.svg")
    print("SVG dosyası yeniden ölçeklendirildi")
