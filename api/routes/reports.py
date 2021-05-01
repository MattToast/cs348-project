from flask import Blueprint

reportRoutes = Blueprint('reportRoutes', __name__)


@reportRoutes.route('/transfers')
def transfers():
    return "Get Transfer Report"


@reportRoutes.route('empsales/<empID>')
def employeeSales(empID):
    return f"Get employee sales for employee with id {empID}"

