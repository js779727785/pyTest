"""
https://www.cnblogs.com/yoyoketang/p/12004145.html
1.配置以下3项：
pip install pytest
pip install allure-pytest
https://github.com/allure-framework/allure2/releases
2.写完相关casedemo后，用以下运行测试用例（在pytest+allure所在目录）
pytest --alluredir ./report/allure_raw
启动allure服务：
allure serve report/allure_raw
"""