"""
有序，且无重复数组中包含tar的数组下标，没有则输出-1

https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html#%E7%9B%B8%E5%85%B3%E9%A2%98%E7%9B%AE%E6%8E%A8%E8%8D%90
https://github.com/youngyangyang04/leetcode-master/blob/master/problems/0034.%E5%9C%A8%E6%8E%92%E5%BA%8F%E6%95%B0%E7%BB%84%E4%B8%AD%E6%9F%A5%E6%89%BE%E5%85%83%E7%B4%A0%E7%9A%84%E7%AC%AC%E4%B8%80%E4%B8%AA%E5%92%8C%E6%9C%80%E5%90%8E%E4%B8%80%E4%B8%AA%E4%BD%8D%E7%BD%AE.md
二分法查找：
"""
li=[-2,-1,0,1,3,5]
# def f1(lis,tar):
#     l=0
#     r=len(lis)
#     while l<=r:
#         mid=(l+r)//2
#         if tar>lis[mid]:
#             l=mid+1
#         elif tar<lis[mid]:
#             r=mid-1
#         else:
#             return mid
# print(f1(li,5))
"""
2 移除元素
原地移动数组中的重复数，得出新长度；用双指针在一次for循环中判断后者是否等于前置
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度；
"""
# def x1(nums,val):

li1=[-2,-1,0,1,3,5,-1,-2,5,3]
# print(x1(li,-2))
"""
2.2
给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。
"""
# def ff(nums):

li2=[-2,-1,-1,-1,0,1,3,3,5,5]
# print(ff(li2))

"""
2.3
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
"""
# def fu(lis):

# print(fu([0,1,0,3,12]))
"""
4 长度最小的子数组
给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
示例：
输入：s = 7, nums = [2,3,1,2,4,3] 输出：2 解释：子数组 [4,3] 是该条件下的长度最小的子数组。

"""
# def fu(lis,tar):
#     l = len(lis)
#     left = 0
#     right = 0
#     min_len = float('inf')
#     cur_sum = 0  # 当前的累加值
#     while right < l:
#         cur_sum += lis[right]
#         while cur_sum >= tar:  # 当前累加值大于目标值 注意这里是while不是if！！！
#             min_len = min(min_len, right - left + 1)
#             cur_sum -= lis[left]
#             left += 1
#
#         right += 1
#     return min_len if min_len != float('inf') else 0
# s = 7
# nums = [2,3,1,2,4,3]
# print(fu(nums,7))

"""
3输入一个数组nums，和一个值target，找出两数之和为和一个值target的数组下标
"""
# def funn(lis,tar):
# ll=[1,2,1,-3,4,2,1,-3,-2]
# tar=3
# print(funn(ll,tar))

"""
定义链表
"""
class ListNode():
    def __init__(self,head):
        self.head=head
        self.next=None
class Solution():
    def fuc(self,lisnode,tar):
        dummy_head=ListNode(head=0)
        dummy_head.next=lisnode
        cur=dummy_head
        if cur.next.val ==tar:
            cur.next=cur.next.next
        else:
            cur=cur.next


