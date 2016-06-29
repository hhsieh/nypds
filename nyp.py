try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElemeneTree as ET


root = ET.parse("complete.xml") #root is "programs"

## collect data - workID, composerName, workTitle, movement, conductor
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

   
## collect data - soloistName, soloistInstrument, soloistRole 
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

##collect data - workID, composerName
for work in root.findall('program/worksInfo/work'):
    for composerName in work.findall('composerName'):
        if composerName.text != None:
            print work.attrib['ID'], composerName.text
        else:
            print work.attrib['ID'], ''

## collect data - workID, soloistName
for work in root.findall('program/worksInfo/work'):   
    for soloistName in work.findall('soloists/soloist/soloistName'):
        if soloistName.text != None:
            print work.attrib['ID'], soloistName.text
        else:
            print work.attrib['ID'], ''  

## collect data - programID, workID, season, composerName, workTitle, conductorName
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
    

## collect data - programID, workID, season, composerName, workTitle, conductorName, soloistName, soloistInstrument, soloistRole (need some tweats; not work yet)
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
			soloistName = work.find('soloists/soloist/soloistName')
			if soloistName is not None:
			    soloistInstrument = work.find('soloists/soloist/soloistInstrument')
			    if soloistInstrument is not None:				
				soloistRole = work.find('soloists/soloist/soloistRole')
				if soloistRole is not None:	
				    print programID.text, season.text, work.attrib['ID'], composerName.text, workTitle.text, conductorName.text, soloistName.text, soloistInstrument.text, soloistRole.text





        

