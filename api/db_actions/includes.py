import mysql.connector
import connection_info


def get_list_includes():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Includes;"
    inc = []
    try:
        cursor.execute(query)
        for (prodID, locID, saleID, num) in cursor:
            inc.append({
                "Product ID": prodID,
                "Location ID": locID,
                "Sale ID": saleID,
                "Number Bought": num,
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return inc
