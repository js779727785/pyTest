"""6.1写一个冒泡排序和快速排序"""
"""6.2一个list,一个集合，取出在A内不在B内的，输出新的list"""
"""6.3一个list,一个集合，取出即不在A内不在B内的元素，输出新的list"""
"""6.4一个list,一个集合,相互乘积，得到一个新的list并去重排序"""
"""6.5一个list,一个集合，取出AB内共有的元素，输出新的list"""
c=[2,3,4,5,6,3,2,99,88]
n=[3,4,5,2,3,1,3,77,88]
"""6.1 从大到小排  这两个背也要背会"""
def fun(lis):
    count=0
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j]<lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
                count+=1
    return lis,count
def quick_sort(lis):
    if len(lis)<2:
        return lis
    else:
        tem=lis[0]
        less=[i for i in lis if i<tem]
        max =[i for i in lis if i>tem]
        return quick_sort(max)+[tem]+quick_sort(less)
"""6.2"""
def ff(lis1,lis2):
    lis=[i for i in lis1 if i not in lis2]
    return lis
# print(ff(c,n))
"""6.3 set的反交集用法  set(a)^set(b)"""
def zz(lis1,lis2):
    re=list(set(lis1)^set(lis2))
    # re=sorted(re)
    return re
# print(zz(c,n))
"""6.4 map的用法 map(func,iter1,iter2……)"""
def cc(lis1,lis2):
    re=list(map(lambda x,y:x*y,lis1,lis2))
    lis=list(set(re))
    # print(lis)
    new_list=sorted(lis)
    # print(new_list)
    return new_list
# cc(c,n)
"""6.5set的交集用法  set(a)&set(b)"""
def gg(lis1,lis2):
    return list(set(lis1)&set(lis2))

"""类似的map可以做单list的算法"""
def xx(lis):
    re=list(map(lambda x:x*x,lis))
    return re
# print(xx(c))
nums=[8,9,1,2,3,4,5,6,88]
nums1=[88,99]
target=5
def twoSum( nums, target):
    hashtable = dict()
    for i,num in enumerate(nums):
        if target-num in hashtable:
            return i,hashtable(target-num)
        else:
            hashtable[num]=i
