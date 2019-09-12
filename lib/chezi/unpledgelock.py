import uuid,requests,hashlib
from lib.log import logger
from config.demoUrl import base_url

"""直接调取userid的系统撤资,保证user余额为0,且有持有资产,手动传入lockAmount,unpledgeAmount传0"""
def unpledgelock(lockAmount, unpledgeAmount, userId):
    headers = {"Content-type": "application/json"}
    pledgeUrl = "/loan/pledge/unpledgelock"
    key = "72eg204a595f117fc17fe58gg9d33fd56d20b2d2e9f97c5a92c8e141129e2727"
    orderNo = str(uuid.uuid4())
    signEnc = md5Encode(orderNo + orderNo + lockAmount + userId + "HKYW" + key)
    data = {"sign": signEnc,
            "orderNo": orderNo,
            "lockId": orderNo,
            "lockAmount": lockAmount,
            "unpledgeAmount": unpledgeAmount,
            "userId": userId,
            "businessType": "HKYW",
            "subType": "FQD_HKYW",
            # "list": [{"subOrderNo": "XZYnewpledge7631230_01"}]}
            "list": []}
    logger.info("*******调用质押撤资接口请求数据：" + str(data))
    r = requests.post(url=base_url + pledgeUrl, json=data, headers=headers)
    result = r.json()
    logger.info("*******调用质押撤资接口返回数据：" + str(result))
    return result
def md5Encode(str):
    m = hashlib.md5(str.encode(encoding='utf-8'))
    return m.hexdigest()