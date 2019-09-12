import requests
from lib.MySQLHelper import MySQLHelper
from lib.log import logger
from config import url


def ComRepay(loan_id,day):
    # sql_1="update mt_loan set open_time=date_add(NOW(), interval -180 day),close_time=date_add(NOW(), interval -180 day),repay_date=NOW() where id=%s;"
    # MySQLHelper("production").update_one(sql_1,loan_id)
    # sql_2="update mt_possession set loan_close_time=date_add(NOW(), interval -180 day),day=date_add(NOW(), interval -180 day),create_time=NOW() where loan_id="+loan_id+";commit;"
    # MySQLHelper("production").updatesql(sql_2)
    headers = {"Content-Type": "application/json"}
    param = {
        "type": 7,
        "day": day
    }
    requests.packages.urllib3.disable_warnings()
    MakeOverdueResult = requests.post(url=url.MakeOverdueUrl, headers=headers, json=param, verify=False).json()
    print(MakeOverdueResult)

def OverRepay(loan_id,day):
    """day传今天前一天，如今天：2019-09-09，传2019-09-08"""
    # sql_1="update mt_loan set open_time=date_add(NOW(), interval -181 day),close_time=date_add(NOW(), interval -181 day),repay_date=date_add(NOW(), interval -1 day) where id="+loan_id+";commit;"
    # mysqldb('qyddb').updatesql(sql_1)
    # sql_2="update mt_possession set loan_close_time=date_add(NOW(), interval -181 day),day=date_add(NOW(), interval -181 day),create_time=date_add(NOW(), interval -181 day) where loan_id="+loan_id+";commit;"
    # mysqldb('qyddb').updatesql(sql_2)
    headers = {"Content-Type": "application/json"}
    param = {
        "type": 6,
        "day": day
    }
    requests.packages.urllib3.disable_warnings()
    MakeOverdueResult = requests.post(url=url.MakeOverdueUrl, headers=headers, json=param, verify=False).json()
    print(MakeOverdueResult)

ComRepay('16085c40-1eda-4c52-86af-d15144538851','2019-09-09')