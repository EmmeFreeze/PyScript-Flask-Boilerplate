from flask import Flask, render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/todo')
def index():
    return render_template('todo.html')

app.run(host='0.0.0.0', port=81)