import mysql.connector

import connection_info

# TODO: Everying in this file should be rewritten

def get_list_employees():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM employees;"
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
        return []

    cursor.close()
    cnx.close()
    return emps


def get_list_inventory():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM inventory;"
    inv = []
    try:
        cursor.execute(query)
        for (id, name, loc, price, stock) in cursor:
            inv.append({
                "ProductID": id,
                "Name": name,
                "Sold at Location": loc,
                "Price": price,
                "Stock": stock
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return inv


def get_list_locations():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM locations;"
    locs = []
    try:
        cursor.execute(query)
        for (id, own_id, name, cash) in cursor:
            locs.append({
                "LocationID": id,
                "OwnerID": own_id,
                "Name": name,
                "Cash": cash
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return locs


def get_list_customers():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM customers;"
    cust = []
    try:
        cursor.execute(query)
        for (id, name, addr, phone, promote) in cursor:
            cust.append({
                "CustomerID": id,
                "Name": name,
                "Address": addr,
                "Phone": phone,
                "Promote": promote
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return cust

def get_list_sales():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM sales;"
    sales = []
    try:
        cursor.execute(query)
        for (id, prod_id, cust_id, amnt, loc_id) in cursor:
            sales.append({
                "SalesID": id,
                "ProductID": prod_id,
                "CustomerID": cust_id,
                "SaleAmount": amnt,
                "LocationID": loc_id
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return sales