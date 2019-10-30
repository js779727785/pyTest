import uuid,requests,hashlib
from lib.log import logger
from config.demoUrl import base_url

"""
模拟系统撤资
    按照余额,YY持有,处理中,QY持有,处理中顺序,来系统撤资
    直接调取userid的系统撤资,保证user余额为0,且有持有资产,手动传入lockAmount,unpledgeAmount传0
    存在处理中驳回时,在mt_job中跟踪驳回日志:
    grep 'orderNo' qyd_mt.* -C30 | grep '可驳回金额' -C20
    grep '34e7ad2d-ce41-451b-ae30-7be74fddbfd7' qyd_mt.* -C50 | grep '可用余额' -10
    grep '34e7ad2d-ce41-451b-ae30-7be74fddbfd7' qyd_mt.* -C30 | grep '可驳回金额' -C20 | grep 'rejectAmount' -C10
"""
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

"""轻盈交易明细接口
    https://wiki.kaiyuan.net/pages/viewpage.action?pageId=25528688
"""
def getDetailByTransactionId(transactionId):
    url_info=base_url+"/entrance/mt/getDetailByTransactionId/json"
    data={'transactionId':transactionId,'page':1,'size':10}
    reponse=requests.post(url=url_info,json=data)
    print(reponse)
    re_json=reponse.json()
    logger.info("查询QY交易明细结果："+str(re_json))

# unpledgelock('100',0,'46ec6a17-e920-4afe-85dd-da2a2080ee82')
unpledgelock('20',0,'46ec6a17-e920-4afe-85dd-da2a2080ee82')
# getDetailByTransactionId("094b5b58-554a-4d71-93f3-eaa399fb0db3")