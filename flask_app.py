import os
from flask import Flask, jsonify, request, json, url_for, render_template
import json

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello_world():
    return render_template('error.html', error = '404')
    
@app.route('/<id>', methods=['GET'])
def get_uri(id):
    if id.endswith('.json'):
        response = app.response_class(
            response=json.dumps({'id': id.replace('.json', '')}),
            status=200,
            mimetype='application/json'
        )
        return response
    return render_template('error.html', error = '404')