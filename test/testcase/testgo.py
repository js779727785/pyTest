import random
import datetime,requests
from lib.mysql.userQuery import queryOldPossessionInfo
from lib.mysql.divestmentAndBuy import queryAssign,queryTranaction
def testgo():
    """二者之间的随机数"""
    # str(random.randrange(10000000, 99999999))
    r = random.randrange(10,200)
    print(r)
    return r
def randomInt():
    a= random.randint(0,100)
    print(a)
    return a
def nowtime():
    # 获取当前时间 格式为 20170101000000
    currentTime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    print(currentTime)
    return  currentTime
def demomanysql(param):
    possessionInfo=queryOldPossessionInfo(param)
    print(possessionInfo)
    possLen = possessionInfo.__len__()
    print(possLen)

def checkGetMany1():
    """第一种get_many结果的断言语句可以直接拿返回结果，用checkPossessionData判断"""
    items=requests(url="",json="",header="")
    resultInfo=queryAssign
    self.checkPossessionData(resultInfo, items)
def checkGetMany2():
    """第二种get_many在返回结果前在sql中for循环取结果"""
    items = requests(url="", json="", header="")
    resultInfo = queryAssign
    """注意以下对List循环提取写法"""
    if resultInfo is not None or resultInfo.__len__()>0:
        for i in range(resultInfo.__len__()):
            self.assertEquals(resultInfo[i]["sqlStatus"], testdata[0]['exceptStatus'])