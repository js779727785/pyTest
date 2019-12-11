#coding=utf-8
import unittest
import requests
from lib.generateTestCases import __generateTestCases
from lib.log import logger
from config import hm_pyq_url


##发布朋友圈
class ApiV3FriendFeedAdd(unittest.TestCase):
    """发布朋友圈-Jmelody"""
    def setUp(self):
        logger.info("*" * 80)
    def getTest(self,data):
        logger.info("***************网关请求发布朋友圈开始****************")
        case = data['case']
        num=data['tc_num']
        name=data['tc_name']
        code=int(data['code'])
        phone=data['phone']
        password=data['password']
        logger.info(num + "_" + name + "_" + case)
        content=data['content']
        type=data['type']
        resource=data['resource']
        at = data['at']
        cover = data['cover']
        video = data['video']
        Authorization = hm_pyq_url.get_hmsc_token(phone, password, case)
        headers=hm_pyq_url.get_hmlt_header(self)
        # headers = {}
        headers['Authorization']="Bearer "+Authorization
        params = {"content": content, "type": type, "resource": resource, "at": at, "cover": cover, "video": video}
        if num=="t_001":#文字朋友圈正常
            params = {"content": content, "type": type}
        if num=="t_002" :##图片朋友圈正常（图片id假）
            params = {"content": content, "type": type, "resource": resource}
            params['type'] = "1"
        if num=="t_003":##视频朋友圈正常（视频id、视频封面id假）
            params = {"content": content, "type": type, "resource": resource, "cover": cover, "video": video}
            params['type'] = "2"
        if num=="t_004":#文字朋友圈at单人正常
            params = {"content": content, "type": type, "at": at}
            params['type'] = "0"
        if num=="t_005" :##文字朋友圈at多人正常
            params = {"content": content, "type": type, "at": at}
            params['type'] = "0"
            params['at'] = "458a4bfb-0a23-4a88-94f0-04f899930ba1,e10fcde9-a18b-46c1-8634-b6b7d4293582"
        if num=="t_006":##文字朋友圈token为空
            headers['Authorization'] = ""
        if num=="t_007":#文字朋友圈token不存在
            headers.pop("Authorization")
        if num=="t_008" :##文字朋友圈content为空
            params = {"content": content, "type": type}
            params['content'] = ""
        if num=="t_009":##文字朋友圈content不存在
            params = {"content": content, "type": type}
            params.pop("content")
        if num=="t_010":#文字朋友圈type为空
            params = {"content": content, "type": type}
            params['type'] = ""
        if num=="t_011" :##文字朋友圈type不存在
            params = {"content": content, "type": type}
            params.pop("type")
        if num=="t_012":##文字朋友圈有图片id
            params = {"content": content, "type": type, "resource": resource}
        if num=="t_013":#图片朋友圈无图片id
            params = {"content": content, "type": type}
            params['type'] = "1"
        if num=="t_014" :##图片朋友圈视频id和视频封面id
            params = {"content": content, "type": type,"resource": resource, "cover": cover, "video": video}
            params['type'] = "1"
        if num=="t_015":##视频朋友圈无视频id和封面id
            params = {"content": content, "type": type}
            params['type'] = "2"
        if num=="t_016":#视频朋友圈有视频id无封面id
            params = {"content": content, "type": type, "resource": resource, "video": video}
            params['type'] = "2"
        if num=="t_017" :##视频朋友圈无视频id有封面id
            params = {"content": content, "type": type, "cover": cover}
            params['type'] = "2"
        if num=="t_018":##视频朋友圈传图片id
            params = {"content": content, "type": type, "resource": resource}
            params['type'] = "2"
        if num=="t_019":#文字朋友圈at单人id错误
            params = {"content": content, "type": type, "at": at}
            params['type'] = "0"
            params['at'] = "123456"
        if num=="t_020" :##文字朋友圈at多人中文逗号隔开
            params = {"content": content, "type": type, "at": at}
            params['type'] = "0"
            params['at'] = "458a4bfb-0a23-4a88-94f0-04f899930ba1，e10fcde9-a18b-46c1-8634-b6b7d4293582"
        if num=="t_021" :##文字朋友圈type为1（非0）
            params = {"content": content, "type": type}
            params['type'] = "1"
        if num=="t_022":##文字朋友圈type为2（非0）
            params = {"content": content, "type": type}
            params['type'] = "2"
        if num=="t_023":#文字朋友圈type为3（非0）
            params = {"content": content, "type": type}
            params['type'] = "3"
        logger.info(headers)
        logger.info(params)
        requests.packages.urllib3.disable_warnings()
        res = requests.post(hm_pyq_url.get_hmlt_base_url(case)+hm_pyq_url.api_v3_friendFeed_add, json=params, headers=headers,verify=False)
        logger.info(res.text)
        result = res.json()
        logger.info("*******返回数据： " + str(result))
        self.assertEqual(result['code'],code)
        logger.info("****************网关请求发布朋友圈结束****************")
    @staticmethod
    def getTestFunc(arg1):
        def func(self):
            self.getTest(arg1)
        return func

    def tearDown(self):
        logger.info("*" * 80)

__generateTestCases(ApiV3FriendFeedAdd, "api_v3_friendFeed_add",  "api_hm_pyq.xlsx", "发布朋友圈")
