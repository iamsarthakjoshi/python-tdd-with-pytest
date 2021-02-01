## Pytest

- PyTest is a Python unit testing framework.

- It provides the ability to create tests, test modules, test classes, and test fixtures.

- It uses the built-in Python assert statement which makes implementing unit tests much simpler than other Python unit testing frameworks.
- It also adds many useful command line arguments to help specify what tests should be run and in what order.

### How do you create a unit test in Python with PyTest?

- In PyTest, individual tests are Python functions with test at the beginning of the function name.
- The unit tests then execute production code and use the standard Python assert statement to perform verifications on results.
- Similar tests can be grouped together by including them in the same module or class.

### Run pytest

```
# In root of the project

> pytest -v
```

The `-v ` argument tells PyTest to run in `verbose mode` and it will tell me which unit test it's running and if they pass or not.

The `-s` argument, which tells pytest not to capture the console output, so you can see the results of the print statements on the console.

### Test discovery

PyTest will automatically find your tests when you run it from the command line using several naming rules for the test files, test classes, and test functions.

Test `function` names should begin with test.

`Classes` with tests in them should have the word `Test` with a capital `T` at the beginning of the class name. **These classes should also have no \_\_init\_\_ method.**

The `file names` for test modules should start with `test_ ` or end with `_test`.

### An xunit-style setup and teardown

One key feature of all unit test frameworks is providing the ability to execute setup code before and after the test. pytest provides this capability with both `xUnit-style` setup and `teardown functions` and with pytest `fixtures`.

The xUnit-style setup and `teardown functions` allow you to execute code before and after:

- Test modules,

```
    def setup_module():
    def teardown_module():
```

- Test functions,

```
    def setup_function():
    def teardown_function():
```

- Test classes, and

```
    def setup_classe():
    def teardown_classe():
```

- Test methods in Test classes.

```
def setup_method():
def teardown_method():

```

#### Test functions

Using these `setup` and `teardown functions` can help reduce code duplication by letting you specify the setup and teardown code once at each of the different levels as necessary rather than repeating the code in each individual unit test. This can help keep your code clean and manageable.

> I've got two unit tests defined, test one and test two. I've also got the functions setup function and teardown function defined. `pytest` will automatically call setup function before each unit test in that module that is not in a class. It will then call teardown function after each unit test has completed executing.

`Setup function` and `teardown function` are passed in the unit test that is being executed, so the setup and teardown code can be customized per unit test if necessary.

Now lets run this in pytest and see the output.

**Example Code:**
`In ./test_xUnitStyle.py`

```
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

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
```

The pytest output shows that the setup function is called before test one executes and is called again before test two executes.

The `teardown function` is called after test one executes and again after test two executes. Which unit test is being executed is passed in, so the setup and teardown code can easily be customized per unit test.

**Pytest Output:**

```

(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

collected 2 items

test_xUnitStyle.py::test1
Setting up test1 👈
Executing test1 👈
PASSED
Tearing down test1 👈

test_xUnitStyle.py::test2
Setting up test2 👈
Executing test2 👈
PASSED
Tearing down test2 👈

======== 2 passed in 0.01s =========
```

#### Test Modules (with Test Functions)

Lets extend above example to include setup and teardown functions for the `module` itself. These functions will be **called once before** any of the unit tests in the `module` are **executed and again after all the unit tests in the `module` have completed executing**.

Now update the code to include `setup module` and `teardown module` functions with print statements and then execute pytest again to see the updated results.

**Updated Example Code:**
`In ./test_xUnitStyle.py`

```
def setup_module(module):
    print("\n\nSetup Module Called")

def teardown_module(module):
    print("\nTeardown Module Called")

# ... rest of the above code
```

The pytest output shows that now the `setup module function` is called once before any of the unit tests or the unit test `setup and teardown functions` are executed. And the `teardown module function` is called once after all the unit tests in the module and their `setup and teardown functions` have completed.

**Updated Pytest Output:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

test_xUnitStyle.py::test1

Setup Module Called 👈

Setting up test1
Executing test1
PASSED
Tearing down test1

test_xUnitStyle.py::test2
Setting up test2
Executing test2
PASSED
Tearing down test2

Teardown Module Called 👈

======== 2 passed in 0.01s =========
```

#### Test Class (with Test Modules & Functions)

Let's move the `test one` and `test two` unit test functions into a `class` called `TestClass`. Let's also add the **method** `setup class`, `teardown class`, `setup method`, and `teardown method`.

The `setup class` and `teardown class` **methods** have the `@classmethod` **decorator** applied, as they are passed in the uninstantiated class object rather than a unique instance of the class.

- The setup class method will be executed by pytest before any of the unit tests in the class are executed.
- The teardown class method will be executed by pytest after all of the unit tests in the class are executed.
- `Setup method` will be called before each unit test in the class is executed, and the `teardown method` will be executed after each unit test in the class has completed.

**Pytest Test Class Code:**
`In ./test_xUnitClassStyle.py`

```
class TestClass:
    @classmethod
    def setup_class(cls):
        print("\n\nSetup TestClass Called")

    @classmethod
    def teardown_class(cls):
        print("\nTeardown TestClass Called")

    def setup_method(self, method):
        if method == self.test1:
            print("\nSetting up test1")
        elif method == self.test2:
            print("\nSetting up test2")
        else:
            print("\nSetting up unkown test")

    def teardown_method(self, method):
        if method == self.test1:
            print("\nTearing down test1")
        elif method == self.test2:
            print("\nTearing down test2")
        else:
            print("\nTearing down unkown test")

    def test1(self):
        print("Executing test1")
        assert True

    def test2(self):
        print("Executing test2")
        assert True

```

Let's run this in `pytest` and see the results. The pytest output shows that the `setup class method` is called before anything else. Then `setup method` is called before `test one`, and `teardown method` is called after `test one` completes. Then `setup method` is called again before test two, and `teardown method` is called again after test two completes. Lastly, teardown class is called.

**Pytest TestClass Output:**

```
collected 2 items

test_xUnitClassStyle.py::TestClass::test1

Setup TestClass Called 👈

Setting up test1
Executing test1
PASSED
Tearing down test1

test_xUnitClassStyle.py::TestClass::test2
Setting up test2
Executing test2
PASSED
Tearing down test2

Teardown TestClass Called
```

### Pytest Fixtures

Pytest fixtures is feature, which is a powerful alternative to the xUnit style of setup/teardown functions, which utilizes dependency injection.

- Test Fixtures allow for re-use of code across tests by specifying functions that should be executed before the unit test runs.
- Specifying that a function is a Test Fixture is done by applying the `pytest.fixture` decorator to the function.
- Individual unit tests can specify they want to use that function by specifying it in their parameter list, or by using the `pytest.mark.usefixture` decorator.
- The fixture can also set its autouse parameter to true, which will cause all tests in the fixture scope to automatically execute the fixture before the test executes.

#### Test Fixture "Setup"

Example Code::
`In ./test_PyTestFixtureStyleEg1.py`

```
import pytest

### SETUP FIXTURES ###

@pytest.fixture
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
```

> If you do not put 'setup' or '@pytest.mark.usefixtures("setup")' in test functions or methods, then the `setup()` fixture will not run.

Pytest Output:

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

test_PyTestFixtureStyleEg1.py::test1

Initial Setup
Executing test1
PASSED
test_PyTestFixtureStyleEg1.py::test2

Initial Setup
Executing test2
PASSED

======== 2 passed in 0.01s =========
```

It can be very useful for each individual test to be able to specify which test fixtures it needs executed before the test is run. But this can also be cumbersome for those cases where all the tests need to run the same test fixture. In this case, the `autouse `parameter of the test fixture can be set to `true`, and then the fixture will automatically be executed before each test that is in the fixture scope.

Example Code:
`In ./test_PyTestFixtureStyleEg1.py`

```
### SETUP FIXTURES ###

@pytest.fixture(autouse = true)
def setup():
    print("\nInitial Setup")

### TESTS ###

def test1():
    print("Executing test1")
    assert True

def test2():
    print("Executing test2")
    assert True
```

#### Test Fixture "Teardown"

Often, there is some type of teardown or cleanup that a test, class or module needs to perform after testing has been completed. Each Test Fixture can specify their own teardown code that should be executed. There are two methods of specifying a teardown code for a Test Fixture. The `yield` keyword, and the `request-context` object's `addfinalizer` method.

`yield`: The `yield` keyword is the simpler of the two options for teardown code. The code after the yield statement is executed after the fixture goes out of scope. The yield keyword is a replacement for return, and any return values should be passed to it. The addfinalizer method of adding teardown code is a little more complicated, but also a little more capable than the yield statement.

```
@pytest.fixture()
def setup():
    print("Setup")
    yield
    print("Teardown!")
```

`addfinalizer`: With the `addfinalizer` method, one or more finalizer functions are added via the `request-context`'s addfinalizer method. **One of the big differences between this method and the `yield` keyword is that this method allows for multiple finalization functions to be specified.**

```
@pytest.fixture()
def setup():
    print("Setup")
    def teardown():
        print("Teardown!")
    request.addfinalizer(teardown)
```

Example Code:
`In ./test_PyTestFixtureStyleEg2.py`

```

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

def test2setup2(setup2):
    print("Executing test2")
    assert True

```

Pytest Output:

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

collected 2 items

test_PyTestFixtureStyleEg2.py::test1

Setup1 👈
Executing test1
PASSED
Teardown1! 👈

test_PyTestFixtureStyleEg2.py::test2setup2

Setup2 👈
Executing test2
PASSED
TeardownB! 👈
TeardownA! 👈

======== 2 passed in 0.01s =========
```

In the output from above pytest, we can see that the teardown code for `setup1` is called after `test1` finishes executing. And the two teardown functions for `setup2` are called after `test2` finishes.

### Test Fixtures Scopes

Which test a fixture applies to, and how often it is run, depends on the fixture scope. Test Fixtures have four different scopes that are possible.

Test fixtures can have the following four different scopes which specify how often the fixture will be called:

`Function scope`: By default, the scope is set to `Function`. And this specifies that the fixture should be called for all tests in the module.
`Class scope`: specifies that the Test Fixture should be executed once per test class.
`Module scope`: specifies that the fixture should be executed once per module.
`Session scope`: specifies that the fixture should be executed once when `pytest` starts.

**Example #1:**

In this example, I've implemented two modules. In the first module, I have three different test fixtures, each at a different scope. Function fixture, Module fixture, and Session fixture. I've also implemented unit tests test1, and test2.

`In ./test_PyTestFixtureStyleEg3a.py`

```
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
```

**Pytest Output of Example #1:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

collected 4 items

test_PyTestFixtureStyleEg3a.py::test1
Setup Session
Setup Module

Setup Function
Executing test1
PASSED

test_PyTestFixtureStyleEg3a.py::test2
Setup Function
Executing test2
PASSED

======== 2 passed in 0.01s =========
```

The pytest output shows that the Session fixture runs first, and is run once. Then the Module fixture is run once for the first module, and then the Function fixture in the first module is run once for each test in the first module.

**Example #2:**

In the second module, I also have three different test fixtures at three different scopes. Function fixture, Class fixture, and Module fixture. And I've implemented a test class to unit test.

`In ./test_PyTestFixtureStyleEg3b.py`

```
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
```

**Pytest Output of Example #2:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========

test_PyTestFixtureStyleEg3b.py::TestClass::test1b

Setup Module2
Setup Class2

Setup Function2
Executing test1b
PASSED

test_PyTestFixtureStyleEg3b.py::TestClass::test2b
Setup Function2
Executing test2b
PASSED

======== 2 passed in 0.01s =========
```

The pytest output shows that the Module fixture is run first, and its run once. The Class fixture runs next, and then the Function fixture is run once before each of the test classes unit tests.

### Test Fixture Return Objects and Params

- Pytest fixtures allow you to optionally return `data` from the fixture that can be used in the test.
- The optional `params` array argument in the fixture decorator can be used to specify one or more values that should be passed to the test.
- When a `params` argument has multiple values, the test will be called once with each value.

**Example Code:**
`In ./test_PyTestFixtureStyleEg4.py`

```
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
```

**Pytest Output of Example code:**

```
(venv) PythonTDDPractice1|⇒ pytest -v -s
======== test session starts ========
collected 3 items

test_PyTestFixtureStyleEg4.py::test[1]
Setup return val=1
Param from fixture=1
PASSED

test_PyTestFixtureStyleEg4.py::test[2]
Setup return val=2
Param from fixture=2
PASSED

test_PyTestFixtureStyleEg4.py::test[3]
Setup return val=3
Param from fixture=3
PASSED

======== 2 passed in 0.01s =========
```

The pytest output shows that the test fixture and unit test are both run once for each value specified in the params list, as expected. The params feature can be a powerful and easy way to run your unit test with various values. **Care should be taken with this approach, though, as you generally still want to have different test cases and separate unit tests with unique names so that they can be easily identified when they fail.**

## Assert and Testing Exceptions

### Assert

- Pytests allows the use of the built in Python assert statement for performing verifications in a unit test.
- The normal comparison operators can be used on all Python data types. Less than `<`, greater than `>`, less than or equal `<=`, greater than or equal `>=`, equal `==` or non equal `!=`.
- Pytests expands on the messages that are reported for assert failures to provide more context in the test results.

**Eamples:**
`In ./test_PyTestFixtureStyleEg5a.py`

```
def test_IntAssert():
    assert 1 == 1

def test_StrAssert():
    assert "str" == "str"

def test_FloatAssert():
    assert "1.0" == "1.0"

def test_arrayAssert():
    assert [1,3,4] == [1,3,4]

def test_dictAssert():
    assert {"1":1} == {"1":1}
```

#### Comparing FLoating Point Values

- Validating floating point values can sometimes be difficult, as internally the value is stored as a series of binary fractions (i.e. 1/3 is internally 0.333333333...). **Because of this, some comparisons that we'd expect to pass, will fail.**
- Pytests provides the `approx` function, which will validate the two floating point values, or approximately the same value, as each other, to then a default tolerance of one times e to the negative six value.

**Example:**
`In ./test_PyTestFixtureStyleEg5a.py`

```
# Failing Test
def test_BadFloatCompare():
    assert (0.1 + 0.2) == 0.3

# Passing Test
from pytest import approx
def test_BadFloatCompare():
    assert (0.1 + 0.2) == approx(0.3)
```

### Verifing Exceptions

- In some test cases, we need to verify that a function raises an exception under certain conditions.
- Pytest provides the raises helper to perform this verification, using the `with` keyword.
- When the raises helper is used, the unit test will fail, if the specified exception is not thrown in the code block, after the `raises` line.

**Example:**
`In ./test_PyTestFixtureStyleEg5b.py`

```
from pytest import raises

def raisesValueException():
    raise ValueError

def test_Exception():
    with raises(ValueError):
        raisesValueException()
```
