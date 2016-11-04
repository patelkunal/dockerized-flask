from app import app
from app import get_names

@app.route('/')
def index():
    return jsonify({'message': 'Flask is running!'})


@app.route('/data')
def names():
    data = {"names": get_names()}
    return jsonify(data)
