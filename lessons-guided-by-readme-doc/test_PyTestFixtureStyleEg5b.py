from pytest import raises

def raisesValueException():
    raise ValueError

def test_Exception():
    with raises(ValueError):
        raisesValueException()
