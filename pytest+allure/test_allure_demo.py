import allure,pytest

@allure.step("步骤1：点XXX")
def step_1():
    print("step1111")
@allure.step("步骤2：点XXX")
def step_2():
    print("step222")
@allure.step("步骤3：点XXX")
def step_3():
    print("step333")
@allure.feature("编辑页面")
class TestEditPage():
    """编辑页面"""
    @allure.story("这是一个XX用例")
    def test_1(self,login):
        """用例描述：先登录，再去执行XXXX"""
        step_1
        step_2
        print("1111xxx")
    @allure.story("另一个XX")
    def test_2(self,login):
        """用例描述2：xxxxx描述2"""
        step_3
        print("222222")