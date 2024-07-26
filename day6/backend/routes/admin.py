from flask_restful import Resource
from flask import request, jsonify, make_response
from flask_security import roles_accepted, auth_token_required

from models import db, user_datastore

class activateManager(Resource):
    @auth_token_required
    @roles_accepted('admin')
    def post(self):
        data = request.get_json()
        id = data.get('id')
        user = user_datastore.find_user(id=id)
        if user and user.has_role('manager'):
            user_datastore.activate_user(user)
            db.session.commit()
            return jsonify({"message":"User activated successfully"})
        return make_response(jsonify({"message":"User not found"}), 404)