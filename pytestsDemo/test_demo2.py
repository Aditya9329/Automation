import pytest

@pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hii"


def test_secondCreditCard():
    a =4
    b = 6
    assert a+2 == 6 ,"Addition does not match"


