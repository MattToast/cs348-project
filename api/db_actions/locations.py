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


def into_locations(vals):
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "INSERT INTO Locations VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE ownerID = (%s)"
    try:
        cursor.execute(query, (vals[0], vals[1], vals[2], vals[2]))
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print("Oi Got Err:")
        print(e)
    cursor.close()
    cnx.close()
