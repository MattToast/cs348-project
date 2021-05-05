from flask import Blueprint,request
import mysql.connector
import connection_info as ci


import db_actions.transfers as trans
import db_actions.sales as sales

reportRoutes = Blueprint('reportRoutes', __name__)


@reportRoutes.route('/transfers', methods=["GET"])
def transfers():
    transfers_list: 'list[dict]' = trans.get_list_transfers()
    transfer_table = "<table border = '1'>"
    transfer_table += "<tr><th colspan=3>Transfer History</th></tr>"
    transfer_table += "<tr><td>Transfer From</td><td>Transfer To</td><td>Amount</td></tr>"
    for t in transfers_list:
        transfer_table += f"<tr><td>{t['From']}</td><td>{t['To']}</td><td>{t['Amount']}</td></tr>"
    transfer_table += "</table>"
    return transfer_table


@reportRoutes.route('/empsales', methods=["GET"])
def employee_sales():
    since = request.args.get("s")
    title = request.args.get("t")
    if since == None or title == None:
        since = 0
        title = "Sales for all time:"
    vals = (since, 0)
    return sales.get_sales_report(vals, title)


@reportRoutes.route('/complex', methods=["GET"])
def complex_report():
    cnx = mysql.connector.connect(user=ci.MyUser,
                                  password=ci.MyPassword,
                                  host=ci.MyHost,
                                  database=ci.MyDatabase)
    cursor = cnx.cursor()
    report: str = None
    try:
        # Don't know why, but when a mad the stored proc with only one arg I got an
        # 'args must be a sequence' error -> hacky fix but it works
        retVals = cursor.callproc("GetComplexReport", args=(0, 0))
        report = "<h1>Complex Report</h1>" + retVals[-1]
    except Exception as e:
        print("Oi, got err:")
        print(e)
        report = "Something went wrong making the report"
    return report


@reportRoutes.route('/moneyflow', methods=["GET"])
def moneyflow_report():
    cnx = mysql.connector.connect(user=ci.MyUser,
                                  password=ci.MyPassword,
                                  host=ci.MyHost,
                                  database=ci.MyDatabase)
    cursor = cnx.cursor()
    report: str = None
    try:
        # Don't know why, but when a mad the stored proc with only one arg I got an
        # 'args must be a sequence' error -> hacky fix but it works
        retVals = cursor.callproc("MoneyFlowReport", args=(0, 0))
        report = "<h1>Money Flow Report</h1>" + retVals[-1]
    except Exception as e:
        print("Oi, got err:")
        print(e)
        report = "Something went wrong making the report"
    return report
