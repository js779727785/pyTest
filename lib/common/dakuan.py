import json
import requests
from config.demoUrl import qydgateway
from lib.log import logger
from lib.MySQLHelper import MySQLHelper

headers = {
    "Content-Type": "application/json; charset=UTF-8"
}


def dakuan(tel_num,pendingConfirm):
    url=qydgateway+"/paycenter/bankinfoverify/bankresult"
    data={"settlementAmount": 5800,"id": "fdcc81dc-222f-4e7e-b0db-b5aa8f188345","pendingConfirm": pendingConfirm}
    query_info_sql="select * from qydproduction.remit_detail where tel_num=%s order by create_time desc;"
    query_info=MySQLHelper("qydproduction").get_many(query_info_sql,tel_num)
    settlementAmount=query_info[0]['amount']
    logger.info("打款金额:"+str(settlementAmount))
    data["settlementAmount"]=str(settlementAmount*100)
    transfer_id=query_info[0]['transfer_id']
    print(transfer_id)
    query_QydOrder_sql="select * from paycenter.QydOrder WHERE outOrderNo=%s  ORDER BY createTime DESC;"
    query_QydOrder=MySQLHelper("paycenter").get_many(query_QydOrder_sql,transfer_id)
    orderId=query_QydOrder[0]["orderId"]
    data["id"]=orderId
    logger.info("打款传参:"+str(data))
    reponse=requests.post(url=url,json=data,headers=headers)
    logger.info("调打款接口返回结果:"+str(reponse))

dakuan(16803585092,"3")

