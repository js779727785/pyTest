
"""计数，排序
https://www.cnblogs.com/dyl01/p/8563550.html
sorted(dic.items(),key,reverse),
Counter,
list.count('value')
"""
a=[1,2,3,44,55,22,3,4,22]
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
# func(a)
"""快速排序"""
def quick_sort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i < pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] +  quick_sort(greater)
a = [23,33,44,12,55,12,8]
# print(quick_sort(a))
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
import operator
x = sorted(dic.items(),key =operator.itemgetter(0))
print(d)

