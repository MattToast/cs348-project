from flask import Flask, json, jsonify, send_from_directory
import mysql.connector

import connection_info

app = Flask(__name__,
            static_folder="../build",
            static_url_path="/")


@app.route('/api/customers')
def customers():
    return jsonify({"message": "hello world"})


@app.route('/api/employees', methods=["GET", "POST"])
def employees():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    query = "SELECT * FROM employees;"
    cursor = cnx.cursor()
    emps = []
    try:
        cursor.execute(query)
        for (id, pos, sal, loc) in cursor:
            emps.append({
                "EmployeeID": id,
                "Location": loc,
                "Position": pos,
                "Salary": sal
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return jsonify([])

    cursor.close()
    cnx.close()
    return jsonify(emps)


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
