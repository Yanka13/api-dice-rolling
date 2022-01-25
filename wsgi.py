# wsgi.py
import random
from flask import Flask, jsonify


app = Flask(__name__)


# blabla
@app.route('/')
def home():
    return jsonify({ 'roll': random.randint(1,6) })
