def func(n):
    if n==1:
        return 1
    else:
        return n*func(n-1)
# print(func(9))
from functools import reduce
def ff(a):
    re=reduce(lambda x,y:x*y,range(1,a+1))
    print(re)
def zz(x,n):
    if n==0:
        return 1
    else:
        return x*zz(x,n-1)
print(zz(3,4))