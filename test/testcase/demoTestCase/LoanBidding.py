#交易网关投标接口
import unittest
import uuid
import requests
import json
import  random
import time
from config import url
from lib.MySQLHelper import MySQLHelper
from lib.generateTestCases import __generateTestCases
from lib.mysqldb import mysqldb
from lib import OpenLoanUtil
from lib.log import logger


class loanbidding(unittest.TestCase):
    """投标接口---吴小琴"""
    @classmethod
    def setUp(self):
        logger.info("=====投标用例执行开始=====")

    def getTest(self, tc):
        requests.packages.urllib3.disable_warnings()
        params = json.JSONDecoder().decode(tc['params'])
        loanid =str(uuid.uuid4())
        params['borrowerId']=tc['borrower_id']
        params['loanId']=loanid
        params['principal']=tc['open_loan_amount']
        params['lenderId']=tc['lender_id']
        params['orderNo']=str(uuid.uuid4())
        print(params)
        qyd_order = 'select * from QydOrder where outOrderNo="'+str(params["orderNo"]) + '"'
        #result = MySQLHelper("qydproduction").get_one(sql, params)

        print(qyd_order)


    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func


__generateTestCases(loanbidding, "loanbidding", "Transfer.xlsx", "交易网关投标接口")