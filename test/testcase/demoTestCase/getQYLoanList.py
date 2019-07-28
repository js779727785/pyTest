# -*- coding: utf-8 -*-
# Author:LiJingjing
import os,sys
import requests
import json
import unittest
from config import sencondmarket_url
from lib.generateTestCases import __generateTestCases
from lib.log import logger
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

"""通过该demo来学习直接在excel中写好成行的params时，提取的写法"""
class getQYLoanList(unittest.TestCase):

    def setUp(self):
        logger.info("getQYLoanList case is start to run ")

    def getTest(self,testdata):

        headers={"Content-Type":"application/json"}
        caseNum=testdata['test_name']
        caseTitle=testdata['case_title']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseTitle + " 执行开始********")
        info=json.JSONDecoder().decode(testdata['params'])
        logger.info("请求参数："+ str(info))
        requests.packages.urllib3.disable_warnings()
        result=requests.post(headers=headers,url=sencondmarket_url.getQYLoanList,json=info,verify=False).json()
        logger.info("相应结果："+ str(result))
        if result['successful']==True:
            self.assertEquals(str(result['pageSize']),str(info['pageSize']))
        else:
            self.assertEquals(str(result['resultCode']['code']),str(testdata['code']))
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseTitle + " 执行结束********")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func


    def tearDown(self):
        logger.info("getQYLoanList case end to run ")


# 类名称，用例别名，数据文件名，sheet名称
__generateTestCases(getQYLoanList, "getQYLoanList", "secondmarket.xlsx", "getQYLoanList")

if __name__ == "__main__":
    unittest.main(verbosity=1)



