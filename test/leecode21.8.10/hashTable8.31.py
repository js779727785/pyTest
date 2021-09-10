"""
三  哈希表 HashTable
1、数组就是一个哈希表
2、一般哈希表都是用来快速判断一个元素是否出现集合里（但是哈希法也是牺牲了空间换取了时间，因为我们要使用额外的数组，set或者是map来存放数据，才能实现快速的查找。）
3、哈希函数：通过hashCode（hashcode是通过特定编码方式）将其他数据格式转化为不同的数值，这样就把其他数据映射为哈希表上的索引数字了。
4、哈希碰撞：多个数据映射到了一个索引上。
5、一般哈希碰撞有两种解决方法， 拉链法和线性探测法。
6、哈希表常见的数据结构：集合set，数组，映射map
"""

"""
1、有效的字母异位词
https://leetcode-cn.com/problems/valid-anagram/
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
示例 1: 输入: s = "anagram", t = "nagaram" 输出: true
示例 2: 输入: s = "rat", t = "car" 输出: false
说明: 你可以假设字符串只包含小写字母。
"""
s = "anagram"
t = "nagaram"
# print(set(s).issubset(set(t)))
# print(set(s)<=set(t))
def x1(s,t):
    from collections import defaultdict
    s_dict=defaultdict(int)
    t_dict=defaultdict(int)
    for i in s:
        s_dict[i]+=1
    for i in t:
        t_dict[i]+=1
    print(s_dict)
    print(t_dict)
    return s_dict == t_dict
x1(s,t)
"""
1.2给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指字母相同，但排列不同的字符串。
题解：https://leetcode-cn.com/problems/find-all-anagrams-in-a-string/solution/438-zhao-dao-zi-fu-chuan-zhong-suo-you-z-nx6b/
"""

class Solution:
    def findAnagrams(self, s: str, p: str):
        n, m, res = len(s), len(p), []
        if n < m: return res
        p_cnt = [0] * 26
        s_cnt = [0] * 26
        for i in range(m):
            p_cnt[ord(p[i]) - ord('a')] += 1
            s_cnt[ord(s[i]) - ord('a')] += 1
        if s_cnt == p_cnt:
            res.append(0)

        for i in range(m, n):
            s_cnt[ord(s[i - m]) - ord('a')] -= 1
            s_cnt[ord(s[i]) - ord('a')] += 1
            if s_cnt == p_cnt:
                res.append(i - m + 1)
        return res
"""
2 两个数组的交集
https://leetcode-cn.com/problems/intersection-of-two-arrays/

题意：给定两个数组，编写一个函数来计算它们的交集。结果不重复
"""
num1=[1,2,2,3]
num2=[2,4]
def x2(lis1,lis2):
    ll=[]
    lis2=set(lis2) #提前去重
    for i in lis1:
        if i in lis2:
            ll.append(i)  #ll用set的话，这里用set.add(i)
    return ll
"""
2.2接上一个进阶，输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
"""
# class Solution:
#     def intersect(self, nums1,nums2):
#         import collections
#         if len(nums1) > len(nums2):
#             return self.intersect(nums2, nums1)
#
#         m = collections.Counter()
#         for num in nums1:
#             m[num] += 1
#
#         intersection = list()
#         for num in nums2:
#             if (count := m.get(num, 0)) > 0:
#                 intersection.append(num)
#                 m[num] -= 1
#                 if m[num] == 0:
#                     m.pop(num)
#         return intersection

"""
3输入一个数组nums，和一个值target，找出两数之和为和一个值target的数组下标
"""
nums=[8,9,1,2,3,4,5,6,88]
target=5
def twoSum( nums, target):
    hashtable = dict()
    for i,num in enumerate(nums):
        if target-num in hashtable:#注意这里不是在lis而是hashtable
            print(hashtable)
            return [hashtable[target - num], i]
        hashtable[nums[i]] = i
    return []
def fu(lis,tar):
    hashtable=dict()
    for i in range(len(lis)):
        hashtable[lis[i]]=i
        if tar-lis[i] in hashtable:#注意这里不是在lis而是hashtable
            return [hashtable[tar-lis[i]],i]
    return []
# print(twoSum(nums,target))


"""
4编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        set_ = set()
        while 1:
            sum_ = self.getSum(n)
            if sum_ == 1:
                return True
            # 如果这个sum曾经出现过，说明已经陷入了无限循环了，立刻return false
            if sum_ in set_:
                return False
            else:
                set_.add(sum_)
            n = sum_

    # 取数值各个位上的单数之和
    def getSum(self, n):
        sum_ = 0
        while n > 0:
            sum_ += (n % 10) * (n % 10)
            n //= 10
        return sum_