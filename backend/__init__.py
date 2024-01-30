from flask import Flask, jsonify, request
from flask_cors import CORS

from marshmallow import ValidationError

from classes import Users

from db import model

from provider import auth

#Flask app

flask_app = Flask(__name__)

CORS(flask_app)

@flask_app.route('/', methods=['POST'])
def add_user():
    try:
        user_data = Users.UserSchema().load(request.json)
        # Criar uma instância da classe User com os dados desserializados
        usuario = Users.User(email=user_data['email'], senha=user_data['senha'])


        resultado = model.adicionar_na_tabela(usuario)
        if resultado ==True:
            return jsonify({'mensagem': 'Usuário adicionado com sucesso', 'email': usuario.email}), 201
        else:
            return jsonify({'erro': resultado}), 400
    except ValidationError as e:
        # Se houver erros de validação, retornar uma mensagem de erro
        return jsonify({'erro': 'Erro de validação', 'mensagens': e.messages}), 400
    except Exception as e:
        # Se ocorrer um erro diferente, retornar uma mensagem de erro
        print(e)
        return jsonify({'erro': 'Erro interno do servidor'}), 500
    
@flask_app.route('/', methods=['GET'])
def get_user():
    try:
        user_data = Users.UserLoginSchema().load(request.json)
        # Criar uma instância da classe User com os dados desserializados
        usuario = Users.UserLogin(email=user_data['email'], senha=user_data['senha'])

        resultado = model.recuperar_na_tabela(usuario)

        if resultado:
            #Cria o token após sucesso na autenticação
            token = auth.criar_token_acesso({'sub': usuario.email})
            return jsonify({'mensagem': f'Usuário encontrado com sucesso: {usuario.email}', 'token': token, 'email': usuario.email}), 201
        else:
            return jsonify({'erro': f'Usuário não encontrado: {usuario.email}', 'email': usuario.email}), 400
    except ValidationError as e:
        # Se houver erros de validação, retornar uma mensagem de erro
        return jsonify({'erro': 'Erro de validação', 'mensagens': e.messages }), 400
    except Exception as e:
        # Se ocorrer um erro diferente, retornar uma mensagem de erro
        print(e)
        return jsonify({'erro': 'Erro interno do servidor'}), 500
    
@flask_app.route('/', methods=['DELETE'])
def delete_user():
    try:
        user_data = Users.UserLoginSchema().load(request.json)
        # Criar uma instância da classe User com os dados desserializados
        usuario = Users.UserLogin(email=user_data['email'], senha=user_data['senha'])

        resultado = model.deletar_na_tabela(usuario)
        if resultado==True:
            #deleta usuário
            return jsonify({'mensagem': f'Usuário encontrado e deletado com sucesso: {usuario.email}'}), 201
        if resultado == False:
            return jsonify({'erro': 'Usuário não existe'}), 400
    except ValidationError as e:
        # Se houver erros de validação, retornar uma mensagem de erro
        return jsonify({'erro': 'Erro de validação', 'mensagens': e.messages }), 400
    except Exception as e:
        # Se ocorrer um erro diferente, retornar uma mensagem de erro
        print(e)
        return jsonify({'erro': 'Erro interno do servidor'}), 500

# Run the Flask flask_application
if __name__ == '__main__':
    flask_app.run(debug=True)