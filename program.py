import sqlite3
import xml.etree.cElementTree

def insert_program(db_conn, id, programID, orchestra, season, concertInfo, worksInfo):
    curs = db_conn.cursor()
    curs.execute("insert into program values (?,?,?,?,?,?)", (id, programID, orchestra, season, concertInfo, worksInfo))
    db_conn.commit()

def program_data_from_element(element):
    id = element.find("id").text
    programID = element.find("programID").text
    orchestra = element.find("orchestra").text
    season = element.find("season").text
    concertInfo = element.find("concertInfo").text
    worksInfo = element.find("worksInfo").text
    return id, programID, orchestra, season, concertInfo, worksInfo

## add the main loop to get all the programs from the XML file
if __name__ == "__main__":
    conn = sqlite3.connect("program.sqlite3")
    program = xml.etree.cElementTree.parse("complete.xml")
    program = program.findall("program")
    for index, element in enumerate(program):
        id, programID, orchestra, season, concertInfo, worksInfo  = program_data_from_element(element)
        insert_program(conn, id, programID, orchestra, season, concertInfo, worksInfo)

