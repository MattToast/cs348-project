from flask import Flask, json, jsonify, send_from_directory

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")


@app.route('/api/cutomers')
def customers():
    return jsonify({"message": "hello world"})


@app.route('/api/employees')
def employees():
    return jsonify([
        {
            "EmployeeID": 1,
            "position": "manager",
            "salary": 80_000,
            "location": "Chicago"
        }
    ])


@app.route('/api/inventory')
def inventory():
    return jsonify({"message": "hello world"})


@app.route('/api/locations')
def locations():
    return jsonify({"message": "hello world"})


@app.route('/api/sales')
def sales():
    return jsonify({"message": "hello world"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')
