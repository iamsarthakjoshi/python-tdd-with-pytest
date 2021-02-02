import pytest

### SETUP FIXTURES ###

@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")


@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetup Class2")


@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")


### TESTS ###
class TestClass:
    def test1b(self):
        print("Executing test1b")
        assert True

    def test2b(self):
        print("Executing test2b")
        assert True
