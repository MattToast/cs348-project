import mysql.connector
import connection_info

def get_list_locations():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Locations;"
    locs = []
    try:
        cursor.execute(query)
        for (id, money, ownerID) in cursor:
            locs.append({
                "LocationID": id,
                "OwnerID": ownerID,
                "Money": money
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