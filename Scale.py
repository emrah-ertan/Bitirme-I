import xml.etree.ElementTree as ET



def svg(svg_path):
    # SVG dosyasını aç
    tree = ET.parse(svg_path)
    root = tree.getroot()

    # Ölçeklendirme faktörü
    olcek = 7

    # SVG içeriğini dolaşın ve vektör nesnelerini ölçekleyin
    for element in root.iter():
        if 'x' in element.attrib and 'y' in element.attrib:
            element.set('x', str(float(element.get('x')[:3]) * olcek))
            element.set('y', str(float(element.get('y')[:3]) * olcek))
            #element.set('x', str(float(element.get('x')) * float(1920/512)))
            #element.set('y', str(float(element.get('y')) * float(1080/512)))
        if 'width' in element.attrib:
            element.set('width', str(float(element.get('width')[:3]) * olcek))
        if 'height' in element.attrib:
            element.set('height', str(float(element.get('height')[:3]) * olcek))

    # Ölçeklendirilmiş SVG dosyasını kaydet
    tree.write("scaled_vector_graphic.svg")
    print("SVG dosyası yeniden ölçeklendirildi")
