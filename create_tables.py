import cx_Oracle
from tables import *

try:
    conn_db = conn = cx_Oracle.connect("system/12345678@//localhost:1521/XEPDB1")
except Exception as err:
    print('Error with connecting to database', err)
else:
    cursor_db = conn_db.cursor()
    print('Connected to database')
    try:
        cursor_db.execute(sql_create_table_client)
        cursor_db.execute(sql_create_table_credit)
        cursor_db.execute(sql_create_table_relation)
    except Exception as err:
        print('Error with creating tables', err)
finally:
    cursor_db.close()
    conn_db.close()