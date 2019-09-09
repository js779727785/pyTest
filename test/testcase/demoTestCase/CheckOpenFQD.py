#coding=utf-8
import unittest
from lib.generateTestCases import __generateTestCases
from lib.ifcertDataQuery import queryLoanForBorrowerIsCompany, queryLoanForBorrowerIsPerson, queryLoanAmountIsInteger, \
    queryLoanAmountIsDecimal, queryIfcertLoanInfo, queryIfcertLoanStatus, queryIfcertProductInfo
from lib.log import logger


headers = {"Content-type": "application/json"}


"""
分期贷开标应急中心数据检查
"""


class CheckOpenFQD(unittest.TestCase):
    """分期贷开标应急中心数据检查---李竹梅"""
    def setUp(self):
        logger.info("*" * 80)

    def getTest(self, tx):
        logger.info("****************分期贷开标应急中心数据检查开始****************")
        caseNum = tx['test_name']
        caseName = tx['test_description']
        periods = tx['periods']
        userType = tx['userType']
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行开始********")
        if '整数' in caseName:
            loanInfos = queryLoanAmountIsInteger(periods)
        elif '小数' in caseName:
            loanInfos = queryLoanAmountIsDecimal(periods)
        elif userType == "Company":
            loanInfos = queryLoanForBorrowerIsCompany(periods)
        else:
            loanInfos = queryLoanForBorrowerIsPerson(periods)
        for i in range(loanInfos.__len__()):
            loanId = loanInfos[i]['loanId']
            logger.info("****************开始核对数据，标的号为："+loanId)
            # 核对散标信息
            self.checkIfcertLoanInfo(loanId, loanInfos[i])
            # 核对散标状态
            self.checkIfcertLoanStatus(loanId, loanInfos[i])
            # 核对产品信息
            self.checkIfcertProductInfo(loanId, loanInfos[i])
        logger.info("*******测试案例名称： TestCase" + caseNum + "_" + caseName + " 执行完毕********")
        logger.info("****************分期贷开标应急中心数据检查结束****************")

    """产品信息与轻易贷业务数据进行核对"""
    def checkIfcertProductInfo(self, loanId, loanInfo):
        productInfo = queryIfcertProductInfo(loanId)
        if productInfo is None:
            logger.info("****************Oh! My God!定时任务还没执行吧！！！****************")
            return
        # 产品发布时间
        self.assertEquals(loanInfo['openTime'], productInfo['financing_start_time'])
        # 产品名称
        self.assertEquals("众盈-分期贷"+loanInfo['loanCode'], productInfo['product_name'])
        # 预期年化利率
        self.assertEquals(0.090155, float(productInfo['rate']))
        # 最小年化利率
        # self.assertEquals(0.00, productInfo['min_rate'])
        # 最大年化利率
        # self.assertEquals(0.00, productInfo['max_rate'])
        # 产品期限
        self.assertEquals(loanInfo['term'], productInfo['term'])

    """散标状态进行核对"""
    def checkIfcertLoanStatus(self, loanId, loanInfo):
        # 检查存在初始公布的状态
        loanStatus = queryIfcertLoanStatus(loanId, 0)
        self.assertIsNotNone(loanStatus)
        self.assertEqual(loanInfo['openTime'], loanStatus['product_date'])
        # 检查存在筹标中的状态
        loanStatus = queryIfcertLoanStatus(loanId, 6)
        self.assertIsNotNone(loanStatus)
        self.assertEqual(loanInfo['openTime'], loanStatus['product_date'])

    """散标信息与轻易贷业务数据进行核对"""
    def checkIfcertLoanInfo(self, loanId, loanInfo):
        ifcertLoan = queryIfcertLoanInfo(loanId)
        if ifcertLoan is None:
            logger.info("****************Oh! My God!定时任务还没执行吧！！！****************")
            return
        # 借款人
        self.assertEquals(loanInfo['userId'], ifcertLoan['user_id'])
        # 开标时间
        self.assertEquals(loanInfo['openTime'], ifcertLoan['product_start_time'])
        # 散标名称
        self.assertEquals("分期贷"+loanInfo['loanCode'], ifcertLoan['product_name'])
        # 借款用户证件号hash值
        # self.assertEquals(loanInfo['openTime'], ifcertLoan['user_idcard_hash'])
        # 借款用途
        if loanInfo['userType'] == "Company":
            self.assertEquals(2, ifcertLoan['loan_use'])
            # 借款说明
            self.assertEquals("企业流动资金借款", ifcertLoan['loan_describe'])
        else:
            self.assertEquals(1, ifcertLoan['loan_use'])
            # 借款说明
            self.assertEquals("个人非日常大件物品消费，如家具、家装等", ifcertLoan['loan_describe'])
        # 借款年利率
        self.assertEquals(0.090155, float(ifcertLoan['loan_rate']))
        # 借款金额
        self.assertEquals(float(loanInfo['loanAmount']), float(ifcertLoan['amount']))
        # 剩余借款本金
        self.assertEquals(0, ifcertLoan['surplus_amount'])
        # 借款期限
        self.assertEquals(loanInfo['term'], ifcertLoan['term'])
        # 还款类型
        self.assertEquals(2, ifcertLoan['pay_type'])
        # 获取借款的总服务费
        totalFee = float(loanInfo['fees'].split('},{')[0].split(':')[-1][1:-1])
        self.assertEquals(totalFee, float(ifcertLoan['service_cost']))
        # 借款类型
        self.assertEquals(1, ifcertLoan['loan_type'])
        # 担保方式
        self.assertEquals(-1, ifcertLoan['security_type'])
        # 担保公司数量
        self.assertEquals(0, ifcertLoan['security_company_amount'])
        self.assertEquals(None, ifcertLoan['security_company_name'])
        self.assertEquals(None, ifcertLoan['security_company_idcard'])
        self.assertEquals(None, ifcertLoan['is_financing_assure'])
        self.assertEquals(None, ifcertLoan['security_amount'])
        # 散标来源
        self.assertEquals("轻易贷，借款端仍为轻易贷（轻易科技有限公司）", ifcertLoan['project_source'])

    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(CheckOpenFQD, "CheckOpenFQD", "ifcertData.xlsx", "众盈开标数据检查")
