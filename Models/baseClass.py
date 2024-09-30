from datetime import datetime
from typing import Any, overload
import jsonpickle
from DataBase.db import *

#region Rotinas objetos para JSON e JSON para objetos

class DatetimeHandler(jsonpickle.handlers.BaseHandler):
    def flatten(self, obj, data):
        #return obj.strftime('%Y-%m-%d %H:%M:%S')
        return obj.isoformat() # ISO 8601

def objToJSON(o, native = True):
    """Gera o json de uma instância
       Se native = True gera json com referência a classe python py/object...
    """
    jsonpickle.handlers.registry.register(datetime, DatetimeHandler)
    return jsonpickle.encode(o, unpicklable=native)

def jsonToObj(s) -> Any:    
    """Transforma json em objeto"""    
    return jsonpickle.decode(s)

#endregion

# Classe primária com rotinas de conversão JSON
class BaseClass:    
    __json      = None
    __jsonError = None  
    result      = None  
    def __init__(self, *args: Any, **kwds: Any) -> Any:
        """ **Kwds 'json' se informado uma string json monta o objeto com o json fornecido"""        
        self.__json = kwds.get('json') 
        self.jsonImport()

    def __enter__(self):
        return self        

    def __exit__(self, type, value, traceback):
        pass        

    def __str__(self) -> str:
        return self.__class__          
                
    def jsonImport(self, js = None):   
        if js != None: # criado parametro js pois ao setar dados no atributo privado __json não reflete na classe pai 
           self.__json = js 

        if self.__json != '' and self.__json != None:         
            o = jsonToObj(self.__json)
            if type(o) is self.__class__:
                self.__dict__.update(self.__dict__)
                jsonError = False
            elif type(o) is dict:
                self.__dict__.update(o)
                jsonError = False    
            else:
                jsonError = True    
    
    def jsonError(self):
        return self.__jsonError      
    
    # @staticmethod -> não acessa attributos da classe e nem da instância
    # @classmethod  -> acessa atributos da classe mas não da instância 

    # # Exemplo de uso *args e **Kwargs
    # def doArgsKw(self, *args, **Kwargs):
    #     for x in args:
    #         print(x)
    #     a = Kwargs.get('str1')
    #     b = Kwargs.get('str2')
    #     print(a)
    #     print(b)


