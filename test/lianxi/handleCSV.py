"""pandas库是一个强大的数据处理和数据分析库，使用pandas处理csv文件更简单"""

import pandas

# def handleCsv(oldfile,newfile):
def copyCsv():
    """
    负责文件
    :return:
    """
    # Step1：首先，导入必要模块，获取输入输出文件路径。
    # infile = oldfile
    # outfile = newfile
    infile = "/Users/jingshuai/Desktop/old.csv"
    outfile = "/Users/jingshuai/Desktop/new.csv"

    # Step2：使用pandas的read_csv方法将数据存储到一个DataFrame对象中。
    dataframe = pandas.read_csv(infile)
    print(dataframe)
    # Step3：然后使用DataFrame的to_csv方法将其输出到另一张csv表中。
    dataframe.to_csv(outfile, index=False)

def handleCsv2dic():
    """
    负责提取文件数据
    :return:
    """
    # Step1：首先，导入必要模块，获取输入输出文件路径。
    # infile = oldfile
    infile = "/Users/jingshuai/Desktop/old.csv"
    data=pandas.read_csv(infile,header=None)
    print(data)
    print(data.values.tolist())
    val= data.values.tolist()
    # for i in val:
    #     print(i[0])
    #     print(i[1])
handleCsv2dic()
# re = {'variableName': 'phone_student', 'dataType': '0', 'variableValue': '72103581610', 'isUseful': 1}