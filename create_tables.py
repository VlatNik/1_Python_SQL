from tables import *
from connecting_to_db import *


def create_tables(connect,sql_st_table1, sql_st_table2, sql_st_table3):
    cursor_db = connect.cursor()
    try:
        cursor_db.execute(sql_create_table_client)
        cursor_db.execute(sql_create_table_credit)
        cursor_db.execute(sql_create_table_relation)
    except Exception as err:
        print('Error with creating tables:', err)

def insert_data_into_tables(connect):
    cursor_db = connect.cursor()
    try:
        cursor_db.execute(inserting_data_client)
        cursor_db.execute(inserting_data_credit)
        cursor_db.execute(inserting_data_relation)
    except Exception as err:
        print('Error with inserting data tables:', err)

#create_tables(connect, sql_create_table_client, sql_create_table_credit,sql_create_table_relation)