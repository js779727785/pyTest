import os

lst = os.listdir(os.getcwd())

for c in lst:
    if os.path.isfile(c) and c.endswith('.py') and c.find("AllTest") == -1:  # 去掉AllTest.py文件
        print(c)
        i=0
        while i<20:
            #前提时将python配置为了环境变量
            os.system("python ./%s" %c)
            i+=1
            print("撤资执行了%s次"%i)