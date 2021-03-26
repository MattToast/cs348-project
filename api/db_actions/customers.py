import mysql.connector
import connection_info


def get_list_customers():
    cnx = mysql.connector.connect(user=connection_info.MyUser, password=connection_info.MyPassword,
                                  host=connection_info.MyHost,
                                  database=connection_info.MyDatabase)

    cursor = cnx.cursor()
    query = "SELECT * FROM Customers;"
    cust = []
    try:
        cursor.execute(query)
        for (id, name, addr, phone, promote) in cursor:
            cust.append({
                "CustomerID": id,
                "Name": name,
                "Address": addr,
                "Phone": phone,
                "OfferPromotions": promote
            })

    except Exception as e:
        print("Oi Got Err:")
        print(e)
        cursor.close()
        cnx.close()
        return []

    cursor.close()
    cnx.close()
    return cust
