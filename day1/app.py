from flask import Flask, render_template

app = Flask(__name__)


@app.route('/hello_world')
def hello_world():
    var1 = "hello mad2 bootcamp people"
    return render_template('anything.html', var2=var1)

if __name__ == '__main__':
    app.run(debug=True)