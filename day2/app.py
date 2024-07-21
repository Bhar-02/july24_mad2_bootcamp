from flask import Flask, request, jsonify
from flask_security import Security, verify_password, auth_token_required, roles_accepted, current_user

from models import db, user_datastore

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'   
app.config['SECRET_KEY'] = "shhh.... its very secret"
app.config['SECURITY_TOKEN_AUTHENTICATION_HEADER'] = 'Authorization'

db.init_app(app)

security = Security(app, user_datastore)

with app.app_context():
    db.create_all()
    user_datastore.find_or_create_role(name='admin', description='Administrator')
    # new_role = Role(name='admin', description='Administrator')
    # db.session.add(new_role)

    user_datastore.find_or_create_role(name='manager', description='manager')
    user_datastore.find_or_create_role(name='customer', description='customer')

    db.session.commit()

    admin_user = user_datastore.find_user(email="admin@a.com")
    from models import User
    admin__user = User.query.filter_by(email="admin@a.com").first()

    if not admin_user:
        User_admin = user_datastore.create_user(email="admin@a.com", password="admin")
        user_datastore.add_role_to_user(User_admin, 'admin')
    db.session.commit()



@app.route('/api/register', methods=['POST'])
def register():
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


@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email1 = data.get('email')
    password1 = data.get('password')
    user = user_datastore.find_user(email=email1)
    if user:
        if verify_password(password1, user.password):
            return jsonify({"message":"Login successful", "authToken": user.get_auth_token()})



@app.route('/api/test', methods=['POST'])
@auth_token_required
@roles_accepted('admin', 'customer')
def test():
    return jsonify({"message":"Test successful", "id": current_user.id})
    

@app.route('/api/activate', methods=['POST'])
@auth_token_required
@roles_accepted('admin')
def activate_manager():
    data = request.get_json()
    id = data.get('id')
    user = user_datastore.find_user(id=id)
    if user and user.has_role('manager'):
        user_datastore.activate_user(user)
        db.session.commit()
        return jsonify({"message":"User activated successfully"})
    return jsonify({"message":"User not found"})


@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify({"message":"Hello World"})


if __name__ == "__main__":
    app.run(debug=True)