import os
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/<id>', methods=['GET'])
def request_uri(id):
    return id
