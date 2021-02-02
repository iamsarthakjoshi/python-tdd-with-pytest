import pytest

### SETUP FIXTURES ###

@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")

@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("Setup Module")

@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")


### TESTS ###
def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
