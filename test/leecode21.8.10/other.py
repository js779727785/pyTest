"""
其他看到，但不会的练习
"""
"""
1、求一个数的开平方
"""
def x1(i):
    left=0
    right=i
    while left<right:
        mid=left+(right-left)//2
        if mid**2<=i and (mid+1)**2>i:
            return mid
        elif mid**2<i:
            left=mid+1
        elif mid**2>i:
            right=mid-1
# print(x1(8))
"""
2、找出 字符串中的单词
"""
ss='I can because i think i can'
def count(str):
    count_words = str.split()
    count_word = {}
    for word in count_words:
        if word not in count_word.keys():
            count_word[word] = 1
        else:
            count_word[word] += 1
    return count_word
# print(count('I can because i think i can'))

# from collections import Counter
#
# str = 'I can because i think i can'
# counts = Counter(str.split())
# print(counts)

def getS(str,word):
    ss=str.split()
    re={}
    for val in ss:
        if val not in re.keys():
            re[val]=1
        else:
            re[val]+=1
    return re.get(word) if re.get(word) else -1
print(getS(ss,'can1'))

"""
反转整数
"""
def reverse(ii):
    i=list(str(abs(ii)))
    left=0
    right=len(i)-1
    while left<right:
        i[left],i[right]=i[right],i[left]
        left+=1
        right-=1
    re=''.join(i)
    if ii<0:
        return -int(re)
    else:
        return int(re)
# print(reverse(210))
"""99九九乘法表"""
def jiujiu():
    for i in range(1,10):
        for j in range(1,i+1):
            print("{}*{}={}\t".format(j,i,i*j),end="")
        print()
# jiujiu()

"""
压缩字符串
"""
ss="aabcccccaaa"
def func(S) -> str:
    if not S:
        return ""
    ch = S[0]
    ans = ''
    cnt = 0
    for c in S:
        if c == ch:
            cnt += 1
        else:
            ans += ch + str(cnt)
            ch = c
            cnt = 1
    ans += ch + str(cnt)
    return ans if len(ans) < len(S) else S

def compressString(S) -> str:
    N = len(S)
    res = ''
    i = 0
    while i < N:
        j = i
        while j < N and S[j] == S[i]:
            j += 1
        res += S[i] + str(j - i)
        i = j

    if len(res) < len(S):
        return res
    else:
        return S
def compressString(S) -> str:
    N = len(S)
    res = ''
    i = 0
    while i < N:
        j = i
        while j < N and S[j] == S[i]:
            j += 1
        res += S[i] + str(j - i)
        i = j

    if len(res) < len(S):
        return res
    else:
        return S
print(compressString(ss))