import mysql.connector
import connection_info


def get_list_has():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Has;"
    hases = []
    try:
        cursor.execute(query)
        for (locID, prodID, price, stock) in cursor:
            hases.append({
                "Location ID": locID,
                "Product ID": prodID,
                "Price": price,
                "Number in Stock": stock,
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return hases
