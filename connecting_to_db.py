import cx_Oracle
from tables import *

cursor_db = ''


def connecting_to_db():
    try:
        conn_db = conn = cx_Oracle.connect("system/12345678@//localhost:1521/XEPDB1")
    except Exception as err:
        print('Error with connecting to database', err)
    else:
        cursor_db = conn_db.cursor()
        print('Connected to database')

connecting_to_db()
