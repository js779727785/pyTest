import requests
import uuid
import time
from config import url
from lib.log import logger
import random
from lib.mysqldb import mysqldb
import datetime


# 交易网关开标，返回loanID
def openLoan(userid, loanid, borrtotamt,*args):
    data = {
        "callbackUrl": "/entrance/mt/paycenterCallBack/json",
        "context": {
            "pathType": "openLoan"
        },
        "orderId": "16f1e2ae-8df4-4a9d-beff-3092e6b7c14e",
        "userId": userid,
        "loanId": loanid,
        "loanType": "YY",
        "borrTotAmt": borrtotamt,
        "bidName": "XFD398332",
        "bidType": "01",
        "yearRate": "8.10",
        "retInterest": "666",
        "retFee": "0",
        "loanPeriod": "30",
        "loanPeriodUnit": "day",
        "retType": "01",
        "retDate": "20180523",
        "openTime": "2018-04-23 08:00:10"
    }

    """如果C为false的话走老开标流程"""

    if len(args) >=1:
        if args[0] =="false":
            data.update(entrustUserId="00000000-0000-0000-0000-000000000003")
        else:
            data.update(entrustedType="PERSONAL")
            data.update(entrustUserId="9d9b01f7-17b1-4263-b89e-9f921b846d15")
    else:
        data.update(entrustUserId="00000000-0000-0000-0000-000000000003")
    data['userId'] = "a544d7d5-c004-46a5-85a9-3f184ecc1ea3"
    data['orderId'] = str(uuid.uuid4())
    data['bidName'] = "XFDD" + str(random.randrange(10000000, 99999999, 7))
    # logger.info("*******调用交易网关投标请求数据： " + str(data))
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=url.gateway_openloan, json=data, verify=False).json()
    logger.info("*******调用交易网关开标返回数据*******： " + str(r))
    return data['loanId']


# 交易网关投标接口返回账务锁定id和新网冻结id
def loanbidding(userid, loanid, borrtotamt, lenderId):
    data = {
        "authId": "",
        "borrowerId": userid,
        "callbackUrl": "/entrance/xsb/payLoanCallback/json",
        "context": {},
        "description": "一级市场投标",
        "doLock": "true",
        "ext1": "",
        "ext2": "",
        "lenderId": lenderId,
        "loanId": loanid,
        "lockId": "null",
        "orderNo": "a99af5bd-5137-4cf6-aa5d-52bf3b40f440",
        "orderType": "TRANSFER_IN",
        "principal": borrtotamt,
        "subOrderType": "BUY_YY",
        "transactionTime": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "yearRate": "8.10",
        "productType": "YY"
    }
    data['orderNo'] = str(uuid.uuid4())
    data['lockId'] = str(uuid.uuid4())
    # logger.info("*******调用交易网关投标请求数据： " + str(data))
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=url.gateway_loanbidding, json=data, verify=False).json()
    time.sleep(4)
    qyd_order = 'select * from QydOrder where outOrderNo="' + str(data['orderNo']) + '"'
    order_data = mysqldb("paycenter").selectsql(qyd_order)
    if r['message'] == "接受成功" and str(order_data[0]['status']) == "1":
        logger.info("*******调用交易网关投标返回数据*******： " + str(r))
        dic = {'orderNo': data['orderNo'], 'lockId': data['lockId']}
        print("dic is -----", dic)
        return dic
    else:
        return "投标失败，请重试"


# 交易网关放款接口
def loaninterface(userid, loanid, borrtotamt, lenderId, buyerLockId, freezeRequestNo):
    data = {
        "amount": borrtotamt,
        "borrowUserId": userid,
        "callbackUrl": "/entrance/mt/paycenterCallBack/json",
        "context": {
            "pathType": "qyFkLoan"
        },
        "entrustAccountExt1": "YY_QYD_2_DFB",
        "entrustAccountExt2": "月盈转账到垫付宝",
        "entrustDescription": "月盈借款人放款",
        "entrustOpponentAccountExt1": "YY_QYD_2_DFB",
        "entrustOpponentAccountExt2": "月盈收款",
        "entrustedUserId": "00000000-0000-0000-0000-000000000003",
        "loans": [{
            "accountGuidExt1": "",
            "accountGuidExt2": "",
            "amount": borrtotamt,
            "bizType": 0,
            "buyerLockId": buyerLockId,
            "description": "一级市场募集转账",
            "freezeRequestNo": freezeRequestNo,
            "opponentAccountGuidExt1": "",
            "opponentAccountGuidExt2": "消费贷",
            "outUsrId": lenderId,
            "transId": "3a2f02f6-e1ab-4028-9886-5ac605517526"
        }],
        "outOrderNo": loanid,
        "proId": loanid,
        "productType": "YY",
        "transCode": 3
    }
    data['loans'][0]['transId'] = str(uuid.uuid4())
    # logger.info("*******调用交易网关放款请求数据： " + str(data))
    requests.packages.urllib3.disable_warnings()
    r = requests.post(url=url.gateway_loaninterface, json=data, verify=False).json()
    time.sleep(5)
    qyd_order = 'select * from QydOrder where outOrderNo="' + loanid + '"'
    n=0
    while n<10:
        order = mysqldb("paycenter").selectsql(qyd_order)
        status = order[0]["status"]
        if str(status) == "1":
            logger.info("*******调用交易网关放款返回数据*******： " + str(r))
            break
        elif str(status) != "1" and n <= 8:
            logger.info("等待交易网关处理 ……5s")
            time.sleep(5)
            n = n + 1
        else:
            logger.info("*******调用交易网关放款返回数据******：" + str(r))
            break


 # 交易网关修改标的状态接口
def updateloan_status(loanid):
    data_json = {
        "projectNo": loanid,
        "requestNo": str(uuid.uuid4()),
        "status": "REPAYING"
    }
    headers = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    result = requests.post(url=url.gateway_updateloanstatus, json=data_json, headers=headers, verify=False).json()
    if str(result['code']) == "10000":
        logger.info("*******调用交易网关修改标的状态返回数据*******： " + str(result))
    else:
        return "修改标的状态失败，请重试"


 # 交易网关冻结接口 bizType:normal/repay/withdraw  默认为normal锁余额，repay还款锁，withdraw提现锁
#还款前的冻结,parentTransactionGuid是业务系统的billingid，对应的是账务AccountLockfund，AccountLockfundFlows的字段
def account_frozen(borrower,amount):
    parentTransactionGuid=str(uuid.uuid4())
    data_json = {
        "parentTransactionGuid": parentTransactionGuid,
        "qydUserId": borrower,
        "doubleWrite":"true",
        "bizType":"repay",
        "subflows": [
            {
                "subTransactionGuid": str(uuid.uuid4()),
                "systemLock": "FROZEN",
                "amount": amount,
                "accountGuid_ext1": "ext1",
                "accountGuid_ext2": "ext2",
                "description": "冻结一些金额"
            }
  ]
}
    headers = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    print("params:",data_json)
    result = requests.post(url=url.gataway_accountLock, json=data_json, headers=headers, verify=False).json()
    if str(result['code']) == "10000":
        logger.info("*******调用交易网关冻结账户的金额*******： " + str(result))
        return  parentTransactionGuid
    else:
        logger.info("*******调用交易网关冻结失败，原因如下******： " + str(result))



#新众盈、月盈还款预处理
def paycenter_prerepay(freezeRequestNo ,loanid,borrower):
    data_json = {
        "requestNo": str(uuid.uuid4()),
        "projectNo": loanid,
        "freezeRequestNo":freezeRequestNo,
        "bizType":"repay",
        "repayAmount":"3000",
        "repayInterest":"750",
        "interestCompensatoryUserNo":"VVVV",
        "compensatoryAmount":"7000",
        "compensatoryUserNo":"00000000-0000-0000-0000-000000000003",
        "borrowerUserNo":borrower,
        "transactionTime":datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        "orderType":"repay",
        "subOrderType":"",
        "remark":"代偿还款预处理",
}
    headers = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    print("params:", data_json)
    print("url:", url.gateway_prerepay)
    result = requests.post(url=url.gateway_prerepay, json=data_json, headers=headers, verify=False).json()
    if str(result['status']) == "10000":
        ordersql = "select * from QydOrder where outOrderNo='" + data_json["requestNo"] + "'"
        n = 0
        while n < 20:
            order = mysqldb("paycenter").selectsql(ordersql)
            status = order[0]["status"]
            if str(status) == "1":
                logger.info("*******调用交易网关还款预处理的金额*******： " + str(result))
                dir = {"repayInterest": data_json['repayInterest'], 'repayAmount': data_json['repayAmount'],
                       'compensatoryAmount': data_json['compensatoryAmount']}
                return dir
            elif str(status) != "1" and n<=18:
                logger.info("等待交易网关处理 ……10s")
                time.sleep(10)
                n = n + 1
            else:
                logger.info("*******调用交易网关还款预处理失败,请通过requestNo去查询******：" + str(data_json["requestNo"]))
                break

    else:
        logger.info("*******调用交易网关还款预处理失败，原因如下******： " + str(result))




# 交易网关还款转账接口
def tranferaccount(lenderId, loanid, borrtotamt):
    orderid = str(uuid.uuid4())
    data_json = {
        "callbackUrl": "/entrance/mt/paycenterCallBack/json",
        "context": {
            "mtLoanOrderId": str(uuid.uuid4()),
            "pathType": "yyTransfer",
            "loanId": loanid
        },
        "orderId": orderid,
        "bussinessOrderId": orderid,
        "transactionTime": str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')),
        "amount": str(int(borrtotamt) + 1),
        "transferType": "AA",
        "type": "TRANSFER",
        "subType": "TRANSFER_YY",
        "payerId": "00000000-0000-0000-0000-000000000003",
        "payeeId": lenderId,
        "payerFlowType": "TRANSFER",
        "payeeFlowType": "TRANSFER",
        "payerFlowDesc": "月盈垫付宝转入到轻易贷",
        "payeeFlowDesc": "月盈垫付宝转入到轻易贷",
        "description": "月盈垫付宝转入到轻易贷",
        "payerRole": "COLLABORATOR",
        "payeeRole": "BORROWERS"
    }

    headers = {
        "Content-Type": "application/json"
    }
    requests.packages.urllib3.disable_warnings()
    result = requests.post(url=url.gateway_tranferaccount, json=data_json, headers=headers, verify=False).json()
    if str(result['code']) == "10000":
        logger.info("*******调用交易网关还款转账返回数据*******：" + str(result))
    else:
        return "还款转账失败，请重试"

#loanid=openLoan("a544d7d5-c004-46a5-85a9-3f184ecc1ea3",str(uuid.uuid4()),"100000")
# dir=loanbidding("a544d7d5-c004-46a5-85a9-3f184ecc1ea3",loanid,"100000","7106b6b8-36a6-4f85-b99c-c2dc2e348838")
# loaninterface("a544d7d5-c004-46a5-85a9-3f184ecc1ea3",loanid,"100000","7106b6b8-36a6-4f85-b99c-c2dc2e348838",dir['lockId'],dir['orderNo'])
# updateloan_status(loanid):
# tranferaccount("a544d7d5-c004-46a5-85a9-3f184ecc1ea3", loanid, "100000")
#freezeRequestNo=account_frozen("a544d7d5-c004-46a5-85a9-3f184ecc1ea3","1")
#paycenter_prerepay(freezeRequestNo,"d9ad8a5e-5e96-43b5-9b17-d230fbc80ee2","a544d7d5-c004-46a5-85a9-3f184ecc1ea3")






