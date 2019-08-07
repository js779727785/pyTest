import  requests
from lib.common.DemoLogin import qydFrontLogin
from config.demoUrl import qydGetsubmitTokenUrl
from lib.log import logger

def subminToken(phone,pwd):
    data = {}
    token = qydFrontLogin(phone, pwd)
    headers = {"Content-type": "application/json", "X-Auth-Token": token}
    submitToken = requests.post(url=qydGetsubmitTokenUrl, json=data, headers=headers).json()
    # print(submitToken)
    # logger.info("submitToken为"+str(submitToken['entities'][0]['submitToken']))
    return submitToken['entities'][0]['submitToken']

# subminToken('16803581611','js123456')