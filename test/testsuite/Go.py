import os

# lst = os.listdir(os.getcwd())
# """循环执行.py文件"""
# for c in lst:
#     # if os.path.isfile(c) and c.endswith('.py') and c.find("") == -1 :  # 去掉AllTest.py文件
#     if os.path.isfile(c) and c.endswith('demomail.py'):  # demomail.py文件
#         print(c)
#         i=0
#         # while i<2:
#         #     #前提时将python配置为了环境变量
#         os.system("python ./%s" % c)
#         #     i+=1
#         #     print("执行了%s次"%i)
basedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
b=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(b)