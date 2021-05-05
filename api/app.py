from flask import Flask, json, jsonify, send_from_directory, request
import json

from flask.wrappers import Request, Response

# import blueprints
from routes.reports import reportRoutes

#import functionality
import db_actions.locations as loc
import db_actions.employee as emp
import db_actions.inventory as inv
import db_actions.sales as sales
import db_actions.customers as cust
import db_actions.transfers as trans
import db_actions.includes as inc
import db_actions.has as has
import db_actions.buy as buy
import db_actions.owns as owns

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")

app.register_blueprint(reportRoutes, url_prefix='/api/reports')


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


@app.route('/api/sales', methods=["GET", "POST"])
def sales_route():
    if request.method == "GET":
        return jsonify(sales.get_list_sales())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data["saleID"], data["custID"], data["emplID"], data["prodID"], data["num"], data["date"], 0)
        success = sales.into_sales(vals)
        if success:
            return Response(status=204)
        else:
            return Response(status=500)


@app.route('/api/customers', methods=["GET"])
def customers_route():
    return jsonify(cust.get_list_customers())


@app.route('/api/transfers', methods=["GET", "POST"])
def transfers_route():
    if request.method == "GET":
        return jsonify(trans.get_list_transfers())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data['id'], data['fromID'], data['toID'], data['amnt']) # whatever the expected order of the data is as an iterable
        if trans.into_transfers(vals):
            return Response(status=204)
        else:
            return Response(status=500)


@app.route('/api/includes', methods=["GET"])
def includes_route():
    return jsonify(inc.get_list_includes())


@app.route('/api/has', methods=["GET", "POST"])
def has_route():
    if request.method == "GET":
        return jsonify(has.get_list_has())
    elif request.method == "POST":
        data = json.loads(request.data)
        vals = (data['locID'], data['prodID'], data['price'], data['stock']) # whatever the expected order of the data is as an iterable
        if has.into_has(vals):
            return Response(status=204)
        else:
            return Response(status=500)


@app.route('/api/buys', methods=["GET"])
def buys_route():
    return jsonify(buy.get_list_buys())


@app.route('/api/owns', methods=["GET"])
def owns_route():
    return jsonify(owns.get_list_owns())


# Theoretically only used in production
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    print(app.static_folder)
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == "__main__":
    app.run(port=5000)
