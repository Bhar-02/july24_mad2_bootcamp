from flask import Flask, request, jsonify
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'   


db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/hello_world', methods=['GET'])
def hello_world():
    return jsonify({"message":"Hello World"})


if __name__ == "__main__":
    app.run(debug=True)