from flask import Flask, request, jsonify
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user

from models import db, user_datastore

def make_celery(app):
    from celery import Celery
    celery=Celery(app.import_name)
    import celeryconfig
    celery.config_from_object(celeryconfig)
    return celery

def create_app():
    app1 = Flask(__name__)
    from config import DevelopmentConfig
    app1.config.from_object(DevelopmentConfig)
    db.init_app(app1)
    security = Security(app1, user_datastore)

    from flask_restful import Api
    api = Api(app1, prefix='/api')

    from flask_cors import CORS
    CORS(app1)

    from caching import cache
    cache.init_app(app1)

    celery_init = make_celery(app1)

    from mailer import mail
    mail.init_app(app1)

    return app1, api, celery_init

app, api_handler, celery_app = create_app()
import tasks

from celery.schedules import crontab
celery_app.conf.beat_schedule = {
    'sum-test':{
        'task': 'tasks.sum',
        'schedule': crontab(minute=54, hour=21)
    },
    'email-test':{
        'task': 'tasks.test_mail',
        'schedule': crontab(minute=6, hour=22)
    }
}

@app.route('/celery', methods=['GET'])
def test_celery():
    # job = tasks.sum.delay()
    job = tasks.test_db.delay()
    while not job.ready():
        pass
    return jsonify({"message":"Celery task called", "id": job.id, "status": job.status, "result": job.get()})


from routes.test import testRest, testPathParameter
api_handler.add_resource(testRest, '/testRest')
api_handler.add_resource(testPathParameter, '/testRest/<int:var1>')

from routes.auth import signup, login
api_handler.add_resource(signup, '/register')
api_handler.add_resource(login, '/login')

from routes.admin import activateManager
api_handler.add_resource(activateManager, '/activate')

from routes.category import CategoryResource, CategorySpecific
api_handler.add_resource(CategoryResource, '/category')
api_handler.add_resource(CategorySpecific, '/category/<int:id>')


from routes.product import ProductResource, ProductSpecific
api_handler.add_resource(ProductResource, '/product')
api_handler.add_resource(ProductSpecific, '/product/<int:id>')

@app.route('/test', methods=['GET', 'POST', 'PUT', 'DELETE'])
def testMethod():
    if request.method == 'GET':
        var12 = "hello world"
        print("my name", var12)
        return jsonify({"message":"GET Test successful"})
    elif request.method == 'POST':
        data = request.get_json()
        return jsonify({"message":"POST Test successful", "data_got": data})
    elif request.method == 'PUT':
        return jsonify({"message":"PUT Test successful"})
    elif request.method == 'DELETE':
        return jsonify({"message":"DELETE Test successful"})
    
@app.route('/test/<int:var1>', methods=['POST'])
def testMethod1(var1):
    if request.method == 'POST':
        return jsonify({"message":"POST Test successful", "parameter_passed": var1})


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
    return jsonify({"message":"Hello World"}), 900


if __name__ == "__main__":
    app.run(debug=True)