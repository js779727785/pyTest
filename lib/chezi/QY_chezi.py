import  requests
from lib.common.DemoLogin import qydFrontLogin
from lib.common.subminToken import subminToken
from config.demoUrl import qyd_url
from lib.log import logger

"""轻盈撤资"""
def QY_chezi(phone,pwd,Stramount,productType):
    urlInfo="/entrance/mt/withdrawInvestment/json"
    token = qydFrontLogin(phone, pwd)
    headers = {"Content-type": "application/json", "X-Auth-Token": token}
    "submintToken"
    submitToken = subminToken(phone,pwd)
    # productType="XZY"
    amount=Stramount
    # {"amount":"1","terminal":"00","accessesFlag":"0","submitToken":"736fb660-150a-4f38-ba08-6e57ba7a6f92","productType":"QY"}
    parm={"amount":amount,"terminal":"00","accessesFlag":"0","submitToken":submitToken,"productType":productType}
    response= requests.post(url=qyd_url+urlInfo,json=parm,headers=headers)
    re=response.json()
    # print(re)
    logger.info("请求结果："+str(re))
#轻盈
QY_chezi('16803581611','js123456','1','QY')
# QY_chezi('16803581611','js123456','1.5','QY')
# QY_chezi('16803581611','js123456','2','QY')