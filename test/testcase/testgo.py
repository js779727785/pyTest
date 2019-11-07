import random,uuid
import datetime,requests
from lib.mysql.userQuery import queryOldPossessionInfo
from lib.mysql.divestmentAndBuy import queryAssign,queryTranaction
from lib.log import logger
import requests,random
from config.url import qydregisterPhotoUrl,qydregisterSendMsgUrl,qydregisterUrl
from lib.MySQLHelper import MySQLHelper
"""斐波那契数列"""
def func(n):
    if n==1 or n==2:
        return 1
    else:
        return func(n-1)+func(n-2)

a={1,2,3,44,55,22,3,4,22}
"""冒泡排序并统计次数"""
def func(a):
    count=0
    for i in range(len(a)-1):
        for j in range(len(a)-i-j):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count+=1
    return a,count

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

def checkGetMany1(self):
    """第一种get_many结果的断言语句可以直接拿返回结果，用checkPossessionData判断"""
    items=requests(url="",json="",header="")
    resultInfo=queryAssign
    self.checkPossessionData(resultInfo, items)
def checkGetMany2(self):
    """第二种get_many在返回结果前在sql中for循环取结果"""
    items = requests(url="", json="", header="")
    resultInfo = queryAssign
    """注意以下对List循环提取写法"""
    if resultInfo is not None or resultInfo.__len__()>0:
        for i in range(resultInfo.__len__()):
            self.assertEquals(resultInfo[i]["sqlStatus"], testdata[0]['exceptStatus'])
def gogo():
    """用python编程，从屏幕上输入一个字符串，将这个字符串里面所有不同的字符提取出来，放在一个字符数组里面"""
    str = 'today I will go home'
    list = []
    for i in str:
        print(str.count(i))
        if str.count(i) == 1:
            list.append(i)
    print(list)
def howtoUuid():
    orderNo = uuid.uuid4()
    """生成的uuid必须转化为字符串才能打印"""
    print("orderNo:" + str(orderNo))
def imgCheck():
    a = random.randint(0, 100)
    url_info = qydregisterPhotoUrl + str(a)[:2]
    print(url_info)
    imgParm={"validateKey":"01","originType":"PC","platform":"qyd","purpose":"register"}
    imgre=requests.post(url=url_info,json=imgParm)
    print(imgre)
    logger.info("图形验证码返回结果:"+str(imgre))


def queryConfireLoan(self):
    sql_info = "select id from qydproduction.mt_loan where STATUS=%s order by create_time desc limit 2;"
    response = MySQLHelper('qydproduction').get_many(sql_info,"CONFIRM")
    loanId=response[0]['id']
    print(loanId)

def checkType(self,tel_num,product_type):
     sql_info="SELECT * FROM qydnewproduction.mt_reinvestment WHERE user_id=(SELECT id from qydproduction.user where tel_num={}) and product_type='{}';".format(tel_num,product_type)
     response=MySQLHelper("qydnewproduction").selectsql(sql_info)
     rep=response[0]['product_type']
     res=response[0]['status']
     logger.info("a:{},B:{}".format(rep,res))
"""快速排序"""
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] +  quick_sort(greater)
# a = [23,33,44,12,55,12,8]
# print(quick_sort(a))

#老式快速排序
# def partition(arr, low, high):
#     i = (low - 1)  # 最小元素索引
#     pivot = arr[high]
#     for j in range(low, high):
#         # 当前元素小于或等于 pivot
#         if arr[j] <= pivot:
#             i = i + 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[high] = arr[high], arr[i + 1]
#     return (i + 1)
# # arr[] --> 排序数组
# # low  --> 起始索引
# # high  --> 结束索引
# # 快速排序函数
# def quickSort(arr, low, high):
#     if low < high:
#         pi = partition(arr, low, high)
#         quickSort(arr, low, pi - 1)
#         quickSort(arr, pi + 1, high)
# arr = [10, 7, 8, 9, 1, 5]
# n = len(arr)
# quickSort(arr, 0, n - 1)
# print("排序后的数组:")
# for i in range(n):
#     print("%d" % arr[i])
#
# def quick_sort(lis):
#     if len(lis)<2:
#         return lis
#     else:
#         tem=lis[0]
#         max= [i for i in range(lis[1:]) if i>tem]
#         less=[i for i in range(lis[1:]) if i<tem ]
#     return quick_sort(less)+[tem]+quick_sort(max)
"""九九乘法表"""
def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}*{}={}\t".format(j,i,i*j),end="")
        print()
def listDemo(lis):
    """list[start:end:step]
    """
    lis = [1, 2, 3, 4, 5, 6, 7, 8]
    "步长为2,跳跃式取值"
    print(lis[::2])
    print(lis[:2])
    "取值为字符"
    print(lis[0])
    "取值为list"
    print(lis[:1])
    "去除最后一个元素"
    print(lis[:-1])
    print(lis[3:-1])
    "翻转list"
    print(lis[::-1])
    "取从下标为3的元素翻转读取"
    print(lis[3::-1])
    print(lis[2::-2])
    print(lis[6::-2])
listDemo(a)

