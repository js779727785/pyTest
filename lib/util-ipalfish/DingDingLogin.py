import hashlib
import hmac
import time
from base64 import b64encode
from urllib import parse

import requests

from DataFactoryBackend.settings import APPID, APPSECRET
from util.common import dict_data


class DingManage():
    def signature(self, code):
        """
        hmacsha256算法
        :param code:
        :return:
        """
        appkey = APPSECRET  # miyao

        # hmac_sha256加密
        signature = hmac.new(bytes(appkey, encoding='utf-8'), bytes(code, encoding='utf-8'),
                             digestmod=hashlib.sha256).digest()

        # 二进制转为HEX
        HEX = str(b64encode(signature), encoding='utf-8')
        return HEX

    def get_ding_config(self):
        """
        获取钉钉配置
        :param request:
        :return:
        """
        app_id = APPID
        return dict_data(ret=1, data=app_id)

    def dingding_login(self, **kwargs):
        """
        钉钉登录
        :param request:
        :return:
        """

        timestamp = str(int(time.time() * 1000))
        stamp = parse.quote(self.signature(timestamp))
        response = requests.post(
            url='https://oapi.dingtalk.com/sns/getuserinfo_bycode?signature={}&timestamp={}&accessKey=dingoaxxd6gmzeinac7jpz'.format(
                stamp, timestamp), json={
                "tmp_auth_code": kwargs['code']}
        )
        return response

