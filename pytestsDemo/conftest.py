import pytest

@pytest.fixture()
def setup():
    print("i wil lexecuted first")
    yield
    print("last execution of this test")



@pytest.fixture()
def dataLoad():
    print("user profile data is being created")
    return ["rahul","shetty","rahulshettyacademy.com"]