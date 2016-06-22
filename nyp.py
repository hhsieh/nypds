try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElemeneTree as ET
    

#import xml.etree.ElementTree as ET

import untangle

tree = ET.parse('complete.xml')
programs = tree.getroot()
programs.tag, programs.attrib

#for child_of_root in root:
#    for grands in child_of_root:
#        for greats in grands:
#            print greats.tag + ": " +  greats.text
            
programs = tree.findall("program")
for program in programs:
    print program.find("programID").text
    print program.find("orchestra").text
    print program.find("season").text
 

import sqlite3
conn = sqlite3.connect("program.sqlite3")
curs = conn.cursor()
curs.execute("insert into program values (?, ?, ?)", (1,"NYO","2030-2031"))
curs.rowcount
conn.commit()    
    
for row in curs.fetchall():
    print(row)
