from flask import Flask, json, jsonify

app = Flask(__name__, static_folder="../build", static_url_path="/")



@app.route('/api/message')
def hello_world():
    return jsonify({"message": "hello world"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")