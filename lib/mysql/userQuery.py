
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
queryOldPossessionInfo('ad45f833-748c-4fa2-9695-c41514ab6d0a')