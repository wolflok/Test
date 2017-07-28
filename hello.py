import json
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return json.dumps({'response': 'Hello, World!',
                       'test_key': 'test_data',
                       'test_int_value': 123456})