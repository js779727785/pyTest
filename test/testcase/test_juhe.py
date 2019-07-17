from lib.log import logger
import requests
import unittest
from config.demoUrl import base_url
from lib.common.DemoLogin import qydFrontLogin

headers = {"Content-type": "application/json"}
class juhe(unittest.TestCase):
    def setUp(self) -> None:
        logger.info("*"*10+"start")

    def test_gethomeuserinfo(self):
        gethomeuserinfourl="/nbigfront/nw/entrance/apis/register/gethomeuserinfo/json"
        url=base_url+gethomeuserinfourl
        data={"imei":"867401041413693","edition":"new"}
        token=qydFrontLogin('16803581610','js12345678')
        logger.info("token:"+token)
        headers['X-Auth-Token']=token
        logger.info(headers['X-Auth-Token'])
        r=requests.post(url=url,json=data,headers=headers)
        o=requests.post(url=url+"old",json=data,headers=headers)
        response=r.json()
        old=o.json()
        logger.info("response:"+str(response))
        logger.info("old:"+str(old))
        self.assertEqual(response['mapData'],old['mapData'])

    def tearDown(self) -> None:
        logger.info("***end***")