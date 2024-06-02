from tables import *
from connecting_to_db import *


def deleting_tables():
    try:
        cursor_db.execute("DROP TABLE RELATION")
        cursor_db.execute("DROP TABLE CREDIT")
        cursor_db.execute("DROP TABLE CLIENT")
    except Exception as err:
        print('Error with deleting tables', err)
