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

creating_ops = (sql_create_table_credit, sql_create_table_client, sql_create_table_client)

inserting_data_client = """
INSERT INTO 
    CLIENT (ID, FIRST_NAME, LAST_NAME, MIDDLE_NAME) 
VALUES 
    (1, 'John', 'Doe', 'Michael'), (2, 'Jane', 'Smith', 'Anne'), (3, 'Jim', 'Beam', 'Thomas'), (4, 'Jack', 'Daniels', 'Ethan'), (5, 'Jessica', 'Jones', 'Maria')
"""
inserting_data_credit = """
INSERT INTO 
    CREDIT (ID, CREDIT_NUMBER, AMOUNT, BALANCE) 
VALUES 
    (1, 'CREDIT001', 10000, 800), (2, 'CREDIT002', 20000, 350), (3, 'CREDIT003', 30000, 1400), (4, 'CREDIT004', 40000, 610), (5, 'CREDIT005', 50000, 1800);
"""

inserting_data_relation = """
INSERT INTO 
    RELATION (ID, CLIENT, CREDIT) 
VALUES 
    (1, 1, 1), (2, 2, 2), (3, 3, 3), (4, 4, 4), (5, 5, 5)
"""

inserting_ops = (inserting_data_relation, inserting_data_client, inserting_data_relation)