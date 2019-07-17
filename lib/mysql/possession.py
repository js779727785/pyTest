from lib.MySQLHelper import MySQLHelper
from lib.log import logger
from config.config import qydnewproduction
def queryMtPossession(userid):
    sql="SELECT loan_id from mt_possession where user_id=%s"
    re=MySQLHelper(qydnewproduction).get_many(sql,userid)
    # r=re[0]['loan_id']
    # print(r)
    # logger.info(r)
    return re
#queryMtPossession('816bb0ac-c302-4cc7-918a-cb91c30176ac')