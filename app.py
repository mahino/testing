from flask import Flask
from flask import url_for
from flask import request
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "do_the_login"
    else:
        return "show_the_login_form"