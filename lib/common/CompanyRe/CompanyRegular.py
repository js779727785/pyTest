from lib.common.CompanyRe import BackendVerity
from lib.common.CompanyRe import checkCompany, CompanyAuthentication, dakuan,XwCheck
from lib.common import register

"""开通企业投资人存管账号"""
def companyRegular():
    tel_num=register.register()
    CompanyAuthentication.companyauthentication(tel_num)
    # tel_num='16803589912'
    BackendVerity.bankedVerity(tel_num)
    dakuan.dakuan(tel_num, '3')
    checkCompany.checkCompany(tel_num)
    XwCheck.XwCheckUi(tel_num)

companyRegular()