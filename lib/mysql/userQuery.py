
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