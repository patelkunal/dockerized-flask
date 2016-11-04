from flask import jsonify
from app import app, core


@app.route('/')
def index():
    return jsonify({'message': 'Flask is running!'})


@app.route('/data')
def names():
    data = {"names": core.get_names()}
    return jsonify(data)
