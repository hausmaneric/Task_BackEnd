from typing import Any, overload
import sqlite3 as lite

class dbsqlite:
    con = None
    cur = None   
    def __init__(self):        
        super().__init__()   
        self.banco = 'cms.db'
        self.con = lite.connect(self.banco) 
        self.cur = self.con.cursor() 
