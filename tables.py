sql_create_table_client = """
CREATE TABLE CLIENT(
    ID NUMBER PRIMARY KEY,
    FIRST_NAME VARCHAR(255),
    LAST_NAME VARCHAR(255),
    MIDDLE_NAME VARCHAR(255)
)
"""

sql_create_table_credit = """
CREATE TABLE CREDIT(
    ID NUMBER PRIMARY KEY,
    CREDIT_NUMBER VARCHAR(255),
    AMOUNT VARCHAR(255),
    BALANCE VARCHAR(255)
)
"""

sql_create_table_relation = """
CREATE TABLE RELATION(
    ID NUMBER PRIMARY KEY,
    CLIENT VARCHAR(255) FOREIGN KEY(ID) REFERENCES CLIENT(ID),
    CREDIT VARCHAR(255) FOREIGN KEY(ID) REFERENCES CREDIT(ID),
)
"""

