import mysql.connector
import connection_info


def get_list_buys():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Buys;"
    trans = []
    try:
        cursor.execute(query)
        for (custID, EmpId, SalesID) in cursor:
            trans.append({
                "Customer ID": custID,
                "Employee ID": EmpId,
                "Sale ID": SalesID,
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return trans
