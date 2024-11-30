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
ls=list(s)
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
    res.extend([' '] * counter * 2) #注意是extend

    # 原始字符串的末尾，拓展后的末尾
    left, right = len(s) - 1, len(res) - 1 #注意

    while left >= 0:
        if res[left] != ' ':
            res[right] = res[left]
            right -= 1
        else:
            # [right - 2, right), 左闭右开
            res[right - 2: right + 1] = '%20' #注意这里替换写法
            right -= 3
        left -= 1
    return ''.join(res) #将数组转回字符串

"""
4.翻转字符串里的单词
示例 1：
输入: "  hello world!  "
输出: "world! hello"
"""

class Solution:
    # 1.去除多余的空格
    def trim_spaces(self, s):
        n = len(s)
        left = 0
        right = n - 1

        while left <= right and s[left] == ' ':  # 去除开头的空格 #注意这里是 left <= right
            left += 1
        while left <= right and s[right] == ' ':  # 去除结尾的空格
            right = right - 1
        tmp = []
        while left <= right:  # 去除单词中间多余的空格
            if s[left] != ' ':
                tmp.append(s[left]) #注意
            elif tmp[-1] != ' ':  # 当前位置是空格，但是相邻的上一个位置不是空格，则该空格是合理的 #这里要注意是tmp[-1] 而不是s[-1]】
                tmp.append(s[left])
            left += 1
        return tmp #注意这里返回tmp

    # 2.翻转字符数组
    def reverse_string(self, nums, left, right):
        while left < right:  #注意这里是 left < right
            nums[left], nums[right] = nums[right], nums[left]
            left += 1 #注意
            right -= 1
        return None

    # 3.翻转每个单词
    def reverse_each_word(self, nums):
        start = 0
        end = 0
        n = len(nums)
        while start < n: #注意这里
            while end < n and nums[end] != ' ': #注意
                end += 1
            self.reverse_string(nums, start, end - 1) #注意这里
            start = end + 1
            end += 1
        return None

    # 4.翻转字符串里的单词
    def reverseWords(self, s):  # 测试用例："the sky is blue"
        l = self.trim_spaces(s)  # 输出：['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e'
        self.reverse_string(l, 0, len(
            l) - 1)  # 输出：['e', 'u', 'l', 'b', ' ', 's', 'i', ' ', 'y', 'k', 's', ' ', 'e', 'h', 't']
        self.reverse_each_word(l)  # 输出：['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']
        return ''.join(l)  # 输出：blue is sky the
s = "  We are happy. "
# print(Solution().reverseWords(s))

"""
5、左旋转字符串
字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。
示例 1：
输入: s = "abcdefg", k = 2
输出: "cdefgab"
限制：
1 <= k < s.length <= 10000

思路：
1、反转区间为前n的子串  2、反转区间为n到末尾的子串 3、反转整个字符串
"""
class Solution():
    def reverse_str(self,s,left,right):
        s=list(s)
        while left<right:
            s[left],s[right] = s[right],s[left]
            left+=1
            right-=1
        return s
    def go(self,s,n):
        s=self.reverse_str(s,0,n-1)
        s=self.reverse_str(s,n,len(s)-1)
        s=self.reverse_str(s,0,len(s)-1)
        return ''.join(s)
s = "abcdefg"
# print(Solution().go(s,2))

"""
6、实现strStr()
给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1: 输入: haystack = "hello", needle = "ll" 输出: 2

示例 2: 输入: haystack = "aaaaa", needle = "bba" 输出: -1

说明: 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。
#
"""

""""
判断字符串是否是回数
"""
def is_palindrome(s):
    s = s.replace(" ", "").lower()  # 去除空格并转换为小写，以便更准确地判断
    return s == s[::-1]

string = "A man, a plan, a canal: Panama"
if is_palindrome(string):
    print(f"{string} 是回数")
else:
    print(f"{string} 不是回数")