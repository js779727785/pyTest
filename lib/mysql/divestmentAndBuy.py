from lib.MySQLHelper import MySQLHelper
from lib.log import logger

def queryAssign(assign_id):
    sql="select ma.is_buy from mt_assignment ma where transaction_id in ('%s');"
    result=MySQLHelper("qydproduction").get_many(sql,assign_id)
    logger.info(str(result))
    return result

def queryTranaction(transaction_id):
    sql="select ma.is_buy from mt_assignment ma where transaction_id in ('%s');"
    result=MySQLHelper("qydproduction").get_many(sql,transaction_id)
    logger.info(str(result))

    return result