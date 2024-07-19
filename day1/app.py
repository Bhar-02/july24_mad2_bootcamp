from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/hello_world', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        desc = data['desc']
        print(name, desc)
        return 'You are using POST method'
    var1 = "hello mad2 bootcamp people"
    return render_template('anything.html', var2=var1)

if __name__ == '__main__':
    app.run(debug=True)