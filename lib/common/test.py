import random
from lib.common.getUserName import GetUserName
from lib.common import register

#randrange生成5位随机数
def demorandrange():
    tel_num = "a" + str(random.randrange(10000, 99999))
    a=random.randrange(0,100)
    print(tel_num,a)


def user_name():
    user_name=GetUserName.full_name()
    print(user_name)
def test():
    tel_num=register.register()
    print(tel_num)

test()