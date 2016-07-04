try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

root = ET.parse("complete.xml")

f = open("conductor.txt", "w") # Open the file in (w)rite mode

f.write("programID,season,workID,composerLastName,composerFirstName,workTitle,OpusNumber,conductorLastName,conductorFirstName\n")
for program in root.findall('program'):
    programID = program.find('programID').text
    season = program.find('season').text
    worksInfo = program.find('worksInfo')
    if worksInfo is None:
        work = ''
    else: 
        work = worksInfo.find('work')
	if work is None:
	    workID = ''
	    composerName = ''
            workTitle = ''
            conductorName = ''
        else:
            workID = work.get('ID')
            composerName = work.find('composerName')
	    if composerName is None:
		composerName = ''
	    else:
                composerName = composerName.text
                composerLastName = composerName.split(',')[0]
                if len(composerName.split(',')) > 1:
                    composerFirstName = composerName.split(',')[1]
                else:
		    composerFirstName = ''
            workTitle = work.find('workTitle')
	    if workTitle is None:
		workTitle = ''
            else:
		workTitle = workTitle.text
		WorkTitle = workTitle.split(',')[0]
		if len(workTitle.split(',')) > 1:
		    OpusNumber = workTitle.split(',')[1]
                    conductorName = work.find('conductorName')
		    if conductorName is None:
			conductorName = ''
                    else:
			conductorName = conductorName.text
			conductorLastName = conductorName.split(',')[0]
			if len(conductorName.split(',')) > 1:
			    conductorFirstName = conductorName.split(',')[1]
			line = programID + "," + season + "," + workID + "," + composerLastName + ',' + composerFirstName + ',' + WorkTitle + "," + OpusNumber + ',' + conductorLastName + ',' + conductorFirstName + "\n"
                        f.write(line)

f.close()
