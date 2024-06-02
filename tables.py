#sql запросы для создания и наполнения таблиц

sql_create_table_client = """
CREATE TABLE CLIENT(
    ID NUMBER PRIMARY KEY,
    FIRST_NAME VARCHAR2(50),
    LAST_NAME VARCHAR2(50),
    MIDDLE_NAME VARCHAR2(50)
)
"""

sql_create_table_credit = """
CREATE TABLE CREDIT(
    ID NUMBER PRIMARY KEY,
    CREDIT_NUMBER VARCHAR2(50),
    AMOUNT NUMBER,
    BALANCE NUMBER
)
"""

sql_create_table_relation = """
CREATE TABLE RELATION(
    ID NUMBER PRIMARY KEY,
    CLIENT NUMBER,
    CREDIT NUMBER,
    CONSTRAINT fk_client FOREIGN KEY (CLIENT) REFERENCES CLIENT(ID),
    CONSTRAINT fk_credit FOREIGN KEY (CREDIT) REFERENCES CREDIT(ID)
)
"""

creating_ops = (sql_create_table_credit, sql_create_table_client, sql_create_table_relation)