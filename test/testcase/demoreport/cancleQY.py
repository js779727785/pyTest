#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from lib.MySQLHelper import MySQLHelper
from lib.common.DemoLogin import qydFrontLogin
from lib.common.subminToken import subminToken
from config.demoUrl import qyd_url

headers = {"Content-type": "application/json"}

"""
取消撤资
"""

class Test_cancleQY(unittest.TestCase):
    """取消撤资------Jmelody"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************Test_cancleQY接口开始****************")
        urlInfo = "/entrance/mt/cacleAssign/json"
        caseNum = tx['test_name']
        caseName = tx['test_description']
        phone = tx['phone']
        pwd=tx['pwd']
        status = int(tx['status'])
        # successful = tx['successful']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        """代码逻辑"""
        sql_info = "select * from mt_assignment where user_id=(select id from user where tel_num=%s) and `status`='OPEN' and (amount-already_amount-match_amount)!=0 ORDER BY create_time desc;"
        query_info = MySQLHelper("qydproduction").get_many(sql_info, phone)
        logger.info("撤资数据:" + str(query_info))
        if query_info is not None and query_info.__len__() > 0:
            assignIds = []
            for i in range(query_info.__len__()):
                query_res = query_info[i]
                assignId = query_res['id']
                amount = query_res['amount']
                already_amount = query_res['already_amount']
                match_amount = query_res['match_amount']
                cancleAmount = (amount - already_amount - match_amount) / 10000
                logger.info("撤资中assignId：" + str(assignId) + "  ，可驳回金额：" + str(cancleAmount))
                assignIds.append(assignId)
            logger.info("assignIds:" + str(assignIds))
            token = qydFrontLogin(phone, pwd)
            headers = {"Content-type": "application/json", "X-Auth-Token": token}
            "submintToken"
            submitToken = subminToken(phone, pwd)
            # demoParams="{"assignIds":"198a40bc-835f-4aaf-9d00-3b0d94a1c1e1","submitToken":"099c679e-9bd8-42e5-a747-ec54e91694cc"}"
            parm = {"assignIds": assignIds[0], "submitToken": submitToken}
            response = requests.post(url=qyd_url + urlInfo, json=parm, headers=headers)
            re = response.json()
            logger.info("请求结果：" + str(re))
            self.assertEqual(status,re['status'])
        else:
            logger.info("无处理中的撤资数据！！！")


        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************Test_cancleQY接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(Test_cancleQY, "Test_cancleQY", "demo.xlsx", "Test_cancleQY")
