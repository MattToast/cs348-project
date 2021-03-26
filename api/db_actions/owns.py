import mysql.connector
import connection_info


def get_list_owns():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Owns;"
    owns = []
    try:
        cursor.execute(query)
        for (locID, empId) in cursor:
            owns.append({
                "Location ID": locID,
                "Employee ID": empId,
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return owns
