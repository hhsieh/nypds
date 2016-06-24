import sqlite3
import xml.etree.cElementTree

def insert_work(db_conn, workID, composerName, workTitle, movement, conductor):
    curs = db_conn.cursor()
    curs.execute("insert into work values (?,?,?,?,?)", (workID, composerName, workTitle, movement, conductor))
    db_conn.commit()

def work_data_from_element(element):
    workID = element.get("ID")
    if workID != None:
        workID = workID
    else:
        workID = ''
    composerName = element.find("composerName")
    if composerName != None:
        composerName = composerName.text
    else:
        composerName = ''
    workTitle = element.find("workTitle")
    if workTitle != None:
        workTitle = workTitle.text
    else:
        workTitle = ''
    movement = element.find("movement")
    if movement != None:
        movement = movement.text
    else:
        movement = ''
    conductor = element.find("conductor")
    if conductor != None:
        conductor = conductor.text
    else:
        conductor = ''
    return workID, composerName, workTitle, movement, conductor

## add the main loop to get all the work information from the XML file
if __name__ == "__main__":
    conn = sqlite3.connect("work.sqlite3")
    programs = xml.etree.cElementTree.parse("complete.xml")
    work = programs.findall("program/worksInfo/work")
    for index, element in enumerate(work):
        workID, composerName, workTitle, movement, conductor = work_data_from_element(element)
        insert_work(conn, workID, composerName, workTitle, movement, conductor)

