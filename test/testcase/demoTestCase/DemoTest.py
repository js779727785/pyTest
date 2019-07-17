import json
import random
import unittest
from lib.generateTestCases import __generateTestCases
import requests

from config import interface_user_url, xw_url
from lib.common.DemoLogin import qydFrontLogin
from lib.log import logger

class getCommonCodeImage(unittest.TestCase):
    def setUp(self) -> None:
        logger.info("setUp")

    def getTest(self,testdata):

        headers = {"Content-type": "application/json"}
        requests.packages.urllib3.disable_warnings()
        if testdata["flag"]==0:
            tel_num = json.loads(testdata['X-Auth-Token'])['tel_num']
            headers["X-Auth-Token"] = qydFrontLogin(tel_num, "js123456")

        info = json.JSONDecoder().decode(testdata['params'])
        requests.packages.urllib3.disable_warnings()
        r = requests.post(xw_url.Companyiscompleted, headers=headers, json=info, verify=False)
        result = r.json()
        if str(result["successful"]) == str(True):
            result_hasCompleted = json.loads(testdata['code'])['hasCompleted']
            self.assertEqual(str(result["entities"][0]['hasCompleted']), str(result_hasCompleted))
            result_hasBankCardInfo = json.loads(testdata['code'])['hasBankCardInfo']
            print(testdata["tc_num"], "\n预期结果：\n", testdata["remark"], "\n实际结果:\n", result["entities"][0])
            self.assertEqual(str(result["entities"][0]['hasBankCardInfo']), str(result_hasBankCardInfo))

        else:
            print(testdata["tc_num"], "\n预期结果：\n", testdata["remark"], "\n实际结果:\n", result["resultCode"]["message"])
            self.assertEqual(str(result["resultCode"]["code"]), str(testdata["code"]))

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("tearDown")

__generateTestCases(getCommonCodeImage,"getCommonCodeImage","usermodel.xlsx","querybanklistbyservice")
