from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

auth_tokens = []

@app.route('/addtoken')
def add_token():
