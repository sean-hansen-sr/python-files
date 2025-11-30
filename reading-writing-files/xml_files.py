import xml.etree.ElementTree as ET

def parse_xml_etree(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    print('Domains for: ' + root.attrib['name'])
    for child in root:
        print('\t' + child.attrib['name'], child.tag)

def add_xml_element(file_path, el, attr, val):
    tree = ET.parse(file_path)
    root = tree.getroot()
    child = ET.Element(el)
    child.attrib[attr] = val
    root.append(child)
    tree.write(file_path)

def change_xml_element_et(file_path, el, attr, old_val, new_val):
    tree = ET.parse(file_path)
    root = tree.getroot()
    child = root.find("./" + el + "[@" + attr + "='" + old_val + "']")
    child.attrib[attr] = new_val
    tree.write(file_path)

if __name__ == "__main__":
    #parse_xml_etree('./files_to_read/ef_author.xml')
    #add_xml_element('./files_to_read/ef_author.xml', 'domain', 'name', 'Java')
    change_xml_element_et('./files_to_read/ef_author.xml', 'domain', 'name', 'Java', 'JavaScript')