#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from config.demoUrl import dfb_url


headers = {"Content-type": "application/json"}


"""
JD查询企业信息
"""


class queryQy(unittest.TestCase):
    """JD查询企业信息---Jmelody"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************JD查询企业信息接口开始****************")
        infoUrl = "/jd/credit/getEntBaseInfo"
        caseNum = tx['test_name']
        caseName = tx['test_description']
        enterpriseName = tx['enterpriseName']
        ssoId =tx['ssoId']
        platform =tx['platform']
        code = tx['code']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        if caseNum == '002':
            enterpriseName=''
        logger.info("*******测试数据： " + str(enterpriseName))
        test_url=dfb_url+infoUrl+"?enterpriseName="+enterpriseName+"&ssoId="+ssoId+"&platform="+platform
        logger.info("*******测试url： " + str(test_url))
        r = requests.get(url=test_url, headers=headers)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        logger.info("*******requests结果code:  "+str(result['code'])+"     ,预期结果： "+tx['code'])
        self.assertEqual(code, str(result['code']))
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************JD查询企业信息接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(queryQy, "queryQy", "demo.xlsx", "JD查询企业信息")
