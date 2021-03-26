import mysql.connector
import connection_info


def get_list_employees():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Employee;"
    emps = []
    try:
        cursor.execute(query)
        for (id, pos, sal, loc) in cursor:
            emps.append({
                "EmployeeID": id,
                "position": pos,
                "Salary": sal,
                "LocationID": loc
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


def into_employees(vals):
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "INSERT INTO employees VALUES (%d, %s, $d, %d)"
    try:
        cursor.execute(query, vals)
        cnx.commit()
    except Exception as e:
        cnx.rollback()
        print("Oi Got Err:")
        print(e)
    cursor.close()
    cnx.close()
