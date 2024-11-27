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
    data       = ''
    inicio     = ''
    fim        = ''
    
    def __init__(self, *args: Any, **kwds: Any) -> Any:        
        super().__init__(*args, **kwds)  
        self.id         = 0
        self.titulo     = ''
        self.descricao  = ''
        self.id_user    = ''
        self.situacao   = 0
        self.data       = ''
        self.inicio     = ''
        self.fim        = ''
        
def getAllContents(id: int):
    SQL = dbsqlite()
    SQL.cur.execute(f'SELECT id, titulo, descricao, id_user, situacao, data, inicio, fim FROM Contents WHERE id_user = {id}') 
    records = SQL.cur.fetchall()    
    _list = []
    
    for r in records:   
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _content.data       = r[5]
        _content.inicio     = r[6]
        _content.fim        = r[7]
        _list.append(_content.__dict__)          

    SQL.cur.close() 

    return _list 
        
def getContents(id: int, data: str):
    SQL = dbsqlite()
    SQL.cur.execute(f"""SELECT id, titulo, descricao, id_user, situacao, data, inicio, fim  FROM Contents WHERE id_user = {id} AND data = '{data}'""") 
    records = SQL.cur.fetchall()    
    _list = []
    
    for r in records:   
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _content.data       = r[5]
        _content.inicio     = r[6]
        _content.fim        = r[7]
        _list.append(_content.__dict__)          

    SQL.cur.close() 

    return _list 

def getContent(id: int):
    SQL = dbsqlite()
    SQL.cur.execute(f'SELECT id, titulo, descricao, id_user, situacao, data, inicio, fim  FROM Contents WHERE id = {id}') 
    records = SQL.cur.fetchall()     
    _list = []
    
    for r in records:
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _content.data       = r[5]
        _content.inicio     = r[6]
        _content.fim        = r[7]
        _list.append(_content.__dict__)          
    
    SQL.cur.close() 

    return _list

def getContentSituacao(situacao: int):
    SQL = dbsqlite()
    SQL.cur.execute(f'SELECT id, titulo, descricao, id_user, situacao, data, inicio, fim  FROM Contents WHERE situacao = {situacao}') 
    records = SQL.cur.fetchall()     
    _list = []
    
    for r in records:
        _content            = Content()
        _content.id         = r[0]
        _content.titulo     = r[1]
        _content.descricao  = r[2]
        _content.id_user    = r[3]
        _content.situacao   = r[4]
        _content.data       = r[5]
        _content.inicio     = r[6]
        _content.fim        = r[7]
        _list.append(_content.__dict__)          
    
    SQL.cur.close() 

    return _list

def postContent(content: Content):
    titulo      = content.titulo   
    descricao   = content.descricao
    id_user     = content.id_user 
    situacao    = content.situacao 
    data        = content.data 
    inicio      = content.inicio  
    fim         = content.fim
    
    SQL = dbsqlite()
    SQL.cur.execute(
        'INSERT INTO Contents (titulo, descricao, id_user, situacao, data, inicio, fim ) VALUES (?,?,?,?,?,?,?)',
        [titulo, descricao, id_user, situacao, data, inicio, fim]
    )
    
    SQL.con.commit()
    SQL.con.close()
    
    return content

def updateContent(id: int,content: Content):
    titulo      = content.titulo   
    descricao   = content.descricao
    id_user     = content.id_user
    situacao    = content.situacao  
    inicio      = content.inicio  
    fim         = content.fim  
    
    SQL = dbsqlite()
    SQL.cur.execute('UPDATE Contents SET titulo = ?, descricao = ?, id_user = ?, situacao = ?, inicio = ?, fim = ? WHERE id = ?', (titulo,descricao, id_user,situacao, inicio, fim, id))
    
    SQL.con.commit()
    SQL.con.close()
    
    return content


def deleteContent(id: int):
    SQL = dbsqlite()
    SQL.cur.execute('DELETE FROM Contents WHERE id = ?', [id])
    
    SQL.con.commit()
    SQL.con.close()
    
    return {"msg": "Deletado"}
