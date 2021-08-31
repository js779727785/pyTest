import pytest,allure
"""
2020.3.23
https://www.cnblogs.com/sparkling-ly/category/851617.html
https://www.jianshu.com/p/932a4d9f78f8
"""
#demo1
# pytest -v -m "one" pytest_demo.py
@pytest.mark.demo
def test_d1():
    print("run d1")
    assert 2==1+1
#xfail 不计入fail
@pytest.mark.xfail
def test_d2():
    assert 2==1+2
#直接跳过执行
@pytest.mark.skip
def test_d3():
    print("run d3")
    assert 2==1+3
"""
https://blog.csdn.net/liuchunming033/article/details/46501653
"""
#demo2，用pytest做一个简单的单测
def fun(n):
    return n*5
@pytest.mark.fun
def test_fun():
    assert fun(4)==20

#多个测试用例放到一个Test开头类
class TestPydemo:
    @pytest.mark.one
    def test_one(self):
        x="hello"
        assert "h" in x

    @pytest.mark.one
    def test_two(self):
        x="world"
        assert hasattr(x,'check')
#pytest-xdist,多核运行用例，
# pytest -n 4 -v pytest_demo.py
#pytest-html,测试报告
 # pytest -v pytest_demo.py --html=report.html
#运行文件:类：方法
# pytest pytest_demo.py::TestPydemo::test_one

"""
3.@pytest.mark.parametrize("a,b,expected", testdata)
https://blog.csdn.net/lb245557472/article/details/90341297?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
"""
def fun1(x,y):
    expected=x*y
    return expected
def test_fun1():
    assert fun1(4,5)==20

testdata=[(4,5,20),(4,5,30)]
@pytest.mark.parametrize("x,y,expected",testdata)
@allure.feature("test1")
def test_fun2(x,y,expected):
    assert fun1(x,y)==expected

