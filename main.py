from export_csv import *
from connecting_to_db import *

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


export_csv(SQL_ST, connecting_to_db())

