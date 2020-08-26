import psycopg2

class DBconnection(object):
     def __init__(self,database,user,passward,host,port):
         self.database=database
         self.user=user
         self.passward=passward
         self.host=host
         self.port=port

     def _connect_(self):
         self.conn = psycopg2.connect(database="self.database", user = "self.user", password = "self.passward", host = "self.host",port = "self.port")
         return self.conn

     def _exit_(self):
         self.conn.close()

#set the details in the environment






