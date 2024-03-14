import sqlite3
import os


DESTINATION_DIRECTORY = os.getcwd()+'/'
DESTINATION_DB_NAME = 'example.sqlite'
DESTINATION_DB = f"{DESTINATION_DIRECTORY}{DESTINATION_DB_NAME}"


def prep_db(db_name:str)->sqlite3.Connection:
    #print (list(route_table.return_structure.keys())[0])
    tables = {'devices': ['name', 'ip', 'mask', 'admin']}
    router1 = ['"router1"','"192.168.1.1"','"255.255.255.0"','"True"']
    router2 = ['"router2"','"192.168.2.2"','"255.255.255.0"','"False"']

    with sqlite3.connect(db_name) as con:
        cur = con.cursor()
        for table,columns in tables.items():
            try:
                cur.execute(f"create table {table}(id integer primary key autoincrement, {','.join(columns)})")
            except:
                pass
            cur.execute(f'insert into {table}({",".join(columns)}) values ({",".join(router1)})')
            cur.execute(f'insert into {table}({",".join(columns)}) values ({",".join(router2)})')

        con.commit()
    return con
    
def main():
    prep_db(DESTINATION_DB_NAME)

if __name__ == '__main__': main()
