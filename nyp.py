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


#for program in root.findall("program"):
#    id = program.find("id")
#    programID = program.find("programID")
#    orchestra = program.find("orchestra")
#    season = program.find("season")

    



      
import lxml #to get parent nodes

for soloist in root.findall("program/worksInfo/work/soloists/soloist"):
    soloistName = soloist.find("soloistName")
    #parent = soloistName.getparent()
    if soloistName != None:
        soloistName = soloistName.text
    else:
        soloistName = ''
    #if parent != None:
    #    parent = parent.text
    #else:
    #    parent = ''
    print soloistName#, parent


for soloist in root.findall("program/worksInfo/work/soloists/soloist"):
    soloistName = soloist.find("soloistName")
    if soloistName != None:
        soloistName = soloistName.text
    else:
        soloistName = ''
    soloistInstrument = soloist.find("soloistInstrument")
    if soloistInstrument != None:
        soloistInstrument = soloistInstrument.text
    else:
        soloistInstrument = ''
    soloistRole = soloist.find("soloistRoles")
    if soloistRole != None:
        soloistRole = soloistRole.text
    else:
        soloistRole = ''
    print soloistName, soloistInstrument, soloistRole

import lxml



for work in root.findall('program/worksInfo/work'):
    for composerName in work.findall('composerName'):
        if composerName.text != None:
            print work.attrib['ID'], composerName.text
        else:
            print work.attrib['ID'], ''

for work in root.findall('program/worksInfo/work'):   
    for soloistInstrument in work.findall('soloists/soloist/soloistInstrument'):
        if soloistInstrument.text != None:
            print work.attrib['ID'], soloistInstrument.text
        else:
            print work.attrib['ID'], ''  


for program in root.findall('program'):
    programID = program.find('programID')
    season = program.find('season')
    if programID is not None:
        worksInfo = program.find('worksInfo')
        if worksInfo is not None:
            work = worksInfo.find('work')
            if work is not None:
                composerName = work.find('composerName')
                if composerName is not None:
                    workTitle = work.find('workTitle')
                    conductorName = work.find('conductorName')
                    if conductorName is not None:
                        print programID.text, season.text, work.attrib['ID'], composerName.text, workTitle.text, conductorName.text
    




#programID = [programID for programID in root.findall('program/programID')]
#print(len(programID))            


#for work in root.findall('program/worksInfo/work'):
#    workID = [work.attrib['ID'] for work.attrib['ID'] in root.findall('program/worksInfo/work')]
#    soloistName = [soloistName.text for soloistName in work.findall('soloists/soloist/soloistName')]
#    print workID
#    print soloistName


#for Date in root.findall('program/concertInfo/Date'):
#    print Date.text     
     
        

