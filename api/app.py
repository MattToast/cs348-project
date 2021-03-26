from flask import Flask, json, jsonify, send_from_directory, request
import json

import db_actions.locations as loc
import db_actions.employee as emp
import db_actions.inventory as inv
import db_actions.sales as sales
import db_actions.customers as cust

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")


@app.route('/api/locations', methods=["GET", "POST"])
def locations_route():
    return jsonify(loc.get_list_locations())


@app.route('/api/employees', methods=["GET", "POST"])
def employees_route():
    if request.method == "GET":
        return jsonify(emp.get_list_employees())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data['id'], data['position'], data['salary'], data['location_id'])
        print(vals)
        emp.into_employees(vals)
        return jsonify(success=True)


@app.route('/api/inventory', methods=["GET", "POST"])
def inventory_route():
    return jsonify(inv.get_list_inventory())


@app.route('/api/sales', methods=["GET", "POST"])
def sales_route():
    return jsonify(sales.get_list_sales())


@app.route('/api/customers', methods=["GET", "POST"])
def customers_route():
    return jsonify(cust.get_list_customers())


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')
