import mysql.connector
import connection_info


def get_list_has():
    cnx = mysql.connector.connect(user=connection_info.MyUser, 
                                  password=connection_info.MyPassword,
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


def into_has(vals) -> bool:
    cnx = mysql.connector.connect(user=connection_info.MyUser,
                                  password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "INSERT INTO Has VALUES (%s, %s, %s, %s) ON DUPLICATE KEY UPDATE price = (%s), stock = (%s)"
    succ = True
    try:
        cursor.execute(query, (vals[0], vals[1], vals[2], vals[3], vals[2], vals[3]))
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print("Oi Got Err:")
        print(e)
        succ = False
    cursor.close()
    cnx.close()
    return succ
