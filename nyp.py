import xml.etree.ElementTree as ET
import untangle
tree = ET.parse('complete.xml')
root = tree.getroot()
print(root[0])


