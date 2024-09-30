from typing import Any, overload
import pyodbc
import sqlite3 as lite
import mysql.connector

class dbmsqls:
    con = None
    cur = None   
    def __init__(self):        
        super().__init__()   
        self.con = pyodbc.connect(
        # Driver que será utilizado na conexão
        "DRIVER={SQL Server Native Client 11.0};"
        # IP ou nome do servidor\
        "SERVER=EC2AMAZ-OTVQTO8;"
        # Porta
        "PORT=1433;"
        # Banco que será utilizado (Criar banco).
        "DATABASE=CMS;"
        # Nome de usuário (Usuário default da imagem).
        "UID=eric;"
        # Senha.
        f"PWD=30062001Ee@") 
        self.cur = self.con.cursor()   

class dbsqlite:
    con = None
    cur = None   
    def __init__(self):        
        super().__init__()   
        self.banco = 'cvdb.db'
        self.con = lite.connect(self.banco) 
        self.cur = self.con.cursor() 
    
class dbmysql:
    con = None
    cur = None   
    def __init__(self):        
        super().__init__()  
        self.con = mysql.connector.connect(host="localhost:3306",user="root",password="",database="flask_tutorial") 
        self.cur = self.con.cursor()  
        