import json
import requests
import time
from config.demoUrl import qydgateway
from lib.log import logger
from lib.MySQLHelper import MySQLHelper

"""第三步:测试环境模拟向企业打款---Jmelody"""
header = {
    'Content-Type': 'application/json',
}
#pendingConfirm:2 打款失败;pendingConfirm:3,打款成功
def dakuan(tel_num,pendingConfirm):
    dakuan_url=qydgateway+"/paycenter/bankinfoverify/bankresult"
    data= {"settlementAmount": 1800,
     "id": "0010d495-9f52-4503-8bf8-2d1dec0b5491",
     "pendingConfirm": pendingConfirm}
    query_info_sql="select * from qydproduction.remit_detail where tel_num=%s order by create_time desc;"
    query_info=MySQLHelper("qydproduction").get_many(query_info_sql,tel_num)
    settlementAmount=query_info[0]['amount']
    logger.info("打款金额:"+str(settlementAmount))
    """以下传参未转换未int时会报传参错误"""
    data["settlementAmount"]=str(int(settlementAmount) * 100)
    transfer_id=query_info[0]['transfer_id']
    query_QydOrder_sql="select * from paycenter.QydOrder WHERE outOrderNo=%s  ORDER BY createTime DESC;"
    query_QydOrder=MySQLHelper("paycenter").get_many(query_QydOrder_sql,transfer_id)
    orderId=query_QydOrder[0]["orderId"]
    data["id"]=orderId
    logger.info("打款传参:"+str(data))
    reponse=requests.post(url=dakuan_url,json=data)
    print(reponse)
    reponse_json=reponse.json()
    logger.info("调打款接口返回结果:"+str(reponse_json))
    if reponse_json['status']==10000:
        logger.info("-------调打款接口成功----")
        time.sleep(3)
        query_record="select * from company_remit_record where order_no=%s;"
        company_remit_record=MySQLHelper("qydproduction").get_many(query_record,transfer_id)
        if company_remit_record is not None:
            logger.info("company_remit_record:  " + str(company_remit_record))
            """库表更新后需要重新查一遍状态"""
            query_info = MySQLHelper("qydproduction").get_many(query_info_sql, tel_num)
            status = query_info[0]['status']
            if status=='REMIT_SUCCESS':
                logger.info("----打款成功,账户状态为:"+str(status))
                return tel_num
            elif status=='REMIT_FAILURE':
                logger.info("----打款失败,账户状态为:" + str(status))
            else:logger.info("----打款返回status:" + str(status))
        else:logger.error("-----打款接口返回错误----")



# dakuan("16803587128","3")

