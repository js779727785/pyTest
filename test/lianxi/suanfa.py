"""list.insert(index, obj)
index -- 对象 obj 需要插入的索引位置。
obj -- 要插入列表中的对象。
demo:
已知一个队列,如： [1, 3, 5, 7], 如何把第一个数字，放到第三个位置，得到：
[3, 5, 1, 7]
"""
a=[1,2,3,4]
a.insert(2,a[0])
# print(a[1::])
"""
完全数：第一个完全数是 6，它有约数 1、2、3、6，除去它本身 6 外，其余3 个数相加
求 1000 以内的完全数有哪些？
"""
def wanquan():
    a=[]
    for i in range(1,1001):
        re=0
        for j in range(1,i):
            if i%j==0&j<i:
                re+=j
        if re==i:
            print(i)
            a.append(i)
    return a


"""打印出 100-999 所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数
字立方和等于该数本身。例如：153 是一个"水仙花数"，因为 153=1 的三次方＋
5 的三次方＋3 的三次方。"""
def func():
    lis=[]
    for i in range(100,1000):
        re=0
        m=list(str(i))
        for j in m:
            re+=int(j)**len(m)
        if re==i:
            lis.append(re)
    return lis
# print(func())
"""n的阶乘 n!即 n=3 3*2*1"""
from functools import reduce
# def jiecheng(n):
#     if n==1:
#         return n
#     else:
#         return n*jiecheng(n-1)
def digui(n):
    re=reduce(lambda x,y:x*y,range(1,n+1))
    return re
# print(digui(3))
"""斐波那契数列
已知一个数列：1、1、2、3、5、8、13、。。。。的规律为从 3 开始的每一项都
等于其前两项的和，这是斐波那契数列。求满足规律的 100 以内的所以数据"""
def fu():
    a=0
    b=1
    while b<100:
        print(b,end=',')
        a,b=b,a+b
# fu()
"""计算 x 的 n 次方，如：3 的 4 次方 为 3*3*3*3=81"""
def fn(x,n):
    if n==0:
        return 1
    else:
        return x*fn(x,n-1)
# print(fn(3,4))
