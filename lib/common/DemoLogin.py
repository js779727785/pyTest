import base64
import requests
import json
from config import url
from lib.log import logger

headers = {"Content-Type": "application/json"}


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

"""账号密码登录新接口"""
def qydFrontLogin(phone, password):
    queryUrl = "/entrance/qyduser/checkauthorizationloginnew/json"
    auth = phone + ":" + password
    authorization = "Basic " + base64.b64encode(auth.encode(encoding="utf-8")).decode (encoding='utf-8')
    data = {"authorization":authorization,"loginWay":1,"channel":1,"deviceId":"201f49e3a65054aa4b5781e6ed183996","deviceName":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    logger.info("*******账号密码登录新接口请求数据：" + str(data))
    r = requests.post(url=url.base_url+queryUrl, json=data, headers=headers)
    result = r.json()
    logger.info("*******账号密码登录新接口返回数据：" + str(result))
    if result['successful'] is True:
        logger.info("xAuthToken返回数据："+str(result['entity']['xAuthToken']))
        return result['entity']['xAuthToken']
    return ""

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

# qydFrontLogin('16820060113','che001')
qydFrontLogin('16803584422','js123456')
# qydFrontLogin('16803585376','js123456')
# qydManageLogin()

# login_backed()