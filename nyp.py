try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElemeneTree as ET

tree = ET.parse('complete.xml')

root = ET.parse("complete.xml") #root is "programs"

for work in root.findall("program/worksInfo/work"):
    ID = work.get("ID")
    composerName = work.find("composerName")
    if composerName != None:          
       composerName = composerName.text
    else: 
       composerName = ''
    workTitle = work.find("workTitle")
    if workTitle != None:
        workTitle = workTitle.text
    else:
        workTitle = '' 
    movement = work.find("movement")
    if movement != None:
        movement = movement.text
    else:
        movement = ''
    conductor = work.find("conductor")
    if conductor != None:
        conductor = conductor.text
    else:
        conductor = ''
    print ID, composerName, workTitle, movement, conductor


