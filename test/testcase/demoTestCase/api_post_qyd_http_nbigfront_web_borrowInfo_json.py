#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases2
from lib.log import logger
from config.url import  qyd_base_url
from  lib.common.DemoLogin import qydFrontLogin
headers = {"Content-Type": "application/json"}

##我要出借页面聚合接口
class BorrowInfo(unittest.TestCase):
    """我要出借页面聚合接口-Jmelody"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************我要出借页面聚合接口开始****************")
        infoUrl = qyd_base_url+"/nbigfront/web/borrowInfo/json"
        caseNum = tx['tc_num']
        caseName = tx['test_description']
        tel_num=tx['tel_num']
        password=tx['password']
        productType=tx['productType']
        code = int(tx['code'])
        flag=int(tx['flag'])
        print(flag)
        token=qydFrontLogin(tel_num,password)
        headers = {"Content-Type": "application/json","X-Auth-Token":token}
        if caseNum=='009':
            headers = {"Content-Type": "application/json"}
        data = {"productType": productType}
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        logger.info("请求参数："+str(data)+"headers:"+str(headers))
        reponse = requests.post(url=infoUrl, json=data, headers=headers)
        reponse_json = reponse.json()
        print(reponse_json)
        logger.info("请求接口返回结果:" + str(reponse_json))
        self.assertEqual(reponse_json['code'], code)
        if caseNum=='001':
            self.assertEqual(reponse_json['dataList']['QYRemainAmount']['code'], code)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        if caseNum=='002':
            self.assertEqual(reponse_json['dataList']['XYYRemainAmount']['code'], code)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        if caseNum=='003':
            self.assertEqual(reponse_json['dataList']['XZYRemainAmount']['code'], code)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        if caseNum=='004':
            self.assertEqual(reponse_json['dataList']['QYBRemainAmount']['code'], code)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        if flag=='1':
            self.assertEqual(reponse_json['dataList']['appointmentStatus']['code'], code)
            logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************我要出借页面聚合接口结束****************")

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases2(BorrowInfo, "borrowInfo","api_qyd.xlsx", "我要出借页面聚合接口")