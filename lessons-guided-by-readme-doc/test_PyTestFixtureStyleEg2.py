import pytest

### SETUP FIXTURES ###

@pytest.fixture()
def setup1():
    print("\n\nSetup1")
    yield
    print("\nTeardown1!")

@pytest.fixture()
def setup2(request):
    print("\nSetup2")

    def teardown_a():
        print("TeardownA!")

    def teardown_b():
        print("\nTeardownB!")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)

### TESTS ###

def test1(setup1):
    print("Executing test1")
    assert True

def test2(setup2):
    print("Executing test2")
    assert True
