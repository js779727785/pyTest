import  requests
from lib.common.DemoLogin import qydFrontLogin
from lib.common.subminToken import subminToken
from config.demoUrl import qyd_url
from lib.log import logger

"""新月/众盈撤资"""
def dinvestmentDo(phone,pwd,Stramount,productType):
    urlInfo="/entrance/newmt/dinvestmentDo/json"
    token = qydFrontLogin(phone, pwd)
    headers = {"Content-type": "application/json", "X-Auth-Token": token}
    "submintToken"
    submitToken = subminToken(phone,pwd)
    # productType="XZY"
    amount=Stramount
    # parm={"terminal":"00","submitToken":"1f16c18c-217f-4b94-b618-312c5e06b0ee","productType":"XZY","amount":"1"}
    parm={"terminal":"00","submitToken":submitToken,"productType":productType,"amount":amount}
    response= requests.post(url=qyd_url+urlInfo,json=parm,headers=headers)
    re=response.json()
    # print(re)
    logger.info("请求结果："+str(re))
#新众盈
dinvestmentDo('16803581611','js123456','1','XZY')
#新月盈
# dinvestmentDo('16803581611','js123456','1','XYY')
#月盈精选
# dinvestmentDo('16803581611','js123456','1','QYB')
