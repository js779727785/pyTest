
"""计数，排序
https://www.cnblogs.com/dyl01/p/8563550.html
sorted(dic.items(),key,reverse),
Counter,
list.count('value')
"""

"""排序，默认升序
a.sort()
#若要降序，可取反
a.sort(reverse=True)
"""
# print(a)
"""冒泡排序并统计次数"""
def func(a):
    count=0
    for i in range(len(a)-1):
        for j in range(len(a)-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                count+=1
    return a,count
# print(func(a))
"""快速排序"""
def quick_sort(arr):
    if len(arr) < 2: #注意这一步判断
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] +  quick_sort(greater)
a = [23,33,44,12,55,12,8]
print(quick_sort(a))
"""插入排序"""
def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print(insertionSort(arr))

"""
dict字典
dic.items()为('a', 2)
dic含义与dic.key()一样
dic含义与dic.key()一样
"""

dic = {'a':2,'b':1,'c':3}
#循环输出key,value
# for key,value in dic.items():
#     print("key：{},value：{}".format(key,value))
#字典的key-values互换
z={value:key for key,value in dic.items()}
# print(z)
d = sorted(dic,key = lambda k:k[0])
# print(d)

#字典排序
de={'a': 3, 'e': 1, 'n': 1, 'b': 1, 's': 2, 'c': 1, 'd': 1}
#按value排
re1=sorted(de.items(),key=lambda x:x[1],reverse=True) #默认从小到大，加reverse取反从大到小
#按key排
re2=sorted(de.items(),key=lambda x:x[0])

import operator
x = sorted(dic.items(),key =operator.itemgetter(0))
# print(d)
lis=['a','b','b','c','a','b','d','d','d','d']

#按出现次数排序，取出出现最多的
def ff(lis):
    from collections import Counter
    re=Counter(lis)
    # print(re)
    # print(re.most_common())
    rr=max(re.keys(),key=re.get)
    return rr
# print(ff(lis))

# dic = {'a':2,'b':1,'c':3}
# re=max(dic.keys(),key=dic.get)
# # print(re)
lis=[1,1,2,3,3,3,3,4,-1,2,-3]
from collections import Counter
co=Counter(lis)
re=sorted(co.keys(),key=co.get,reverse=True)
print(re)
# re=list(filter(lambda x:x%2==1,lis))
# print(re)
lis2=[1,2,3]
lis3=['a','b','c','d']
# re=[[x,y] for i,x in enumerate(lis2) for y in lis[i]]
re2=[i for i in zip(lis2,lis3)]
# print(re)
# print(re2)
i=1234
re=list(str(i))
# print(re)

#两个list合并为字典
rrr=dict(zip(lis2,lis3))
