import sqlite3
import xml.etree.cElementTree

def insert_program(db_conn, programID, orchestra, season):
    curs = db_conn.cursor()
    curs.execute("insert into program values (?,?,?)", (programID, orchestra, season))
    db_conn.commit()

def program_data_from_element(element):
    programID = element.find("programID").text
    orchestra = element.find("orchestra").text
    season = element.find("season").text
    return programID, orchestra, season

## add the main loop to get all the programs from the XML file
if __name__ == "__main__":
    conn = sqlite3.connect("program.sqlite3")
    program = xml.etree.cElementTree.parse("complete.xml")
    program = program.findall("program")
    for index, element in enumerate(program):
        programID, orchestra, season = program_data_from_element(element)
        insert_program(conn, programID, orchestra, season)

