import sqlite3

connect = sqlite3.connect('test.db')

connect.execute("DROP TABLE IF EXISTS CUSTOMER")

connect.execute(''' CREATE TABLE CUSTOMER
             (ID INT PRIMARY KEY NOT NULL,
             NAME TEXT NOT NULL,
             AGE INT NOT NULL);''')

db_data = connect.execute("SELECT * FROM CUSTOMER")
for row in db_data:
    print(row)

connect.execute("INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (1, 'test', 24)")
connect.execute("INSERT INTO CUSTOMER (ID, NAME, AGE) VALUES (2, 'test2', 20)")

print("After insert operation")

db_data = connect.execute("SELECT * FROM CUSTOMER")
for row in db_data:
    print(row)

connect.execute("UPDATE CUSTOMER SET AGE = 21 WHERE ID = 2")

print("After update operation")

db_data = connect.execute("SELECT * FROM CUSTOMER")
for row in db_data:
    print(row)


connect.execute("DELETE FROM CUSTOMER WHERE ID = 2")

print("After delete operation")

db_data = connect.execute("SELECT * FROM CUSTOMER")
for row in db_data:
    print(row)

connect.close()