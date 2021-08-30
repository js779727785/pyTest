#coding=utf-8
"""
https://blog.csdn.net/DaxiaLeeSuper/article/details/90613459
1.pytest可执行用例脚本
2.pytest -v -s allure_demo.py --alluredir=report  在当前目录生成report文件夹，report中包含.json文件
3. allure generate --clean report 将report转换生成新的allure_report文件，运行其中的index.html(必须在pycharm右键使用chrome打开，或者火狐直接打开)
"""

import pytest
import allure

marketid = ['101','102']
testlist = ['1','test','test1']
testlist2 = ['test0','test2','test3']

#市场id对应也生成相同的数组

@pytest.fixture(scope='module',autouse=True)
@allure.feature('测试准备')
def prepare():
    print('这是测试准备哦')
    yield
    print('module 测试结束')

@allure.feature('期权强平测试')
class Test_module1:
    @allure.feature('期权市价委托强平')
    @pytest.mark.parametrize('str1',testlist)
    @pytest.mark.parametrize('str2',testlist2)
    def test1(self,str1,str2):
        """
            用例描述：期权强平市价委托
        """
        stradd = str1 + str2
        print('这是test1')
        assert 1 == 2

    @allure.feature('期权限价委托强平')
    def test2(self):
        with allure.step("调节持仓"):
            x = '1'
            allure.attach(x)
            print('这是test2')
        with allure.step('进行强平的操作'):
            print('DTE')
# `在这里插入代码片`
class Test_module2:
    def test3(self):
        with allure.step("调节持仓"):
            x = '1'
            allure.attach(x)
            print('这是test2')
        with allure.step('进行强平的操作'):
            print('DTE')
