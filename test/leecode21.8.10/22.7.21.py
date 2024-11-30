"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效
"""
def isValid(s: str) -> bool:
    stack = []
    mapping = {
        '(': ')',
        '[': ']',
        '{': '}'
    }
    for item in s:
        if item in mapping.keys():
            stack.append(mapping[item])
        elif not stack or stack[-1] != item:
            return False
        else:
            stack.pop()
    return True if not stack else False
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

"""
1、无重复字符的最长子串
如：abcabcbb 输出abc 3
"""
ss="abcbabc"
def LongofStr(str):
    re = set()
    left = 0
    cur_len = max_len = 0
    for i in range(len(str)):
        cur_len += 1
        # 加入之前判断，有重复的话一直左推出，直到没重复
        while str[i] in re: #注意这里是while 不是if
            re.remove(str[left])
            left += 1
            cur_len -= 1 #注意
        if cur_len > max_len:
            max_len = cur_len
        re.add(str[i])
    return max_len

"""
反转链表
"""
#双指针
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = head
        pre = None
        while(cur!=None):
            temp = cur.next # 保存一下 cur的下一个节点，因为接下来要改变cur->next
            cur.next = pre #反转
            #更新pre、cur指针
            pre = cur
            cur = temp
        return pre

"""
6、买股票的最佳时机（后者-前者差额最大值）？
如输入：lis=[7,1,5,3,6,4]输出5；输入[7,6,4,3,1]输出0
"""
def fun3(lis):
    minprice=float("inf") #注意这里定义最小钱不是0而是正无穷大
    maxprice=0
    for i in range(len(lis)):
        maxprice=max(lis[i]-minprice,maxprice)
        minprice=min(lis[i],minprice)
    return maxprice
ll3=[7,1,5,3,6,4]
print(fun3(ll3))
"""
最大子数组和？
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
nums = [-2,1,-3,4,-1,2,1,-5,4],输出6
"""

def maxSubArray(nums):
    pre = 0
    res = nums[0]
    for i in range(len(nums)):
        pre = max(nums[i], pre + nums[i])
        res = max(res, pre)
    return res
"""
值第K大的数
用heapq
"""
def fu11(lis,k):
    import heapq
    re=[]
    for i in range(len(lis)):
        heapq.heappush(re,-lis[i])
    for _ in range(k-1):
        heapq.heappop(re)
    return -heapq.heappop(re)
nums = [-2,1,-3,4,-1,2,1,-5,4,7,6]
print(fu11(nums,1))

"""
出现频率第K大的数
"""
def fu12(lis,k):
    re={}
    for v in lis:
        re[v]=re.get(v,0)+1
    re=sorted(re,key=re.get,reverse=True)
    return re[k-1]

"""
峰值所在索引
如果数组是 [1, 5, 3, 2, 4] ，那么峰值索引为 1（对应值 5）。如果数组是 [2, 2, 2, 2] ，则没有峰值，函数将返回一个空列表。
"""
lis=[1,3,2,4,5,3,2,4,1]
def fun(lis):
    re=[]
    res=[]
    for i in range(1,len(lis)-1):
        if lis[i]>lis[i-1] and lis[i]>lis[i+1]:
            re.append(lis[i])
    for i in re:
        res.append(lis.index(i))
    return res
print(fun(lis))