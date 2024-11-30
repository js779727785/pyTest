"""¬无重复的最长字符串"""

def longest_substring(str):
    n = len(str)
    re = {}
    max_length = 0
    start = 0
    for end in range(n):
        if str[end] in re and start <= re[str[end]]:
            start = re[str[end]] + 1
        else:
            max_length = max(max_length, end - start + 1)
        re[str[end]] = end
    return max_length
"""
判断字符串是否是回文 24.8阿里智能信息面
string = "A man, a plan, a canal: Panama"
先去除字符串中的非字母数字字符，将字符串转换为统一的大小写，然后比较字符串与其反转后的字符串是否相同。如果相同，则该字符串是回文；否则，不是回文。
"""
def is_palindrome(s):
    cleaned_str = ''.join(filter(str.isalnum, s)).lower()
    return cleaned_str == cleaned_str[::-1]


"""最长回文子串"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s or len(s) == 1:
            return s

        max_str = ""
        max_length = 0
        for inx, v in enumerate(s):

            # 1个元素作为中心
            left = inx
            right = inx
            while left >=0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_str = s[left: right + 1]
                        max_length = right - left + 1
                    left -= 1
                    right += 1
                else:
                    break

            # 2个元素做为中心
            left = inx
            right = inx + 1

            while left >=0 and right <= len(s) - 1:
                if s[left] == s[right]:
                    if right - left + 1 > max_length:
                        max_str = s[left: right + 1]
                        max_length = right - left + 1
                    left -= 1
                    right += 1
                else:
                    break

        return max_str

def longest_palindrome(s):
    max_length = 0
    start = 0
    end = 0

    for i in range(len(s)):
        # 奇数长度的回文
        len1 = expand_around_center(s, i, i)
        # 偶数长度的回文
        len2 = expand_around_center(s, i, i + 1)
        length = max(len1, len2)

        if length > max_length:
            max_length = length
            start = i - (length - 1) // 2
            end = i + length // 2

    return s[start:end + 1]

def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

# 测试
s = "babad"
print(longest_palindrome(s))