from flask import Blueprint,request

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