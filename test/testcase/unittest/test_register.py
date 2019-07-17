from lib.log import logger
import requests,random
import unittest
from config.url import qydregisterPhotoUrl,qydregisterSendMsgUrl,qydregisterUrl

headers = {"Content-type": "application/json"}
class register(unittest.TestCase):
    def setUp(self) -> None:
        logger.info("*"*10+"start")

    def test_register(self):
        """注册用户"""
        tel_num = "168552" + str(random.randrange(10000, 99999, 5))
        print(tel_num)
        a = random.randint(0, 100)
        validateKey = str(a)
        """图形验证码校验"""
        imgre=requests.get(url=qydregisterPhotoUrl + str(a)[:2])
        # result=r.json()
        # logger.info("result:"+str(result))
        """发送短信验证码校验"""
        sms_body = {"validateKey": validateKey, "type": "1", "telNum": tel_num,
                    "autoCode": "0000", "businessType": 1}
        rep= requests.post(url=qydregisterSendMsgUrl,json=sms_body).json()
        print(rep)
        print(rep['successful'])
        self.assertEqual(str(rep['successful']),"True")
        """注册"""
        password='js123456'
        body = {"validateKey":validateKey,"telNum":tel_num, "phoneCheckNo": "0000",
                "payPassword": "js12345678", "password":password }
        regrep=requests.post(url=qydregisterUrl,json=body).json()
        print(regrep)
        self.assertEqual(str(regrep['successful']),"True")
        logger.info("注册成功："+tel_num+","+password)





    def tearDown(self) -> None:
        logger.info("***end***")