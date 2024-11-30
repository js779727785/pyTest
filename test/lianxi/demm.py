# teststep = {
#             'name': "step.get('desc')"
#         }
# teststep.setdefault('aa','11')
# teststep['bb']='222'
# teststep['aa']='333'
# teststep['bb']='444'
# print(teststep)



# id='3'
# class A():
#     def __init__(self):
#         self.array_list = ['1','2']
#
#     def handle_case(self):
#         if id:
#             self.array_list.append(id)
#     def do(self):
#         self.handle_case()
#         print(self.array_list)
#     def do2(self):
#         print(self.array_list)
# if __name__ == '__main__':
#     a=A()
#     a.do2()

"""
dict字典
dic.items()为('a', 2)
dic含义与dic.key()一样
dic含义与dic.key()一样
"""
dic = {'a':2,'b':1,'c':3}
#循环输出key,value
# for key,value in dic.items():
#     print("key：{},value：{}".format(key,value))
#字典的key-values互换
z={value:key for key,value in dic.items()}
# print(z)
d = sorted(dic,key = lambda k:k[0])
import operator
x = sorted(dic.items(),key =operator.itemgetter(0))
print(d)


key=[]
value=[]
for i in dic :
    key.append(i)
    value.append(dic[i])
print(key)
print(value)

