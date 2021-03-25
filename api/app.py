from flask import Flask, json, jsonify

app = Flask(__name__, static_folder="../build", static_url_path="/")


@app.route('/')
def index():
    return app.send_static_file("index.html")

@app.route('/api/message')
def hello_world():
    return jsonify({"message": "hello world"})