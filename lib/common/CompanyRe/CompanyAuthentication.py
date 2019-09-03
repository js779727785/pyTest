import json
import requests
import random
from config import xw_url
from lib.log import logger
from lib.common import register,IDcard,DemoLogin
from lib.common.getUserName import GetUserName


"""企业开通存管第一步:注册+提交审核并审批通过----Jmelody"""
def companyauthentication(tel_num):
    if tel_num is not None:
        logger.info("******注册手机号码：" + str(tel_num))
        """企业实名认证"""
        logger.info(" 企业实名认证开始...")
        token_no = DemoLogin.qydFrontLogin(tel_num,"js123456")
        headers1 = {
            "Content-Type": "application/json; charset=UTF-8", "X-Auth-Token": token_no
        }
        """组装参数"""
        body_cp = { "type":"1",
                    "bankCord":"ICBC",
                    "bankCard":"6222020706029352246",
                    "bankName":"中国工商银行",
                    "bankBranch":"中国工商银行股份有限公司北京知春路支行",
                    "bankCity":"北京市",
                    "bankProvince":"北京市",
                    "contactName":"沈痛",
                    "contactTelNum":"16803588396",
                    "bankLicense":"110101196109251220",
                    "bankLicensePath":"f33d559c-caeb-11e9-b7a0-0242ac143f11",
                    "legalFacePath":"f33d559c-caeb-11e9-b7a0-0242ac143f11",
                    "legalBackPath":"f33d559c-caeb-11e9-b7a0-0242ac143f11",
                    "companyName":"荆测试卜耳的企业",
                    "legalName":"汪以克",
                    "legalCode":"110101197801087919",
                    "registCode":"516602399718941902",
                    "businessPath":"f33d559c-caeb-11e9-b7a0-0242ac143f11"}
        body_cp["companyName"] = "荆测试" + str(GetUserName.full_name()) + "的企业"
        body_cp["legalName"] = str(GetUserName.full_name())
        body_cp["contactName"] = str(GetUserName.full_name())
        body_cp["bankCard"] = "622202070602" + str(random.randrange(1000000, 9999999, 7))
        body_cp["registCode"] = str(random.randrange(100000000000000000, 999999999999999999, 18))
        body_cp["legalCode"] = str(IDcard.getRandomIdNumber())
        body_cp["contactTelNum"] = str(tel_num)
        body_cp["contactIdentity"] = str(IDcard.getRandomIdNumber())
        body_cp["bankLicense"] = "J" + str(random.randrange(1000000, 9999999, 7))
        logger.info("实名传参："+str(body_cp))
        """实名认证提交信息"""
        Refercompany = requests.post(url=xw_url.Companyauthentication,json=body_cp,headers=headers1)
        Refercompany_json=Refercompany.json()
        logger.info("响应数据:"+str(Refercompany))
        """垫付宝后台进行企业审核：认领任务"""
        if Refercompany_json['successful'] == True:
            logger.info("====轻易贷实名信息提交成功====,return手机号为:"+str(tel_num))
            return tel_num
        else:
            logger.error("轻易贷实名信息提交失败")
    else:
        logger.error("手机号传入错误!!!!")


# companyauthentication(register.register())

