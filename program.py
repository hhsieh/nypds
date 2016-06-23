import sqlite3

def insert_program(db_conn, programID, orchestra, season):
    curs = db_conn.cursor()
    curs.execute("insert into program values (?,?,?)", (programID, orchestra, season))
    db_conn.commit()


def program_data_from_element(element):
    programID = element.find("programID").text
    orchestra = element.find("orchestra").text
    season = element.find("season").text
    return programID, orchestra, season

