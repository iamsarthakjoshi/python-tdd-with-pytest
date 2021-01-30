### SETUP AND TEARDOWN MODULE FOR BEFORE AND AFTER COMPLETION (respectively) OF TESTS AS A WHOLE  ###

def setup_module(module):
    print("\n\nSetup Module Called")

def teardown_module(module):
    print("\nTeardown Module Called")

### SETUP AND TEARDOWN FUNCTION FOR EACH TEST ###

def setup_function(function):
    if function == test1:
        print("\nSetting up test1")
    elif function == test2:
        print("\nSetting up test2")
    else:
        print("\nSetting up unkown test")

def teardown_function(function):
    if function == test1:
        print("\nTearing down test1")
    elif function == test2:
        print("\nTearing down test2")
    else:
        print("\nTearing down unkown test")


### TESTS ###

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True