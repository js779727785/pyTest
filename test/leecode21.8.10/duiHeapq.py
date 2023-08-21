
"""
堆栈
堆heapq

"""
import heapq
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)  # 加入堆

# print(heap[0])  # 如果只是想获取最小值而不是弹出，使用heap[0]
# print([heapq.heappop(heap) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]

# 第二种
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
# print([heapq.heappop(nums) for _ in range(len(nums))])  # 堆排序结果
# out: [1, 2, 3, 5, 23, 54, 132]

"""
merge
"""
num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

res = heapq.merge(num1, num2)
# print(list(res))

"""
1、字符串中第二大的数
给你一个混合字符串 s ，请你返回 s 中 第二大 的数字，如果不存在第二大的数字，请你返回 -1 。
混合字符串 由小写英文字母和数字组成。
输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。
输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。
"""

class Solution:
    def secondHighest(self, s: str) -> int:
        q = []
        for ch in s:
            if ch.isdigit():
                n = int(ch)
                if not q or -n != q[0]: # 这里不能出现重复的字符
                    heapq.heappush(q, -n) # Python里heapq用的是小顶堆所以要取相反数
        if not q: return -1
        heapq.heappop(q)
        return -heapq.heappop(q) if q else -1
s = "dfa12321afd"
# print(Solution().secondHighest(s))

"""
第K大的数
"""
# class Solution:
#     def findKthLargest(self, nums,k) -> int:
#         maxHeap = []
#         for x in nums:
#             heapq.heappush(maxHeap, -x)
#         for _ in range(k - 1):
#             heapq.heappop(maxHeap)
#         return -maxHeap[0]
"""
第K大的数
利用堆，先将str中是整型的数推入heapq,最大需取反，再依次推出k-1次，最后判断堆内还有数据则继续推出为第K大的数，否则-1不存在
"""
s="111133332222555"
import heapq
class Solu():
    def fun11(self,str,k):
        re=[]
        for i in str:
            if i.isdigit():
                i=int(i)
                if not re or -i !=re[0]:
                    heapq.heappush(re,-i)
        for j in range(k-1):
            heapq.heappop(re)
        if not re:
            return -1
        if re:
            return -heapq.heappop(re)
        else:
            return -1



"""前K个高频元素"""
# 时间复杂度：O(nlogk)
# 空间复杂度：O(n)
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        # 要统计元素出现频率
        map_ = {}  # nums[i]:对应出现的次数
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        # 对频率排序
        # 定义一个小顶堆，大小为k
        pri_que = []  # 小顶堆

        # 用固定大小为k的小顶堆，扫面所有频率的数值
        for key, freq in map_.items():
            heapq.heappush(pri_que, (freq, key))
            if len(pri_que) > k:  # 如果堆的大小大于了K，则队列弹出，保证堆的大小一直为k
                heapq.heappop(pri_que)

        # 找出前K个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0] * k
        for i in range(k - 1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]
        return result
