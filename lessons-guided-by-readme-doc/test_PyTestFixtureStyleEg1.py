import pytest

### SETUP FIXTURES ###

@pytest.fixture()
def setup():
    print("\n\nInitial Setup")

### TESTS ###

def test1(setup):
    print("Executing test1")
    assert True

@pytest.mark.usefixtures("setup")
def test2():
    print("Executing test2")
    assert True
