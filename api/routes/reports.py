from flask import Blueprint

import db_actions.transfers as trans

reportRoutes = Blueprint('reportRoutes', __name__)


@reportRoutes.route('/transfers', methods=["GET"])
def transfers():
    transfers_list: 'list[dict]' = trans.get_list_transfers()
    transfer_table = "<html><table border = '1'>"
    transfer_table += "<tr><th colspan=3>Transfer History</th></tr>"
    transfer_table += "<tr><td>Transfer From</td><td>Transfer To</td><td>Amount</td></tr>"
    for t in transfers_list:
        transfer_table += f"<tr><td>{t['From']}</td><td>{t['To']}</td><td>{t['Amount']}</td></tr>"
    transfer_table += "</table></html>"
    return transfer_table


@reportRoutes.route('empsales/<empID>', methods=["GET"])
def employee_sales(empID):
    return f"Get employee sales for employee with id {empID}"
