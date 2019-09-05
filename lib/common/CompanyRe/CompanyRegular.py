from lib.common.CompanyRe import BackendVerity
from lib.common.CompanyRe import checkCompany, CompanyAuthentication, dakuan
from lib.common.CompanyRe import XwCheck
from lib.common import register
"""开通企业投资人存管账号"""
def companyRegular():
    tel_num=register.register()
    # tel_num = '16803583276'
    CompanyAuthentication.companyauthentication(tel_num)
    BackendVerity.bankedVerity(tel_num)
    dakuan.dakuan(tel_num, '3')
    checkCompany.checkCompany(tel_num)
    XwCheck.XwCheckUi(tel_num)
companyRegular()