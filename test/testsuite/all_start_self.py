# -*- coding: utf-8 -*-

# import unittest
# import time
# import sys
#
# import os
#
# basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# sys.path.append(basedir)
#
# from lib.HTMLTestRunner3 import HTMLTestRunner
# from lib import send_email
# from lib.log import logger
#
#
# def all_cases_starter():
#     suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase/', pattern='*.py')
#     # unittest.defaultTestLoader(): defaultTestLoader()类，通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（test*.py），
#     # 并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover。
#     # unittest.TextTestRunner(verbosity=2).run(suite)
#     with open(basedir + "/report/APIGatewayReport.html", "wb") as fp:
#         runner = HTMLTestRunner(
#             stream=fp,
#             title='API网关自动化测试报告',
#             description='API网关自动化测试报告'
#         )
#         runner.run(suite)
#     time.sleep(1)
#     send_email.send_mail_report("*****API网关自动化测试报告*****")

# if __name__ == "__main__":
#     logger.info("Start to run test cases!!!")
#     all_cases_starter()
#     logger.info("Finish all test cases!!!")

import unittest
import time
import os.path
import sys
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(basedir)
from lib import HTMLTestRunner3
from lib import send_email


"""unittest.defaultTestLoader(): defaultTestLoader()类，
通过该类下面的discover()方法可自动根据测试目录start_dir匹配查找测试用例文件（test*.py），
并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover"""
#suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase/', pattern='*.py')
suite = unittest.defaultTestLoader.discover(basedir + '/test/testcase/demoreport', pattern='*.py')

filePath = basedir + "/report/APIGatewayReport.html"
fp = open(filePath, 'wb')

"""生成报告的Title,描述"""
#runner = HTMLTestRunner3.HTMLTestRunner(stream=fp, title='API网关自动化测试报告', description='API网关自动化测试报告')
runner = HTMLTestRunner3.HTMLTestRunner(stream=fp, title='demoreport自动化测试报告', description='demoreport——description')
runner.run(suite)
fp.close()
# unittest.TextTestRunner(verbosity=2).run(suite)
time.sleep(3)
#send_email.send_mail_report("*****API网关自动化测试报告*****")
send_email.send_mail_report("*****demoreport自动化测试报告*****")
