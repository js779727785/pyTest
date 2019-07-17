from lib.log import logger
import requests,random
from lib.common.DemoLogin import qydFrontLogin
from lib.common.getUserName import GetUserName
from lib.common import IDcard
from config.url import qydregisterPhotoUrl,qydregisterSendMsgUrl,qydregisterUrl
from  config.xw_url import NewPersonUrl

"""个人开通银行存管"""

def regular():
    """个人绑卡"""
    tel_num='16855262500'
    password='js123456'
    token =qydFrontLogin(tel_num,password)
    # token='2AJdf2aFa05gBJNbak3sXpkN3WJeexCfwl5iCO3Mjvhsq0Tkn5ZZ554C2C18A02qNOKHp'
    headers={"Content-Type": "application/json; charset=UTF-8", "X-Auth-Token": token}
    user_name=GetUserName.full_name()
    print(user_name)
    # body = {"realName": "到代", "idCardNo": "11010119600925431X", "bankcardNo": "6222020703025077248",
    #         "bankcode": "CMBC", "redirectUrl": "https://www.baidu.com"}
    idCardNo=IDcard.getRandomIdNumber()
    bankcardNo=IDcard.bankidCardNo()
    Message_body = {"realName": user_name, "idCardNo": idCardNo, "bankcardNo": bankcardNo, "mobile": tel_num,
                    "redirectUrl": "https://www.baidu.com",
                    "bankcode": "CMBC"}

    New_RegularRN = requests.post(url=NewPersonUrl,json=Message_body,headers=headers)
    # New_RegularRN_json =New_RegularRN.json()
    print(New_RegularRN)

regular()
