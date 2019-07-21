import decimal

from lib.MySQLHelper import MySQLHelper
from lib.log import logger

def queryuser(pho):
    if pho is None:
        logger.info("sql中pho为空")
    sql="SELECT id from qydproduction.user where tel_num=%s"
    result= MySQLHelper("qydproduction").get_one(sql=sql,params=pho)
#    logger.info(result['id'])
    return result
# queryuser('16803581610')

"""以下两个学习get_many的用法
    返回结果内容为list，取值方式为：
    results = MySQLHelper("DB").get_many(sql, params)
    if result is not None or result.__len__() >0:
        for i in range(results.__len__()):
            mysqlresponse = result[i].get('mysqlziduan')
            logger.info("result:"+str(result[I]['mysqlziduan']))
"""


# 查询投资人
def queryOldPossessionInfo(loanId):
    sql = "select buyer_id,amount,request_time,create_time,transaction_id from mt_possession_order where status in (-1,0,1) and " \
          "type='LOAN' and loan_id =%s"

    params = (loanId)
    result = MySQLHelper("qydnewproduction").get_many(sql, params)

    print(result.__len__())
    logger.info("result:"+str(result[0]['buyer_id']))
    logger.info("result:" + str(result[1]['buyer_id']))
    return result
# queryOldPossessionInfo('ad45f833-748c-4fa2-9695-c41514ab6d0a')

# 查询用户某个账户未关闭且已违约账单的欠款情况
def queryDueBillsDebtInfo(userGuid, billingType):
    sql = "select * from KyBilling where LogicalDel=0 and status!=2 and UserDueDate<=now() and UserGuid=%s and BillingType=%s ORDER BY CreateTime"
    #注意多参数传递写法
    params = (userGuid, billingType)
    result = MySQLHelper("front").get_many(sql, params)
    bills = {}
    if result is not None and result.__len__() > 0:
        billList = []
        for i in range(result.__len__()):
            billingProcessGuid = result[i].get('BillingProcessGuid')
            reduUserFees = decimal.Decimal(0.00)
            reduLateFees = decimal.Decimal(0.00)
            # 查看是否有有效的减免
            reduction = queryKyReductionLateFees(billingProcessGuid)
            if reduction.get('ReduUserFees') is not None:
                reduUserFees = reduction.get('ReduUserFees')
            if reduction.get('ReduLateFees') is not None:
                reduLateFees = reduction.get('ReduLateFees')
            p = result[i].get('Principal')-result[i].get('HaPrincipal')-result[i].get('RefundAmount')
            u = result[i].get('UserFees')-result[i].get('HaUserFees')-reduUserFees
            l = result[i].get('LateFees')-result[i].get('HaLateFees')-reduLateFees
            debtInfo = {"billingProcessGuid": billingProcessGuid,
                        "remainPrincipal": saveTwoDecimal(p/10000),
                        "remainUserFees": saveTwoDecimal(u/10000),
                        "remainLateFees": saveTwoDecimal(l/10000),
                        "remainTotalAmount": saveTwoDecimal((p+u+l)/10000),
                        "lateDays": result[i].get('LateDays')}
            billList.append(debtInfo)
        bills['bills'] = billList
    logger.info("**************用户未关闭账单欠款详情为： "+str(bills))
    return bills