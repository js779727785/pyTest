#coding=utf-8
import unittest
import requests
from config.demoUrl import qyd_url
from lib.generateTestCases import __generateTestCases
from lib.log import logger


headers = {"Content-type": "application/json","X-Auth-Token":"FaUHf9-j-Wu2Itq4d7OsJbW6UsfnCFuuST1KkLK2obM-"}


"""
债券收购
"""


class updateAssignIsBuy(unittest.TestCase):
    """债券收购---Jmelody"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************债券收购接口开始****************")
        infoUrl = "/backend-qyd/divestmentAndBuy/updateAssignIsBuy"
        caseNum = tx['test_name']
        caseName = tx['test_description']
        transactionId = tx['transactionId']
        id = tx['id']
        status = tx['status']
        parms = {"transactionId":transactionId,"id":id}
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        if caseNum=="002":
            parms = {"id": id}


        if caseNum=="003":
            parms = {"transactionId": transactionId}
        logger.info("*******测试数据： " + str(parms))
        test_url = qyd_url + infoUrl
        logger.info("*******测试url： " + str(test_url))
        r = requests.post(url=test_url, json=parms,headers=headers)
        print(r)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(status, bool(result['status']))


        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************债券收购接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(updateAssignIsBuy, "updateAssignIsBuy", "demo.xlsx", "债券收购")
