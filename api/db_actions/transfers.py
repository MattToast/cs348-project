import mysql.connector
from mysql.connector.errors import custom_error_exception
import connection_info


def get_list_transfers() -> 'list[dict]':
    cnx = mysql.connector.connect(user=connection_info.MyUser,
                                  password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Transfers;"
    trans = []
    try:
        cursor.execute(query)
        for (id, fromID, toID, amnt) in cursor:
            trans.append({
                "Transfer ID": id,
                "From": fromID,
                "To": toID,
                "Amount": amnt,
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


def into_transfers(data) -> bool:
    cnx = mysql.connector.connect(user=connection_info.MyUser,
                                  password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query0 = "INSERT INTO Transfers VALUES (%s, %s, %s, %s);"
    query1 = "UPDATE Locations SET money = money - (%s) WHERE (%s) = (%s);"
    query2 = "UPDATE Locations SET money = money + (%s) WHERE (%s) = (%s);"
    succ = True
    try:
        cursor.execute(query0, data)
        cursor.execute(query1, (data[3], data[1], data[1]))
        cursor.execute(query2, (data[3], data[2], data[2]))
        cnx.commit()
    except Exception as e:
        print(e)
        succ = False
    cursor.close()
    cnx.close()
    return succ

    
