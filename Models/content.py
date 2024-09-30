from typing import Any, overload
from flask import jsonify
from DataBase.db import *
from Models.baseClass import *

class Content(BaseClass):
    id         = 0
    titulo     = ''
    descricao  = ''
    id_user    = ''
    situacao   = 0
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds)  
        self.id         = 0
        self.titulo     = ''
        self.descricao  = ''
        self.id_user    = ''
        self.situacao   = 0
        
def getContents(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(f'SELECT id, titulo, descricao, id_user, situacao FROM Contents WHERE id_user = {id}') 
    records = SQL.cur.fetchall()    
    _list = []
    
    for r in records:   
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _list.append(_content.__dict__)          

    SQL.cur.close() 

    return _list 

def getContent(id: int):
    SQL = dbmsqls()
    SQL.cur.execute(f'SELECT id, titulo, descricao, id_user, situacao FROM Contents WHERE id = {id}') 
    records = SQL.cur.fetchall()     
    _list = []
    
    for r in records:
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _list.append(_content.__dict__)          
    
    SQL.cur.close() 

    return _list

def getContentSituacao(situacao: int):
    SQL = dbmsqls()
    SQL.cur.execute(f'SELECT id, titulo, descricao, id_user, situacao FROM Contents WHERE situacao = {situacao}') 
    records = SQL.cur.fetchall()     
    _list = []
    
    for r in records:
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _list.append(_content.__dict__)          
    
    SQL.cur.close() 

    return _list

def postContent(content: Content):
    titulo      = content.titulo   
    descricao   = content.descricao
    id_user     = content.id_user 
    situacao    = content.situacao 
    
    SQL = dbmsqls()
    SQL.cur.execute('INSERT INTO Contents (titulo, descricao, id_user, situacao) VALUES (?,?,?,?)', [titulo, descricao, id_user, situacao])
    
    SQL.con.commit()
    SQL.con.close()
    
    return content

def updateContent(id: int,content: Content):
    titulo      = content.titulo   
    descricao   = content.descricao
    id_user     = content.id_user
    situacao    = content.situacao  
    
    SQL = dbmsqls()
    SQL.cur.execute('UPDATE Contents SET titulo = ?, descricao = ?, id_user = ?, situacao = ? WHERE id = ?', (titulo,descricao, id_user,situacao, id))
    
    SQL.con.commit()
    SQL.con.close()
    
    return content

def deleteContent(id: int):
    SQL = dbmsqls()
    SQL.cur.execute('DELETE FROM Contents WHERE id = ?', [id])
    
    SQL.con.commit()
    SQL.con.close()
    
    return {"msg": "Deletado"}
