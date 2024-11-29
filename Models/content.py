from typing import Any, List, Optional, overload
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

import calendar

def postContentAll(content: Content, anos: Optional[List[int]] = None, meses: Optional[List[int]] = None, dias_semana: Optional[List[int]] = None):
    """
    Cria registros na tabela 'Contents' para datas específicas com base nos parâmetros fornecidos.
    
    Parâmetros:
    - content: Objeto Content contendo os dados básicos do conteúdo.
    - anos: Lista de anos para criar registros (ex.: [2024]).
    - meses: Lista de meses para criar registros (ex.: [1, 2, 12] para janeiro, fevereiro e dezembro).
    - dias_semana: Lista de dias da semana para criar registros (0 = segunda-feira, 6 = domingo).
    """
    
    data_atual = datetime.now()
    
    anos = anos or [data_atual.year]
    meses = meses or list(range(1, 13))
    dias_semana = dias_semana or list(range(7))  
    dias_semana = [int(dia) for dia in dias_semana]  
    
    datas_para_inserir = []
    for ano in anos:
        for mes in meses:
            num_dias = calendar.monthrange(ano, mes)[1]  
            for dia in range(1, num_dias + 1):
                data = datetime(ano, mes, dia)
                if data >= data_atual and data.weekday() in dias_semana:
                    datas_para_inserir.append(data)
    
    
    SQL = dbsqlite()  
    for data in datas_para_inserir:
        print(content.titulo)
        SQL.cur.execute(
            'INSERT INTO Contents (titulo, descricao, id_user, situacao, data, inicio, fim) VALUES (?,?,?,?,?,?,?)',
            [
                content.titulo,
                content.descricao,
                content.id_user,
                content.situacao,
                data.strftime('%Y-%m-%d'),
                content.inicio,
                content.fim
            ]
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
