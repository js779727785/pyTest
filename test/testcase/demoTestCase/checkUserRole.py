#coding=utf-8
import unittest
import requests
from Config.url import base_url as qyd
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from lib.userDataQuery import getSsoIdByCheckUserRole, getSsoIdByCheckUserRoleNotInXW, getSsoIdByBestsignBlack, \
    getSsoIdByBestsignBlackNotIn

headers = {"Content-type": "application/json"}


"""
判断用户身份
"""


class checkUserRole(unittest.TestCase):
    """判断用户身份---李竹梅"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************判断用户身份接口开始****************")
        infoUrl = "/entrance/qyduser/checkUserRole"
        caseNum = tx['test_name']
        caseName = tx['test_description']
        userRole = tx['userRole']
        status = tx['status']
        successful = tx['successful']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        logicalDel = 0
        if status == -1:
            logicalDel = 1
        if userRole == "GUARANTOR" and status in (0, -1):
            userInfo = getSsoIdByBestsignBlack(logicalDel)
        elif userRole == "GUARANTOR" and status == 1:
            userInfo = getSsoIdByBestsignBlackNotIn()
        elif userRole in ('INVESTOR', 'BORROWERS') and status == 0:
            userInfo = getSsoIdByCheckUserRoleNotInXW(userRole)
        elif userRole in ('INVESTOR', 'BORROWERS') and status in (4, 1, -1):
            userInfo = getSsoIdByCheckUserRole(logicalDel, userRole, status)
        else:
            userInfo = {}
        if userInfo is None:
            return
        ssoId = userInfo['ssoId']
        data = {"ssoId": ssoId, "userRole": userRole}
        logger.info("*******测试数据： " + str(data))
        r = requests.post(url=qyd+infoUrl, json=data, headers=headers)
        result = r.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(successful, bool(result['successful']))
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************判断用户身份接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(checkUserRole, "checkUserRole", "userData.xlsx", "判断用户身份")
