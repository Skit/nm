import os

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return 'It works'


@app.route('/broadcast', methods=['GET'])
def broadcast():
    print(os.system('./broadcast.py'), flush=False)
    return 'OK'
