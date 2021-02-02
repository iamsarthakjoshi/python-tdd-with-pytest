import pytest

### SETUP FIXTURES ###
@pytest.fixture(params=[1,2,3])
def _param(request):
    retVal = request.param
    print(f"\nSetup return val={retVal}")
    return retVal

### TESTS ###
def test(_param):
    print(f"Param from fixture={_param}")
    assert True
