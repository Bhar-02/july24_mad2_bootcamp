from flask import Flask, request, jsonify
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user

from models import db, user_datastore

def create_app():
    app1 = Flask(__name__)
    from config import DevelopmentConfig
    app1.config.from_object(DevelopmentConfig)
    db.init_app(app1)
    security = Security(app1, user_datastore)

    from flask_restful import Api
    api = Api(app1, prefix='/api')
    return app1, api

app, api_handler = create_app()

from routes.test import testRest, testPathParameter
api_handler.add_resource(testRest, '/testRest')
api_handler.add_resource(testPathParameter, '/testRest/<int:var1>')

from routes.auth import signup, login
api_handler.add_resource(signup, '/register')
api_handler.add_resource(login, '/login')

from routes.admin import activateManager
api_handler.add_resource(activateManager, '/activate')


@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def testMethod():
    if request.method == 'GET':
        return jsonify({"message":"GET Test successful"})
    elif request.method == 'POST':
        return jsonify({"message":"POST Test successful"})
    elif request.method == 'PUT':
        return jsonify({"message":"PUT Test successful"})
    elif request.method == 'DELETE':
        return jsonify({"message":"DELETE Test successful"})
    
@app.route('/test/<int:var1>', methods=['POST'])
def testMethod1(var1):
    if request.method == 'POST':
        return jsonify({"message":"POST Test successful", "parameter_passed": var1})




# @app.route('/api/register', methods=['POST'])
# def register():
#     data = request.get_json()
#     email1 = data.get('email')
#     password1 = data.get('password')
#     role1 = data.get('role')
#     user = user_datastore.find_user(email=email1)
#     if not user:
#         user = user_datastore.create_user(email=email1, password=password1)
#         if role1 == "manager":
#             # user.active = False
#             user_datastore.add_role_to_user(user, "manager")
#             user_datastore.deactivate_user(user)
#         elif role1 == "customer":
#             user_datastore.add_role_to_user(user, 'customer')
#         db.session.commit()
#         return jsonify({"message":"User registered successfully"})
#     return jsonify({"message":"User already exists"})


# @app.route('/api/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email1 = data.get('email')
#     password1 = data.get('password')
#     user = user_datastore.find_user(email=email1)
#     if user:
#         if verify_password(password1, user.password):
#             return jsonify({"message":"Login successful", "authToken": user.get_auth_token()})



@app.route('/api/test', methods=['POST'])
@auth_token_required
@roles_accepted('admin', 'customer')
def test():
    return jsonify({"message":"Test successful", "id": current_user.id})
    

# @app.route('/api/activate', methods=['POST'])
# @auth_token_required
# @roles_accepted('admin')
# def activate_manager():
#     data = request.get_json()
#     id = data.get('id')
#     user = user_datastore.find_user(id=id)
#     if user and user.has_role('manager'):
#         user_datastore.activate_user(user)
#         db.session.commit()
#         return jsonify({"message":"User activated successfully"})
#     return jsonify({"message":"User not found"})


@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify({"message":"Hello World"})


if __name__ == "__main__":
    app.run(debug=True)