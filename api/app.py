from flask import Flask, json, jsonify, send_from_directory

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")


@app.route('/api/message')
def hello_world():
    return jsonify({"message": "hello world"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')
