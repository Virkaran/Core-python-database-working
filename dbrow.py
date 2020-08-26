import psycopg2

conn = psycopg2.connect(database="testdb", user = "postgres", password = "karan", host = "127.0.0.1", port = "5432")

cur = conn.cursor()

insert_query='''INSERT INTO Employee(ID,NAME)VALUES (%s,%s)'''
record=(1,"karan")
cur.execute(insert_query,record)
conn.commit()
print("added")