from lib.log import logger
import requests,random
from config.url import qydregisterPhotoUrl,qydregisterSendMsgUrl,qydregisterUrl


headers = {"Content-type": "application/json"}
def register():
    """注册用户"""
    tel_num = "1680358" + str(random.randrange(1000, 9999,4 ))
    logger.info("申请注册的手机号为："+tel_num)
    a = random.randint(0, 100)
    validateKey = str(a)
    """图形验证码校验"""
    url_info = qydregisterPhotoUrl + str(a)[:2]
    print(url_info)
    imgParm={"validateKey":validateKey,"originType":"PC","platform":"qyd","purpose":"register"}
    imgre=requests.post(url=url_info,json=imgParm)
    logger.info("图形验证码返回结果:"+str(imgre))
    """发送短信验证码校验"""
    sms_body = {"validateKey": validateKey, "type": "1", "telNum": tel_num, "autoCode": "0000", "businessType": 1,
     "originType": "PC", "platform": "qyd", "purpose": "register"}
    rep= requests.post(url=qydregisterSendMsgUrl,json=sms_body).json()
    print(rep)
    logger.info("发送短信验证码返回结果："+str(rep))
    if str(rep['successful']) == "True":
        """注册"""
        password='js123456'
        payPassword='js12345678'
        body = {"validateKey":validateKey,"telNum":tel_num, "phoneCheckNo": "0000",
                "payPassword": payPassword, "password":password }
        regrep=requests.post(url=qydregisterUrl,json=body)
        print(regrep)
        regrep_json = regrep.json()
        if str(regrep_json['successful'])=='True':
            logger.info("注册返回结果："+str(regrep_json))
            logger.info("注册成功："+tel_num+","+password)
            return tel_num


register()