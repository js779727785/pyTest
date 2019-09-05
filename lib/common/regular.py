from lib.log import logger
import requests,random,json
from lib.common.DemoLogin import qydFrontLogin
from lib.common.getUserName import GetUserName
from lib.common import IDcard,register,public_way
from config import xw_url
from  config.xw_url import NewPersonUrl
import time
from lib.mysqldb import mysqldb


"""个人开通银行存管---Jmelody"""

def regular(tel_num,password):
    """个人绑卡"""
    token =qydFrontLogin(tel_num,password)
    headers={"Content-Type": "application/json; charset=UTF-8", "X-Auth-Token": token}
    user_name=GetUserName.full_name()
    print(user_name)
    idCardNo=IDcard.getRandomIdNumber()
    bankcardNo=IDcard.bankidCardNo()
    Message_body = {"realName": user_name, "idCardNo": idCardNo, "bankcardNo": bankcardNo, "mobile": tel_num,
                    "redirectUrl": "https://azure-www.qingyidai.com/usermanagement/account.shtml",
                    "bankcode": "CMBC"}
    logger.info("请求传参："+str(Message_body))
    New_RegularRN = requests.post(url=NewPersonUrl,json=Message_body,headers=headers)
    print(New_RegularRN)
    New_RegularRN_json =New_RegularRN.json()
    xw_data = New_RegularRN_json['entities'][0]['requestParam']
    """从请求参数中获取平台用户编号，即xw_id"""
    platformUserNo = json.loads(str(New_RegularRN_json['entities'][0]['requestParam']['reqData']))[
        'platformUserNo']
    """请求新网流水号，用于接收回调等关键字段"""
    requestNo = json.loads(str(New_RegularRN_json['entities'][0]['requestParam']['reqData']))['requestNo']
    New = requests.post(url=xw_url.gateway, data=xw_data, verify=False)
    register_url = New.url
    Location = register_url[-36:]
    """获取卡宾"""
    data1 = {"bankcardNo": "", "serviceType": "BANKCARD_AUTH", "requestKey": ""}
    data1['bankcardNo'] = Message_body['bankcardNo']
    data1['requestKey'] = Location
    requests.post(url=xw_url.bankcardbin, data=data1, verify=False)
    """新网页面填写投资人角色信息"""
    bodySMS = {"requestKey": "", "bizType": "REGISTER", "mobile": ""}
    bodySMS['requestKey'] = Location
    bodySMS['mobile'] = tel_num
    """发送短信验证码"""
    SMS = requests.post(url=xw_url.smsForEnterprise, data=bodySMS, verify=False)
    if SMS.json()['status'] == 'SUCCESS':
        logger.info("====发送新网短信成功：" + SMS.json()['message'])
        """新网个人注册绑卡"""
        personalRegisterbody = {
            "serviceType": "BANKCARD_AUTH",
            "realName": "",
            "credType": "PRC_ID",
            "idCardNo": "110108199203221114",
            "maskedCredNum": "11010**********114",
            "bankcardNo": "6222020203021504245",
            "branchName": "",
            "branchNo": "",
            "mobile": "16832191335",
            "smsCode": "000000",
            "smsCount": "",
            "password": "js12345678 ",
            "confirmPassword": "js12345678",
            "maskPassword": "",
            "randomNumPass": "",
            "maskPasswordAgain": "",
            "randomNumPassAgain": "",
            "requestKey": ""
        }
        z = random.random() * 100
        personalRegisterbody['realName'] = Message_body['realName']
        personalRegisterbody['idCardNo'] = Message_body['idCardNo']
        personalRegisterbody['maskedCredNum'] = Message_body['idCardNo']
        personalRegisterbody['bankcardNo'] = data1['bankcardNo']
        personalRegisterbody['mobile'] = tel_num
        personalRegisterbody['smsCount'] = str(int(z))
        personalRegisterbody['requestKey'] = bodySMS['requestKey']
        headers2 = {"content-type": "application/x-www-form-urlencoded"}
        requests.post(url=xw_url.personalRegisterExpand, data=personalRegisterbody, headers=headers2,
                      verify=False)

        """查询新网用户情况"""
        url1 = public_way.zhilian_url
        reqData = {
            "platformUserNo": str(platformUserNo),
            "timestamp": public_way.current
        }
        sign = public_way.getSHA1Sign(reqData)
        data = public_way.getCommonData("QUERY_USER_INFORMATION", reqData, sign)
        requests.packages.urllib3.disable_warnings()
        result_data = requests.post(url=url1, data=data, verify=False).json()
        if result_data['auditStatus'] == "PASSED":
            logger.info("====查询新网开通投资人角色成功：" + str(result_data).replace("'", '"'))
            """查询轻易贷是否接到回调"""
            n = 0  # 尝试查询次数，此为程序处理异步回调缓冲
            time.sleep(3)
            xw_usermodel_callback_sql = 'SELECT * FROM xw_usermodel_callback WHERE request_no="' + str(
                requestNo) + '";'
            xw_usermodel_callback = mysqldb('qyddb_QA').selectsql(xw_usermodel_callback_sql)
            while n <= 3:
                if xw_usermodel_callback != None:
                    logger.info("====新网回调成功====" + str(xw_usermodel_callback))
                    break
                else:
                    logger.debug("----等待新网回调----")
                    xw_usermodel_callback_sql = 'SELECT * FROM xw_usermodel_callback WHERE request_no="' + str(
                        requestNo) + '";'
                    xw_usermodel_callback = mysqldb('qyddb_QA').selectsql(xw_usermodel_callback_sql)
                    time.sleep(3)
            m = 0
            xw_user_role_sql = 'select * from xw_user_role where  user_role="INVESTOR" AND user_id=(select id from user where tel_num="' + str(
                tel_num) + '");'
            xw_user_role = mysqldb('qyddb_QA').selectsql(xw_user_role_sql)
            while m <= 3:
                if xw_user_role != None:
                    logger.info("====轻易贷开通投资人角色成功====" + str(xw_user_role))
                    break
                else:
                    logger.debug("----等待轻易贷开通投资人角色----")
                    xw_user_role_sql = 'select * from xw_user_role where  user_role="INVESTOR" AND user_id=(select id from user where tel_num="' + str(
                        tel_num) + '");'
                    xw_user_role = mysqldb('qyddb_QA').selectsql(xw_user_role_sql)
                    time.sleep(3)
            logger.info("开通成功" + str(tel_num))
            logger.info("返回结果：" + str(result_data))
            user_sql = 'select * from user where tel_num="' + str(tel_num) + '";'
            user = mysqldb('qyddb_QA').selectsql(user_sql)
            logger.info("user表结果：" + str(user[0]))

        else:
            logger.error("----新网开通投资人角色失败----")
            logger.info("返回结果："+str(result_data['auditStatus']))

regular(register.register(),"js123456")
