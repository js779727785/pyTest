import json
import requests
import time
from config import xw_url
from lib.log import logger
from lib.MySQLHelper import MySQLHelper
from lib.common import DemoLogin


"""第四步:测试环境用户确认打款---Jmelody"""


def checkCompany(tel_num):
    token_no = DemoLogin.qydFrontLogin(tel_num,"js123456")
    print(token_no)
    header = {
        "Content-Type": "application/json; charset=UTF-8", "X-Auth-Token": token_no
    }
    query_info_sql="select * from qydproduction.remit_detail where tel_num=%s order by create_time desc;"
    query_info=MySQLHelper("qydproduction").get_many(query_info_sql,tel_num)
    checkAmount=query_info[0]['amount']
    count=query_info[0]['count']
    data = {"amount": str(float(checkAmount) / 100),
                                "redirectUrl": "https://azure-www.qingyidai.com/xwcallback/companyFlow"}
    logger.info("确认打款传参:"+str(data))
    response= requests.post(url=xw_url.CheckAmountAndRegisterXW,json=data, headers=header)
    print(response)
    response_json=response.json()
    if response_json['status']==200:
        logger.info("返回结果:"+str(response_json))
        if response_json['resultCode']['code']=='CHECK_SUCCESS':
            logger.info("-----确认打款成功-----")
            xw_data = response_json['entities'][0]['requestParam']
            logger.info("******请求新网参数" + str(xw_data).replace("'", '"'))
            New = requests.post(url=xw_url.gateway, data=xw_data)
            register_url = New.url
            logger.info("******跳转新网页面地址" + str(register_url))
            Location = register_url[-36:]
            logger.info("====跳转新网页面成功====")
            xw_CompanySMSdata = {"requestKey": "", "bizType": "REGISTER"}
            xw_CompanySMSdata['requestKey'] = Location
            SMS = requests.post(url=xw_url.Xwsmsurl, data=xw_CompanySMSdata, verify=False).json()
            if SMS['status'] == "SUCCESS":
                headers2 = {"content-type": "application/x-www-form-urlencoded"}
                RegisterEnterprisebody = {
                    "protocolCheckBox": "false",
                    "randomNumPassAgain": "",
                    "branchName": "中国工商银行上海市中原支行",
                    "branchNo": "102290028965",
                    "maskPasswordAgain": "",
                    "smsCode": "000000",
                    "randomNumPass": "",
                    "password": "js12345678",
                    "confirmPassword": "js12345678",
                    "bankCode": "ICBK",
                    "maskPassword": "",
                    "amount": "10000000",
                    "authLimitSwitch": "true",
                    "defaultValue": "false",
                    "failTime": "2118年03月28日",
                    "requestKey": ""
                }
                RegisterEnterprisebody['requestKey'] = Location
                logger.info("******企业用户在新网填写信息" + str(RegisterEnterprisebody))
                requests.post(url=xw_url.XWregisterEnterpriseurl, data=RegisterEnterprisebody,
                              headers=headers2)
                time.sleep(5)
                xw_id_sql = 'select xw_id from xw_user_role WHERE user_id=(SELECT id FROM user WHERE tel_num="' + str(
                    tel_num) + '");'
                xw_id = MySQLHelper('qydproduction').selectsql(xw_id_sql)
                if xw_id is not None:
                    logger.info("*******新网审核中,企业用户手机号：" + str(tel_num) + " 新网用户编号：" + str(
                        xw_id[0]['xw_id']))
                else:logger.info("xw_user_role  is  None!!!!")
        else:
            logger.info("-----确认打款失败-----"+str(response_json['resultCode']['code'])+" , error_message: "+str(response_json['resultCode']['message']))
    else:logger.error("-----确认打款接口异常-----")

# checkCompany('16803582520')

