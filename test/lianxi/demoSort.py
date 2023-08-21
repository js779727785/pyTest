"""
数组中第tar大的字符
"""

lis=['b','a','a','a','d','d']

"""方法1"""
def fu1(lis):
    re={}
    for i in range(len(lis)):
        re[lis[i]]=re.get(lis[i],0)+1
    re=sorted(re,key=re.get,reverse=True)
    return re
"""方法2"""
from collections import Counter
re=Counter(lis)
re=sorted(re,key=re.get,reverse=True)
# re=max(re,key=re.get)


"""python将一个list按出现次数从大到小排序
https://blog.csdn.net/HuaCode/article/details/79763687
sorted(iterable,key,reverse)
"""

list_a = [1,2,3,4,5,6,1,1,1,2,2,3,4,4,5,5,5,5,6,6,6,6,6,6]
#原始方法
#print("list_a: " + str(list_a) + '\n')
#
# set_a = list(set(list_a))  # 去重得到一个集合
# print("set_a: " + str(set_a) + '\n')
#
# count_set_a = {}  # 存放元素和出现次数的字典，key为元素,value为出现次数
# for item in set_a:
#     count_set_a[item] = list_a.count(item)
# print("count_set_a: " + str(count_set_a) + '\n')
#
# # 将cou_set_a按value值排序，返回一个list，list中元素是形式为(1,4)的tuple，tuple[0]为键值，tuple[1]为出现次数
# sorted_list_a = sorted(count_set_a.items(), key=operator.itemgetter(1))
# print("sorted_list_a: " + str(sorted_list_a) + '\n')
#
# result_a = []  # 存放最后的结果
# for item in sorted_list_a[::-1]: # 按value值从大到小排序
#     result_a.append(item[0])
# print("result_a: " + str(result_a) + '\n')
"""
1.Counter得到dic
2.用sorted对dic排序
3.循环输出排序后的dic
"""
from collections import Counter
dic=Counter(list_a)
print(dic)
re=sorted(dic.keys(),key=dic.get,reverse=True)
print(re)
a=[22,3333,3333,4444,4444,22,3333,222,22,333,333,22,22,3333,3333,4444,4444,11,22,22,11,22]
from collections import Counter
import operator
# def sortFunc(lis):
#     dic=Counter(lis)
#     print(dic)
#     sort_lis=sorted(dic.items(),key=operator.itemgetter(1))
#     res=[]
#     for i in sort_lis:
#         res.append(i[0])
#     print(res)
#     return res
# sortFunc(a)
# coding:utf-8
from collections import Counter
re=Counter(a)
print(re)
print(max(re.keys()))
#学习max用法，前面的传参为后面key传入fun，输出为前面参数内最大值
print(max(re.keys(),key=re.get))
# #max中无key，则直接比较参数大小，输出参数内最大值
# print(max(re.values()))

# ~~~~~~
re=[{'name':'Homer', 'age':39}, {'name':'Bart', 'age':10}]
d1={'name':'Homer', 'age':39}
# def sortedDictValues1(adict):
#     items = adict.items()
#     items.sort()
#     return [value for key, value in items]
# print(sortedDictValues1(d1))