# -*- coding:utf-8 -*-
import hashlib
import random
import datetime

def getValidateCheckout(id17):
    '''获得校验码算法'''
    weight=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2] #十七位数字本体码权重
    validate=['1','0','X','9','8','7','6','5','4','3','2'] #mod11,对应校验码字符值

    sum=0
    mode=0
    for i in range(0,len(id17)):
        sum = sum + int(id17[i])*weight[i]
    mode=sum%11
    return validate[mode]


def getRandomIdNumber():
    '''产生随机可用身份证号，sex = 1表示男性，sex = 0表示女性'''
    #地址码产生
    addrInfo = "110101"#随机选择一个值,北京市东城区
    idNumber = str(addrInfo)
    #出生日期码
    start, end = "1960-01-01","2000-2-28" #生日起止日期
    days = (datetime.datetime.strptime(end, "%Y-%m-%d") - datetime.datetime.strptime(start, "%Y-%m-%d")).days + 1
    birthDays = datetime.datetime.strftime(datetime.datetime.strptime(start, "%Y-%m-%d") + datetime.timedelta(random.randint(0,days)), "%Y%m%d")
    idNumber = idNumber + str(birthDays)
    #顺序码
    for i in range(2):#产生前面的随机值
        n = random.randint(0,9)# 最后一个值可以包括
        idNumber = idNumber + str(n)
    # 性别数字码
    sexId = random.randint(1,2) #性别码
    idNumber = idNumber + str(sexId)
    # 校验码
    checkOut = getValidateCheckout(idNumber)
    idNumber = idNumber + str(checkOut)
    print(idNumber)
    return idNumber

def bankidCardNo():
    bankCard = "622202070302" + str(random.randrange(1000000, 9999999, 7))
    print(bankCard)
    return bankCard

# getRandomIdNumber()
# bankidCardNo()