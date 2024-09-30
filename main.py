from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Models.content import *
from Models.users import *

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*", "methods": "GET, POST, PUT, DELETE", "headers":"Origin, Content-Type, X-Auth-Token"}})
app.config['JSON_AS_ASCII'] = False

@app.route('/') 
def main():
    return 'API OK 0.0.1' 

@app.route("/favicon.ico")
def favicon():
    return "", 200

#region Users 
@app.route('/api/users/',     methods = ['GET', 'POST'])
@app.route('/api/users/<id>', methods = ['GET', 'PUT', 'DELETE'])
def users(id=0):
    users  = User()
    if request.method == 'GET':
        if id != 0:
            return getUser(id)
        else:
            return getUsers()
    elif request.method == 'POST': 
        if request.is_json:
            users.__dict__.update(request.get_json())          
            return postUser(users).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            users.__dict__.update(request.get_json()) 
            return updateUser(id, users).__dict__   
    elif request.method == 'DELETE': 
        return deleteUser(id)
#endregion

#region Content 
@app.route('/api/content/<id>', methods = ['GET', 'PUT', 'DELETE'])
def contents(id=0):
    contents  = Content()
    if request.method == 'GET':
            return getContent(id)
    elif request.method == 'POST': 
        if request.is_json:
            contents.__dict__.update(request.get_json())          
            return postContent(contents).__dict__ 
    elif request.method == 'PUT': 
        if request.is_json:
            contents.__dict__.update(request.get_json()) 
            return updateContent(id, contents).__dict__   
    elif request.method == 'DELETE': 
        return deleteContent(id)
    
@app.route('/api/contents/<id_user>',     methods = ['GET'])
@app.route('/api/content/',     methods = ['POST'])
def content(id_user = 0):
    contents  = Content()
    if request.method == 'GET':
            return getContents(id_user)
    elif request.method == 'POST': 
        if request.is_json:
            contents.__dict__.update(request.get_json())          
            return postContent(contents).__dict__ 
        
@app.route('/api/situacao/',     methods = ['GET', 'POST'])
def contentSituacao(situacao = 0):
    if request.method == 'GET':
      return getContentSituacao(situacao)  
#endregion

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
