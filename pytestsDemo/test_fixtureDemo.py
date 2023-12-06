import pytest
#it is another way we have 
"""@pytest.fixture()
def setup():
    print("i wil lexecuted first")
    yield
    print("last execution of this test")"""




"""
def test_fixtureDemo(setup):
    print("i wil lexecuted steps in fixtureDemo method")


def test_fixtureDemo1(setup):
    print("i wil lexecuted steps in fixtureDemo method")

def test_fixtureDemo2(setup):
    print("i wil lexecuted steps in fixtureDemo method")

def test_fixtureDemo3(setup):
    print("i wil lexecuted steps in fixtureDemo method")"""


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo(self):
        print("i wil lexecuted steps in fixtureDemo method")


    def test_fixtureDemo1(self):
        print("i wil lexecuted steps in fixtureDemo method")

    def test_fixtureDemo2(self):
        print("i wil lexecuted steps in fixtureDemo method")

    def test_fixtureDemo3(self):
        print("i wil lexecuted steps in fixtureDemo method")