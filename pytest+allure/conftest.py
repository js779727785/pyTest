import pytest

@pytest.fixture(scope="session")
def login():
    print("用例先登录")
