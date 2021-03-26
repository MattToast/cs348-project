import mysql.connector
import connection_info


def get_list_inventory():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Inventory;"
    inv = []
    try:
        cursor.execute(query)
        for (id, name) in cursor:
            inv.append({
                "ProductID": id,
                "Name": name,
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

def into_inventory(vals):
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "INSERT INTO Inventory VALUES (%s, %s)"
    try:
        cursor.execute(query, vals)
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print("Oi Got Err:")
        print(e)
    cursor.close()
    cnx.close()
