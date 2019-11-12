import random,uuid
from lib.log import logger
import operator
""""计数，排序
sorted(dic.items(),key,reverse),
Counter,
list.count('value')
"""
a=[1,2,3,44,55,22,3,4,22]
"""排序，默认升序
a.sort()
#若要降序，可取反
a.reverse()"""
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
# func(a)
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