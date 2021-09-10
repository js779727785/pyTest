"""
字符串
字符串是若干字符组成的有限序列，也可以理解为是一个字符数组
数组和字符串转换
s = "We are happy."
ls=list(s)
re=''.join(ls)
print(ls)
print(re)
s="1,2,3"
ls=list[s]
"""
"""
1、反转字符串
示例 1：
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
"""
def x1(str):
    left=0
    right=len(str)-1
    while left<right:
        str[left],str[right]=str[right],str[left]
        left+=1
        right-=1
    return str
# s1=["h","e","l","l","o"]
s1=("h","e","l","l","o")
# print(x1(list(s1)))
"""
反转字符串II
给定一个字符串 s 和一个整数 k，你需要对从字符串开头算起的每隔 2k 个字符的前 k 个字符进行反转。

如果剩余字符少于 k 个，则将剩余字符全部反转。

如果剩余字符小于 2k 但大于或等于 k 个，则反转前 k 个字符，其余字符保持原样。

示例:

输入: s = "abcdefg", k = 2
输出: "bacdfeg"

#
"""
def reverseStr(self, s: str, k: int) -> str:
    """
    1. 使用range(start, end, step)来确定需要调换的初始位置
    2. 对于字符串s = 'abc'，如果使用s[0:999] ===> 'abc'。字符串末尾如果超过最大长度，则会返回至字符串最后一个值，这个特性可以避免一些边界条件的处理。
    3. 用切片整体替换，而不是一个个替换.
    """

    def reverse_substring(text):
        left, right = 0, len(text) - 1
        while left < right:
            text[left], text[right] = text[right], text[left]
            left += 1
            right -= 1
        return text

    res = list(s)

    for cur in range(0, len(s), 2 * k):
        res[cur: cur + k] = reverse_substring(res[cur: cur + k])

    return ''.join(res)

"""
3、请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

示例 1： 输入：s = "We are happy."
输出："We%20are%20happy."
#
"""

def replaceSpace( s: str) -> str:
    counter = s.count(' ')

    res = list(s)
    # 每碰到一个空格就多拓展两个格子，1 + 2 = 3个位置存’%20‘
    res.extend([' '] * counter * 2)

    # 原始字符串的末尾，拓展后的末尾
    left, right = len(s) - 1, len(res) - 1

    while left >= 0:
        if res[left] != ' ':
            res[right] = res[left]
            right -= 1
        else:
            # [right - 2, right), 左闭右开
            res[right - 2: right + 1] = '%20'
            right -= 3
        left -= 1
    return ''.join(res)

