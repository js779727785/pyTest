import base64
import requests
import json
from config import url
from lib.log import logger




def qydManageLogin():
    """轻易贷管理台登录"""
    logger.info("qydManageLogin login is running...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
        "Content-Type": "application/json; charset=UTF-8",
        "Connection": "keep-alive"
    }
    requests.packages.urllib3.disable_warnings()
    r=requests.get(url.qydManageLoginUrl,headers=headers,verify=False)
    result=r.json()
    logger.info(result['data']['token'])
    return result['data']['token']

def qydFrontLogin(username,passwd):
    # u"""轻易贷前端登录"""#备注，如果不同设备登录的话需要验证码验证登录，这块逻辑复杂暂时没有写
    # headers = {"Content-Type": "application/json"}
    # requests.packages.urllib3.disable_warnings()
    # token = base64.b64encode((username+":"+passwd).encode("utf-8"))
    # data = 'Basic %s' % token
    # data=data.replace("'","").replace("b","")
    # print(data)
    # body={  "loginWay":1,
    #         "channel":1,
    #         "deviceId":"c13a03ae13eefce4abc366dd64784179",
    #         "deviceName":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    #         }
    # body["authorization"]=data
    # data_json = json.dumps(body)
    # r=requests.post(url=url.qydFrontLoginUrl,data=data_json,headers=headers,verify=False)
    # result=r.json()
    # logger.info("轻易贷前端登录获取token..："+str(result['entities'][1]['xAuthToken']))
    # return result['entities'][1]['xAuthToken']
    u"""轻易贷前端登录"""
    headers = {"Content-Type": "application/json"}
    requests.packages.urllib3.disable_warnings()
    token = base64.b64encode((username+":"+passwd).encode("utf-8"))
    data = 'Basic %s' % token
    data=data.replace("'","").replace(" b"," ")
    body={}
    body["authorization"]=data
    data_json = json.dumps(body)
    r=requests.post(url=url.qydFrontLoginUrl11,data=data_json,headers=headers,verify=False)
    result=r.json()
    logger.info(result)
    logger.info("轻易贷前端登录获取token..："+str(result['entities'][0]['xAuthToken']))
    return result['entities'][0]['xAuthToken']


#qydFrontLogin('16820060113','che001')
# qydFrontLogin('16803581610','js12345678')
# qydManageLogin()