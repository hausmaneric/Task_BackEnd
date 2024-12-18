from typing import Any, overload
from flask import jsonify
from DataBase.db import *
from Models.baseClass import *

class User(BaseClass):
    id      = 0
    nome    = ''
    login   = ''
    senha   = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds)  
        self.id       = 0
        self.nome     = ''
        self.login    = 0
        self.senha    = 0
        
def getUsers():
    SQL = dbsqlite()
    SQL.cur.execute(f'SELECT id, nome, login, senha FROM Users') 
    records = SQL.cur.fetchall()    
    _list = []
    
    for r in records:   
        _user          = User()
        _user.id       = r[0]
        _user.nome     = r[1]
        _user.login    = r[2]
        _user.senha    = r[3]
        _list.append(_user.__dict__)          

    SQL.cur.close() 

    return _list 

def getUser(id: int):
    SQL = dbsqlite()
    SQL.cur.execute(f'SELECT id, nome, login, senha  FROM Users WHERE id = {id}') 
    records = SQL.cur.fetchall()     
    _list = []
    
    for r in records:
        _user          = User()
        _user.id       = r[0]
        _user.nome     = r[1]
        _user.login    = r[2]
        _user.senha    = r[3]
        _list.append(_user.__dict__)          
    
    SQL.cur.close() 

    return _list

def postUser(user: User):
    nome        = user.nome
    login       = user.login
    senha       = user.senha
    
    SQL = dbsqlite()
    SQL.cur.execute('INSERT INTO Users (nome, login, senha) VALUES (?,?,?)', [nome, login, senha])
    
    SQL.con.commit()
    SQL.con.close()
    
    return user

def updateUser(id: int,user: User):
    nome        = user.nome
    login       = user.login
    senha       = user.senha
    
    SQL = dbsqlite()
    SQL.cur.execute('UPDATE Users SET nome = ?, login = ?, senha = ? WHERE id = ?', (nome,login, senha, id))
    
    SQL.con.commit()
    SQL.con.close()
    
    return user

def updateUserPsw(user: User):
    login       = user.login
    senha       = user.senha
    SQL = dbsqlite()
    SQL.cur.execute('UPDATE Users SET senha = ? WHERE login = ?', (senha, login))
    
    SQL.con.commit()
    SQL.con.close()
    
    return jsonify({"status": True, "message": "Senha alterada com sucesso!"}), 200

def deleteUser(id: int):
    SQL = dbsqlite()
    SQL.cur.execute('DELETE FROM Users WHERE id = ?', [id])
    
    SQL.con.commit()
    SQL.con.close()
    
    return {"msg": "Deletado"}
