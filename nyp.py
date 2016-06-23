try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElemeneTree as ET
    

#import xml.etree.ElementTree as ET

#import untangle

tree = ET.parse('complete.xml')
programs = tree.getroot()
programs.tag, programs.attrib

