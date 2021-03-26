from flask import Flask, json, jsonify, send_from_directory, request
import json

import db_actions.locations as loc
import db_actions.employee as emp
import db_actions.inventory as inv
import db_actions.sales as sales
import db_actions.customers as cust
import db_actions.transfers as trans
import db_actions.includes as inc
import db_actions.has as has
import db_actions.buy as buy

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")


@app.route('/api/locations', methods=["GET", "POST"])
def locations_route():
    if request.method == "GET":
        return jsonify(loc.get_list_locations())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data['id'], data['money'], data['owner'])
        loc.into_locations(vals)
        return jsonify(success=True)


@app.route('/api/employees', methods=["GET", "POST"])
def employees_route():
    if request.method == "GET":
        return jsonify(emp.get_list_employees())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data['id'], data['position'], data['salary'], data['location_id'])
        emp.into_employees(vals)
        return jsonify(success=True)


@app.route('/api/inventory', methods=["GET", "POST"])
def inventory_route():
    if request.method == "GET":
        return jsonify(inv.get_list_inventory())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data['id'], data['name'])
        inv.into_inventory(vals)
        return jsonify(success=True)


@app.route('/api/sales', methods=["GET"])
def sales_route():
    return jsonify(sales.get_list_sales())


@app.route('/api/customers', methods=["GET"])
def customers_route():
    return jsonify(cust.get_list_customers())


@app.route('/api/transfers', methods=["GET"])
def transfers_route():
    return jsonify(trans.get_list_transfers())


@app.route('/api/includes', methods=["GET"])
def includes_route():
    return jsonify(inc.get_list_includes())


@app.route('/api/has', methods=["GET"])
def has_route():
    return jsonify(has.get_list_has())


@app.route('/api/buys', methods=["GET"])
def buys_route():
    return jsonify(buy.get_list_buys())


# @app.route('/api/owns', methods=["GET"])
# def owns_route():
#     return jsonify(trans.get_list_transfers())


# Theoretically only used in production
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')
