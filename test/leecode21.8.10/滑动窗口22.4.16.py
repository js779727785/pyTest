"""
https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/

"""
"""
1、无重复字符的最长子串
如：abcabcbb 输出abc 3
"""

def LongofStr(str):
    re = set()
    left = 0
    cur_len = max_len = 0
    for i in range(len(str)):
        cur_len += 1
        # 加入之前判断，有重复的话一直左推出，直到没重复
        while str[i] in re:
            re.remove(str[left])
            left += 1
            cur_len -= 1 #注意
        if cur_len > max_len:
            max_len = cur_len
        re.add(str[i])
    return max_len


ss = "abcbabcbb"
# print(LongofStr(ss))

"""
76. 最小覆盖子串
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
"""
s = "ADOBECODEBANC"
t = "ABC"
class Solution:
    def minWindow(self, s: 'str', t: 'str') -> 'str':
        from collections import defaultdict
        lookup = defaultdict(int)
        for c in t:
            lookup[c] += 1
        start = 0
        end = 0
        min_len = float("inf")
        counter = len(t)
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0:
                counter -= 1
            lookup[s[end]] -= 1
            end += 1
            while counter == 0:
                if min_len > end - start:
                    min_len = end - start
                    res = s[start:end]
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1
                start += 1
        return res

#至多包含K个不同字符的最长字符串
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        from collections import defaultdict
        lookup = defaultdict(int)
        start = 0
        end = 0
        max_len = 0
        counter = 0
        while end < len(s):
            if lookup[s[end]] == 0:
                counter += 1
            lookup[s[end]] += 1
            end += 1
            while counter > k:
                if lookup[s[start]] == 1:
                    counter -= 1
                lookup[s[start]] -= 1
                start += 1
            max_len = max(max_len, end - start)
        return max_len

"""
2、lis=[2,3,5,1,7,3,2],s=9,和为s的最小子串，下标

"""
lis = [2, 3, 5, 1, 7, 3, 2]
s = 15

def minoflis(lis, val):
    left = 0
    Sum = 0
    re = 0
    for i in range(len(lis)):
        Sum += lis[i]
        while Sum >= val: #注意是while不是if
            re = i - left + 1
            Sum -= lis[left]
            left += 1
    if re == 0:
        return -1
    else:
        return re

# print(minoflis(lis,s))



"""
4.2
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
"""
s = "ADOBECODEBANC"
t = "ABC"

import collections
def minWindow( s: str, t: str) -> str:
    need = collections.defaultdict(int)
    for c in t:
        need[c] += 1
    needCnt = len(t)
    i = 0
    res = (0, float('inf'))
    for j, c in enumerate(s):
        if need[c] > 0:
            needCnt -= 1
        need[c] -= 1
        if needCnt == 0:  # 步骤一：滑动窗口包含了所有T元素
            while True:  # 步骤二：增加i，排除多余元素
                c = s[i]
                if need[c] == 0:
                    break
                need[c] += 1
                i += 1
            if j - i < res[1] - res[0]:  # 记录结果
                res = (i, j)
            need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口
            needCnt += 1
            i += 1
    return '' if res[1] > len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果
"""
【快手】和为 K 的子数组
https://leetcode.cn/problems/subarray-sum-equals-k/
"""


def subarraySum(nums, k) -> int:
    # key：前缀和，val：对应的数量
    pre_sum_map = {0: 1}  # 初始化，前缀和为 0 的个数为 1

    pre_sum = 0  # 记录自首个元素累计的前缀和
    count = 0

    for num in nums:  # 遍历所有元素：计算前缀和，寻找 k，更新 map
        pre_sum += num  # 累计前缀和

        # 根据 pre - (pre - k) = k，寻找连续数组为 pre - k 的数量，即连续数组的和为 k 的数量
        # 说明：pre 为自首个元素开始累计的连续数组；
        # pre - k 为包含在连续数组 pre 中的一个连续子数组（自首个元素开始累计）
        # 连续数组 - 连续子数组 = 连续子数组，对应 pre - (pre - k) = k
        # 则连续数组的和为 pre - k 的数量，即为连续数组的和为 k 的数量
        if pre_sum - k in pre_sum_map:
            count += pre_sum_map[pre_sum - k]

        if pre_sum in pre_sum_map:  # 此时的前缀和被记录过，则在原始记录上 + 1
            pre_sum_map[pre_sum] += 1
        else:  # 如果此时的前缀和没有出现过，则初始化为 1
            pre_sum_map[pre_sum] = 1
    return count
lis=[1,1,1,2]
print(subarraySum(lis,2))