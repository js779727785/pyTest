pidList = ['少儿']
repidList = ['教师', 'CRM']
aa = ['教师', 'CRM']
casereid3 =['aaa','xxx']
repidList2 = ['教师', '少儿','CRM']


dict1={"aa":'11',"bb":[1,2,3],"cc":{}}

# 遍历list
# for i in aa:
#     print("序号：%s   值：%s" % (aa.index(i) + 1, i))
#遍历dict
# for key in dict1:
#     print("dict的key是：%s    value为：%s" % (key,dict1[key]))


#Python验证多个元素都在list中,前者是后者的子集,或者用A <= B 小于号判断
# def inList():
#     r = set(aa).issubset(set(repidList))
#     print(r)
#
# #Python验证两个list是否有交集
# if list(set(repidList) & set(casereid3)):
#     print('2')
