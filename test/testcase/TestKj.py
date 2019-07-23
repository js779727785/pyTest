import time
import unittest
import json
import requests

from lib import mysqldb
from lib.log import logger
from lib.generateTestCases import __generateTestCases

"""框架大纲可以查看该demo，实际写test_case的class可以直接复制demoTestCase中的模板进行改写"""
class TestKj(unittest.TestCase):
    def setUp(self):
        logger.info('SetUp*******')

    def getTest(self,testdata):
        #将excel中的数据提取为json
        data = json.JSONDecoder().decode(testdata)
        print(data)
        #先定义传参格式：在excel中写好取；或者代码里写好模板
        parm=data['parm']
        logger.info("Test Start:"+testdata["casename"])
        #对模板的参数值进行重写,也可能根据不同的tel_num做判断来写不同的传参
        newstr=''
        data["someStr"]= newstr
        #请求本次测试的核心接口
        r = requests.post(url="config.apiurl",json=data)
        """这个地方有时候在requests内会加：verity=Flase，原因参考：https://www.jianshu.com/p/5bb96ddfbdc8
        ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1056)"""
        respones =r.json()
        print(respones)
        # 校验接口请求响应成功。self.assertEqual(respones['code'],code)
        logger.info("接口返回reponse："+respones)
        time.sleep(5)
        #返回结果进行业务断言
        if testdata["test_num"]=="001":
            """"print在断言前，这样能看清异常时所产生的输出"""
            print("reponse[0]['status']"+respones[0]['status'],"testdata['exceptStatus']:"+testdata['exceptStatus'])
            """直接判断返回结果是否符合预期"""
            self.assertEquals(respones[0]['status'],testdata['exceptStatus'])
            """依照结果的参数查库表，将查到的结果做断言"""
            testsql = "select * from QydOrder where outOrderNo='"+respones["outOrderNo'"]
            sqlresult = mysqldb("paycenter").selectsql(testsql)
            print("sqlresult"+sqlresult,"testdata['exceptStatus']:"+testdata['exceptStatus'])
            self.assertEquals(sqlresult[0]["sqlStatus"],testdata[0]['exceptStatus'])
        elif testdata["test_num"]=="002":
            """同样的"""
            self.assertEquals(respones[0]['status'], testdata['exceptStatus'])
        """校验json中每一项的key，value是否符合预期"""
        # #以下为例子
        # jsondemo = {"borrowData": borrowData,
        #         "operationData": operationData}
        # #请求结果的response格式如下
        # response ={"entity": entity,
        #         "entities": [entities]}
        # #把要比较的业务数据提取出来
        # entity = response[entity]
        # entities =response[entities][0]
        # for key in jsondemo.keys():
        #     self.assertEqual(jsondemo['key'],entity[key])
        #     self.assertEqual(jsondemo['key'],entities[key])


    def tearDown(self):
        logger.info('*********tearDown')

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)

        return func


__generateTestCases(TestKj,"TestKj","data.xlsx","sheet")