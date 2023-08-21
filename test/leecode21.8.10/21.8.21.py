"""¬两数之和"""
num=[1,2,3,4,5,6,7,8]
target=5
def twoSum(num,target):
    hashmap={}
    for i,num in enumerate(num):
        if target-num in hashmap:
            return i,hashmap[target-num]
        hashmap[num]=i
        print(hashmap)
# twoSum(num,target)

"""找lis中的多数（出现次数大于len(lis)/2）"""
num1=[3,3,3,2,2,2,5,5,5]
def duoShu(lis):
    if len(lis)<2:
        return None
    else:
        for num in num1:
            co =num1.count(num)
            print(co)
            if co >len(num1)/2:
                return num
# print(duoShu(num1))
import collections
def majorityElement(nums):
    counts = collections.Counter(nums)
    print(counts)
    print(counts.keys())
    return max(counts.keys(), key=counts.get)

"""等差数列，lis中包含子等差数列数量"""
def func(lis):
    if len(lis)<3:
        return 0
    else:
        diff = lis[0]-lis[1]
        t= 0
        count=0
        for i in range(2,len(lis)):
            if lis[i-1]-lis[i]==diff:
                t+=1
            else:
                diff=lis[i-1]-lis[i]
            count+=t
        return count
# li=[1,2,3,4]
# print(func(li))
