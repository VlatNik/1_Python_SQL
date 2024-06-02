from export_csv import *
from connecting_to_db import *

#финальный sql запрос
SQL_ST = """SELECT 
    CLIENT.FIRST_NAME || ' ' || CLIENT.LAST_NAME AS FULL_NAME,
    CREDIT.CREDIT_NUMBER
FROM 
    CLIENT
JOIN 
    RELATION ON CLIENT.ID = RELATION.CLIENT
JOIN 
    CREDIT ON RELATION.CREDIT = CREDIT.ID
WHERE 
    CREDIT.BALANCE > 1000"""

#выгрузка в csv
export_csv(SQL_ST, connecting_to_db())

