from flask import Flask, jsonify

app = Flask('testapp')

z = 141

@app.route("/")
def hello():
    return jsonify({"z": z})

if __name__ == '__main__':
    app.run(debug=True)
