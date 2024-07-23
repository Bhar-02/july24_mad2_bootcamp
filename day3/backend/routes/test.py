from flask_restful import Resource
from flask import jsonify


class testRest(Resource):
    def post(self):
        return jsonify({"message":"POST test successful"})
    
    def get(self):
        return jsonify({"message":"GET rupanshi test successful"})
    
    def put(self):
        return jsonify({"message":"PUT test successful"})
    
    def delete(self):
        return jsonify({"message":"DELETE test successful"})
    
    def anchit(self):
        return jsonify({"message":"Anchit test successful"})
    

class testPathParameter(Resource):
    def post(self, var1):
        return jsonify({"message":"POST test successful", "parameter_passed": var1})