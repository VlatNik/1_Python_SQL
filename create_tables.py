from tables import *
from connecting_to_db import *


def ops_tables(connect,sql_st_table):
    #создание курсора
    cursor_db = connect.cursor()
    try:
        cursor_db.execute(sql_st_table)
    except Exception as err:
        print('Error with ops with tables:', err)
    finally:
        #закрытие курсора и коннекшна
        cursor_db.close()
        connect.close()


#создание и добавление данных
for op in creating_ops:
    ops_tables(connecting_to_db(), op)

for op in inserting_ops:
    ops_tables(connecting_to_db(), op)
