from flask_restful import Resource
from flask import request, jsonify

from models import db, user_datastore

class signup(Resource):
    def post(self):
        data = request.get_json()
        email1 = data.get('email')
        password1 = data.get('password')
        role1 = data.get('role')
        user = user_datastore.find_user(email=email1)
        if not user:
            user = user_datastore.create_user(email=email1, password=password1)
            if role1 == "manager":
                # user.active = False
                user_datastore.add_role_to_user(user, "manager")
                user_datastore.deactivate_user(user)
            elif role1 == "customer":
                user_datastore.add_role_to_user(user, 'customer')
            db.session.commit()
            return jsonify({"message":"User registered successfully"})
        return jsonify({"message":"User already exists"})

class login(Resource):
    def post(self):
        data = request.get_json()
        email1 = data.get('email')
        password1 = data.get('password')
        user = user_datastore.find_user(email=email1)
        if user:
            from flask_security.utils import verify_password
            if verify_password(password1, user.password):
                return jsonify({"message":"Login successful", "authToken": user.get_auth_token(), "role":user.roles[0].name})