from lib.log import logger
from lib.MySQLHelper import MySQLHelper
from config import demoUrl
import requests
"""
修改XZY,XYY到期还款时间
"""
def DaoqiXX(loanId):
    sql1="update qydnewproduction.mt_loan set open_time=date_add(NOW(), interval -32 day),close_time=date_add(NOW(), interval -32 day),repay_date=NOW() where id='"+loanId+"';";
    sql2="update qydnewproduction.repay_billing set repay_date=NOW() where loan_id='"+loanId+"';";
    sql3="update qydnewproduction.mt_possession set loan_close_time=DATE_ADD(NOW(),INTERVAL -32 day),end_date=NOW(),`day`=DATE_ADD(NOW(),INTERVAL -32 day) where loan_id='"+loanId+"';";
    sql1="update qydnewproduction.mt_loan set open_time=date_add(NOW(), interval -20 day),close_time=date_add(NOW(), interval -20 day),repay_date=NOW() where id='"+loanId+"';";
    sql2="update qydnewproduction.repay_billing set repay_date=NOW() where loan_id='"+loanId+"';";
    sql3="update qydnewproduction.mt_possession set loan_close_time=DATE_ADD(NOW(),INTERVAL -20 day),end_date=NOW(),`day`=DATE_ADD(NOW(),INTERVAL -20 day) where loan_id='"+loanId+"';";
    MySQLHelper('qydnewproduction').updatesql(sql1)
    MySQLHelper('qydnewproduction').updatesql(sql2)
    MySQLHelper('qydnewproduction').updatesql(sql3)
    reponseSql1="SELECT * from qydnewproduction.mt_loan where id =%s"
    reponseSql2 = "SELECT * from qydnewproduction.repay_billing where loan_id =%s"
    reponse1=MySQLHelper('qydnewproduction').get_many(reponseSql1,loanId)
    reponse2= MySQLHelper('qydnewproduction').get_many(reponseSql2, loanId)
    logger.info(loanId+"mt_loan修改后的repay_date为："+str(reponse1[0]['repay_date']))
    logger.info(loanId+"repay_billing修改后的repay_date为：" + str(reponse2[0]['repay_date']))

"""
修改XZY,XYY违约还款时间
"""
def WeiyueXX(loanId):
    sql1="update qydnewproduction.mt_loan set open_time=date_add(NOW(), interval -32 day),close_time=date_add(NOW(), interval -32 day),repay_date=date_add(NOW(), interval -1 day) where id='"+loanId+"';";
    sql2="update qydnewproduction.repay_billing set repay_date=date_add(NOW(), interval -1 day) where loan_id='"+loanId+"';";
    sql3="update qydnewproduction.mt_possession set loan_close_time=DATE_ADD(NOW(),INTERVAL -32 day),end_date=date_add(NOW(), interval -1 day),`day`=DATE_ADD(NOW(),INTERVAL -32 day) where loan_id='"+loanId+"';";
    MySQLHelper('qydnewproduction').updatesql(sql1)
    MySQLHelper('qydnewproduction').updatesql(sql2)
    MySQLHelper('qydnewproduction').updatesql(sql3)
    reponseSql1="SELECT * from qydnewproduction.mt_loan where id =%s"
    reponseSql2 = "SELECT * from qydnewproduction.repay_billing where loan_id =%s"
    reponse1=MySQLHelper('qydnewproduction').get_many(reponseSql1,loanId)
    reponse2= MySQLHelper('qydnewproduction').get_many(reponseSql2, loanId)
    logger.info(loanId+",mt_loan修改后的repay_date为："+str(reponse1[0]['repay_date']))
    logger.info(loanId+",repay_billing修改后的repay_date为：" + str(reponse2[0]['repay_date']))

"""
修改QY到期还款时间
"""
def DaoqiQY(loanId):
    sql1="update mt_loan set open_time=date_add(NOW(), interval -180 day),close_time=date_add(NOW(), interval -180 day),repay_date=NOW() where id='"+loanId+"';";
    sql2="update mt_possession set loan_close_time=date_add(NOW(), interval -180 day),day=date_add(NOW(), interval -180 day),create_time=date_add(NOW(), interval -180 day) where loan_id='"+loanId+"';";
    sql3 = "UPDATE mt_possession_order set create_time= date_add(create_time,INTERVAL -180 day) where loan_id='" + loanId + "';";
    MySQLHelper('qydproduction').updatesql(sql1)
    MySQLHelper('qydproduction').updatesql(sql2)
    MySQLHelper('qydproduction').updatesql(sql3)
    reponseSql1="select * from mt_loan where id=%s"
    reponseSql2 = "select * from mt_possession where loan_id =%s"
    reponse1=MySQLHelper('qydproduction').get_many(reponseSql1,loanId)
    reponse2= MySQLHelper('qydproduction').get_many(reponseSql2, loanId)
    logger.info(loanId+"mt_loan修改后的repay_date为："+str(reponse1[0]['repay_date']))
    logger.info(loanId+"mt_possession修改后的day为：" + str(reponse2[0]['day']))
def WeiYueQY(loanId):
    sql1="update mt_loan set open_time=date_add(NOW(), interval -280 day),close_time=date_add(NOW(), interval -280 day),repay_date=date_add(NOW(), interval -100 day) where id='"+loanId+"';";
    sql2="update mt_possession set loan_close_time=date_add(NOW(), interval -280 day),day=date_add(NOW(), interval -280 day),create_time=date_add(NOW(), interval -280 day) where loan_id='"+loanId+"';";
    sql3 = "UPDATE mt_possession_order set create_time= date_add(create_time,INTERVAL -180 day) where loan_id='" + loanId + "';";
    MySQLHelper('qydproduction').updatesql(sql1)
    MySQLHelper('qydproduction').updatesql(sql2)
    MySQLHelper('qydproduction').updatesql(sql3)
    reponseSql1="select * from mt_loan where id=%s"
    reponseSql2 = "select * from mt_possession where loan_id =%s"
    reponse1=MySQLHelper('qydproduction').get_many(reponseSql1,loanId)
    reponse2= MySQLHelper('qydproduction').get_many(reponseSql2, loanId)
    logger.info(loanId+"mt_loan修改后的repay_date为："+str(reponse1[0]['repay_date']))
    logger.info(loanId+"mt_possession修改后的day为：" + str(reponse2[0]['day']))

"""
修改月盈精选QYB到期时间
"""
def DaoqiQYB(loanId):
    sql1="update qydnewproduction.mt_loan set open_time=date_add(NOW(), interval -130 day),close_time=date_add(NOW(), interval -130 day),repay_date=NOW() where id='"+loanId+"';";
    sql2="update qydnewproduction.repay_billing set repay_date=NOW() where loan_id='"+loanId+"';";
    sql3="update qydnewproduction.mt_possession set loan_close_time=DATE_ADD(NOW(),INTERVAL -130 day),end_date=NOW(),`day`=DATE_ADD(NOW(),INTERVAL -130 day) where loan_id='"+loanId+"';";
    MySQLHelper('qydnewproduction').updatesql(sql1)
    MySQLHelper('qydnewproduction').updatesql(sql2)
    MySQLHelper('qydnewproduction').updatesql(sql3)
    reponseSql1="SELECT * from qydnewproduction.mt_loan where id =%s"
    reponseSql2 = "SELECT * from qydnewproduction.repay_billing where loan_id =%s"
    reponse1=MySQLHelper('qydnewproduction').get_many(reponseSql1,loanId)
    reponse2= MySQLHelper('qydnewproduction').get_many(reponseSql2, loanId)
    logger.info(loanId+"mt_loan修改后的repay_date为："+str(reponse1[0]['repay_date']))
    logger.info(loanId+"repay_billing修改后的repay_date为：" + str(reponse2[0]['repay_date']))
"""
    查询qydnewproduction标的状态
"""
def queryMtStatus(loanId):
    reponseSql1="SELECT * from qydnewproduction.mt_loan where id =%s"
    reponse1=MySQLHelper('qydnewproduction').get_many(reponseSql1,loanId)
    logger.info(loanId+"的status为："+str(reponse1[0]['status']))
"""轻盈还款"""
def MakeOverdue(nowday):
    headers={"Content-Type":"application/json"}
    #到期还款："type": 5,违约还款："type": 6,撤资还款：type：”7“
    param={
        "type": 6,
        "day": nowday,
        "key": "QY"
    }
    requests.packages.urllib3.disable_warnings()
    MakeOverdueResult=requests.post(url=demoUrl.MakeOverdueUrl,headers=headers,json=param,verify=False).json()
    print(MakeOverdueResult)

'''违约不想还款的话，先确保账户没钱；参数传标的id和当前日期的前一天'''

DaoqiQY('982039be-0efb-4cf9-a669-4802a657005e')
# WeiYueQY('982039be-0efb-4cf9-a669-4802a657005e')
# MakeOverdue("2019-10-24")
# DaoqiXX('4206fbc0-1623-4943-a309-6f5db42df686')