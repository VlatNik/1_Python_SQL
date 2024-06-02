import cx_Oracle

#подключение к дб
def connecting_to_db():
    try:
        #создание коннекшена
        conn_db = cx_Oracle.connect("system/12345678@//localhost:1521/XEPDB1")
    except Exception as err:
        print('Error with connecting to database:', err)
    else:
        return conn_db
        print('Connected to database')



