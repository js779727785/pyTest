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

"""垫付宝管理台登录"""
def login_backed():
    username = "admin"
    password = "che001"
    auth = username + ":" + password
    headers = {"Content-Type": "application/json",
                   "authorization": "Basic " + base64.b64encode(auth.encode(encoding="utf-8")).decode(encoding='utf-8')}
    head = requests.get(url=url.host_admin_login, headers=headers)
    """学习用以下response.headers['X-Auth-Token']去提取响应中header的内容"""
    head_json=head.json()
    logger.info(str(head_json))
    if(head_json['status']==200):
        logger.info("登录成功,token:" + str(head.headers['X-Auth-Token']))
        return head.headers['X-Auth-Token']

"""轻易贷运营平台登录"""
def login_yy():
    body = {"username": "16816000029", "password": "che001"}
    data_json = json.dumps(body)
    # logger.info("请求数据为：" + str(data_json))
    headers = {"Content-Type": "application/json"}
    """请求体用data传入数据"""
    r = requests.post(url = qydYunyingTokenUrl, data=data_json, headers=headers, verify=False)
    result = r.json()
    # logger.info("返回数据为" + str(result))
    return result["entities"][0]["token"]


#qydFrontLogin('16820060113','che001')
# qydFrontLogin('16803581600','js123456')
# qydManageLogin()

# login_backed()