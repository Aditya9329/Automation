import pytest

@pytest.fixture()
def setup():
    print("I will be executing first")
    yield
    print("i wil lbe executed last")

def test_fixtureDemo(setup):
    print("I wil lexecute steps in fixtureDemo method")