import json
import requests
import random
from config import xw_url
from lib.log import logger
from lib.MySQLHelper import MySQLHelper
from lib.common.DemoLogin import login_backed

"""第二步:QYD后台认领任务并审批通过----Jmelody"""
def bankedVerity(tel_num):
    """1.认领任务get请求"""
    queryCompanyIdSql="SELECT * FROM user_company WHERE user_id=(select id from user where tel_num=%s );"
    queryUserCompany=MySQLHelper("qydproduction").get_many(queryCompanyIdSql,tel_num)
    companyId=queryUserCompany[0]['id']
    claimId=queryUserCompany[0]['claim_id']
    userId=queryUserCompany[0]['user_id']
    logger.info("queryCompanyId:"+str(companyId))
    logger.info("claimId:"+str(claimId))
    claim_url=xw_url.claimTaskurl+ str(companyId) + "&claimId=" + str(claimId) + "&operatorName=admin&userId=" + str(userId)
    logger.info("认领请求url:"+claim_url)
    header = {
        'Content-Type': 'application/json',
        'X-Auth-Token': login_backed()
    }
    reponse=requests.get(url=claim_url,headers=header)
    reponse_json=reponse.json()
    if reponse_json['status']==200:
        logger.info("--------认领任务成功--------")
        logger.info("------后台审批任务开始------")
        parm={"userId":"aa76306f-75bc-43d0-b43d-cc2e243905f0","remark":"BEIZHU","companyId":"a625628a-4ce8-4f5d-8db4-1b0d47817e77","userFund":"1000","userProvince":"北京市 北京市","userAddress":"北京市永丰用友科技园21","registerDate":"2019-09-01","industry":"IT","logout":"0"}
        parm['userId']=userId
        parm['companyId']=companyId
        logger.info("审批请求参数:"+str(parm))
        auditReponse=requests.post(url=xw_url.auditCompanyPassurl,json=parm,headers=header)
        print(auditReponse)
        auditReponse_json=auditReponse.json()
        if auditReponse_json['status']==200:
            logger.info("--------后台审批通过,手机号为--------"+str(tel_num))
            return tel_num
        else:
            logger.error("--------审批接口提交失败--------")
    else:logger.error("--------认领任务失败--------")


# bankedVerity(16803584422)



