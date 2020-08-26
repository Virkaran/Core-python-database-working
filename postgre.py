import psycopg2

conn = psycopg2.connect(database="testdb", user = "postgres", password = "******", host = "127.0.0.1", port = "5432")

cur = conn.cursor()
create_table='''CREATE TABLE Employee
      (info     string[]);'''
cur.execute(create_table)
conn.commit()
print("Created")

# create_table='''CREATE TABLE Employee
#       (ID INT PRIMARY KEY     NOT NULL,
#       NAME  TEXT    NOT NULL);'''
