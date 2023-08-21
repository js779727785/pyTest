"""
关于数组的一些Leecode算法  1数组
1.数组是存放在连续内存空间上的相同类型数据的集合。
2.二维数据在内存中不是 3*4 的连续地址空间，而是四条连续的地址空间组成(二维数组第二索引数量)！
数组查询和删除时间复杂度：O(n),查询时间复杂度O(1)
"""

"""
!!!
数组内各个数出现次数
def listodic(lis):
    re={}
    for i in range(len(lis)):
        re[lis[i]]=re.get(lis[i],0)+1
    return re
数组中第tar大的字符
def fu1(lis,tar):
    #取出字符
    re={}
    for i in lis:
        re[i]=re.get(i,0)+1
    #按照值排序，默认从小到大，取反
    re=sorted(re,key=re.get,reverse=True)
    #取第tar的值
    return re[tar-1]
print(fu1(lis,3))
"""


def xdeNci(x,n):
    if n==0:
        return 1
    return x*(xdeNci(x,n-1))
# print(xdenci(2,3))

def febo(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return febo(n-1)+febo(n-2)
# print(febo(4))
nums = [-1, 0, 3, 5, 9, 12]

lisss=[1,3,5,6]
"""
1 二分法时间复杂度：O(logn)
二分法查找：有序，且无重复数组中包含tar的数组下标，没有则输出-1
https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E7%9B%B8%E5%85%B3%E9%A2%98%E7%9B%AE%E6%8E%A8%E8%8D%90
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0034.%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.md

"""
# 1.暴力枚举没有利用有序的特点
def shazi(lis,tar):
    if len(lis)>0:
        for i in lis:
            if i == tar:
                return lis.index(i)
    return -1
#
def fen2(lis,tar):
    left,right=0,len(lis)-1
    while left <= right: #注意用while不是for
        #注意Python中//为整除，/结果为float,
        # mid =left+((right-left)//2)
        mid =(left+right)//2
        if tar<lis[mid]:
            right=mid-1
        elif tar>lis[mid]:
            left=mid+1
        else:
            return mid
    return -1
"""
2 移除元素
原地移动数组中的重复数，得出新长度；用双指针在一次for循环中判断后者是否等于前置
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度；

时间复杂度：$O(n)$
空间复杂度：$O(1)$

"""

def yichu(lis,val):
    j=0
    for i in range(len(lis)):
        if lis[i]!=val:
            lis[j]=lis[i]
            j+=1
    return j
# def yi(lis,val):
#     j=0
#     for i in lis:
#         if i != val:
#             lis[j]=i
#             j+=1
#     return j
# nums = [0,1,2,2,3,0,4,3]
# print(yi(nums,2))
"""
2.2
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
"""
nums=[-3,-2,-2,0,1,1,2,2,3,3,3,4]
def fu(lis):
    if len(lis)<2:
        return lis
    else:
        j=1
        for i in range(1,len(lis)):
            if lis[i]!=lis[i-1]:
                lis[j]=lis[i]
                j+=1
        return lis[:j],j,lis

def xx(lis):
    if len(lis)<1:
        return 0
    else:
        j=1
        for i in range(1,len(lis)): #注意这里也从1开始
            if lis[i]!=lis[i-1]:
                lis[j]=lis[i]
                j+=1
        return j,lis
# print(xx(nums))

"""
2.3
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""
def x1(nums):
    if len(nums)<1:
        return nums
    else:
        j=0
        for i in range(len(nums)):
            if nums[i]!=0:
                nums[j]=nums[i]
                j+=1
        print(j,nums[:j])
        for j in range(j,len(nums)): #注意范围
            nums[j]=0
        return nums
# de=[0,1,0,3,12]
# print(x1(de))

"""
3 有序数组的平方
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序
"""
ll=[-4,1,3,4]
def pingfang(nums):
    if len(nums)<1:
        return nums
    else:
        l1=[]
        for i in nums:
            i=i*i
            l1.append(i)
        l1=sorted(l1)
        return l1
# print(pingfang(ll))

# re=list(map(lambda x:x*x,ll))
# print(sorted(re))

#涉及到双指针的左右判断可以临时再看看，https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html

"""
4 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

"""
nums = [2,3,1,2,4,3]
def x3(lis,s):
    """
    时间复杂度：$O(n)$
    空间复杂度：$O(1)$
    """
    if len(lis)<1:
        return None
    else:
        slow=Sum=0
        re=float("inf")
        for i in range(len(lis)):
            Sum+=lis[i]
            while Sum>=s: #注意
                re=i-slow+1
                Sum-=lis[slow]
                slow+=1
        if re==float("inf"):
            return 0
        else:
            return re
# print(x3(nums,7))
"""
6、买股票的最佳时机
如输入：lis=[7,1,5,3,6,4]输出5；输入[7,6,4,3,1]输出0
"""
def fun3(lis):
    minprice=float("inf") #注意这里定义最小钱不是0而是正无穷大
    maxprice=0
    for i in range(len(lis)):
        maxprice=max(lis[i]-minprice,maxprice)
        minprice=min(lis[i],minprice)
    return maxprice
ll3=[7,6,4,3,1]
print(fun3(ll3))


"""
5  螺旋数组
题目地址：https://leetcode-cn.com/problems/spiral-matrix-ii/ 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
示例:
输入: 3 输出: [ [ 1, 2, 3 ], [ 8, 9, 4 ], [ 7, 6, 5 ] ]

"""
class Solution:
    def generateMatrix(self, n: int):
        left, right, up, down = 0, n-1, 0, n-1
        matrix = [ [0]*n for _ in range(n)]
        num = 1
        while left<=right and up<=down:
            # 填充左到右
            for i in range(left, right+1):
                matrix[up][i] = num
                num += 1
            up += 1
            # 填充上到下
            for i in range(up, down+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            # 填充右到左
            for i in range(right, left-1, -1):
                matrix[down][i] = num
                num += 1
            down -= 1
            # 填充下到上
            for i in range(down, up-1, -1):
                matrix[i][left] = num
                num += 1
            left += 1
        return matrix
