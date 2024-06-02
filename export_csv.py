import csv
import datetime
from connecting_to_db import *

SQL_ST = "SELECT * FROM CLIENT"
def export_csv(sql_st, cnct_to_db):
    filename = 'report' + str(datetime.datetime.now().date()) + '.csv'
    file = open(filename, 'w+')
    output = csv.writer(file, dialect='excel')
    con_db = cnct_to_db
    cur_db = con_db.cursor()
    cur_db.execute(sql_st)
    columns = [i[0] for i in cur_db.description]
    try:
        output.writerow(columns)
        for row in cur_db:
            print(row)
            output.writerow(row)

    except Exception as err:
        ("Error with export data:", err)
    finally:
        if cur_db:
            cur_db.close()
        if file:
            file.close()

