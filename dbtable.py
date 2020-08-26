import psycopg2
import dbconnect

class _Table_(object):
    def __init__(self,ID,name,conn,create_tb):
        self.ID=ID
        self.name=name
        self.conn=conn
        self.create_tb=create_tb
    
    def _connection_(self,cur,conn):
        cur=conn.cursor()
        return cur

    def _createtb_(self):
       self.create_tb='''CREATE TABLE self.table
      (self.ID INT PRIMARY KEY     NOT NULL,
      self.name  TEXT    NOT NULL);'''
        
    def _runtb(self,create_tb,cur):
        self.cur=cur.execute(create_tb)
        return cur

    def _exit_(self,conn):
        self.conn.commit()






 

    

