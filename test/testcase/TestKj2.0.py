#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
headers = {"Content-Type": "application/json"}

"""
统一风格的模板，author：Jmelody
文件命名：api_post_qyd_http_nbigfront_entrance_newmt_XX_json.py
接口文档：
getZyBackMoneyPlan
api_post_qyd_http_nbigfront_web_accessionlist_json.py
"""
class InstanseName(unittest.TestCase):
    """demo接口-Jmelody"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************demo接口开始****************")
        infoUrl = qyd_base_url + "/nbigfront/"
        caseNum = tx['tc_num']
        caseName = tx['test_description']
        tel_num = tx['tel_num']
        password = tx['password']
        productType = tx['productType']
        flag=tx['flag']
        code = int(tx['code'])
        token = qydFrontLogin(tel_num, password)
        headers = {"Content-Type": "application/json", "X-Auth-Token": token}
        data = {"productType": productType}
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        logger.info("请求参数：" + str(data) + "headers:" + str(headers))
        reponse = requests.post(url=infoUrl, json=data, headers=headers)
        reponse_json = reponse.json()
        # print(reponse_json)
        logger.info("请求接口返回结果:" + str(reponse_json))
        self.assertEqual(reponse_json['code'], code)
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************demo接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(InstanseName, "instanseName", "api_qyd.xlsx", "sheetName")
