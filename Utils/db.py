"""
Utility file for all database functions.
"""

import os
from Assets.constants import DataBase
import sqlite3 as sql 
import logging as log

""" 
table created
cur.execute(f"CREATE TABLE {DataBase.table_name}(
                                                Question varchar, 
                                                Option1 varchar,
                                                Option2 varchar,
                                                Option3 varchar,
                                                Option4 varchar,
                                                correct int,
                                                User varchar
                                            )")
"""

def get_connection():   
    con = sql.connect(DataBase.db_name)
    return con 
    
def upload_question(question, opt1, opt2, opt3, opt4, correct , user_name) -> bool:
    cmd = f"""INSERT INTO {DataBase.table_name} VALUES(
    '{question}',
    '{opt1}', 
    '{opt2}',
    '{opt3}',
    '{opt4}',
    {correct},
    '{user_name}'
    )"""
    try:
        con = get_connection()
        cursor = con.cursor()
        
        cursor.execute(cmd)
        con.commit()
        con.close()
        return True
    
    except Exception as e : 
        log.error(f"Error occurred while uploading trivia question to db:- ({e})")
        con.close()
        return False

def download_qeustion():
    """Use query 'SELECT * FROM table ORDER BY RANDOM() LIMIT 1;' to fetch a random row"""
    pass 

if __name__ == "__main__":
    con = get_connection()

    cur = con.cursor()

    cur.execute(f"SELECT * FROM {DataBase.table_name}")

    result = cur.fetchall()
    for x in result:
        print(x)