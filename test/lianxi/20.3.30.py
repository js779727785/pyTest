"""
filter(fun,arg),过滤得到满足函数的结果
"""
n=[1,2,3,4,5]
a=[4,5,6,7,8]
# re=list(filter(lambda x:x%2==1,n))
# print(re)
# re=list(map(lambda x,y:x*y,a,n))
# print(re)

"""
1.异常捕获
try:
    xxx
except:
    xxx
except Exception:
    xxx
else:
    xxx
finally:
    xxx

"""
"""
2.raise
3.traceback
"""
# import traceback
# def cc():
#      # 捕获具体异常信息模块
#     while True:
#         num = input('请输入数字：')
#         try:
#             print('100/%s=%s' % (num, 100.0 / int(num)))
#         except:
#             print('有异常!!', traceback.format_exc())  # 捕获具体异常信
re= list(filter(lambda x:x%2==1,n))
print(re)