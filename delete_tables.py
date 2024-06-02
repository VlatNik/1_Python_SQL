from tables import *
from connecting_to_db import *


def deleting_tables(connect):
    cursor_db = connect.cursor()
    try:
        cursor_db.execute("DROP TABLE CREDIT")
        cursor_db.execute("DROP TABLE CLIENT")
        cursor_db.execute("DROP TABLE RELATION")
    except Exception as err:
        print('Error with deleting tables', err)


deleting_tables(connecting_to_db())