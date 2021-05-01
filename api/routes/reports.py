from flask import Blueprint

reportRoutes = Blueprint('reportRoutes', __name__)


@reportRoutes.route('/transfers', methods=["GET"])
def transfers():
    return "Get Transfer Report"


@reportRoutes.route('empsales/<empID>', methods=["GET"])
def employee_sales(empID):
    return f"Get employee sales for employee with id {empID}"

