from tables import *
from connecting_to_db import *


def create_tables():
    try:
        cursor_db.execute(sql_create_table_client)
        cursor_db.execute(sql_create_table_credit)
        cursor_db.execute(sql_create_table_relation)
    except Exception as err:
        print('Error with creating tables', err)
