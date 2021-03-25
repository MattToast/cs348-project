from flask import Flask, json, jsonify, send_from_directory

import db_queries

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")


@app.route('/api/customers', methods=["GET", "POST"])
def customers():
    return jsonify(db_queries.get_list_customers())


@app.route('/api/employees', methods=["GET", "POST"])
def employees():
    return jsonify(db_queries.get_list_employees())


@app.route('/api/inventory', methods=["GET", "POST"])
def inventory():
    return jsonify(db_queries.get_list_inventory())


@app.route('/api/locations', methods=["GET", "POST"])
def locations():
    return jsonify(db_queries.get_list_locations())


@app.route('/api/sales', methods=["GET", "POST"])
def sales():
    return jsonify(db_queries.get_list_sales())


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')
