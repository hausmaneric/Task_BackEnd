import random
from typing import Any, overload
import smtplib
from email.message import EmailMessage

from DataBase.db import dbsqlite
from Models.baseClass import BaseClass
verification_code = {}

class Email(BaseClass):
    assunto  : str
    body     : str
    to       : str 
    def __init__(self) -> None:        
        self.assunto   = None
        self.body      = None

def sendEmail(email: Email):
    assunto         = email.assunto
    body            = email.body
    to              = email.to
    email_address   = 'eric.hausman.m@gmail.com'
    email_password  = 'xdwbsvcwrqrpnufo'

    msg = EmailMessage()
    msg['Subject']  = assunto
    msg['From']     = email_address
    msg['To']       = to
    password        = email_password
    msg.add_header('Content-type', 'text/html')
    msg.set_content(body)
    
    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    
    return {"msg":"Email enviado"}

def generate_code():
    return str(random.randint(1000, 9999))

def send_verification_code_by_email(email, codigo):
    verification_code[email] = codigo
    email_obj = Email()
    email_obj.assunto = 'Código de verificação'
    email_obj.body = f'Seu código de verificação é: {codigo}'
    email_obj.to = email

    if sendEmail(email_obj):
        return True
    else:
        return False

def user_email(email: str):
    try:
        SQL = dbsqlite()
        SQL.cur.execute(f"SELECT COUNT(*) AS Total FROM Users WHERE Login = '{email}'")
        total = SQL.cur.fetchone()[0]

        return 0 if total == 0 else 1
    except Exception as e:
        return {'status': False, 'error': 'Error when querying data', 'details': str(e)}
    finally:
        SQL.cur.close()
     

def send_code(email: str):
    __email = user_email(email)
    response = {}

    try:
        if __email == 1:
            code = generate_code()
            send_verification_code_by_email(email, code)

            response['status'] = True
            response['message'] = 'Email enviado'
        elif __email == 0:
            response['status'] = False
            response['warning'] = True
            response['message'] = 'Email não enviado'
    except Exception as e:
        response['status'] = False
        response['error'] = 'Error sending the e-mail'
        response['details'] = str(e)

    return response

def checkcode(email, codigo):
    response = {}
    stored_code = verification_code.get(email)

    try:
        if stored_code and codigo == stored_code:
            del verification_code[email]
            response['status'] = True
            response['message'] = 'Codigo verificado com sucesso!'
        else:
            response['status'] = False
            response['warning'] = True
            response['message'] = 'Codigo incorreto!'
    except Exception as e:
        response['status'] = False
        response['error'] = 'Erro ao tentar verificar o código'
        response['details'] = str(e)

    return response