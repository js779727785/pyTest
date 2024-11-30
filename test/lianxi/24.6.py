lis=[2,3,4,5,6,3,2,99,88]
n=[3,4,5,2,3,1,3,77,88]
def q1(lis):
    for i in range(len(lis)-1):
        for j in range(len(lis)-i-1):
            if lis[j]>lis[j+1]:
                lis[j],lis[j+1]=lis[j+1],lis[j]
    return lis

def q2(lis):
    if len(lis)<2:
        return lis
    else:
        tem = lis[0]
        less = [i for i in lis if i < tem]
        max = [i for i in lis if i > tem]
        return q2(less)+[tem]+q2(max)

def q3(lis,n):
    re=[i for i in lis if i not in n]
    rr=[i for i in n if i not in  lis]
    return re+rr
def q4(lis,n):
    re=list(set(lis)^set(n))
    return re

def q5(lis,n):
    re=list(map(lambda x:x*x,lis))
    print(re)
    print(sorted(re))
    re=list(map(lambda x,y:x*y,lis,n))
    print(re)


# print(q5(lis, n))

lis=['b','a','a','a','d','d']

from collections import Counter
c=Counter(lis)
re=sorted(c,key=lambda x:c[x],reverse=True)


