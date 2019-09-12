#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from lib.MySQLHelper import MySQLHelper

headers = {"Content-type": "application/json"}

"""
复制模板
"""

class checkUserRole(unittest.TestCase):
    """demoKJ------Jmelody"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************接口开始****************")
        infoUrl = "/entrance/qyduser/checkUserRole"
        caseNum = tx['test_name']
        caseName = tx['test_description']
        userRole = tx['userRole']
        status = tx['status']
        successful = tx['successful']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        """代码逻辑"""
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(checkUserRole, "checkUserRole", "caseExcel.xlsx", "sheetName")