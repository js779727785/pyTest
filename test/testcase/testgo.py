import random,uuid
import datetime,requests
from lib.mysql.userQuery import queryOldPossessionInfo
from lib.mysql.divestmentAndBuy import queryAssign,queryTranaction
from lib.log import logger
import requests,random
import operator
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


def checkType(self,tel_num,product_type):
     sql_info="SELECT * FROM qydnewproduction.mt_reinvestment WHERE user_id=(SELECT id from qydproduction.user where tel_num='%s') and product_type='%s';"%(tel_num,product_type)
     print(sql_info)
     print("我叫%s，今年%d岁" % ('James', 12))
     print("我叫{}，今年{}岁".format('James', '12'))
# checkType('1',16803581611,'QYD')

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
    print(lis[3::-2])
    print(lis[6::-2])
# listDemo(a)

"""abs绝对值函数"""
def absdemo(n):
    print(abs(-1))
    print(abs(0))
    print(abs(n))
    return abs(n)
# absdemo(1)

"""map练习
https://blog.csdn.net/qq_29666899/article/details/88623026
map函数的原型是map(function, iterable, …)
"""
def mul(x):
    return x*x
def mul2(x,y):
    return x*y
n=[1,2,3,4,5]
c=[2,3,4,5,6]
re=map(mul,n)
res=map(mul2,n,c)
"""<map object at 0x000001F78B92A6D8>报错，原因：python3中map()返回iterators类型，不再是list类型。进行list转换即可"""
# print(list(re))
# print(list(res))
"""用lambd表达式简化"""
# print(list(map(lambda x:x**2,n)))
# print(list(map(lambda x,y:x*y,n,c)))

"""set函数
是一个无序不重复元素集
基本功能包括关系测试和消除重复元素.
"""
#1.消除重复
a=[2,3,5,1,2,3,2,3,4,5,3]
# print(set(a))
# print(list(set(a)))
#2.关系测试：
x=set('spam')
y=set(['h','a','m'])
z=set(['a','m'])
#交集。（&  或者 intersection）
# print(list(x&y))
#并集。（| 或者 union）
# print(list(x|y))
#差集。（- 或者 difference）
# print(list(x-y))
#反交集。 （^ 或者 symmetric_difference）即去重后再取交集
# print(list(x^y))
#子集与超集,issubset
# print(z<x)
#set中的增，删，查
#https://www.cnblogs.com/crazylover/p/9672833.html
set1=set({'jim','Jordan','Spider Man'})
set1.add('James')
set1.remove('jim')#如果元素不存在，移除时会报错
set1.discard('cc')#如果元素不存在，移除时不不不会报错
#随机删除集合的某一个元素
set1.pop()
#清空集合
set1.clear()

# print(set1)
# for i in set1:
    # print(i)

"""两个list去重之后取交集，返回list,注意返回是无序的，用sorted(list)进行排序或list.sort()"""
def setDemo(lis1,list2):
    lis= list(set(lis1)^set(list2))
    print(lis)
    return lis
a=[1,2,3,666,4,5]
b=[999,6,5,4,2,999,4,2,4,5,666,2]
# setDemo(a,b)
"""反交集并排序"""
def setDemo2(lis1,lis2):
    lis= sorted(list(set(lis1)^set(lis2)))
    print(lis)
    return lis
# setDemo2(a,b)
"""对数组元素出现个数计数"""
def countNum(lis,strValue):
    num=str(lis).count(strValue)
    print(num)
    return num
"""todo{}集合如何计数？？？？"""
# num=str(b).count('2')
# num=b.count(2)
# print(num)
# countNum(b,'2')


"""python将一个list去重并按出现次数从大到小排序"""
list_a = [1,2,3,4,5,6,1,1,1,2,2,3,4,4,5,5,5,5,6,6,6,6,6,6]
print("list_a: " + str(list_a) + '\n')

set_a = list(set(list_a))  # 去重得到一个集合
print("set_a: " + str(set_a) + '\n')

count_set_a = {}  # 存放元素和出现次数的字典，key为元素,value为出现次数
for item in set_a:
    count_set_a[item] = list_a.count(item)
print("count_set_a: " + str(count_set_a) + '\n')

# 将cou_set_a按value值排序，返回一个list，list中元素是形式为(1,4)的tuple，tuple[0]为键值，tuple[1]为出现次数
sorted_list_a = sorted(count_set_a.items(), key=operator.itemgetter(1))
print("sorted_list_a: " + str(sorted_list_a) + '\n')

result_a = []  # 存放最后的结果
for item in sorted_list_a[::-1]: # 按value值从大到小排序
    result_a.append(item[0])
print("result_a: " + str(result_a) + '\n')
