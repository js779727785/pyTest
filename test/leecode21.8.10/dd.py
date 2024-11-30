class Demo():
    def __init__(self):
        print("init")
    def __enter__(self):
        print("enter")
        return self
    def __exit__(self,type,value,traceback):
        print("exit")
with Demo() as d:
    print("go")


# 使用 Python 语言来判断文本文件中是否存在目标字符串的示例代码
# def check_target_string_in_file(file_path, target_string):
#     with open(file_path, 'r') as file:
#         content = file.readlines()
#         for line in content:
#             if target_string in line:
#                 return True
#     return False
#
# # 请将 'your_file.txt' 替换为实际的文件路径，'your_target_string' 替换为目标字符串
# file_path = 'your_file.txt'
# target_string = 'your_target_string'
# if check_target_string_in_file(file_path, target_string):
#     print(f"文件中存在目标字符串 '{target_string}'")
# else:
#     print(f"文件中不存在目标字符串 '{target_string}'")

"""
空瓶换汽水问题：给N瓶汽水，每tar可换1瓶
"""
def fun(N,tar):
    total=N
    emp=N
    while emp>=tar:
        tem=emp//tar
        total+=tem
        emp=emp%tar+tem
    return total
print(fun(15,4))

"""给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false"""

string = "A man, a plan, a canal: Panama"
l='12233344555222'

def fun(l):
    lis=list(l)
    re={}
    for v in lis:
        re[v]=re.get(v,0)+1
    most_char=None
    max_count=0
    for i,v in re.items():
        if v>max_count:
            most_char=i
            max_count=v
    return most_char,max_count
print(fun(l))
dic={'1': 1, '2': 5, '3': 3, '4': 2, '5': 3}