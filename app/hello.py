from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Flask is running!'})


@app.route('/data')
def names():
    data = {"names": ["kunal", "nirali"]}
    return jsonify(data)


if __name__ == "__main__":
    print("starting flask application !!")
    app.run(debug=True)
