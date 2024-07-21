from flask import Flask, render_template, request, jsonify
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

# db = SQLAlchemy(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/hello_world', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.form
        name1 = data['name']
        desc1 = data['desc']
        print(name1, desc1)
        new_user = User(name=name1, desc=desc1)
        db.session.add(new_user)
        db.session.commit()
        return 'You are using POST method'
    var1 = "hello mad2 bootcamp people"
    user_data = User.query.all()
    return render_template('anything.html', var2=var1, user=user_data)

@app.route('/hello_world_mad2', methods=['GET', 'POST', 'PUT', 'DELETE'])
def hello_world_mad2():
    #  post part _______________________________________________________
    if request.method == 'POST':
        data = request.get_json()
        name1 = data['name']
        desc1 = data['desc']
        print(name1, desc1)
        new_user = User(name=name1, desc=desc1)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message":"You are using POST method", "id": new_user.id})
    
    #  put part _______________________________________________________
    if request.method == "PUT":
        data = request.get_json()
        name1 = data['name']
        desc1 = data['desc']
        id = data['id']

        user = User.query.filter_by(id=id).first()

        user.name = name1
        user.desc = desc1

        db.session.commit()

        return jsonify({"message":"You are using PUT method", "id": id, "name": user.name, "desc": user.desc})
        

    #  delete part _______________________________________________________

    if request.method == "DELETE":
        data = request.get_json()
        id = data['id']

        user = User.query.filter_by(id=id).first()

        db.session.delete(user)
        db.session.commit()

        return jsonify({"message":"You are using DELETE method", "id": id})

    

    #  get part _______________________________________________________
    var1 = "hello mad2 bootcamp people"
    user_data = []
    users = User.query.all()
    for user in users:
        user_data.append(
                {
                "name":user.name, 
                "desc":user.desc
                }
            )
    return jsonify({"var2":var1, "user":user_data})


if __name__ == '__main__':
    app.run(debug=True)