import os
from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from Models.content import *
from Models.email import checkcode, send_code
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
    
@app.route('/api/userspsw',     methods = ['POST'])
def userspsw():
    users  = User()
    if request.method == 'POST':
        if request.is_json:
            users.__dict__.update(request.get_json())   
        return updateUserPsw(users)
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
    
@app.route('/api/contentcreate/', methods=['POST'])
def create_content():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            print(data)
            content = Content()
            content.__dict__.update(request.get_json())
            anos        = data.get('anos')  
            meses       = data.get('meses') 
            dias_semana = data.get('dias_semana')  

            created_content = postContentAll(content, anos=anos, meses=meses, dias_semana=dias_semana)
            
            return jsonify({"message": "Content created successfully", "content": created_content.__dict__}), 201
        else:
            return jsonify({"error": "Request must be JSON"}), 400
    
@app.route('/api/contents/<id_user>',     methods = ['GET'])
@app.route('/api/content/',     methods = ['POST'])
def content(id_user = 0):
    contents  = Content()
    if request.method == 'GET':
            return getAllContents(id_user)
    elif request.method == 'POST': 
        if request.is_json:
            contents.__dict__.update(request.get_json())          
            return postContent(contents).__dict__ 
        
@app.route('/api/cts/<id_user>/<data>', methods = ['GET'])
def cts(id_user = 0, data = ''):
    if request.method == 'GET':
      return getContents(id_user, data)  
#endregion

@app.route('/api/sendcode', methods=['GET'])
def _sendCode():
    _email = request.headers.get('Email')
    
    if _email:
        try:
            # Chama a função de envio de código
            result = send_code( _email)
            if isinstance(result, dict) and 'status' in result and result['status']:
                return jsonify({"status": True, "message": result['message']})
            else:
                return jsonify({"status": False, "message": "Email não encontrado ou erro ao enviar o código."}), 400
        except Exception as e:
            return jsonify({"status": False, "message": "Erro ao enviar o código", "error": str(e)}), 500
    else:
        return jsonify({"status": False, "message": "Email não fornecido."}), 400

@app.route('/api/verificationcode', methods=['GET'])
def _verificationCode():
    _email = request.headers.get('Email')
    _code = request.headers.get('Code')
    
    if _email and _code:
        try:
            # Chama a função de verificação do código
            result = checkcode(_email, _code)
            if isinstance(result, dict) and 'status' in result and result['status']:
                return jsonify({"status": True, "message": "Código verificado com sucesso!"})
            else:
                return jsonify({"status": False, "message": "Código incorreto!"}), 400
        except Exception as e:
            return jsonify({"status": False, "message": "Erro ao tentar verificar o código", "error": str(e)}), 500
    else:
        return jsonify({"status": False, "message": "Email ou código não fornecido."}), 400


if __name__ == '__main__':
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", port=5000, debug=True)
