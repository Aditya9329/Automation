
import pytest 


@pytest.fixture()
def setup():
    print("i wil lexecuted first")
    yield
    print("last execution of this test")

#test method names always start with test_
@pytest.mark.smoke
# @pytest.mark.skip
def test_firstProgram(setup):
    print("Hiii")

def test_greetSecondCreditCard():
    print("Good morning")



