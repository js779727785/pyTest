"""新网查询直连接口：通用参数，签名计算"""
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
import base64
import time
import os


zhilian_url = "https://hubk.lanmaoly.com/bha-neo-app/lanmaotech/service"
gateway_url = "https://hubk.lanmaoly.com/bha-neo-app/lanmaotech/gateway"
current = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))


# 获取新网直连通用请求参数
def getCommonData(serviceName, reqData, sign):
    param = {
        "serviceName": serviceName,
        "platformNo": "6000003832",
        "reqData": str(reqData),
        "keySerial": "1",
        "sign": sign
    }
    return param


# 私钥签名
def sign_string(private_key_path, unsigned_string):
    # 开始计算签名
    key = RSA.importKey(open(private_key_path).read())
    signer = PKCS1_v1_5.new(key)
    signature = signer.sign(SHA.new(unsigned_string.encode("utf8")))
    # base64 编码，转换为unicode表示并移除回车
    sign = base64.encodebytes(signature).decode("utf8").replace("\n", "")
    return sign


# 给json串签名
def getSHA1Sign(reqdata):
    sign = sign_string(os.path.dirname(os.path.abspath(__file__))+"/privatekey.pem", str(reqdata))
    return sign